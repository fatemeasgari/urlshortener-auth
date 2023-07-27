from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def hello (request):
    return HttpResponse('Hello World!')
    
#def echo (request):
#   get= request.GET
#   post= request.POST
#   return HttpResponse(get)

@csrf_exempt
def echo (request):
    get= request.GET
    post= request.POST
    #return HttpResponse(get)
    #return HttpResponse(post)
    return JsonResponse(post)
