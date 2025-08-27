class SerPy:
    def __init__(self):

        print("SerPy is initializing!")

    async def __call__(self, scope, receive, send):

        print(scope , receive , send)
        if scope["type"] == "http":
            
            await send({
                "type": "http.response.start",
                "status": 200,
                "headers": [[b"content-type", b"text/plain"]],
            })
            await send({
                "type": "http.response.body",
                "body": b"Welcome to the SerPy!",
            })