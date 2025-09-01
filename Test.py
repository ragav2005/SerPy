from SerPy import SerPy, Response
from users.users import user_router

app = SerPy()
app.include_router(user_router, prefix="/users")

@app.route("/", methods=["GET"])
async def home(request):
    return Response({"message": "Welcome to the home page!"})
