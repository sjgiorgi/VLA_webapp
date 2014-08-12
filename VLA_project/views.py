from __future__ import absolute_import
import re
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#from .models import *

def home(request):
    # Display course list in sidebar
    #cour_list = get_course_list()
    #context_dict = {'cour_list': cour_list}
    
    # Set searched flags to false and get complete question and definition lists
    #context_dict['def_searched'] = False
    #context_dict['def_list'] = Node.objects.all()
    #context_dict['question_searched'] = False
    #context_dict['question_list'] = AnswerWithQuestion.objects.all()
    
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/index.html', '')


