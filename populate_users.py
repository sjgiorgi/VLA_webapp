import os

'''
Script to populate Users, and assigned Courses and Laboratories:

THIS MUST BE CALLED AFTER COURSES/LABS ARE POPULATED
'''

def populate():
    
    # Create guest user and profile
    guest = User.objects.create_user('guest', 'guest@guest.com', 'password')
    add_user_profile(guest, 'John', 'Doe', 999999999)
    
    # Assign all courses and their labs
    add_courses_and_labs(guest)
    
    sg = User.objects.get(username='salvatoregiorgi')
    add_user_profile(sg, 'Salvatore', 'Giorgi', 111111111)
    
    # Assign all courses and their labs
    add_courses_and_labs(sg)
        
    # Print out what we have added to the user.
    for u in User.objects.all():
        for cp in CoursePermission.objects.filter(course=u):
            print "- {0} - {1}".format(str(u), str(cp))

# Add user, user profile, course permission, and lab progress
def add_user():
    u = User.objects.get_or_create(user=user, first_name=first_name,
                                           last_name=last_name, TUid=TUid)[0]
    return u

def add_user_profile(user, first_name, last_name, TUid):
    up = UserProfile.objects.get_or_create(user=user, first_name=first_name,
                                           last_name=last_name, TUid=TUid)[0]
    return up

def add_course_permission(user, course):
    cp = CoursePermission.objects.get_or_create(user=user, course=course,
                                           course_finished=False)[0]
    return cp

def add_lab_progress(user, lab):
    lp = LabProgress.objects.get_or_create(user=user, lab=lab,
                                           theory_finished=False,
                                           theory_test_finished=False,
                                           simulation_finished=False,
                                           sim_test_finished=False,
                                           hardware_finished=False,
                                           results_finished=False,
                                           lab_test_finished=False,
                                           lab_finished=False,
                                           theory_test_score=0,
                                           lab_test_score=0,
                                           sim_test_score=0)[0]
    return lp

# Give permission to guest for all Courses, and all Labs within each course
def add_courses_and_labs(user):
    courses = Course.objects.all()
    for course in courses:
        add_course_permission(user, course)
        labs = Laboratory.objects.filter(course=course)
        for lab in labs:
            add_lab_progress(user, lab)
            
# Start execution here!
if __name__ == '__main__':
    print "Starting USER population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VLA_project.settings')
    from VLA.models import Course, Laboratory
    from student.models import UserProfile, CoursePermission, LabProgress, User
    populate()