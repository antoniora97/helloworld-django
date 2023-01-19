
from django.http import HttpResponse

def index (request):
    return HttpResponse("<h1>Hola Mundo de Antonio Ramos</h1>")