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

SL = 'Soldado'
SR = 'Sargento'
CA = 'Capitan'
CO = 'Comandante'
RANK_OPTIONS = (
    ('SL', SL),
    ('SR', SR),
    ('CA', CA),
    ('CO', CO),
)


class Member(DateModificationModelMixin):
    nick = models.CharField(max_length=200)
    real_name = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS)
    rank = models.CharField(max_length=2, choices=RANK_OPTIONS, default=SL)
    played = models.IntegerField(blank=True)
    picture = models.FileField(upload_to='media', blank=True)
    units = models.ManyToManyField('Unit', through='MemberUnit')
    awards = models.ManyToManyField('Award', through='MemberAward')

    def __unicode__(self):
        return self.nick

    def get_rank(self):
        return getattr(self, self.rank)

    def get_status(self):
        return getattr(self, self.status)

    def get_picture(self):
        if self.picture:
            return self.picture
        else:
            return 'media/static/tercio.png'


class Unit(DateModificationModelMixin):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    picture = models.FileField(upload_to='media/units', blank=True)
    members = models.ManyToManyField('Member', through='MemberUnit')

    def __unicode__(self):
        return self.name

    def get_picture(self):
        if self.picture:
            return self.picture
        else:
            return 'media/static/tercio.png'


class Award(DateModificationModelMixin):
    C = 'Mencion'
    M = 'Medalla'
    LEVEL_OPTIONS = (
        ('C', C),
        ('M', M),
    )
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    award_type = models.CharField(max_length=200)
    level = models.CharField(max_length=1, choices=LEVEL_OPTIONS)
    picture = models.FileField(upload_to='media/awards', blank=True)
    awarded = models.ManyToManyField('Member', through='MemberAward')

    def __unicode__(self):
        return self.name

    def get_level(self):
        return getattr(self, self.level)

    def get_picture(self):
        if self.picture:
            return self.picture
        else:
            return 'media/static/tercio.png'


class MemberUnit(DateModificationModelMixin):
    member = models.ForeignKey('Member', related_name='members')
    unit = models.ForeignKey('Unit', related_name='units')
    rank = models.IntegerField(default=0)


class MemberAward(DateModificationModelMixin):
    member = models.ForeignKey('Member', related_name='awarded')
    award = models.ForeignKey('Award', related_name='awards')
    reason = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField('date awarded')
