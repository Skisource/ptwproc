from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist

from .models import PTW, Isolation, Inhibit, SafeEntry, get_total_audits, SIMOPS, Restriction, Drill


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'ptw/index.html'
    extra_context = {'audits': str(get_total_audits(7))}


class PTWView(generic.ListView):
    template_name = 'ptw/ptw_index.html'
    context_object_name = 'latest_active_list'

    def get_queryset(self):
        """Return records"""
        return PTW.objects.filter(
            Q(status__exact='authorized') | Q(status__exact='created') | Q(status__exact='suspended')
        )


def board(request):
    # Fetch active work permits with related location data
    permits = PTW.objects.filter(status='authorized').select_related('work_location')

    # Prepare location data for the template
    locations = [
        {
            'name': permit.work_location.name,
            'x': permit.work_location.x,
            'y': permit.work_location.y,
            'permit_id': permit.id,
            # Add any other permit data you need
        }
        for permit in permits
    ]

    context = {
        'locations': locations,
    }

    return render(request, 'ptw/board.html', context)


class IsolationActiveView(generic.ListView):
    template_name = 'ptw/isolation_index.html'
    context_object_name = 'active_isolations'

    def get_queryset(self):
        return Isolation.objects.filter(
            Q(status__exact='authorized') | Q(status__exact='created') | Q(status__exact='long term')
        )


class SafeEntryView(generic.ListView):
    template_name = 'ptw/safeentry_index.html'
    context_object_name = 'safeentry'

    def get_queryset(self):
        return SafeEntry.objects.filter(
            Q(status__exact='authorized') | Q(status__exact='created')
        )


class InhibitView(generic.ListView):
    template_name = 'ptw/inhibit_index.html'
    context_object_name = 'inhibit'

    def get_queryset(self):
        return Inhibit.objects.filter(
            Q(status__exact='authorized') | Q(status__exact='created')
        )

class DrillsView(generic.ListView):
    template_name = 'ptw/drill_register.html'
    context_object_name = 'drill'

    def get_queryset(self):
        return Drill.objects.all()


def permit(request, ptw_id):
    this_permit = get_object_or_404(PTW, pk=ptw_id)
    active_ptws = PTW.objects.filter(status__exact='authorized')
    simops = SIMOPS.objects.all()
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
            restrictions.append(f'no additional measures required for {this_permit.id}')
            descriptions.append(no_rest)

    context = {'this_permit': this_permit,
               'active_ptws': active_ptws,
               'simops': simops,
               'restrictions': restrictions,
               'descriptions': descriptions,
               }
    return render(request, 'ptw/detail.html', context)


def drill(request, drill_id):
    this_drill = get_object_or_404(Drill, pk=drill_id)
    context = {'this_drill': this_drill,
               'type': this_drill.type,
               'sub_type': this_drill.sub_type,
               'date': this_drill.date,
               'date_next': this_drill.date_next,
               'description': this_drill.description,
               'long_description': this_drill.long_description,
               'personnel': this_drill.personnel,
               }
    return render(request, 'ptw/drill_report.html', context)