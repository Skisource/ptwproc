from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import PTW, Isolation, Inhibit, SafeEntry


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'ptw/index.html'


class PTWView(generic.ListView):
    template_name = 'ptw/ptw_index.html'
    context_object_name = 'latest_active_list'

    def get_queryset(self):
        """Return the last ten authorized records"""
        return PTW.objects.filter(
            status__exact='authorized'
        )


class PTWDetailView(generic.DetailView):
    model = PTW
    template_name = 'ptw/detail.html'

    def get_queryset(self):
        """
        Excludes any records that aren't published yet.
        """
        return PTW.objects.filter(pub_date__lte=timezone.now())


class IsolationActiveView(generic.ListView):
    template_name = 'ptw/isolation_index.html'
    context_object_name = 'active_isolations'

    def get_queryset(self):
        return Isolation.objects.filter(
            status__exact='authorized'
        )


class IsolationLongtermView(generic.ListView):
    template_name = 'ptw/longterm_index.html'
    context_object_name = 'longterm_isolations'

    def get_queryset(self):
        return Isolation.objects.filter(
            status__exact='long term'
        )


class SafeEntryView(generic.ListView):
    template_name = 'ptw/safeentry_index.html'
    context_object_name = 'safeentry'

    def get_queryset(self):
        return SafeEntry.objects.filter(
            status__exact='authorized'
        )


class InhibitView(generic.ListView):
    template_name = 'ptw/inhibit_index.html'
    context_object_name = 'inhibit'

    def get_queryset(self):
        return Inhibit.objects.filter(
            status__exact='authorized'
        )