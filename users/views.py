from django.views.generic import *
from django.urls import path
from .models import *
from .forms import *
from rest_framework.generics import *
from rest_framework.views import APIView
from .serializers import *

class IndexView(TemplateView):
    template_name = "index.html"



class UserProfile_CreateView(CreateView):
    template_name = "userprofile/userprofile_create.html"
    model = UserProfile
    form_class = UserProfile_MF

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
	        return reverse("userprofile_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class UserProfile_ListView(ListView):
    template_name = "userprofile/userprofile_list.html"
    model = UserProfile
    queryset = UserProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class UserProfile_UpdateView(UpdateView):
    template_name = "userprofile/userprofile_update.html"
    model = UserProfile
    form_class = UserProfile_MF

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
	        return reverse("userprofile_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class UserProfile_DetailView(DetailView):
    template_name = "userprofile/userprofile_detail.html"
    model = UserProfile
    queryset = UserProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class UserProfile_DeleteView(DeleteView):
    template_name = "userprofile/userprofile_delete.html"
    model = UserProfile

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("userprofile_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Role_CreateView(CreateView):
    template_name = "role/role_create.html"
    model = Role
    form_class = Role_MF

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
	        return reverse("role_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Role_ListView(ListView):
    template_name = "role/role_list.html"
    model = Role
    queryset = Role.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Role_UpdateView(UpdateView):
    template_name = "role/role_update.html"
    model = Role
    form_class = Role_MF

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
	        return reverse("role_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Role_DetailView(DetailView):
    template_name = "role/role_detail.html"
    model = Role
    queryset = Role.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Role_DeleteView(DeleteView):
    template_name = "role/role_delete.html"
    model = Role

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("role_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Permission_CreateView(CreateView):
    template_name = "permission/permission_create.html"
    model = Permission
    form_class = Permission_MF

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
	        return reverse("permission_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Permission_ListView(ListView):
    template_name = "permission/permission_list.html"
    model = Permission
    queryset = Permission.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Permission_UpdateView(UpdateView):
    template_name = "permission/permission_update.html"
    model = Permission
    form_class = Permission_MF

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
	        return reverse("permission_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Permission_DetailView(DetailView):
    template_name = "permission/permission_detail.html"
    model = Permission
    queryset = Permission.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Permission_DeleteView(DeleteView):
    template_name = "permission/permission_delete.html"
    model = Permission

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("permission_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Message_CreateView(CreateView):
    template_name = "message/message_create.html"
    model = Message
    form_class = Message_MF

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
	        return reverse("message_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Message_ListView(ListView):
    template_name = "message/message_list.html"
    model = Message
    queryset = Message.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Message_UpdateView(UpdateView):
    template_name = "message/message_update.html"
    model = Message
    form_class = Message_MF

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
	        return reverse("message_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Message_DetailView(DetailView):
    template_name = "message/message_detail.html"
    model = Message
    queryset = Message.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Message_DeleteView(DeleteView):
    template_name = "message/message_delete.html"
    model = Message

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("message_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


