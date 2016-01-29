# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# django imports
import os
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class LoginView(TemplateView):
    """
    Attributes:
    """
    http_method_names = ["get"]
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated():
        #     return HttpResponseRedirect(reverse('panel:panel-list'))
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
