from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    # course info
    name = models.CharField(max_length=128, unique=True)
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
    objective = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.objective
    
class LabEquipment(models.Model):
    lab = models.ForeignKey(Laboratory)
    equipment = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.equipment

# The following classes are needed for each Laboratory  
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
    image_input = models.FileField(upload_to='VLA/static/VLA/images/', blank=True)
    equation_input = models.CharField(max_length=64, blank=True)
    video_input = models.CharField(max_length=64, blank=True)
    TYPE_CHOICES = (
        ('text', 'text'),
        ('image', 'image'),
        ('equation', 'equation'),
        ('latex', 'latex'),
        ('video', 'video'),
        ('table', 'table'),
    )
    element_type = models.CharField(choices=TYPE_CHOICES, max_length=8)
    
    def __unicode__(self):
        return self.name
    
class TheoryTest(models.Model):
    lab = models.ForeignKey(Laboratory)
    name = models.CharField(max_length=128)
    is_completed = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name
    
class TheoryTestQuestion(models.Model):
    theorytest = models.ForeignKey(TheoryTest)
    question = models.CharField(max_length=128)
    answer_one = models.CharField(max_length=128)
    answer_two = models.CharField(max_length=128)
    answer_three = models.CharField(max_length=128, blank=True)
    answer_four = models.CharField(max_length=128, blank=True)
    correct_answer_number = models.IntegerField(blank=True)
    correct_response = models.CharField(max_length=128, blank=True)
    incorrect_response = models.CharField(max_length=128, blank=True)
    is_answered = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.question
    
class Simulation(models.Model):
    lab = models.ForeignKey(Laboratory)
    name = models.CharField(max_length=128)
    is_completed = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name

class SimulationElement(models.Model):
    simulation = models.ForeignKey(Simulation)
    name = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='static/', blank=True)
    equation_input = models.CharField(max_length=256, blank=True)
    video_input = models.CharField(max_length=64, blank=True)
    TYPE_CHOICES = (
        ('text', 'text'),
        ('image', 'image'),
        ('equation', 'equation'),
        ('latex', 'latex'),
        ('video', 'video'),
        ('table', 'table'),
    )
    element_type = models.CharField(choices=TYPE_CHOICES, max_length=8)
    
    def __unicode__(self):
        return self.name
    
class SimulationTest(models.Model):
    lab = models.ForeignKey(Laboratory)
    name = models.CharField(max_length=128)
    is_completed = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name

class SimulationTestQuestion(models.Model):
    simulationtest = models.ForeignKey(SimulationTest)
    question = models.CharField(max_length=128)
    answer_one = models.CharField(max_length=128)
    answer_two = models.CharField(max_length=128)
    answer_three = models.CharField(max_length=128, blank=True)
    answer_four = models.CharField(max_length=128, blank=True)
    correct_answer_number = models.IntegerField(blank=True)
    correct_response = models.CharField(max_length=128, blank=True)
    incorrect_response = models.CharField(max_length=128, blank=True)
    is_answered = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.question
    
class Hardware(models.Model):
    lab = models.ForeignKey(Laboratory)
    name = models.CharField(max_length=128, unique=True)
    is_completed = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name
    
class HardwareElement(models.Model):
    hardware = models.ForeignKey(Hardware)
    name = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='static/', blank=True)
    equation_input = models.CharField(max_length=64, blank=True)
    video_input = models.CharField(max_length=64, blank=True)
    TYPE_CHOICES = (
        ('text', 'text'),
        ('image', 'image'),
        ('equation', 'equation'),
        ('latex', 'latex'),
        ('video', 'video'),
        ('table', 'table'),
    )
    element_type = models.CharField(choices=TYPE_CHOICES, max_length=8)
    
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

### User Classes

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.user.username
    
# Class for storing User Test answers
class StudentSitting(models.Model):
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.name
    
### Help Module classes: VocabDomain and Rulebase

# The following classes are needed for the VocabDomain
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
    topic = models.ForeignKey(VocabTopic)
    word = models.CharField(max_length=128)
    definition = models.CharField(max_length=256)
    views = models.IntegerField(default=0)
    date_added = models.DateTimeField('date added')
    
    def __unicode__(self):
        return self.word
    
class Synonym(models.Model):
    word = models.CharField(max_length=128)
    node = models.ForeignKey(Node)
    
    def __unicode__(self):
        return self.word

# The following classes are for the Rulebase
class Rulebase(models.Model):
    name = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name
  
class AnswerTopic(models.Model):
    rulebase = models.ForeignKey(Rulebase)
    TYPE_CHOICES = (
        ('Safety', 'Safety'),
        ('Equipment', 'Equipment'),
        ('VLA', 'VLA'),
        ('Simulation', 'Simulation'),
        ('Hardware', 'Hardware'),
        ('Theory', 'Theory'),
        ('General', 'General'),
    )
    topic = models.CharField(choices=TYPE_CHOICES, max_length=10)
    
    def __unicode__(self):
        return self.topic
  
class AnswerWithQuestion(models.Model):
    rulebase = models.ForeignKey(Rulebase)
    topic = models.ManyToManyField(AnswerTopic)
    question = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    date_added = models.DateTimeField('date added')
    
    def __unicode__(self):
        return self.question
    
class AnswerElement(models.Model):
    answer_with_question = models.ForeignKey(AnswerWithQuestion)
    text_input = models.TextField(blank=True)
    image_input = models.FileField(upload_to='static/', blank=True)
    equation_input = models.CharField(max_length=64, blank=True)
    video_input = models.CharField(max_length=64, blank=True)
    TYPE_CHOICES = (
        ('text', 'text'),
        ('image', 'image'),
        ('equation', 'equation'),
        ('latex', 'latex'),
        ('table', 'table'),
        ('video', 'video'),
    )
    element_type = models.CharField(choices=TYPE_CHOICES, max_length=8)
    
    def __unicode__(self):
        return self.answer_with_question.question
    
class AnswerKeyword(models.Model):
    answer_with_question = models.ForeignKey(AnswerWithQuestion)
    node = models.ForeignKey(Node)
    
    def __unicode__(self):
        return self.node.word

    
