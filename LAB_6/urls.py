from django.conf.urls import url
from django.contrib import admin
from LAB6_dj.views import ServiceView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ServiceView.as_view())
    ]