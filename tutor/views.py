#from __future__ import absolute_import
import re
from django.shortcuts import render
from django.contrib.auth import authenticate

from .models import *
from VLA.models import Course
from student.models import CoursePermission

# View for displaying main Help page
# Gets all definitions and questions
# as well as most viewed and recently added questions and definitions
def help(request):
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        # Get user and username
        user = request.user
        username = request.user.username
        
        # Display Course list in sidebar
        cour_list = get_course_list(user)
        context_dict = {'cour_list': cour_list}
        
        # Get most viewed definitions and questions
        top_def_list = Node.objects.order_by('-views')[:5]
        for definition in top_def_list:
            definition.url = definition.word.replace(' ', '_')
        context_dict['top_def_list'] = top_def_list
        top_question_list = AnswerWithQuestion.objects.order_by('-views')[:5]
        for question in top_question_list:
            question.url = re.sub(r'([^\s\w]|_)+','', question.question).replace(' ', '_')
        context_dict['top_question_list'] = top_question_list
        
        # Get recently added definitions and questions
        topic_list = VocabTopic.objects.filter(def_useful=False)
        recent_def_list = Node.objects.all().exclude(topic__in=topic_list).order_by('-date_added')[:5]
        for definition in recent_def_list:
            definition.url = definition.word.replace(' ', '_')
        context_dict['recent_def_list'] = recent_def_list
        recent_question_list = AnswerWithQuestion.objects.all().order_by('-date_added')[:5]
        for question in recent_question_list:
            question.url = re.sub(r'([^\s\w]|_)+','', question.question).replace(' ', '_')
        context_dict['recent_question_list'] = recent_question_list
        # NEED TO ADD GET RECENT QUESTIONS SECTION
        
        # Set searched flags to false and get complete question and definition lists
        context_dict['def_searched'] = False
        context_dict['def_list'] = Node.objects.all()
        context_dict['question_searched'] = False
        context_dict['question_list'] = AnswerWithQuestion.objects.all()
        
        # Get definition and question topics
        context_dict['def_topics'] = get_vocab_topic_list()
        context_dict['question_topics'] = get_question_topic_list()
    
        context_dict['logged_in'] = True
        return render(request, 'VLA/help.html', context_dict)

# View for displaying all definitions for a given Vocab topic
def vocab_topic(request, vocab_topic_name_url):
    # Get list of vocab topics and names
    vocab_topic_list = get_vocab_topic_list()
    context_dict = {'vocab_topic_list': vocab_topic_list}
    vocab_topic_name = vocab_topic_name_url.replace('_', ' ')
    context_dict['vocab_topic_name'] = vocab_topic_name
    
    # Get list of all definitions if requested
    # Otherwise, get topic by requested name
    if vocab_topic_name == 'definitionlist':
        context_dict['vocab_topic_name'] = 'Definition List'
        vocab_topic = VocabTopic.objects.filter(def_useful=True).order_by('word')
    else:
        vocab_topic = VocabTopic.objects.get(topic=vocab_topic_name)
    context_dict['vocab_topic'] = vocab_topic
    
    # Get list of words and synonyms in specified topic
    vocab_words = Node.objects.filter(topic=vocab_topic).order_by('word')
    for words in vocab_words:
        words.url = words.word.replace(' ', '_')
        words.synonyms = Synonym.objects.filter(node=words)
    context_dict['vocab_words'] = vocab_words
    
    # Set searched flags to false and get complete question and definition lists
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    context_dict['question_searched'] = False
    context_dict['question_list'] = AnswerWithQuestion.objects.all()
    
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/vocabtopic.html', context_dict)
    
# View for displaying all questions under a given topic
def question_topic(request, question_topic_name_url):
    # Get topic list and names
    question_topic_list = get_question_topic_list()
    context_dict = {'question_topic_list': question_topic_list}
    question_topic_name = question_topic_name_url.replace('_', ' ')
    context_dict['question_topic_name'] = question_topic_name
    
    # Get list of all questions if requested
    # Otherwise, get questions by requested topic name
    if question_topic_name == 'questionlist':
        context_dict['question_topic_name'] = 'Question List'
        question_topic = AnswerWithQuestion.objects.all().order_by('question')
        for question in question_topic:
            question.url = re.sub(r'([^\s\w]|_)+','', question.question).replace(' ', '_')
        context_dict['question_topic'] = question_topic
    else:
        question_topic = AnswerWithQuestion.objects.filter(topic__topic=question_topic_name).order_by('question')
        for question in question_topic:
            question.url = re.sub(r'([^\s\w]|_)+','', question.question).replace(' ', '_')
        context_dict['question_topic'] = question_topic
        
    # Set searched flags to false and get complete question and definition lists
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    context_dict['question_searched'] = False
    context_dict['question_list'] = AnswerWithQuestion.objects.all()
    
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/questiontopic.html', context_dict)

# View for displaying a single definition
def definition(request, definition_name_url):
    # Get definition name, definition, and synoyms
    definition_name = definition_name_url.replace('_', ' ')
    context_dict = {'definition_name': definition_name}
    definition = Node.objects.get(word=definition_name)
    context_dict['synonyms'] = Synonym.objects.filter(node=definition)
    context_dict['definition'] = definition
    
    # Get Vocab Topic list
    context_dict['vocab_topic_list'] = get_vocab_topic_list()
    
    # Set searched flags to false and get complete question and definition lists
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    context_dict['question_searched'] = False
    context_dict['question_list'] = AnswerWithQuestion.objects.all()
    
    # Update number of views if link was clicked
    if request.method == 'GET':
        definition.views = definition.views + 1
        definition.save()
        
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/definition.html', context_dict)
    
# View for displaying a single question
def question(request, question_name_url):
    # Get question name and find correct AnswerWithQuestion
    question_name = question_name_url.replace('_', ' ')
    context_dict = {'question_name': question_name}
    question = AnswerWithQuestion.objects.get(question=question_name)
    context_dict['question'] = question
    
    # Get question topic list and answers
    context_dict['question_topic_list'] = get_question_topic_list()
    context_dict['answer_elements'] = AnswerElement.objects.filter(answer_with_question=question)
    
    # Set searched flags to false and get complete question and definition lists
    context_dict['def_searched'] = False
    context_dict['def_list'] = Node.objects.all()
    context_dict['question_searched'] = False
    context_dict['question_list'] = AnswerWithQuestion.objects.all()
    
    # Update number of views if link was clicked
    if request.method == 'GET':
        question.views = question.views + 1
        question.save()
        
    # Check if user is logged in, if not authenticated, send user to login
    if not request.user.is_authenticated():
        return render(request, 'VLA/login.html')
    else:
        return render(request, 'VLA/question.html', context_dict)
    
# Get complete question topic list and create URLs
def get_question_topic_list():
    question_topic_list = AnswerTopic.objects.all().order_by('topic')
    for topic in question_topic_list:
        topic.url = topic.topic.replace(' ', '_')
        
    return question_topic_list

# Get complete defintiion topic list and create URLs
def get_vocab_topic_list():
    vocab_topic_list = VocabTopic.objects.filter(def_useful=True).order_by('topic')
    for topic in vocab_topic_list:
        topic.url = topic.topic.replace(' ', '_')
        
    return vocab_topic_list

# Used in definition search
# Get list of definitions that begin with starts_with
# Return list of definitions of length max_results
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

# Used in question search
# Get list of questions that exactly match the keywords found in starts_with
# Return list of definitions of length max_results
def get_question_list(max_results=0, starts_with=''):
    node_list = Node.objects.all()
    exact_question = []
    possible_questions = []
    syn_list = []
    def_list = []
    keyword_node_list = []
    for node in node_list:
        def_list.append(node.word.lower())
    
    # Find Nodes/Synonyms which correspond to keywords entered by user
    # If found, add Node.word to keyword_node_list
    if starts_with:
        keywords = re.sub(r'[^a-zA-Z0-9]',' ', starts_with).lower().split()
        for node in node_list:
            # Check if nodes are in keyword set
            if node.word.lower() in keywords:
                keyword_node_list.append(node.word.lower())
            else:
                # Check if any synonyms are in the keyword set
                syn_list = Synonym.objects.filter(node=node)
                for syn in syn_list:
                    if syn.word.lower() in keywords:
                        keyword_node_list.append(node.word.lower())
            
    for answer in AnswerWithQuestion.objects.all():
        answer_keywords = []
        for keyword in AnswerKeyword.objects.filter(answer_with_question=answer):
            answer_keywords.append(keyword.node.word.lower())
        if set(answer_keywords) == set(keyword_node_list):
            exact_question.append(answer)
        power = powerset(keyword_node_list)
        for subset in power:
            # ignore singleton sets which consist of action words
            if not (len(subset) == 1 and set(subset).issubset(set(['what', 'how', 'why', 'where']))):
                # ignore the empty set and consider only proper subsets
                if subset and (set(answer_keywords) != set(keyword_node_list)) and set(subset).issubset(set(answer_keywords)):
                    possible_questions.append(answer)
    
     # Use set() to remove duplicates
    possible_questions = set(possible_questions)
    
    for answer in exact_question:
        answer.url = re.sub(r'([^\s\w]|_)+','', answer.question).replace(' ', '_')
        
    for answer in possible_questions:
        answer.url = re.sub(r'([^\s\w]|_)+','', answer.question).replace(' ', '_')
        
    return {'exact_question': exact_question,
            'possible_questions': possible_questions}

# Used in definition search
# Set searched flag to True
# Call get_definition_list for searching and returning list of definitions
def suggest_definition(request):
    def_list = []
    context_dict = {'def_searched': True}
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['definition_suggestion']

    context_dict['def_list'] = get_definition_list(8, starts_with)
        
    return render(request, 'VLA/definition_list.html', context_dict)

# Used in question search
# Set searched flag to True
# Call get_question_list for searching and returning list of questions
def suggest_question(request):
    question_list = []
    context_dict = {'question_searched': True}
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['question_suggestion']

    context_dict['question_list'] = get_question_list(8, starts_with)
        
    return render(request, 'VLA/question_list.html', context_dict)

# Get permissible course list and create URLs
def get_course_list(user):
    permissions = CoursePermission.objects.filter(user=user)
    cour_list = []
    for permission in permissions:
        cour_list.append(permission.course)

    for cour in cour_list:
        cour.url = cour.name.replace(' ', '_')
    return cour_list

# Returns all the subsets of the generator
def powerset(generator):
    if len(generator) <= 1:
        yield generator
        yield []
    else:
        for item in powerset(generator[1:]):
            yield [generator[0]]+item
            yield item