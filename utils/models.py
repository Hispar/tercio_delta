"""
License boilerplate should be used here.
"""

# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DateModificationModelMixin(models.Model):
    """An abstract model for dates modification.
    This mixin add two fields to the models that use it, date_added and
    date_modified, that stores the datetime when the model instance was
    created and updated.
    Note: django metaclass for models requires that the inherited class must be
    a subclass of models.Model in order to create the stored fields declared
    in that class.
    Attributes:
        creation_date: A datetime that automatically stores the datetime
            of the model creation.
        modification_date: A datetime that automatically stores the datetime
            of the model creation.
    """
    creation_date = models.DateTimeField(
        verbose_name=_('creation date'),
        auto_now_add=True,
        editable=False,
        db_index=True
    )
    modification_date = models.DateTimeField(
        verbose_name=_('modification date'),
        auto_now=True,
        editable=False
    )

    class Meta:
        abstract = True
