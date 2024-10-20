import azure.functions as func
import numpy as np
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="numericalintegralservice/{lower}/{upper}")
def integrallFunc(req: func.HttpRequest) -> func.HttpResponse:
    lower = req.route_params.get('lower')
    upper = req.route_params.get('upper')

    if not lower or not upper:
        return func.HttpResponse(
            "Please pass lower and upper bounds in the URL path",
            status_code=400
        )

    try:
        lower, upper = float(lower), float(upper)
        Ns = [10, 100, 1000, 10000, 100000, 1000000]
        results = [numerical_integration(lower, upper, N) for N in Ns]
        return func.HttpResponse(json.dumps(results), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(
            f"An error occurred: {str(e)}",
            status_code=500
        )

def numerical_integration(lower, upper, N):
    x = np.linspace(lower, upper, N + 1)
    dx = (upper - lower) / N
    y = np.abs(np.sin(x))
    area = np.sum(y[:-1] * dx)
    return area
