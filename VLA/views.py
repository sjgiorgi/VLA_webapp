from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from VLA.forms import CourseForm, UserForm
from VLA.models import Course, Laboratory, Theory, TheoryTest, Simulation, SimulationTest, Hardware, HardwareElement, Results
from VLA.models import TheoryTestQuestion, ResultsQuestions, TheoryElement, LabObjective, SimulationElement, SimulationTestQuestion
from VLA.models import VocabDomain, VocabTopic, Node, Synonym

def index(request):
    cour_list = get_course_list()
    context_dict = {'cour_list': cour_list}
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/index.html', context_dict)


def about(request):
    cour_list = get_course_list()
    context_dict = {'cour_list': cour_list}
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    if not request.user.is_authenticated():
        context_dict['logged_in'] = False
    else:
        context_dict['logged_in'] = True
    return render(request, 'VLA/about.html', context_dict)


def course(request, course_name_url):
    course_name = course_name_url.replace('_', ' ')
    context_dict = {'course_name': course_name, 'course_name_url': course_name_url}
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    try:
        course = Course.objects.get(name=course_name)
        context_dict['course'] = course
    except Course.DoesNotExist:
        pass
    try:
        labs = Laboratory.objects.filter(course=course).order_by('lab_number')
        for lab in labs:
            lab.url = lab.name.replace(' ', '_')
        context_dict['labs'] = labs
    except Laboratory.DoesNotExist:
        pass
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/course.html', context_dict)
    
def lab(request, course_name_url, lab_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
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
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
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
        if request.method == 'POST':
            context_dict['theory'].is_completed = True
            context_dict['theory'].save()
        return render(request, 'VLA/theory.html', context_dict)
    
def theorytest(request, course_name_url, lab_name_url, theorytest_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    theorytest_name = theorytest_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    context_dict['questions_filled'] = True
    try:
        course = Course.objects.get(name=course_name)
        lab = Laboratory.objects.filter(course=course).get(name=lab_name)
        lab.url = lab_name_url
        course.url = course_name_url
        context_dict['lab'] = lab
        context_dict['course'] = course
        context_dict = get_sections(context_dict, lab)
        theorytest_questions = TheoryTestQuestion.objects.filter(theorytest=context_dict['theorytest'])
        context_dict['theorytest_questions'] = theorytest_questions
    except Course.DoesNotExist:
        pass
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
        context_dict['just_finished'] = True
        context_dict['theorytest_questions'] = theorytest_questions
        context_dict['theorytest'].is_completed = True
        context_dict['theorytest'].save()
    else:
        context_dict['just_finished'] = False
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/theorytest.html', context_dict)

def simulation(request, course_name_url, lab_name_url, simulation_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    simulation_name = simulation_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    try:
        course = Course.objects.get(name=course_name)
        lab = Laboratory.objects.filter(course=course).get(name=lab_name)
        lab.url = lab_name_url
        course.url = course_name_url
        context_dict['lab'] = lab
        context_dict['course'] = course
        context_dict = get_sections(context_dict, lab)
        context_dict['simulation_elements'] = SimulationElement.objects.filter(simulation=context_dict['simulation'])
    except Course.DoesNotExist:
        pass
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        if request.method == 'POST':
            context_dict['simulation'].is_completed = True
            context_dict['simulation'].save()
        return render(request, 'VLA/simulation.html', context_dict)

def simulationtest(request, course_name_url, lab_name_url, simulationtest_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    simulationtest_name = simulationtest_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    context_dict['questions_filled'] = True
    try:
        course = Course.objects.get(name=course_name)
        lab = Laboratory.objects.filter(course=course).get(name=lab_name)
        lab.url = lab_name_url
        course.url = course_name_url
        context_dict['lab'] = lab
        context_dict['course'] = course
        context_dict = get_sections(context_dict, lab)
        simulationtest_questions = SimulationTestQuestion.objects.filter(simulationtest=context_dict['simulationtest'])
        context_dict['simulationtest_questions'] = simulationtest_questions
    except Course.DoesNotExist:
        pass
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
        context_dict['just_finished'] = True
        context_dict['simulationtest_questions'] = simulationtest_questions
        context_dict['simulationtest'].is_completed = True
        context_dict['simulationtest'].save()
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/simulationtest.html', context_dict)
    
def hardware(request, course_name_url, lab_name_url, hardware_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    hardware_name = hardware_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
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
        if request.method == 'POST':
            context_dict['hardware'].is_completed = True
            context_dict['hardware'].save()
        return render(request, 'VLA/hardware.html', context_dict)


def results(request, course_name_url, lab_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/results.html', context_dict)
    
def resultsquestions(request, course_name_url, lab_name_url):
    lab_name = lab_name_url.replace('_', ' ')
    course_name = course_name_url.replace('_', ' ')
    context_dict = {'lab_name': lab_name}
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/resultsquestions.html', context_dict)
    

### HELP VIEWS
def help(request):
    cour_list = get_course_list()
    context_dict = {'cour_list': cour_list}
    context_dict['def_searched'] = False
    context_dict['def_topics'] = get_vocab_topic_list()
    context_dict['def_list'] = Node.objects.all()
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        context_dict['logged_in'] = True
        return render(request, 'VLA/help.html', context_dict)


def vocab_topic(request, vocab_topic_name_url):
    vocab_topic_list = get_vocab_topic_list()
    context_dict = {'vocab_topic_list': vocab_topic_list}
    vocab_topic_name = vocab_topic_name_url.replace('_', ' ')
    context_dict['vocab_topic_name'] = vocab_topic_name
    if vocab_topic_name == 'definitionlist':
        context_dict['vocab_topic_name'] = 'Definition List'
        vocab_topic = VocabTopic.objects.filter(def_useful=True).order_by('word')
    else:
        vocab_topic = VocabTopic.objects.get(topic=vocab_topic_name)
    context_dict['vocab_topic'] = vocab_topic
    vocab_words = Node.objects.filter(topic=vocab_topic).order_by('word')
    for words in vocab_words:
        words.url = words.word.replace(' ', '_')
        words.synonyms = Synonym.objects.filter(node=words)
    context_dict['vocab_words'] = vocab_words
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/vocabtopic.html', context_dict)

def definition(request, definition_name_url):
    definition_name = definition_name_url.replace('_', ' ')
    context_dict = {'definition_name': definition_name}
    definition = Node.objects.get(word=definition_name)
    context_dict['synonyms'] = Synonym.objects.filter(node=definition)
    context_dict['definition'] = definition
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    context_dict['vocab_topic_list'] = get_vocab_topic_list()
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/definition.html', context_dict)

### UNNEEDED VIEWS
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

### REGISTER / LOGIN VIEWS
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

def get_vocab_topic_list():
    vocab_topic_list = VocabTopic.objects.filter(def_useful=True).order_by('topic')

    for topic in vocab_topic_list:
        topic.url = topic.topic.replace(' ', '_')
    return vocab_topic_list

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
        resultsquestions = ResultsQuestions.objects.filter(lab=lab).get(lab=lab)
        resultsquestions.url = resultsquestions.name.replace(' ', '_')
        context_dict['results_questions'] = resultsquestions
    except ResultsQuestions.DoesNotExist:
        pass
    return context_dict

def get_definition_list(max_results=0, starts_with=''):
    topic_list = VocabTopic.objects.filter(def_useful=False)
    def_list = []
    if starts_with:
        def_list = Node.objects.filter(word__istartswith=starts_with).exclude(topic__in=topic_list)
    
    if max_results > 0:
        if len(def_list) > max_results:
            def_list = def_list[:max_results]

    for definition in def_list:
        definition.url = definition.word.replace(' ', '_')
    
    return def_list
    
def suggest_definition(request):
    def_list = []
    context_dict = {'def_searched': True}
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['definition_suggestion']

    context_dict['def_list'] = get_definition_list(8, starts_with)
        
    return render(request, 'VLA/definition_list.html', context_dict)
