from django.views.generic import *
from django.urls import path, reverse
from .models import *
from .forms import *
from rest_framework.generics import *
from rest_framework.views import APIView
from .serializers import *





class Report_CreateView(CreateView):
    template_name = "report/report_create.html"
    model = Report
    form_class = Report_MF

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
        return reverse("report_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Report_ListView(ListView):
    template_name = "report/report_list.html"
    model = Report
    queryset = Report.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Report_UpdateView(UpdateView):
    template_name = "report/report_update.html"
    model = Report
    form_class = Report_MF

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
        return reverse("report_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Report_DetailView(DetailView):
    template_name = "report/report_detail.html"
    model = Report
    queryset = Report.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Report_DeleteView(DeleteView):
    template_name = "report/report_delete.html"
    model = Report

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
        return reverse("report_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class FlaggedContent_CreateView(CreateView):
    template_name = "flaggedcontent/flaggedcontent_create.html"
    model = FlaggedContent
    form_class = FlaggedContent_MF

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
        return reverse("flaggedcontent_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class FlaggedContent_ListView(ListView):
    template_name = "flaggedcontent/flaggedcontent_list.html"
    model = FlaggedContent
    queryset = FlaggedContent.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class FlaggedContent_UpdateView(UpdateView):
    template_name = "flaggedcontent/flaggedcontent_update.html"
    model = FlaggedContent
    form_class = FlaggedContent_MF

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
        return reverse("flaggedcontent_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class FlaggedContent_DetailView(DetailView):
    template_name = "flaggedcontent/flaggedcontent_detail.html"
    model = FlaggedContent
    queryset = FlaggedContent.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class FlaggedContent_DeleteView(DeleteView):
    template_name = "flaggedcontent/flaggedcontent_delete.html"
    model = FlaggedContent

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
        return reverse("flaggedcontent_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


