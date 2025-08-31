import json


class Request:

    def __init__(self, scope):
        self.scope = scope

    @property
    def path(self):
        return self.scope['path']

    @property
    def method(self):
        return self.scope['method']


class Response:

    def __init__(self, content, status_code=200):
        self.content = content
        self.status_code = status_code

    async def send_to_asgi(self, send):
        body = json.dumps(self.content).encode("utf-8")

        await send({
            "type": "http.response.start",
            "status": self.status_code,
            "headers": [[b"content-type", b"application/json"]],
        })

        await send({
            "type": "http.response.body",
            "body": body,
        })


class SerPy:
    def __init__(self):
        print("SerPy is initializing!")
        self.routes = {}

    def route(self, path, methods=None):
        
        if methods is None:
            methods = ["GET"]

        def wrapper(handler):

            for method in methods:
                self.routes[(method.upper(), path)] = handler
            return handler

        return wrapper

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            print("SerPy is only configured for Http requests.")
            return
        
        request = Request(scope)
        handler = self.routes.get((request.method, request.path))

        if handler:
            response = await handler(request)
        else:
            response = Response(content={"error": "Route Not Found"}, status_code=404)

        await response.send_to_asgi(send)
