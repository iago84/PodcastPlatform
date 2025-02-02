from django.views.generic import *
from django.urls import path
from .models import *
from .forms import *
from rest_framework.generics import *
from rest_framework.views import APIView
from .serializers import *

class IndexView(TemplateView):
    template_name = "index.html"



class Plan_CreateView(CreateView):
    template_name = "plan/plan_create.html"
    model = Plan
    form_class = Plan_MF

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
	        return reverse("plan_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Plan_ListView(ListView):
    template_name = "plan/plan_list.html"
    model = Plan
    queryset = Plan.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Plan_UpdateView(UpdateView):
    template_name = "plan/plan_update.html"
    model = Plan
    form_class = Plan_MF

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
	        return reverse("plan_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Plan_DetailView(DetailView):
    template_name = "plan/plan_detail.html"
    model = Plan
    queryset = Plan.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Plan_DeleteView(DeleteView):
    template_name = "plan/plan_delete.html"
    model = Plan

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("plan_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Subscription_CreateView(CreateView):
    template_name = "subscription/subscription_create.html"
    model = Subscription
    form_class = Subscription_MF

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
	        return reverse("subscription_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Subscription_ListView(ListView):
    template_name = "subscription/subscription_list.html"
    model = Subscription
    queryset = Subscription.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Subscription_UpdateView(UpdateView):
    template_name = "subscription/subscription_update.html"
    model = Subscription
    form_class = Subscription_MF

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
	        return reverse("subscription_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Subscription_DetailView(DetailView):
    template_name = "subscription/subscription_detail.html"
    model = Subscription
    queryset = Subscription.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Subscription_DeleteView(DeleteView):
    template_name = "subscription/subscription_delete.html"
    model = Subscription

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("subscription_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Transaction_CreateView(CreateView):
    template_name = "transaction/transaction_create.html"
    model = Transaction
    form_class = Transaction_MF

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
	        return reverse("transaction_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Transaction_ListView(ListView):
    template_name = "transaction/transaction_list.html"
    model = Transaction
    queryset = Transaction.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Transaction_UpdateView(UpdateView):
    template_name = "transaction/transaction_update.html"
    model = Transaction
    form_class = Transaction_MF

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
	        return reverse("transaction_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Transaction_DetailView(DetailView):
    template_name = "transaction/transaction_detail.html"
    model = Transaction
    queryset = Transaction.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Transaction_DeleteView(DeleteView):
    template_name = "transaction/transaction_delete.html"
    model = Transaction

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("transaction_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


