from __future__ import absolute_import
import re
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserProfileForm
from .models import *

def index(request):
    # Display course list in sidebar
    cour_list = get_course_list()
    context_dict = {'cour_list': cour_list}
    
    # Set searched flags to false and get complete question and definition lists
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    context_dict['question_searched'] = False
    context_dict['question_list'] = AnswerWithQuestion.objects.all()
    
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/index.html', context_dict)

# View used to display About information on VLA
def about(request):
    # Display course list in sidebar
    cour_list = get_course_list()
    context_dict = {'cour_list': cour_list}
    
    # Set searched flags to false and get complete question and definition lists
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    context_dict['question_searched'] = False
    context_dict['question_list'] = AnswerWithQuestion.objects.all()
    
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        context_dict['logged_in'] = False
    else:
        context_dict['logged_in'] = True
    return render(request, 'VLA/about.html', context_dict)

# View used to present Course with all course, instructor, TA info
def course(request, course_name_url):
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
    
    # Display all course related labs in the sidebar
    try:
        context_dict['labs'] = get_lab_list(course)
    except Laboratory.DoesNotExist:
        pass
    
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/course.html', context_dict)
    
# View used to present Laboratory and Objectives for a given Course
def lab(request, course_name_url, lab_name_url):
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
        context_dict['objectives'] = LabObjective.objects.filter(lab=lab)
        context_dict['equipment'] = LabEquipment.objects.filter(lab=lab)
        
        # Display lab sections in sidebar
        context_dict = get_sections(context_dict, lab)
    except Laboratory.DoesNotExist:
        pass
    
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/lab.html', context_dict)


# Lab section views: theory, theorytest, simulation, hardward, etc.

# View used for presenting Theory section of a given Laboratory/Course
# Information is presented in the form of text, images, equations, videos, or tables
def theory(request, course_name_url, lab_name_url, theory_name_url):
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
        context_dict = get_sections(context_dict, lab)
        context_dict['theory_elements'] = TheoryElement.objects.filter(theory=context_dict['theory'])
    except Laboratory.DoesNotExist:
        pass
    
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # If request is a POST, try to pull out relevant information
        # Set is_completed to True
        if request.method == 'POST':
            context_dict['theory'].is_completed = True
            context_dict['theory'].save()
        return render(request, 'VLA/theory.html', context_dict)
    
# View used for giving test on theory
# Questions are multiple choice, with at least two choices needed
def theorytest(request, course_name_url, lab_name_url, theorytest_name_url):
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
        counter = 0
        for question in theorytest_questions:
            counter = counter + 1
            name = 'choice' + str(counter)
            if name in request.POST:
                question.given_answer = int(request.POST[name])
                question.is_answered = True
                question.save()
            else:
                context_dict['questions_filled'] = False
                context_dict['test_complete'] = False
                return render(request, 'VLA/theorytest.html', context_dict)
        # Set just_finished and is_completed to True and save
        context_dict['just_finished'] = True
        context_dict['theorytest_questions'] = theorytest_questions
        context_dict['theorytest'].is_completed = True
        context_dict['theorytest'].save()
    else:
        context_dict['just_finished'] = False
        
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/theorytest.html', context_dict)

# View for displaying directions for circuit simulation
# Information is presented in the form of text, images, equations, videos, or tables
# Simulation results will be recorded in the form of an image uploaded by the User
def simulation(request, course_name_url, lab_name_url, simulation_name_url):
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
        context_dict = get_sections(context_dict, lab)
        context_dict['simulation_elements'] = SimulationElement.objects.filter(simulation=context_dict['simulation'])
    except Laboratory.DoesNotExist:
        pass
    
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # If request is a POST, try to pull out relevant information.
        # Set is_completed to True
        if request.method == 'POST':
            context_dict['simulation'].is_completed = True
            context_dict['simulation'].save()
        return render(request, 'VLA/simulation.html', context_dict)

# View used for giving test on simulation
# Questions are multiple choice, with at least two choices needed
def simulationtest(request, course_name_url, lab_name_url, simulationtest_name_url):
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
        counter = 0
        for question in simulationtest_questions:
            counter = counter + 1
            name = 'choice' + str(counter)
            if name in request.POST:
                question.given_answer = int(request.POST[name])
                question.is_answered = True
                question.save()
            else:
                context_dict['questions_filled'] = False
                context_dict['test_complete'] = False
                return render(request, 'VLA/simulationtest.html', context_dict)
        # Set just_finished and is_completed to True and save
        context_dict['just_finished'] = True
        context_dict['simulationtest_questions'] = simulationtest_questions
        context_dict['simulationtest'].is_completed = True
        context_dict['simulationtest'].save()
    
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/simulationtest.html', context_dict)
    
# View for displaying directions for hardware experiment
# Information is presented in the form of text, images, equations, videos, or tables
def hardware(request, course_name_url, lab_name_url, hardware_name_url):
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
        context_dict = get_sections(context_dict, lab)
        context_dict['hardware_elements'] = HardwareElement.objects.filter(hardware=context_dict['hardware'])
    except Laboratory.DoesNotExist:
        pass
    
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # If request is a POST, try to pull out relevant information.
        # Set is_completed to True
        if request.method == 'POST':
            context_dict['hardware'].is_completed = True
            context_dict['hardware'].save()
        return render(request, 'VLA/hardware.html', context_dict)

# NEEDS TO BE FINISHED
# View for displaying forms for user to input hardware results
# The information entered by the user will added to a generated Word document
def results(request, course_name_url, lab_name_url, results_name_url):
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
        context_dict = get_sections(context_dict, lab)
        results_questions = ResultsQuestions.objects.filter(results=context_dict['results'])
        context_dict['results_questions'] = results_questions
    except Laboratory.DoesNotExist:
        pass
    
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # If request is a POST, try to pull out relevant information.
        # Set is_completed to True
        if request.method == 'POST':
            context_dict['results'].is_completed = True
            context_dict['results'].save()
        return render(request, 'VLA/results.html', context_dict)
    
# NEEDS TO BE FINISHED
# View for displaying questions about results
# These questions and their given answers will added to a generated Word document
def resultsquestions(request, course_name_url, lab_name_url):
    # Get course name and lab name
    course_name = course_name_url.replace('_', ' ')
    lab_name = lab_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    
    # Set searched flags to false and get complete question and definition lists
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    context_dict['question_searched'] = False
    context_dict['question_list'] = AnswerWithQuestion.objects.all()
    
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/resultsquestions.html', context_dict)

# Login, register, and profile views
def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If request is a POST, try to pull out relevant information.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'VLA/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    # If request is a POST, try to pull out relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/VLA/')
            else:
                # An inactive account was used - no logging in!
                context_dict = {'disabled_account': True}
                return render(request, 'VLA/login.html', context_dict)
        else:
            # Bad login details were provided. So we can't log the user in.
            context_dict = {'error': True}
            return render(request, 'VLA/login.html', context_dict)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        context_dict = {'error': False, 'disabled_account': False}
        return render(request, 'VLA/login.html', context_dict)

def profile(request, user_name_url):
    # Display course list in sidebar
    cour_list = get_course_list()
    context_dict = {'cour_list': cour_list}
    user_name = user_name_url.replace('_', ' ')
    
    
    # Set searched flags to false and get complete question and definition lists
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    context_dict['question_searched'] = False
    context_dict['question_list'] = AnswerWithQuestion.objects.all()
    try:
        if not User.objects.get(username=user_name):
            return render(request, 'VLA/login.html')
        else:
            this_user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        pass
    
    try: 
        context_dict['user_info'] = UserProfile.objects.get(user=this_user)
    except UserProfile.DoesNotExist:
        context_dict['user_info'] = ''
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/profile.html', context_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/VLA')

# Get complete course list and create URLs
def get_course_list():
    cour_list = Course.objects.all().order_by('subj', 'course_number')

    for cour in cour_list:
        cour.url = cour.name.replace(' ', '_')
    return cour_list

# Get complete lab list for a given course and create URLs
def get_lab_list(course):
    lab_list = Laboratory.objects.filter(course=course).order_by('lab_number')
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

