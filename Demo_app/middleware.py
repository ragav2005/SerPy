import time
from SerPy import Request, Response


async def timing_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration_ms = (time.time() - start_time) * 1000
    response.headers["X-Processing-Time-ms"] = str(duration_ms)
    print(f"Request took {duration_ms:.2f}ms")
    return response

async def auth_middleware(request: Request, call_next):
    print("Checking for authorization...")

    if  request.headers["x-auth-token"] != "12345":
        return Response({"error": "Unauthorized"}, status_code=401)
    
    response = await call_next(request)
    return response