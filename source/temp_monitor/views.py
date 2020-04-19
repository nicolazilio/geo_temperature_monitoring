from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Temperature
from django import forms
from django.contrib.admin import widgets
from .tables import TemperatureTable
from django_tables2 import SingleTableView

class AddTemperatureView(CreateView):
    model = Temperature
    fields = ['temp', 'temp_taken_date_time', 'latitude', 'longitude']
    template_name = 'temp_monitor/add_temp.html'
    
    def get_form(self, form_class=None):
        form = super(AddTemperatureView, self).get_form(form_class)
        form.fields['latitude'].widget = forms.HiddenInput()
        form.fields['longitude'].widget = forms.HiddenInput()
        # form.fields['temp_taken_date_time'].widget = widgets.AdminSplitDateTime()
        return form

    def get_ip_address(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        try:
            validate_ipv46_address(ip)
            return ip
        except:
            return None

    def form_valid(self, form):
        request = self.request
        measurement = form.save(commit=False)
        measurement.user = request.user
        measurement.ip_address = self.get_ip_address(request)
        
        lat = form.cleaned_data['latitude']
        lon = form.cleaned_data['longitude']
        measurement.latitude = lat if lat else None
        measurement.longitude = lon if lon else None
        
        measurement.save()
        
        messages.success(
            request, _('Measurement successfully added'))
        
        return redirect('..')

class TemperatureTableView(ListView):
    model = Temperature
    table_class = TemperatureTable
    template_name = 'temp_monitor/temp_list.html'


def person_list(request):
    table = TemperatureTable(Temperature.objects.filter(user=request.user).order_by('-temp_taken_date_time'))

    return render(request, "temp_monitor/temp_list.html", {
        "table": table
    })
