from __future__ import absolute_import, division
import re
#import cv, cv2, sys, math, numpy as np # all for circuit image processing
from django.shortcuts import render
from django.contrib.auth import authenticate

from .models import *
from .forms import UserSimulationImage
from student.models import UserProfile, CoursePermission, LabProgress
from tutor.models import Node, AnswerWithQuestion, AnswerElement


def index(request):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username
        
        # Display course list in sidebar
        cour_list = get_course_list(user)
        context_dict = {'cour_list': cour_list}
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()

        return render(request, 'VLA/index.html', context_dict)

# View used to display About information on VLA
def about(request):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        context_dict = {'logged_in': False}
    else:
        # Get user and username
        user = request.user
        username = request.user.username
        
        # Display course list in sidebar
        cour_list = get_course_list(user)
        context_dict = {'cour_list': cour_list}
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()  

        context_dict['logged_in'] = True
    return render(request, 'VLA/about.html', context_dict)

# View used to present Course with all course, instructor, TA info
def course(request, course_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username
        
        # Get course name and set course url
        course_name = course_name_url.replace('_', ' ')
        context_dict = {'course_name': course_name, 'course_name_url': course_name_url}
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()
        
        # Get all course information for selected course
        try:
            course = Course.objects.get(name=course_name)
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass

        # Get prereq information for selected course
        try:
            prereq = Prereq.objects.get(course = course)
            context_dict['prereq_name_url'] = prereq.name.replace(' ','_')  
            context_dict['prereq'] = prereq
        except Prereq.DoesNotExist:
            pass
        
        # Display all course related labs in the sidebar
        try:
            context_dict['labs'] = get_lab_list(course, user)
        except Laboratory.DoesNotExist:
            pass
    
        return render(request, 'VLA/course.html', context_dict)


# View used to present Prereqs for a given course
def prereq(request, course_name_url, prereq_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username
        
        # Get course name and prereq name and set course url
        course_name = course_name_url.replace('_', ' ')
        prereq_name = prereq_name_url.replace('_', ' ')
        context_dict = {'course_name': course_name, 'course_name_url': course_name_url,
                        'prereq_name': prereq_name, 'prereq_name_url': prereq_name_url}
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()
        
        # Get all course information for selected course
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass

        # Get all prereq information for selected course
        # prereq info consists of AnswerWithQuestion object with associated AnswerElement 
        try:
            prereq = Prereq.objects.get(course = course)
            context_dict['prereq'] = prereq
            prereq_topics = prereq.topic.all()
            for topic in prereq_topics:
                topic.answer = AnswerElement.objects.filter(answer_with_question=topic)
            context_dict['prereq_topics']= prereq_topics

        except Prereq.DoesNotExist:
            pass
            
        # Display all course related labs in the sidebar
        try:
            context_dict['labs'] = get_lab_list(course, user)
        except Laboratory.DoesNotExist:
            pass
    
        return render(request, 'VLA/prereq.html', context_dict)

    
# View used to present Laboratory and Objectives for a given Course
def lab(request, course_name_url, lab_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username
        
        # Get lab and course name
        lab_name = lab_name_url.replace('_', ' ')
        course_name = course_name_url.replace('_', ' ')
        
        # Set searched flags to false and get complete question and definition lists
        context_dict = {'lab_name': lab_name}
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()
        
        # Get selected course 
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass
        
        # Get selected lab and extract objectives
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict['objectives'] = LabObjective.objects.filter(lab=lab)
            context_dict['equipment'] = LabEquipment.objects.filter(lab=lab)
            
            # Display lab sections in sidebar
            context_dict = get_sections(context_dict, lab)
        except Laboratory.DoesNotExist:
            pass
    
        return render(request, 'VLA/lab.html', context_dict)


# Lab section views: theory, theorytest, simulation, hardward, etc.

# View used for presenting Theory section of a given Laboratory/Course
# Information is presented in the form of text, images, equations, videos, or tables
def theory(request, course_name_url, lab_name_url, theory_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username
    
        # Get course name and lab name
        course_name = course_name_url.replace('_', ' ')
        lab_name = lab_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()
        
        # Get Course and set course URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass
        
        # Get Laboratory, lab sections, and theory elements
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            context_dict['theory_elements'] = TheoryElement.objects.filter(theory=context_dict['theory'])
        except Laboratory.DoesNotExist:
            pass
    
        # If request is a POST, try to pull out relevant information
        # Set is_completed to True
        if request.method == 'POST':
            context_dict['student_progress'].theory_finished = True
            context_dict['student_progress'].save()
        return render(request, 'VLA/theory.html', context_dict)
    
# View used for giving test on theory
# Questions are multiple choice, with at least two choices needed
def theorytest(request, course_name_url, lab_name_url, theorytest_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username
        
        # Get course name and lab name
        course_name = course_name_url.replace('_', ' ')
        lab_name = lab_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}
        
        # Set to true before test is taken, in order to surpress error message
        # If all questions are not answered will be set to false
        context_dict['questions_filled'] = True
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()
        
        # Get course and construct course URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass
        
        # Get lab, lab sections, and theory test questions
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            theorytest_questions = TheoryTestQuestion.objects.filter(theorytest=context_dict['theorytest'])
            context_dict['theorytest_questions'] = theorytest_questions
        except Laboratory.DoesNotExist:
            pass
        
        # If request is a POST, try to pull out relevant information.
        # Checks to see if each question is answered
        # if not return questions_filled=False and send to theorytest.html
        # Assigns each answer to question.given_answer
        if request.method == 'POST':
            num_of_questions = 0
            num_of_correct = 0
            for question in theorytest_questions:
                num_of_questions = num_of_questions + 1
                name = 'choice' + str(num_of_questions)
                if name in request.POST:
                    question.given_answer = int(request.POST[name])
                    question.is_answered = True
                    question.save()
                else:
                    context_dict['questions_filled'] = False
                    context_dict['test_complete'] = False
                    return render(request, 'VLA/theorytest.html', context_dict)
                if question.given_answer == question.correct_answer_number:
                    num_of_correct = num_of_correct + 1
                    
            # Calculate test score            
            context_dict['student_progress'].theory_test_score = num_of_correct/num_of_questions*100

            # Set just_finished and is_completed to True and save
            context_dict['just_finished'] = True
            context_dict['theorytest_questions'] = theorytest_questions
            context_dict['student_progress'].theory_test_finished = True
            context_dict['student_progress'].save()
        else:
            context_dict['just_finished'] = False
        
        return render(request, 'VLA/theorytest.html', context_dict)

# View for displaying directions for circuit simulation
# Information is presented in the form of text, images, equations, videos, or tables
# Simulation results will be recorded in the form of an image uploaded by the User
def simulation(request, course_name_url, lab_name_url, simulation_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username
        
        # Get course name, lab name, and simulation name
        course_name = course_name_url.replace('_', ' ')
        lab_name = lab_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()
        
        # Get course and construct URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass
        
        # Get lab, lab sections, and simulation elements
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            context_dict['simulation_elements'] = SimulationElement.objects.filter(simulation=context_dict['simulation'])
        except Laboratory.DoesNotExist:
            pass
        
        # Send form to view
        context_dict['image_form'] = UserSimulationImage()
        
        # Error message is used to tell user they haven't selected an image to upload
        context_dict['error_message'] = False
        
        # If request is a POST, try to pull out relevant information.
        # Set is_completed to True
        if request.method == 'POST':
            form = UserSimulationImage(request.POST, request.FILES)
            # check if form is valid and image has been selected and is of type PNG
            if form.is_valid() and request.FILES['image'] and request.FILES['image'].name.endswith('.png'):
                context_dict['student_progress'].sim_image = request.FILES['image']
                # Run image processing on uploaded images and return processed image
                # context_dict['student_progress'].sim_image = circuit_recognizer(request.FILES['image'])
                context_dict['student_progress'].simulation_finished = True
                context_dict['student_progress'].save()
            else:
                # User did not select an image
                context_dict['error_message'] = True
        return render(request, 'VLA/simulation.html', context_dict)

# View used for giving test on simulation
# Questions are multiple choice, with at least two choices needed
def simulationtest(request, course_name_url, lab_name_url, simulationtest_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username
        
        # Get lab name, course name, an simulation test name
        lab_name = lab_name_url.replace('_', ' ')
        course_name = course_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}
        
        # Set to true before test is taken, in order to surpress error message
        # If all questions are not answered will be set to false
        context_dict['questions_filled'] = True
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()
        
        # Get course and construct URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass
        
        # Get lab, lab sections, and simulation test questions
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            simulationtest_questions = SimulationTestQuestion.objects.filter(simulationtest=context_dict['simulationtest'])
            context_dict['simulationtest_questions'] = simulationtest_questions
        except Laboratory.DoesNotExist:
            pass
        
        # If request is a POST, try to pull out relevant information.
        # Checks to see if each question is answered
        # if not return questions_filled=False and send to theorytest.html
        # Assigns each answer to question.given_answer
        if request.method == 'POST':
            num_of_questions = 0
            num_of_correct = 0
            for question in simulationtest_questions:
                num_of_questions = num_of_questions + 1
                name = 'choice' + str(num_of_questions)
                if name in request.POST:
                    question.given_answer = int(request.POST[name])
                    question.is_answered = True
                    question.save()
                else:
                    context_dict['questions_filled'] = False
                    context_dict['test_complete'] = False
                    return render(request, 'VLA/simulationtest.html', context_dict)
                if question.given_answer == question.correct_answer_number:
                    num_of_correct = num_of_correct + 1
                    
            # Calculate test score            
            context_dict['student_progress'].sim_test_score = num_of_correct/num_of_questions*100
            
            # Set just_finished and is_completed to True and save
            context_dict['just_finished'] = True
            context_dict['simulationtest_questions'] = simulationtest_questions
            context_dict['student_progress'].sim_test_finished = True
            context_dict['student_progress'].save()
    
        return render(request, 'VLA/simulationtest.html', context_dict)
    
# View for displaying directions for hardware experiment
# Information is presented in the form of text, images, equations, videos, or tables
def hardware(request, course_name_url, lab_name_url, hardware_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username
        
        # Get course name and lab name
        course_name = course_name_url.replace('_', ' ')
        lab_name = lab_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()
        
        # Get course and construct URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass
        
        # Get lab, lab sections, and hardware elements
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            context_dict['hardware_elements'] = HardwareElement.objects.filter(hardware=context_dict['hardware'])
        except Laboratory.DoesNotExist:
            pass
    
        # If request is a POST, try to pull out relevant information.
        # Set is_completed to True
        if request.method == 'POST':
            context_dict['student_progress'].hardware_finished = True
            context_dict['student_progress'].save()
        return render(request, 'VLA/hardware.html', context_dict)

# NEEDS TO BE FINISHED
# View for displaying forms for user to input hardware results
# The information entered by the user will added to a generated Word document
def results(request, course_name_url, lab_name_url, results_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username
        
        # Get course name and lab name
        course_name = course_name_url.replace('_', ' ')
        lab_name = lab_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()
        
        # Get course and construct URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass
        
        # Get lab, lab sections, and hardware elements
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            results_questions = ResultsQuestions.objects.filter(results=context_dict['results'])
            context_dict['results_questions'] = results_questions
        except Laboratory.DoesNotExist:
            pass
    
        # If request is a POST, try to pull out relevant information.
        # Set is_completed to True
        if request.method == 'POST':
            context_dict['student_progress'].results_finished = True
            context_dict['student_progress'].save()
        return render(request, 'VLA/results.html', context_dict)

# View used for giving test on simulation
# Questions are multiple choice, with at least two choices needed
def labtest(request, course_name_url, lab_name_url, labtest_name_url):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username
        
        # Get lab name, course name, an simulation test name
        lab_name = lab_name_url.replace('_', ' ')
        course_name = course_name_url.replace('_', ' ')
        context_dict = {'lab_name': lab_name}
        
        # Set to true before test is taken, in order to surpress error message
        # If all questions are not answered will be set to false
        context_dict['questions_filled'] = True
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()
        
        # Get course and construct URL
        try:
            course = Course.objects.get(name=course_name)
            course.url = course_name_url
            context_dict['course'] = course
        except Course.DoesNotExist:
            pass
        
        # Get lab, lab sections, and simulation test questions
        try:
            lab = Laboratory.objects.filter(course=course).get(name=lab_name)
            lab.url = lab_name_url
            context_dict['lab'] = lab
            context_dict['student_progress'] = LabProgress.objects.filter(user=user).get(lab=lab)
            context_dict = get_sections(context_dict, lab)
            labtest_questions = LabTestQuestion.objects.filter(labtest=context_dict['labtest'])
            context_dict['labtest_questions'] = labtest_questions
        except Laboratory.DoesNotExist:
            pass
        
        # If request is a POST, try to pull out relevant information.
        # Checks to see if each question is answered
        # if not return questions_filled=False and send to theorytest.html
        # Assigns each answer to question.given_answer
        if request.method == 'POST':
            num_of_questions = 0
            num_of_correct = 0
            for question in labtest_questions:
                num_of_questions = num_of_questions + 1
                name = 'choice' + str(num_of_questions)
                if name in request.POST:
                    question.given_answer = int(request.POST[name])
                    question.is_answered = True
                    question.save()
                else:
                    context_dict['questions_filled'] = False
                    context_dict['test_complete'] = False
                    return render(request, 'VLA/labtest.html', context_dict)
                if question.given_answer == question.correct_answer_number:
                    num_of_correct = num_of_correct + 1
                    
            # Calculate test score            
            context_dict['student_progress'].lab_test_score = num_of_correct/num_of_questions*100
            
            # Set just_finished and is_completed to True and save
            context_dict['just_finished'] = True
            context_dict['labtest_questions'] = labtest_questions
            context_dict['student_progress'].lab_test_finished = True
            context_dict['student_progress'].save()
    
        return render(request, 'VLA/labtest.html', context_dict)


# Get permissible course list and create URLs
def get_course_list(user):
    permissions = CoursePermission.objects.filter(user=user)
    cour_list = []
    for permission in permissions:
        cour_list.append(permission.course)

    for cour in cour_list:
        cour.url = cour.name.replace(' ', '_')
    return cour_list

# Get complete lab list for a given course and create URLs
def get_lab_list(course, user):
    lab_list = []
    permissions = LabProgress.objects.filter(user=user)
    for permission in permissions:
        if permission.lab.course == course:
            lab_list.append(permission.lab)
    
    for lab in lab_list:
        lab.url = lab.name.replace(' ', '_')
        
    return lab_list

# Get complete section list for a given lab and create URLs
def get_sections(context_dict, lab):
    try:
        theory = Theory.objects.filter(lab=lab).get(lab=lab)
        theory.url = theory.name.replace(' ', '_')
        context_dict['theory'] = theory
    except Theory.DoesNotExist:
        pass
    try:
        theorytest = TheoryTest.objects.filter(lab=lab).get(lab=lab)
        theorytest.url = theorytest.name.replace(' ', '_')
        context_dict['theorytest'] = theorytest
    except TheoryTest.DoesNotExist:
        pass
    try:
        simulation = Simulation.objects.filter(lab=lab).get(lab=lab)
        simulation.url = simulation.name.replace(' ', '_')
        context_dict['simulation'] = simulation
    except Simulation.DoesNotExist:
        pass    
    try:
        simulationtest = SimulationTest.objects.filter(lab=lab).get(lab=lab)
        simulationtest.url = simulationtest.name.replace(' ', '_')
        context_dict['simulationtest'] = simulationtest
    except SimulationTest.DoesNotExist:
        pass
    try:
        hardware = Hardware.objects.filter(lab=lab).get(lab=lab)
        hardware.url = hardware.name.replace(' ', '_')
        context_dict['hardware'] = hardware
    except Hardware.DoesNotExist:
        pass
    try:
        results = Results.objects.filter(lab=lab).get(lab=lab)
        results.url = results.name.replace(' ', '_')
        context_dict['results'] = results
    except Results.DoesNotExist:
        pass
    try:
        labtest = LabTest.objects.filter(lab=lab).get(lab=lab)
        labtest.url = labtest.name.replace(' ', '_')
        context_dict['labtest'] = labtest
    except LabTest.DoesNotExist:
        pass
    
    return context_dict



# NOT WORKING
# Incomplete method used for extracting text elements from elements
# and replacing all keywords with mouseover definitions and links
def replace_with_definitions(elements):
    # get all useful definitions
    topic_list = VocabTopic.objects.filter(def_useful=False)
    def_list = Node.objects.all().exclude(topic__in=topic_list)
    
    # split text into list of words
    for element in elements:
        if element.element_type == 'text':
            words = element.text_input.split()
            for definition in def_list:
                if definition.word in words:
                    words = [w.replace(definition.word, definition.word) for w in words]
                #words = [word.replace(word, 'aaa')]
        # join words
        joined_words = '--'.join(words)
        element.text_input = joined_words
    
    return elements

###
#def GenerateDocument(request):
#    
#    document = Document()
#    docx_title="TEST_DOCUMENT.docx"
#    # ---- Cover Letter ----
#    document.add_picture((r'%s/static/images/my-header.png' % (settings.PROJECT_PATH)), width=Inches(4))
#    document.add_paragraph()
#    document.add_paragraph("%s" % date.today().strftime('%B %d, %Y'))
#
#    document.add_paragraph('Dear Sir or Madam:')
#    document.add_paragraph('We are pleased to help you with your widgets.')
#    document.add_paragraph('Please feel free to contact me for any additional information.')
#    document.add_paragraph('I look forward to assisting you in this project.')
#
#    document.add_paragraph()
#    document.add_paragraph('Best regards,')
#    document.add_paragraph('Acme Specialist 1]')
#    document.add_page_break()
#
#    # Prepare document for download        
#    # -----------------------------
#    f = StringIO()
#    document.save(f)
#    length = f.tell()
#    f.seek(0)
#    response = HttpResponse(
#        f.getvalue(),
#        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
#    )
#    response['Content-Disposition'] = 'attachment; filename=' + docx_title
#    response['Content-Length'] = length
#    return response


# Classes and Methods for image processing of circuit image
class Component:
    def set_component(self,type, term1, term2, index):
        self.type = type
        self.term1 = term1
        self.term2 = term2
        self.node1 = -1
        self.node2 = -1
        self.connections = []
        self.value = 0
        self.index = index
                
    def print_component(self):
        print "{" + " Type\t\t => " + str(self.type) + "\t\t}"
        print "{" + " Term1\t\t => " + str(self.term1) + "\t}"
        print "{" + " Term2\t\t => " + str(self.term2) + "\t}"
        print "{" + " Node1\t\t => " + str(self.node1) + "\t\t}"
        print "{" + " Node2\t\t => " + str(self.node2) + "\t\t}"
        print "{" + " Value\t\t => " + str(self.value) + "\t\t}"
        print "{" + " Connections\t => " + str( len(self.connections)) +"\t\t}"
        print "{" + " Index \t => " + str(self.index) + "\t\t}"
        print "------------------------------------------"
                
    def add_connections(self, adj_comp):
        if (self.check_duplicate(adj_comp)):
            return
        else: 
            self.connections.append(adj_comp.index)

    def check_duplicate(adj_comp):
        for x in self.connections:
            if adj_comp.index == x: return False
            else: return True

def area_thresholding(thresh):
    thresh_src = np.zeros((thresh.shape[0], thresh.shape[1],3), np.uint8)
    thresh_src[:] = (255,255,255)
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    area_thresh = 100
    for x in range(0,len(contours)):
        if len(contours[x]) > 100:
            cv2.drawContours(thresh_src,contours, x, (0,0,0), 1)
    cv2.imwrite("Area Thresh.png", thresh_src)
    return thresh_src

def calculate_distance(comp1pt1, comp1pt2, comp2pt1, comp2pt2):
    dist_pt11 = math.sqrt(math.pow((comp1pt1[0] - comp2pt1[0]),2) + math.pow((comp1pt1[1] - comp2pt1[1]),2))
    dist_pt12 = math.sqrt(math.pow((comp1pt1[0] - comp2pt2[0]),2) + math.pow((comp1pt1[1] - comp2pt2[1]),2))
    dist_pt21 = math.sqrt(math.pow((comp1pt2[0] - comp2pt1[0]),2) + math.pow((comp1pt2[1] - comp2pt1[1]),2))
    dist_pt22 = math.sqrt(math.pow((comp1pt2[0] - comp2pt2[0]),2) + math.pow((comp1pt2[1] - comp2pt2[1]),2))
    return (dist_pt11,dist_pt12,dist_pt21,dist_pt22)

def check_terminals():
    return;

def check_wires():
    return;

def conjoin_wires():
    return;

def fix_wires():
    return;

def intersection_operations(comp_under_test, comp_list, wire_list):
    # Create individual arrays for each component
    gnd_count = 0; vsrc_count = 0; isrc_count = 0; res_count = 0; ind_count = 0; cap_count = 0;
    
    # Iterate through components
    
    return;

def list_traversal():
    return;

def print_netlist():
    return;

def test_template_method(not_black, templates):
    # Read in RGB img and initialize variables
    src = cv2.imread('Contours.png',-1)
    blank = np.zeros((src.shape[0],src.shape[1],3),np.uint8)
    blank[:] = (255,255,255)
    index = 0
    comp_tup = ([])
    comp_list = []; wire_list = []; super_list = [];
    #Iterate over all template images
    for x in templates:
        # Set type of component
        if "ground" in x       : type = "Gnd"
        elif "capacitor" in x : type = "C"
        elif "inductor" in x   : type = "L"
        elif "resistor" in x    : type = "R"
        elif "vsource" in x   : type = "Vsrc"
        elif "isource" in x    : type = "Isrc"
        elif "wire" in x        : type = "Wire"
        else: type = "none"
        # Apply template matching
        threshold = 0.72
        copycat = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
        template = cv2.imread(x, 0)
        res = cv2.matchTemplate(copycat, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where (res >= threshold)
        w,h = template.shape[::-1]
        loc = np.where( res >= threshold)
        # Iterate over matches, creating rectangles
        for pt in zip(*loc[::-1]):
            dont_draw = False
            temp_comp = Component()
            # Set terminal points
            if w > h   and "vsource0" not in x:
                term1 = (pt[0],pt[1]+h/2) 
                term2 = (pt[0] + w, pt[1] + h/2)
            else: 
                term1 =  (pt[0] + w/2, pt[1]) 
                term2 =  (pt[0] + w/2, pt[1] + h)
            if "ground" in x:
                    term1 = term2
            # Iterate over lists, trying to delete any unnecessary wires
            if type == "Wire":
                for iter_comp in comp_list:
                    # If term1[0] (temp_comp X) is between any X and Y, don't draw 
                    if term2[0] <= iter_comp.term2[0] and term1[0] >= iter_comp.term1[0] and term1[1]  >= iter_comp.term1[1] and term2[1] <= iter_comp.term2[1]:
                        dont_draw = True
            if type == "Wire":
                for iter_wire in wire_list:
                    # If Both Y are within 2 pix, and starting term within 5 pix, don't draw
                    if term1[1] - 2 <= iter_wire.term1[1] and term1[1] + 2 >= iter_wire.term1[1] and term1[0] - 5 <= iter_wire.term1[0] and term1[0] + 5 >= iter_wire.term1[0]:
                        dont_draw = True
                    # If both X are within 2 pix, and starting term within 5 pix, don't draw
                    if term1[0] -2 <= iter_wire.term1[0] and term1[0] + 2 >= iter_wire.term1[0] and term1[1] - 5 <= iter_wire.term1[1] and term1[1] + 5 >= iter_wire.term1[1]:
                        dont_draw = True
                    # Iterate over comp list to make sure wire is not inside rect 
                                
                    for iter_comp in comp_list:
                        if term1[0] in range(iter_comp.vertex[0]-2, iter_comp.vertex[0] + iter_comp.cols+4) and term1[1] in range(iter_comp.vertex[1]-4, iter_comp.vertex[1] + iter_comp.rows+4):
                            if term2[0] in range(iter_comp.vertex[0]-2, iter_comp.vertex[0] + iter_comp.cols+4) and term2[1] in range(iter_comp.vertex[1]-4, iter_comp.vertex[1] + iter_comp.rows+4):
                                dont_draw = True
            # Check distance in 
            for comp in super_list:
                (pt_11,pt_12,pt_21,pt_22) =  calculate_distance(comp.term1, comp.term2, comp.term1, comp.term2)
                if pt_11 == 0 or pt_12==0 or pt_21==0 or pt_22 == 0:
                    continue
                elif pt_11 <= 5 or pt_12 <= 5 or pt_21 <= 5 or pt_22 <= 5:
                    dont_draw = True

            # Ignore components which have triggered one of the if statements
            if (dont_draw):
                continue

            # Add component to the list         
            temp_comp.set_component(type,term1,term2,index)
               
            if type != "Wire":
                temp_comp.cols = w; temp_comp.rows = h; temp_comp.vertex = pt
                comp_list.append(temp_comp)
                super_list.append(temp_comp)
            else: 
                wire_list.append(temp_comp)
                super_list.append(temp_comp)
                
            # Draw Rectangles
            cv2.rectangle(blank, pt, (pt[0] + w, pt[1] + h), (0,0,255),2)
            cv2.rectangle(src,pt,(pt[0] + w, pt[1] + h), (0,0,255),2)
            # Increment the index of the component
            index += 1

        # Write final image:
        cv2.imwrite('res.png', blank)

    return (super_list, blank)

def get_erosion_element():
    return;

def circuit_recognizer(argv):
    #Make Template List
    templates = []
    templates.append("capacitor0.png")
    templates.append("capacitor90.png")
    templates.append("inductor0.PNG")
    templates.append("inductor90.png")
    templates.append("inductor180.png")
    templates.append("inductor270.png")
    templates.append("vsource0.png")
    templates.append("vsource90.png")
    templates.append("vsource180.png")
    templates.append("vsource270.png")
    templates.append("isource0.png") 
    templates.append("isource90.png")
    templates.append("isource180.png")
    templates.append("isource270.png")
    templates.append("resistor0.png")
    templates.append("resistor90.PNG")
    templates.append("ground0.png")
    templates.append("ground90.PNG")
    templates.append("ground180.PNG")
    templates.append("ground270.PNG")
    templates.append("wire0.PNG")
    templates.append("wire90.PNG")
        
    # Create color arrays
    black = np.array([0,0,0])
    not_black = np.array([100,100,100])
    white = np.array([255,255,255])
        
    # Read in source
    source = cv2.imread(argv[1],-1)
    width,height = source.shape[:2]
    
    # Create blank matrix
    blank = np.zeros((width,height,3), np.uint8) 
    blank[:] = white
    cv2.imwrite("blank.png",blank)
    
    # Apply thresholding
    hsv =  cv2.cvtColor(source, cv2.COLOR_BGR2HSV)
    upper_thresh = np.array([215,215,215])
    lower_thresh = np.array([0,0,0])
    thresh = cv2.inRange(hsv, lower_thresh,upper_thresh)
    cv2.imwrite("inrange.png", thresh)

    # Draw contours onto copycat image
    copycat = blank.copy()
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(copycat,contours, -1, lower_thresh, 1)
    cv2.imwrite("Contours.png", copycat)
    # Apply Template Matching & Area Thresholding
    super_list = []; comp_list = []; wire_list = []
    super_list,matched_src = test_template_method(not_black, templates)
    # Split the lists in to wire and component lists
    for temp_comp in super_list:
            if temp_comp.type == "Wire":
                    wire_list.append(temp_comp)
            else:
                    comp_list.append(temp_comp)
                    temp_comp.print_component()
    # Apply area thresholding to remove text
    thresh_src = area_thresholding(thresh)
    final_src = cv2.addWeighted(thresh_src,0.5,matched_src,0.5,0)
    cv2.imwrite("add weighted.png", final_src)
    #  Connect Components
    intersection_operations(super_list, comp_list, wire_list)
