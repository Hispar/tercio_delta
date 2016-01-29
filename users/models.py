"""
License boilerplate should be used here.
"""

# django imports
from django.contrib.auth.models import User
from django.db import models
from utils.models import DateModificationModelMixin

A = 'Activo'
R = 'Reserva'
N = 'Novato'
STATUS_OPTIONS = (
    ('A', A),
    ('R', R),
    ('N', N),
)


class Member(DateModificationModelMixin):
    user = models.OneToOneField(User)
    nick = models.CharField(max_length=200)
    real_name = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS)
    # rank = models.CharField(max_length=2, choices=RANK_OPTIONS)
    # rank = models.ForeignKey(Rank, unique=True)
    played = models.IntegerField(blank=True)
    picture = models.FileField(upload_to='media', blank=True)
    add_date = models.DateTimeField('date registered')
    mod_date = models.DateTimeField('date modified')
    # units = models.ManyToManyField('Unit', through='MemberUnit')
    # awards = models.ManyToManyField('Award', through='MemberAward')
