from SerPy import SerPy, Response

app = SerPy()


@app.route("/" , methods=['GET'])
async def home(request):
    return Response({"message": "This is a GET request to the home page."})


@app.route("/home/{id}", methods=['GET'])
async def get_user(request, id):
    
    return Response({
        "message": f"Fetching details for User ID: {id}",
        "requested_path": request.path
    })
