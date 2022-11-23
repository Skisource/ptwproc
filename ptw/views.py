from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist

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
            Q(status__exact='authorized') | Q(status__exact='created') | Q(status__exact='suspended')
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
    simops = SIMOPS.objects.all( )
    restrictions = []
    descriptions = []
    for active in active_ptws:
        try:
            obj = simops.get(work_type_1__exact=this_permit.work_type, work_type_2__exact=active.work_type)
            desc = Restriction.objects.get(restriction__exact=obj.restriction)
            restrictions.append(obj)
            descriptions.append(desc)
        except ObjectDoesNotExist:
            no_rest = Restriction.objects.get(restriction__exact='R0')
            restrictions.append(f'{active.prefix} {active.id} requires no additional measures for {this_permit.id}')
            descriptions.append(no_rest)

    context = {'this_permit': this_permit,
               'active_ptws': active_ptws,
               'simops': simops,
               'restrictions': restrictions,
               'descriptions': descriptions,
               }
    return render(request, 'ptw/detail.html', context)
