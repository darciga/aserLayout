from sbadmin.models import servicio
from django.shortcuts import render_to_response,get_object_or_404,render
from django.template.context import RequestContext

# Create your views here.
def index(request):
	servicios = servicio.objects.all()
	template = 'index.html'
	return render_to_response(template,context_instance= RequestContext(request,locals()))

def consultarCli(request):
	template = 'consultar.html'
	return render_to_response(template)

def actualizar(request):
	template = 'actualizar.html'
	return render_to_response(template)

def nuevoser(request):
	template = 'newser.html'
	return render_to_response(template)

def consultarSer(request):
	template = 'conser.html'
	return render_to_response(template)

def detailSer(request):
	template = 'detalleser.html'
	return render_to_response(template)

def login(request):
	template = 'login.html'
	return render_to_response(template)
