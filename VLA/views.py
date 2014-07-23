from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from VLA.forms import CourseForm, UserForm
from VLA.models import Course, Laboratory, Theory, Pretest, Prelab, PrelabTest, Hardware, HardwareElement, Results
from VLA.models import PretestQuestion, ResultsQuestions, TheoryElement, LabObjective, PrelabElement, PrelabTestQuestion
from VLA.models import VocabDomain, VocabTopic, Node, Synonym

def index(request):
    course_list = Course.objects.order_by('subj')
    cour_list = get_course_list()
    context_dict = {'courses': course_list}
    context_dict['cour_list'] = cour_list
    
    for course in course_list:
        course.url = course.name.replace(' ', '_')
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/index.html', context_dict)

def about(request):
    cour_list = get_course_list()
    context_dict = {'cour_list': cour_list}
    if not request.user.is_authenticated():
        context_dict['logged_in'] = False
    else:
        context_dict['logged_in'] = True
    return render(request, 'VLA/about.html', context_dict)
    #return HttpResponse("Lou Says: I like to eat bones. <a href='/VLA/'>BACK</a>")

def help(request):
    cour_list = get_course_list()
    context_dict = {'cour_list': cour_list}
    #topic_list = get_topic_list()
    #question_list = get_question_list()
    #context_dict = {'topic_list': topic_list, 'question_list': question_list}
    context_dict['def_topics'] = VocabTopic.objects.filter(def_useful=True).order_by('topic')
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        context_dict['logged_in'] = True
        return render(request, 'VLA/help.html', context_dict)

def course(request, course_name_url):
    course_name = course_name_url.replace('_', ' ')
    context_dict = {'course_name': course_name, 'course_name_url': course_name_url}
    try:
        course = Course.objects.get(name=course_name)
        labs = Laboratory.objects.filter(course=course).order_by('lab_number')
        for lab in labs:
            lab.url = lab.name.replace(' ', '_')
        context_dict['labs'] = labs
        context_dict['course'] = course
    except Course.DoesNotExist:
        pass
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/course.html', context_dict)
    
def lab(request, course_name_url, lab_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    try:
        course = Course.objects.get(name=course_name)
        lab = Laboratory.objects.filter(course=course).get(name=lab_name)
        lab.url = lab_name_url
        course.url = course_name_url
        context_dict['lab'] = lab
        context_dict['course'] = course
        context_dict['objectives'] = LabObjective.objects.filter(lab=lab)
        context_dict = get_sections(context_dict, lab)
    except Course.DoesNotExist:
        pass
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/lab.html', context_dict)

def theory(request, course_name_url, lab_name_url, theory_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    theory_name = theory_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    try:
        course = Course.objects.get(name=course_name)
        lab = Laboratory.objects.filter(course=course).get(name=lab_name)
        lab.url = lab_name_url
        course.url = course_name_url
        context_dict['lab'] = lab
        context_dict['course'] = course
        context_dict = get_sections(context_dict, lab)
        context_dict['theory_elements'] = TheoryElement.objects.filter(theory=context_dict['theory'])
    except Course.DoesNotExist:
        pass
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/theory.html', context_dict)
    
def pretest(request, course_name_url, lab_name_url, pretest_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    pretest_name = pretest_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    if request.method == 'POST':
        context_dict['test_complete'] = True
        context_dict['choice'] = (request.POST['choice1'], request.POST['choice2'], request.POST['choice3'])
    else:
        context_dict['test_complete'] = False
    try:
        course = Course.objects.get(name=course_name)
        lab = Laboratory.objects.filter(course=course).get(name=lab_name)
        lab.url = lab_name_url
        course.url = course_name_url
        context_dict['lab'] = lab
        context_dict['course'] = course
        context_dict = get_sections(context_dict, lab)
        context_dict['pretest_questions'] = PretestQuestion.objects.filter(pretest=context_dict['pretest'])
    except Course.DoesNotExist:
        pass
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/pretest.html', context_dict)

def prelab(request, course_name_url, lab_name_url, prelab_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    prelab_name = prelab_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    try:
        course = Course.objects.get(name=course_name)
        lab = Laboratory.objects.filter(course=course).get(name=lab_name)
        lab.url = lab_name_url
        course.url = course_name_url
        context_dict['lab'] = lab
        context_dict['course'] = course
        context_dict = get_sections(context_dict, lab)
        context_dict['prelab_elements'] = PrelabElement.objects.filter(prelab=context_dict['prelab'])
    except Course.DoesNotExist:
        pass
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/prelab.html', context_dict)

    
def prelabtest(request, course_name_url, lab_name_url, prelabtest_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    prelabtest_name = prelabtest_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    try:
        course = Course.objects.get(name=course_name)
        lab = Laboratory.objects.filter(course=course).get(name=lab_name)
        lab.url = lab_name_url
        course.url = course_name_url
        context_dict['lab'] = lab
        context_dict['course'] = course
        context_dict = get_sections(context_dict, lab)
        context_dict['prelabtest_questions'] = PrelabTestQuestion.objects.filter(prelabtest=context_dict['prelabtest'])
    except Course.DoesNotExist:
        pass
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/prelabtest.html', context_dict)
    
def hardware(request, course_name_url, lab_name_url, hardware_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    hardware_name = hardware_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    try:
        course = Course.objects.get(name=course_name)
        lab = Laboratory.objects.filter(course=course).get(name=lab_name)
        lab.url = lab_name_url
        course.url = course_name_url
        context_dict['lab'] = lab
        context_dict['course'] = course
        context_dict = get_sections(context_dict, lab)
        context_dict['hardware_elements'] = HardwareElement.objects.filter(hardware=context_dict['hardware'])
    except Course.DoesNotExist:
        pass
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/hardware.html', context_dict)


def results(request, course_name_url, lab_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/results.html', context_dict)
    
def resultsquestions(request, course_name_url, lab_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/resultsquestions.html', context_dict)

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CourseForm()
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/add_course.html', {'form': form})

def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        #profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid(): #and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            #profile = profile_form.save(commit=False)
            #profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            #profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors#, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        #profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'VLA/register.html',
            {'user_form': user_form, 'registered': registered})
            #{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
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
                return HttpResponse("Your VLA account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'VLA/login.html')

@login_required
def restricted(request):
    return render(request, 'VLA/restricted.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/VLA')

def get_course_list():
    cour_list = Course.objects.all().order_by('subj', 'course_number')

    for cour in cour_list:
        cour.url = cour.name.replace(' ', '_')
    return cour_list

def get_sections(context_dict, lab):
    try:
        theory = Theory.objects.filter(lab=lab).get(lab=lab)
        theory.url = theory.name.replace(' ', '_')
        context_dict['theory'] = theory
    except Theory.DoesNotExist:
        pass
    try:
        pretest = Pretest.objects.filter(lab=lab).get(lab=lab)
        pretest.url = pretest.name.replace(' ', '_')
        context_dict['pretest'] = pretest
    except Pretest.DoesNotExist:
        pass
    try:
        prelab = Prelab.objects.filter(lab=lab).get(lab=lab)
        prelab.url = pretest.name.replace(' ', '_')
        context_dict['prelab'] = prelab
    except Prelab.DoesNotExist:
        pass    
    try:
        prelabtest = PrelabTest.objects.filter(lab=lab).get(lab=lab)
        prelabtest.url = prelabtest.name.replace(' ', '_')
        context_dict['prelabtest'] = prelabtest
    except PrelabTest.DoesNotExist:
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
        resultsquestions = ResultsQuestions.objects.filter(lab=lab).get(lab=lab)
        resultsquestions.url = resultsquestions.name.replace(' ', '_')
        context_dict['results_questions'] = resultsquestions
    except ResultsQuestions.DoesNotExist:
        pass
    return context_dict
