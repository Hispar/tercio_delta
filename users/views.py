import logging

from django.http import Http404
from django.shortcuts import render

from users.models import Member, Unit, Award

logger = logging.getLogger(__name__)


def index(request):
    logger.info('dime algo')
    members_list = Member.objects.order_by('id')
    return render(request, 'members/index.html', {'members_list': members_list})


def units(request):
    units_list = Unit.objects.order_by('id')
    return render(request, 'units/index.html', {'units_list': units_list})


def awards(request):
    awards_list = Award.objects.order_by('id')
    return render(request, 'awards/index.html', {'awards_list': awards_list})


def member(request, member_id):
    try:
        member = Member.objects.get(pk=member_id)
    except Member.DoesNotExist:
        raise Http404
    return render(request, 'members/detail.html', {'member': member})


def unit(request, unit_id):
    try:
        unit = Unit.objects.get(pk=unit_id)
    except Unit.DoesNotExist:
        raise Http404
    return render(request, 'units/detail.html', {'unit': unit})


def award(request, award_id):
    try:
        award = Award.objects.get(pk=award_id)
    except Award.DoesNotExist:
        raise Http404
    return render(request, 'awards/detail.html', {'award': award})
