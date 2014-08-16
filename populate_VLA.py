import os

'''
Script to populate VLA with:

COURSES:
EE Science I Course

LABORATORIES:
Ohm's Law Laboratory
'''



# Start execution here!
if __name__ == '__main__':
    print "Starting VLA population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VLA_project.settings')
    execfile("populate_vocab.py")
    execfile("populate_EE1.py")
    execfile("populate_EE2.py")
    execfile("populate_users.py")

    