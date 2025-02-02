from django.views.generic import *
from django.urls import path, reverse
from .models import *
from .forms import *
from rest_framework.generics import *
from rest_framework.views import APIView
from .serializers import *





class Recommendation_CreateView(CreateView):
    template_name = "recommendation/recommendation_create.html"
    model = Recommendation
    form_class = Recommendation_MF

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
        return reverse("recommendation_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Recommendation_ListView(ListView):
    template_name = "recommendation/recommendation_list.html"
    model = Recommendation
    queryset = Recommendation.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Recommendation_UpdateView(UpdateView):
    template_name = "recommendation/recommendation_update.html"
    model = Recommendation
    form_class = Recommendation_MF

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
        return reverse("recommendation_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Recommendation_DetailView(DetailView):
    template_name = "recommendation/recommendation_detail.html"
    model = Recommendation
    queryset = Recommendation.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Recommendation_DeleteView(DeleteView):
    template_name = "recommendation/recommendation_delete.html"
    model = Recommendation

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
        return reverse("recommendation_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context




class Algorithm_CreateView(CreateView):
    template_name = "algorithm/algorithm_create.html"
    model = Algorithm
    form_class = Algorithm_MF

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
        return reverse("algorithm_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Algorithm_ListView(ListView):
    template_name = "algorithm/algorithm_list.html"
    model = Algorithm
    queryset = Algorithm.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Algorithm_UpdateView(UpdateView):
    template_name = "algorithm/algorithm_update.html"
    model = Algorithm
    form_class = Algorithm_MF

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
        return reverse("algorithm_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Algorithm_DetailView(DetailView):
    template_name = "algorithm/algorithm_detail.html"
    model = Algorithm
    queryset = Algorithm.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


class Algorithm_DeleteView(DeleteView):
    template_name = "algorithm/algorithm_delete.html"
    model = Algorithm

    def get_success_url(self):
        # Define dinámicamente la URL de redirección al completar con éxito
        return reverse("algorithm_list")
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_data': 'value'})
        return context


