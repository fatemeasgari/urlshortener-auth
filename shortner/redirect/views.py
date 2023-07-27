from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import *

@csrf_exempt
def echo(request):
    get = request.GET
    post = request.POST
    return JsonResponse(post)

def links(request):
    context = {}
    if request.POST.get('delete_short_link' , ''):
        short_link.objects.filter(pk = request.POST['link_id']).delete()
        s_links = short_link.objects.filter(user_id = request.user)
        context.update({'deleted_successfully': True, 's_links' : s_links})
        return render(request, 'index.html', context)
    s_links = short_link.objects.filter(user_id = request.user)
    context.update({'s_links' : s_links})
    return render(request, 'index.html', context)
