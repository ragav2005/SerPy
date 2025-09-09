# import fix for dev purposes when running uvicorn from Demo_app/
import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# App code starts here
from SerPy import SerPy, Response
from users.users import user_router

app = SerPy()
app.include_router(user_router, prefix="/users")

@app.route("/", methods=["GET"])
async def home(request):
    return Response({"message": "Welcome to the home page!"})

@app.route("/search")
async def search(request):
    search_term = request.query.getall("q", default="")
    limit = int(request.query.get("limit", default=10))

    return Response({
        "message": f"Searching for {search_term}",
        "limit": limit
    })