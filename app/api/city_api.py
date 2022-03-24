from typing import Optional
from fastapi_utils.inferring_router import InferringRouter
from urllib.request import urlopen, Request
from settings import settings
import json

city_router = InferringRouter()

@city_router.get("/city")
async def get_city(id: Optional[int] = None, province: Optional[int] = None):
    if id != None and province != None:
        url_province = f"https://api.rajaongkir.com/starter/city?id={id}&province={province}"
    if id != None and province == None:
        url_province = f"https://api.rajaongkir.com/starter/city?id={id}"
    if id == None and province != None:
        url_province = f"https://api.rajaongkir.com/starter/city?province={province}"
    if id == None and province == None:
        url_province = f"https://api.rajaongkir.com/starter/city"
    req = Request(url_province)
    req.add_header("key", settings.KEY)
    content = urlopen(req).read()
    return json.loads(content)
