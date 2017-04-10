from django.shortcuts import render
from cmsUsersPutApp.models import Page
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def cms_put(request, rec):
    if request.method == "GET":
        try:
            page = Page.objects.get(name=rec)
            resp = page.page
        except ObjectDoesNotExist:
            return HttpResponse("Content not found", status=404)
    elif request.method == "PUT":
        if request.user.is_authenticated():
            page = Page(name=rec, page=request.body)
            page.save()
            resp = "<h1>Succesfully added page: " + rec + "</h1>"
        else:
            resp = "<h1>Action not allowed.</h1>"
    else:
        return HttpResponse("Method not allowed", status=405)

    if request.user.is_authenticated():
        resp += "<p>Logged in as " + request.user.username + ". <a href='logout'>Logout</a></p>"
    else:
        resp += "<p>Not Logged in. <a href='login'>Login</a></p>"
    return HttpResponse(resp)

def barra(request):
    resp = "<h1>Pages:</h1>"
    for i in Page.objects.all():
        resp += "<br/><a href='" + i.name + "'>" + i.name + "</a>"

    if request.user.is_authenticated():
        resp += "<p>Logged in as " + request.user.username + ". <a href='logout'>Logout</a></p>"
    else:
        resp += "<p>Not Logged in. <a href='login'>Login</a></p>"
    return HttpResponse(resp)
