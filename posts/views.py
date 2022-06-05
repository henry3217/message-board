from django.views.generic import ListView
from .models import post
from django.views.generic import TemplateView
from django.http import HttpResponse


class HomePageView(ListView):
    model = post
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
