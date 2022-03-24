from fastapi import Form
from fastapi_utils.inferring_router import InferringRouter
from settings import settings
import http.client
import json

cost_router = InferringRouter()

@cost_router.post("/cost")
async def get_cost(origin: int = Form(...), destination: int = Form(...), 
                       weight: int = Form(...), courier: str = Form(...)):
    conn = http.client.HTTPConnection("api.rajaongkir.com")
    payload = f"origin={origin}&destination={destination}&weight={weight}&courier={courier}"
    headers = {
    'key': settings.KEY,
    'content-type': "application/x-www-form-urlencoded"
    }
    conn.request("POST", "/starter/cost", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data)