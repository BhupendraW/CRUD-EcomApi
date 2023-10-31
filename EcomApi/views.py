
from django.http import HttpResponse,JsonResponse
def home(request):
    print("home page requested")
    
    data = {'url':"http://localhost:8000/api/"}
    
    return JsonResponse(data,safe=False)



