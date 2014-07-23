from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    # course info
    name = models.CharField(max_length=128)
    crn = models.IntegerField(default=0, blank=True)
    subj = models.CharField(max_length=10)
    course_number = models.IntegerField(default=0)
    section_number = models.IntegerField(default=0, blank=True)
    start_date = models.DateField('Course Start Date', blank=True, null=True)
    end_date = models.DateField('Course End Date', blank=True, null=True)
    lecture_time = models.TimeField('Lecture Time', blank=True, null=True)
    lecture_days = models.CharField(max_length=50, blank=True)
    lecture_location = models.CharField(max_length=50, blank=True)
    lab_time = models.TimeField('Lab Time', blank=True, null=True)
    lab_days = models.CharField(max_length=50, blank=True)
    lab_location = models.CharField(max_length=50, blank=True)
    course_description = models.TextField(max_length=500, blank=True)
    course_overview = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)
    
    # instructor info
    instructor_name = models.CharField(max_length=50, blank=True)
    instructor_email = models.EmailField(blank=True)
    instructor_office_hours = models.TimeField(blank=True, null=True)
    instructor_office_days = models.CharField(max_length=50, blank=True)
    instructor_office_location = models.CharField(max_length=50, blank=True)
    instructor_phone = models.CharField(max_length=50, blank=True)
    
    # TA info
    TA_name = models.CharField(max_length=50, blank=True)
    TA_email = models.EmailField(blank=True)
    TA_office_hours = models.TimeField(blank=True, null=True)
    TA_office_days = models.CharField(max_length=50, blank=True)
    TA_office_location = models.CharField(max_length=50, blank=True)
    TA_phone = models.CharField(max_length=128, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name
    
class Laboratory(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=128)
    start_date = models.DateTimeField('Date Assigned', blank=True, null=True)
    due_date = models.DateTimeField('Date Due', blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    lab_number = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name
    
class LabObjective(models.Model):
    lab = models.ForeignKey(Laboratory)
    objective = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.objective
     
class Theory(models.Model):
    lab = models.ForeignKey(Laboratory)
    name = models.CharField(max_length=128)
    is_completed = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name

class TheoryElement(models.Model):
    theory = models.ForeignKey(Theory)
    name = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='static/', blank=True)
    equation_input = models.CharField(max_length=64, blank=True)
    is_text = models.BooleanField(default=False)
    is_image = models.BooleanField(default=False)
    is_equation = models.BooleanField(default=False)
    is_latex = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name
    
class Pretest(models.Model):
    lab = models.ForeignKey(Laboratory)
    name = models.CharField(max_length=128)
    is_completed = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name
    
class PretestQuestion(models.Model):
    pretest = models.ForeignKey(Pretest)
    question = models.CharField(max_length=128)
    answer_one = models.CharField(max_length=128)
    answer_two = models.CharField(max_length=128)
    answer_three = models.CharField(max_length=128, blank=True)
    answer_four = models.CharField(max_length=128, blank=True)
    corrent_answer_number = models.IntegerField(blank=True)
    correct_response = models.CharField(max_length=128, blank=True)
    incorrect_response = models.CharField(max_length=128, blank=True)
    is_answered = models.BooleanField(default=False)
    def __unicode__(self):
        return self.question
    
class Prelab(models.Model):
    lab = models.ForeignKey(Laboratory)
    name = models.CharField(max_length=128)
    is_completed = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name

class PrelabElement(models.Model):
    prelab = models.ForeignKey(Prelab)
    name = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='static/', blank=True)
    equation_input = models.CharField(max_length=256, blank=True)
    is_text = models.BooleanField(default=False)
    is_image = models.BooleanField(default=False)
    is_equation = models.BooleanField(default=False)
    is_latex = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name
    
class PrelabTest(models.Model):
    lab = models.ForeignKey(Laboratory)
    name = models.CharField(max_length=128, unique=True)
    is_completed = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name

class PrelabTestQuestion(models.Model):
    prelabtest = models.ForeignKey(PrelabTest)
    question = models.CharField(max_length=128)
    answer_one = models.CharField(max_length=128)
    answer_two = models.CharField(max_length=128)
    answer_three = models.CharField(max_length=128, blank=True)
    answer_four = models.CharField(max_length=128, blank=True)
    corrent_answer_number = models.IntegerField(blank=True)
    correct_response = models.CharField(max_length=128, blank=True)
    incorrect_response = models.CharField(max_length=128, blank=True)
    is_answered = models.BooleanField(default=False)
    def __unicode__(self):
        return self.question
    
class Hardware(models.Model):
    lab = models.ForeignKey(Laboratory)
    name = models.CharField(max_length=128, unique=True)
    def __unicode__(self):
        return self.name
    
class HardwareElement(models.Model):
    hardware = models.ForeignKey(Hardware)
    name = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='static/', blank=True)
    equation_input = models.CharField(max_length=64, blank=True)
    is_text = models.BooleanField(default=False)
    is_image = models.BooleanField(default=False)
    is_equation = models.BooleanField(default=False)
    is_latex = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name

class Results(models.Model):
    lab = models.ForeignKey(Laboratory)
    name = models.CharField(max_length=128)
    is_completed = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name
    
class ResultsQuestions(models.Model):
    lab = models.ForeignKey(Laboratory)
    name = models.CharField(max_length=128)
    is_completed = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name
    
#class Question(model.Models):
    

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.user.username
    
    
class VocabDomain(models.Model):
    name = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name

class VocabTopic(models.Model):
    topic = models.CharField(max_length=128)
    domain = models.ForeignKey(VocabDomain)
    def_useful = models.BooleanField(default=False)
    def __unicode__(self):
        return self.topic
    
class Node(models.Model):
    word = models.CharField(max_length=128)
    definition = models.CharField(max_length=256)
    topic = models.ForeignKey(VocabTopic)
    def __unicode__(self):
        return self.word
    
class Synonym(models.Model):
    word = models.CharField(max_length=128)
    Node = models.ForeignKey(Node)
    def __unicode__(self):
        return self.word

    