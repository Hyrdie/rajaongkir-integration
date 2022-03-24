from typing import Optional
from fastapi_utils.inferring_router import InferringRouter
from urllib.request import urlopen, Request
from settings import settings
import json

province_router = InferringRouter()

@province_router.get("/province")
async def get_province(id: Optional[int] = None):
    if id == None:
        url_province = f"https://api.rajaongkir.com/starter/province"
    else:
        url_province = f"https://api.rajaongkir.com/starter/province?id={id}"
    req = Request(url_province)
    req.add_header("key", settings.KEY)
    content = urlopen(req).read()
    return json.loads(content)
