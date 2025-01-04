TOKEN = "securetoken123"

def is_authenticated(request):
    return request.headers.get("Authorization") == f"Bearer {TOKEN}"
