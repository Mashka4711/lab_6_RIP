from django.shortcuts import render
from django.views.generic import View
from LAB6_dj.models import ServiceModel


class ServiceView(View):
    def get(self,request):
        services = ServiceModel.objects.all()
        return render(request, 'service.html', {'services':services})