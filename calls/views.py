from django.views.generic import *
from django.urls import path
from .models import *
from .forms import *
from rest_framework.generics import *
from rest_framework.views import APIView
from .serializers import *

class IndexView(TemplateView):
    template_name = "index.html"



class Call_CreateView(CreateView):
    template_name = "call/call_create.html"
    model = Call
    form_class = Call_MF

	    def form_valid(self, form):
	        # Personaliza lo que sucede cuando el formulario es válido
	        self.object = form.save()
	        # Agrega lógica personalizada aquí (e.g., mensajes o redirecciones)
	        return super().form_valid(form)

	    def form_invalid(self, form):
	        # Personaliza lo que sucede cuando el formulario no es válido
	        # Por ejemplo, puedes registrar un mensaje de error
	        return super().form_invalid(form)
	
	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("call_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Call_ListView(ListView):
    template_name = "call/call_list.html"
    model = Call
    queryset = Call.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Call_UpdateView(UpdateView):
    template_name = "call/call_update.html"
    model = Call
    form_class = Call_MF

	    def form_valid(self, form):
	        # Personaliza lo que sucede cuando el formulario es válido
	        self.object = form.save()
	        # Agrega lógica personalizada aquí (e.g., mensajes o redirecciones)
	        return super().form_valid(form)

	    def form_invalid(self, form):
	        # Personaliza lo que sucede cuando el formulario no es válido
	        # Por ejemplo, puedes registrar un mensaje de error
	        return super().form_invalid(form)
	
	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("call_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Call_DetailView(DetailView):
    template_name = "call/call_detail.html"
    model = Call
    queryset = Call.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Call_DeleteView(DeleteView):
    template_name = "call/call_delete.html"
    model = Call

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("call_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class VideoCall_CreateView(CreateView):
    template_name = "videocall/videocall_create.html"
    model = VideoCall
    form_class = VideoCall_MF

	    def form_valid(self, form):
	        # Personaliza lo que sucede cuando el formulario es válido
	        self.object = form.save()
	        # Agrega lógica personalizada aquí (e.g., mensajes o redirecciones)
	        return super().form_valid(form)

	    def form_invalid(self, form):
	        # Personaliza lo que sucede cuando el formulario no es válido
	        # Por ejemplo, puedes registrar un mensaje de error
	        return super().form_invalid(form)
	
	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("videocall_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class VideoCall_ListView(ListView):
    template_name = "videocall/videocall_list.html"
    model = VideoCall
    queryset = VideoCall.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class VideoCall_UpdateView(UpdateView):
    template_name = "videocall/videocall_update.html"
    model = VideoCall
    form_class = VideoCall_MF

	    def form_valid(self, form):
	        # Personaliza lo que sucede cuando el formulario es válido
	        self.object = form.save()
	        # Agrega lógica personalizada aquí (e.g., mensajes o redirecciones)
	        return super().form_valid(form)

	    def form_invalid(self, form):
	        # Personaliza lo que sucede cuando el formulario no es válido
	        # Por ejemplo, puedes registrar un mensaje de error
	        return super().form_invalid(form)
	
	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("videocall_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class VideoCall_DetailView(DetailView):
    template_name = "videocall/videocall_detail.html"
    model = VideoCall
    queryset = VideoCall.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class VideoCall_DeleteView(DeleteView):
    template_name = "videocall/videocall_delete.html"
    model = VideoCall

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("videocall_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class CallHistory_CreateView(CreateView):
    template_name = "callhistory/callhistory_create.html"
    model = CallHistory
    form_class = CallHistory_MF

	    def form_valid(self, form):
	        # Personaliza lo que sucede cuando el formulario es válido
	        self.object = form.save()
	        # Agrega lógica personalizada aquí (e.g., mensajes o redirecciones)
	        return super().form_valid(form)

	    def form_invalid(self, form):
	        # Personaliza lo que sucede cuando el formulario no es válido
	        # Por ejemplo, puedes registrar un mensaje de error
	        return super().form_invalid(form)
	
	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("callhistory_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class CallHistory_ListView(ListView):
    template_name = "callhistory/callhistory_list.html"
    model = CallHistory
    queryset = CallHistory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class CallHistory_UpdateView(UpdateView):
    template_name = "callhistory/callhistory_update.html"
    model = CallHistory
    form_class = CallHistory_MF

	    def form_valid(self, form):
	        # Personaliza lo que sucede cuando el formulario es válido
	        self.object = form.save()
	        # Agrega lógica personalizada aquí (e.g., mensajes o redirecciones)
	        return super().form_valid(form)

	    def form_invalid(self, form):
	        # Personaliza lo que sucede cuando el formulario no es válido
	        # Por ejemplo, puedes registrar un mensaje de error
	        return super().form_invalid(form)
	
	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("callhistory_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class CallHistory_DetailView(DetailView):
    template_name = "callhistory/callhistory_detail.html"
    model = CallHistory
    queryset = CallHistory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class CallHistory_DeleteView(DeleteView):
    template_name = "callhistory/callhistory_delete.html"
    model = CallHistory

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("callhistory_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


