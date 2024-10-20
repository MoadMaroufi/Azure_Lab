### Usage
- curl the link of the  link of the mapReduce fucntion:
```
curl https://mymapreduce-cloud-homework-moaad-maaroufi.azurewebsites.net/api/orchestrators/master_orchestrator
```
- we get this :
```
{
  "id": "<INSTANCE_ID>",
  "statusQueryGetUri": "https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/durabletask/instances/<INSTANCE_ID>?taskHub=<TASK_HUB_NAME>&connection=Storage&code=<ACCESS_CODE>",
  "sendEventPostUri": "https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/durabletask/instances/<INSTANCE_ID>/raiseEvent/{eventName}?taskHub=<TASK_HUB_NAME>&connection=Storage&code=<ACCESS_CODE>",
  "terminatePostUri": "https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/durabletask/instances/<INSTANCE_ID>/terminate?reason={text}&taskHub=<TASK_HUB_NAME>&connection=Storage&code=<ACCESS_CODE>",
  "rewindPostUri": "https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/durabletask/instances/<INSTANCE_ID>/rewind?reason={text}&taskHub=<TASK_HUB_NAME>&connection=Storage&code=<ACCESS_CODE>",
  "purgeHistoryDeleteUri": "https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/durabletask/instances/<INSTANCE_ID>?taskHub=<TASK_HUB_NAME>&connection=Storage&code=<ACCESS_CODE>",
  "restartPostUri": "https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/durabletask/instances/<INSTANCE_ID>/restart?taskHub=<TASK_HUB_NAME>&connection=Storage&code=<ACCESS_CODE>",
  "suspendPostUri": "https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/durabletask/instances/<INSTANCE_ID>/suspend?reason={text}&taskHub=<TASK_HUB_NAME>&connection=Storage&code=<ACCESS_CODE>",
  "resumePostUri": "https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/durabletask/instances/<INSTANCE_ID>/resume?reason={text}&taskHub=<TASK_HUB_NAME>&connection=Storage&code=<ACCESS_CODE>"
}
```
- then to get the result we curl the **statusQueryGetUri**:
```
curl "https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/durabletask/instances/<INSTANCE_ID>?taskHub=<TASK_HUB_NAME>&connection=Storage&code=<ACCESS_CODE>"
```
- Finally we get the desired ouput:
```
{"name":"master_orchestrator","instanceId":"51920a14f6f54c7cb2cc7ea94aea357c","runtimeStatus":"Completed","input":null,"customStatus":null,"output":{"With":4,"tuppence":1,"for":1,"paper":1,"and":2,"strings":1,"You":2,"can":2,"have":1,"your":6,"own":1,"set":1,"of":3,"wings":1,"feet":1,"on":2,"the":10,"ground":1,"You're":1,"a":7,"bird":1,"in":1,"flight":1,"fist":1,"holding":1,"tight":2,"To":2,"string":2,"kite":8,"Oh-oh-oh":2,"Let's":4,"go":6,"fly":6,"Up":6,"to":2,"highest":2,"height":2,"And":2,"send":3,"it":3,"soaring":2,"through":2,"atmosphere":2,"where":2,"air":3,"is":2,"clear":2,"Oh,":2,"let's":2,"When":1,"you":1,"flyin'":1,"up":1,"there":1,"All":1,"at":1,"once":1,"you're":1,"lighter":1,"than":1,"dance":1,"breeze":1,"Over":1,"'ouses":1,"trees":1,"first":1,"'olding":1},"createdTime":"2024-01-03T13:20:43Z","lastUpdatedTime":"2024-01-03T13:20:50Z"}
```