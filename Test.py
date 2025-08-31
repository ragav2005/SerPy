from SerPy import SerPy, Response

app = SerPy()

@app.route("/" , methods=['GET'])
async def home(request):
    return Response({"message": "This is a GET request to the home page."})

