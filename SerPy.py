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

class Router:
    def __init__(self):
        self.routes = {}
    
    def route(self, path, methods=None):
        if methods is None:
            methods = ["GET"]
        
        def wrapper(handler):
            for method in methods:
                self.routes[(method.upper(), path)] = handler
            return handler
        return wrapper
    

class SerPy:
    def __init__(self):
        print("SerPy is initializing!")
        self.routes = {}


    def include_router(self , router:Router, prefix):
        for (method , path) , handler in router.routes.items():
            self.routes[(method, prefix+path)] = handler
            
    
    def route(self, path, methods=None):
        
        if methods is None:
            methods = ["GET"]

        def wrapper(handler):

            for method in methods:
                self.routes[(method.upper(), path)] = handler
            return handler

        return wrapper

    def find_route(self, route_method , route_path):
        
        for (method, path), handler in self.routes.items():
            
            if(method != route_method):
                continue
            
            route_parts  = path.split('/')
            path_parts = route_path.split('/') 
            
            if( len(route_parts) != len(path_parts)):
                continue
            
            params = {}
            match = True
            
            for route_part , path_part in zip(route_parts, path_parts):
                if route_part.startswith('{') and route_part.endswith('}'):
                    param_name = route_part[1:-1]
                    params[param_name] = path_part
                elif route_part != path_part:
                    match = False
                    break

            if match:
                return handler, params

        return None, None

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            print("SerPy is only configured for Http requests.")
            return
        
        request = Request(scope)
        handler, params = self.find_route(request.method, request.path)

        if handler:
            response = await handler(request, **params)
        else:
            response = Response(content={"error": "Route Not Found"}, status_code=404)

        await response.send_to_asgi(send)
