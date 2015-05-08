# -*- coding: utf-8 -*-

import urllib
import json
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

def full_page_effect(request, template_name='full-page-effect.html'):
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def loading(request, template_name='loading.html'):
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def fade_text(request, template_name='fade-text.html'):
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))