import sanic
from sanic import Sanic
from sanic.log import logger
from sanic.response import json

app = Sanic(__name__)


def request_to_dict(request: sanic.Request) -> dict:
    request_dict = {
        "url": str(request.url),
        "method": request.method,
        "headers": dict(request.headers),
        "args": dict(request.args),
        "form": dict(request.form),
        "json": request.json,
        # "body": request.body.decode('utf-8'),
    }
    return request_dict


@app.on_request()
async def log_request(request: sanic.Request):
    logger.info(request_to_dict(request))


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
async def catch_all(request: sanic.Request):
    return json({})


if __name__ == '__main__':
    app.run(auto_reload=True, host='0.0.0.0')
