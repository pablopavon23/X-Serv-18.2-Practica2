from django.shortcuts import render
from django.http import HttpResponse
from models import urls
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

import urllib

@csrf_exempt

def mostrar_URLs(request):
    if request.method == 'GET':     #si es un GET debemos mostar lo que hay y un formulario para meter mas
        respuesta = '<form method="POST" action="">' \
        + 'URL para acortar: <input type="text" name="url"><br>' \
        + '<input type="submit" value="Enviar"><br>' \
        + '</form>'
        paginas = urls.objects.all()
        for pagina in paginas:      #imprimimos cada pagina que haya en nuestra lista
            respuesta += '<li><a href="/' + str(pagina.Url_corta) + '">' + str(pagina.Url_larga) + '</a>\t'
            respuesta += '->\t'
            respuesta += '<a href="/' + str(pagina.Url_corta) + '">' + str(pagina.Url_corta) + '</a>'

    elif request.method == 'POST' or request.method == 'PUT':       #si el metodo no es GET es que estamos introduciendo una nueva
        Url_nueva = request.body.split("=")[1]
        Url_nueva =  urllib.unquote(Url_nueva).decode('utf8') #por si acaso,en python3: urllib.parse.unquote(Url_nueva, encoding='utf-8', errors='replace')
        http = Url_nueva.split("://")[0]
        
        if (http != 'http') and (http != 'https'):
            Url_nueva = 'https://' + str(Url_nueva)

        try:                                                #hay que comprobar que la introducida no este en nuestra lista ya
            urlcorta = urls.objects.get(Url_larga=Url_nueva)
            respuesta = '<h1>URL ya acortada. Introduzca otra distinta</h1></br>'\
            +'<html><body><a href="'+ Url_nueva +'">' + Url_nueva + ' </a></br></body></html>'\
            + '<html><body><a href="'+ urlcorta.Url_corta +'">'+ urlcorta.Url_corta + ' </a></br></body></html>'
        except urls.DoesNotExist:                           #si no lo esta la metemos
            paginas = urls.objects.all()
            numerodepaginas = 0     #numerodepaginas nos sirve para darle el identificador adecuado a nuestra nueva pagina segun las que haya, puesto que sera el primero libre
            for pagina in paginas:
                numerodepaginas = numerodepaginas + 1
            Url_nueva_acortada = 'http://localhost:1234/' + str(numerodepaginas)
            p = urls(Url_corta=Url_nueva_acortada, Url_larga=Url_nueva)
            p.save()
            pagina = urls.objects.get(Url_corta=Url_nueva_acortada)
            respuesta = "<h1>Se ha acortado la URL de forma correcta. Vuelva a la pagina principal para ver la lista actualizada.</br></h1>" \
            +'<a href="'+ str(pagina.Url_larga) +'">' + str(pagina.Url_larga) + ' </a></br>'\
            + '<a href="'+ str(pagina.Url_corta) +'">'+ str(pagina.Url_corta) + ' </a></br>'

    else:
        respuesta=('Ha ocurrido un error')

    return HttpResponse(respuesta)

# ------------------------------------------------------------------------------
def redireccion_a_URL(request, url):
  try:
    pagina = urls.objects.get(Url_corta=url)
    respuesta = '<html><head><meta http-equiv="Refresh" content="5;url='+ pagina.Url_larga +'"></head>' \
    	+ "<body><h1> Espere, a ser redirigido ... " \
    	+ "</h1></body></html>"
  except urls.DoesNotExist:
    try:
    	url = 'http://localhost:1234/' + str(url)
    	pagina = urls.objects.get(Url_corta=url)
    	respuesta = '<html><head><meta http-equiv="Refresh" content="5;url='+ pagina.Url_larga +'"></head>' \
    		+ "<body><h1> Espere, a ser redirigido ...  " \
    		+ "</h1></body></html>"
    except urls.DoesNotExist:
    	respuesta = '<h1>La pagina solicitada no esta en la lista</h1>'

  return HttpResponse(respuesta)
