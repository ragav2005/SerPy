# import fix for dev purposes when running uvicorn from Demo_app/
import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# App code starts here
from SerPy import SerPy, Response, Request
from middleware import timing_middleware, auth_middleware

app = SerPy()


app.add_middleware(timing_middleware)

@app.route("/")
async def public_route(request):
    return Response({"message": "This is a public route."})

@app.route("/profile", middleware=[auth_middleware], methods=["GET"])
async def protected_route(request):
    return Response({"message": "This is a protected route. You are authorized."})