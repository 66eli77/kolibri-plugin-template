from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.PluginTemplateView.as_view()),
]
