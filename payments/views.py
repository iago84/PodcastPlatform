from django.views.generic import *
from django.urls import path
from .models import *
from .forms import *
from rest_framework.generics import *
from rest_framework.views import APIView
from .serializers import *

class IndexView(TemplateView):
    template_name = "index.html"



class Payment_CreateView(CreateView):
    template_name = "payment/payment_create.html"
    model = Payment
    form_class = Payment_MF

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
	        return reverse("payment_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Payment_ListView(ListView):
    template_name = "payment/payment_list.html"
    model = Payment
    queryset = Payment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Payment_UpdateView(UpdateView):
    template_name = "payment/payment_update.html"
    model = Payment
    form_class = Payment_MF

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
	        return reverse("payment_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Payment_DetailView(DetailView):
    template_name = "payment/payment_detail.html"
    model = Payment
    queryset = Payment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Payment_DeleteView(DeleteView):
    template_name = "payment/payment_delete.html"
    model = Payment

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("payment_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Invoice_CreateView(CreateView):
    template_name = "invoice/invoice_create.html"
    model = Invoice
    form_class = Invoice_MF

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
	        return reverse("invoice_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Invoice_ListView(ListView):
    template_name = "invoice/invoice_list.html"
    model = Invoice
    queryset = Invoice.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Invoice_UpdateView(UpdateView):
    template_name = "invoice/invoice_update.html"
    model = Invoice
    form_class = Invoice_MF

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
	        return reverse("invoice_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Invoice_DetailView(DetailView):
    template_name = "invoice/invoice_detail.html"
    model = Invoice
    queryset = Invoice.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Invoice_DeleteView(DeleteView):
    template_name = "invoice/invoice_delete.html"
    model = Invoice

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("invoice_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Payout_CreateView(CreateView):
    template_name = "payout/payout_create.html"
    model = Payout
    form_class = Payout_MF

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
	        return reverse("payout_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Payout_ListView(ListView):
    template_name = "payout/payout_list.html"
    model = Payout
    queryset = Payout.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Payout_UpdateView(UpdateView):
    template_name = "payout/payout_update.html"
    model = Payout
    form_class = Payout_MF

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
	        return reverse("payout_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Payout_DetailView(DetailView):
    template_name = "payout/payout_detail.html"
    model = Payout
    queryset = Payout.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Payout_DeleteView(DeleteView):
    template_name = "payout/payout_delete.html"
    model = Payout

	    def get_success_url(self):
	        # Define dinámicamente la URL de redirección al completar con éxito
	        return reverse("payout_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


