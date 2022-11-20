from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime
from .models import PTW, Isolation, Inhibit, SafeEntry, get_total_audits, SIMOPS, Restriction


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'ptw/index.html'
    extra_context = {'audits': str(get_total_audits(7))}



class PTWView(generic.ListView):
    template_name = 'ptw/ptw_index.html'
    context_object_name = 'latest_active_list'


    def get_queryset(self):
        """Return authorized records"""
        return PTW.objects.filter(
            status__exact='authorized'
        )


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


def permit(request, ptw_id):
    this_permit = get_object_or_404(PTW, pk=ptw_id)
    active_ptws = PTW.objects.filter(status__exact='authorized')
    simops = SIMOPS.objects.all()
    restrictions = []
    for active in active_ptws:
        if not simops.filter(work_type_1__exact=this_permit.work_type,work_type_2__exact=active.work_type):
            restrictions.append(f'{this_permit.id} does not conflict with {active.id}')
        else:
            restrictions.append(f'{this_permit.id} is restricted by {active.id}')

    context = {'this_permit': this_permit,
               'active_ptws': active_ptws,
               'simops': simops,
               'restrictions': restrictions,
               }
    return render(request, 'ptw/detail.html', context)
