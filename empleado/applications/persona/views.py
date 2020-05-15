from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
) 
# models
from .models import Empleado
# forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'inicio.html'


class ListaAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'fisrt_name'
    context_object_name = 'empleados'
    #model = Empleado
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'fisrt_name'
    context_object_name = 'empleados'
    model = Empleado
    
    
class ListaByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__name=area
        )
        return lista


class ListaByTrabajo(ListView):
    template_name = 'persona/list_by_trabajo.html'

    def get_queryset(self):
        trabajo = self.kwargs['jobempleado']
        lista2 = Empleado.objects.filter(
            job=trabajo
        )
        return lista2


class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('******************')
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            fisrt_name=palabra_clave
        )
        
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=8)
        return empleado.habilidades.all()



class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.fisrt_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form) 


class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado 
    fields = ['fisrt_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('***************METODO POST*************')
        print('=======================================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        
        print('***********METODO form valid***********')
        print('***************************************')
        return super(EmpleadoUpdateView, self).form_valid(form) 



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')


        
    #queryset = Empleado.objects.filter(
        #departamento__name='area de contabilidad'
    #)
    #tarea al final listar empleados por trabajo.

    #como controlar lo que llevamos y hacemos para sustentar el costo.
    
    