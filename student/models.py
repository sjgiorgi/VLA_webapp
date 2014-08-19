from django.db import models
from django.contrib.auth.models import User

from VLA.models import Course, Laboratory

def get_file_path(instance, filename):
    if not instance.id:
        instance.save()
    lab_name = instance.lab.name.replace(' ', '_')
    return 'users/%s/%s/simulation.png' % (instance.user.username, lab_name)
    
### User Classes
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    first_name = models.CharField(max_length=64, help_text="Please enter your first name.", blank=False)
    last_name = models.CharField(max_length=64, help_text="Please enter your last name.", blank=False)
    TUid =  models.PositiveIntegerField(help_text="Please enter your TUid.", blank=False)
    
    def __unicode__(self):
        return self.user.username
    
# Class for giving students access to a Course
class CoursePermission(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    course_finished = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.course.name
    
# Class for storing completion status and test scores for
# each Laboratory and User
class LabProgress(models.Model):
    user = models.ForeignKey(User)
    lab = models.ForeignKey(Laboratory)
    theory_finished = models.BooleanField(default=False)
    theory_test_finished = models.BooleanField(default=False)
    simulation_finished = models.BooleanField(default=False)
    sim_test_finished = models.BooleanField(default=False)
    hardware_finished = models.BooleanField(default=False)
    results_finished = models.BooleanField(default=False)
    lab_test_finished = models.BooleanField(default=False)
    lab_finished = models.BooleanField(default=False)
    
    theory_test_score = models.FloatField(blank=True)
    sim_test_score = models.FloatField(blank=True)
    lab_test_score = models.FloatField(blank=True)

    sim_image = models.FileField(upload_to=get_file_path, blank=True)

    def __unicode__(self):
        return self.lab.name


