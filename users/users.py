from SerPy import Router, Response

user_router = Router()

@user_router.route("/all", methods=["GET"])
async def get_users(request):
    return Response({"message": "Here are all the users"})

@user_router.route("/{id}", methods=["GET"])
async def get_user(request, id):
    return Response({"message": f"Here is user {id}"})