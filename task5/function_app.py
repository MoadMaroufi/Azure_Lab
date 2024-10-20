import azure.functions as func
import azure.durable_functions as df
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


myApp = df.DFApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@myApp.route(route="orchestrators/{functionName}")
@myApp.durable_client_input(client_name="client")
async def http_start(req: func.HttpRequest, client):
    function_name = req.route_params.get('functionName')
    instance_id = await client.start_new(function_name, None, None)
    response = client.create_check_status_response(req, instance_id)
    return response





@myApp.orchestration_trigger(context_name="context")
def master_orchestrator(context):
    mapped_results = []

    container_name = "mapreduce"
    input_lines = yield context.call_activity("GetInputDataFn", container_name)

    #notice here that we don't yield directly in repsect of the fan-in fan-out pattern 
    mapper_tasks = [context.call_activity("mapper", (line_number, line))
                    for line_number, line in input_lines]
    aggregated_mapper_results = yield context.task_all(mapper_tasks)
    mapped_results = [item for sublist in aggregated_mapper_results for item in sublist]

   
    shuffled = yield context.call_activity("shuffler", mapped_results)

    # Same thing here for the fan in fan out pattern
    reducer_tasks = [context.call_activity("reducer", (word, counts))
                     for word, counts in shuffled.items()]
    reducer_results = yield context.task_all(reducer_tasks)

    
    reduced = {word: count for reducer_result in reducer_results for word, count in reducer_result.items()}
    return reduced




@myApp.activity_trigger(input_name="line")
def mapper(line):
    ##eventhough line number is not useful here but we use 
    #in accordance with the specification sof the assingment
    line_number, line_string = line
    words = line_string.split()
    return [(word, 1) for word in words]



@myApp.activity_trigger(input_name="mappedData")
def shuffler(mappedData):
    shuffled = {}
    for word, count in mappedData:
        if word not in shuffled:
            shuffled[word] = []
        shuffled[word].append(count)
    return shuffled



@myApp.activity_trigger(input_name="shuffledData")
def reducer(shuffledData):
    word, counts = shuffledData
    reduced = {word: sum(counts)}
    return reduced


@myApp.activity_trigger(input_name="containerName")
def GetInputDataFn(containerName):
    ##This should be done with an envirroment variable but for the sake of simplicity we do it in this naive manner
    connection_string = "PlaceHolder"

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(containerName)

    input_data = []
    for blob in container_client.list_blobs():
        blob_client = container_client.get_blob_client(blob)
        blob_data = blob_client.download_blob().readall()
        lines = blob_data.decode('utf-8').splitlines()
        for line_number, line in enumerate(lines, start=1):
            input_data.append((line_number, line))

    return input_data

