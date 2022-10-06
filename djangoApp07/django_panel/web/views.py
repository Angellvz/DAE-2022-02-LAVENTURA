from django.shortcuts import render,redirect

# importamos la libreria generic
from django.views import View
from .models import *
from .forms import *

# Create your views here.
class AlumnoView(View):
    

    def get(self,request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request,'index.html',context)

    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            # <process form cleaned data>
            return redirect('/')
