import os
from django.utils import timezone

'''
Script to populate VLA with:

COURSES:
EE Science I Course

LABORATORIES:
Ohm's Law Laboratory
'''

def populate():
    # Circuits I class
    circuits_course = add_course("EE Science I", subj='ECE',
                                 course_number=2312, crn=999999,
                                 section_number=1, start_date=timezone.now(),
                                 end_date=timezone.now(),
                                 lecture_time=timezone.now(),
                                 lecture_days="MWF",
                                 lecture_location="ENGR 302",
                                 lab_time=timezone.now(), lab_days="TH",
                                 lab_location="ENGR 705",
                                 course_description="Electric circuit fundamentals including DC and transient circuit analysis are covered in the course. Topics include" +
                                    "independent and dependent sources, circuit elements such as resistors, inductors, capacitors and operational amplifiers, linearity, source" +
                                    "transformation, Thevenin and Norton equivalent circuits, as well as the analysis and design of first and second order circuits. ",
                                 course_overview="The goal of this course is NOT to teach you the intracies of circuit analysis as though it is some art. Circuit analysis is a " +
                                    "topic that applies to many fields beyond electrical engineering (e.g. acoustics, fluid flow). This is really a course in linear system theory." +
                                    " Eventually you will learn all the techniques discussed in this class can be replaced with a generalized approach based on state variables. " +
                                    "However, the specific goals for this course are to teach you the basics on AC and DC circuit analysis. We will build on what you have learned" +
                                    " in physics about inductors and capacitors, and what you are learning in match about differential equations, and will develop simple models of " +
                                    "these components that allow electrical circuits to be designed and analyzed using some simple theoretical calculations. We will also rely heavily " +
                                    "on computer simulation tools such as MutliSim, to handle complex circuits. The laboratory experience will teach you how to design, prototype" +
                                    "and fabricate simple electrical circuits. Extensive use of simulation tools will be made to debug and verify hardware performance. ",
                                 website="http://www.course.com",
                                 instructor_name="Dr. Chang-Hee Won",
                                 instructor_email="instructor@instructor.com",
                                 instructor_office_hours=timezone.now(),
                                 instructor_office_days="MWF",
                                 instructor_office_location="ENGR 703",
                                 instructor_phone="(999) 999-9999",
                                 TA_name="Firdous Saleheen",
                                 TA_email="TA@TA.com",
                                 TA_office_hours=timezone.now(),
                                 TA_office_days="TH",
                                 TA_office_location="ENGR 703d",
                                 TA_phone="(999) 999-9999")

    # Ohms law lab
    ohms_law = add_lab(course=circuits_course, name="Ohms Law",
                       start_date=timezone.now(), due_date=timezone.now(),
                       lab_number=1)
    
    add_lab_objective(lab=ohms_law,
                      objective="Become familiar with the dc power supply and setting the output voltage.")
    add_lab_objective(lab=ohms_law,
                      objective="Measure the current in a dc circuit.")
    add_lab_objective(lab=ohms_law,
                      objective="Apply and plot Ohm's law.")
    add_lab_objective(lab=ohms_law,
                      objective="Determine the slope of an IV curve.")
    add_lab_objective(lab=ohms_law,
                      objective="Become more familiar with the use of the analog VOM and digital DMM.")
    
    add_lab_equipment(lab=ohms_law,
                      equipment="1 - 1 k&#937; Resistor")
    add_lab_equipment(lab=ohms_law,
                      equipment="1 - 3.3 k&#937; Resistor")
    add_lab_equipment(lab=ohms_law,
                      equipment="Digital Multimeter (DMM)")
    add_lab_equipment(lab=ohms_law,
                      equipment="DC Power Supply")
    add_lab_equipment(lab=ohms_law,
                      equipment="Volt-Ohm-Milliampere Meter (VOM)")

    # Ohms law theory
    ohms_law_theory = add_theory(lab=ohms_law, name="Ohms Law Theory")
    
    add_theory_element(theory=ohms_law_theory, name="ohms law theory 1", number=1,
                       text_input="In any active circuit there must be source of power. In the laboratory, it is convenient to use " +
                       "a source that requires a minimum of maintenance and, more important, whose output voltage can be varies easily. " +
                       "Power supplies are rated as to maximum voltage and current output. For example, a supply rated 040 V at 500 mA " +
                       "will provide a maximum voltage of 40 V and a maximum current of 500 mA at any voltage.",
                       image_input=None, equation_input="", video_input="", element_type='text')
    
    # Ohms law theory test
    ohms_law_theory_test = add_theory_test(lab=ohms_law, name="Ohms Law Theory Test")
    
    add_theory_test_question(theorytest=ohms_law_theory_test,
                             question="A common DC power supply usually has how many terminals?",
                             answer_one="1", answer_two="2",
                             answer_three="3", answer_four="4",
                             correct_answer_number=1,
                             correct_response="This is why...",
                             incorrect_response="This is a hint why...")
    add_theory_test_question(theorytest=ohms_law_theory_test,
                             question="When using a voltmeter, measurments should be taken in...",
                             answer_one="Series", answer_two="Parallel",
                             answer_three="", answer_four="",
                             correct_answer_number=2,
                             correct_response="This is why...",
                             incorrect_response="This is a hint why...")
    add_theory_test_question(theorytest=ohms_law_theory_test,
                             question="When using an ammeter, measurements should be taken in...",
                             answer_one="Series", answer_two="Parallel",
                             answer_three="", answer_four="",
                             correct_answer_number=1,
                             correct_response="This is why...",
                             incorrect_response="This is a hint why...")
    add_theory_test_question(theorytest=ohms_law_theory_test,
                             question="Which one of these variables is not found in Ohm's Law?",
                             answer_one="Current", answer_two="Power",
                             answer_three="Resistance", answer_four="Voltage",
                             correct_answer_number=2,
                             correct_response="This is why...",
                             incorrect_response="This is a hint why...")
    
    # Ohms law simulation
    ohms_law_simulation = add_simulation(lab=ohms_law, name="Ohms Law Simulation")
    
    add_simulation_element(simulation=ohms_law_simulation,
                           name="ohms law simulation 1", number=1,
                           text_input="The purpose of this laboratory exercise is to acquaint you with the equipment, so do not rush. If you are a member of a squad, don't let one individual make all the measurements. You must become comfortable with the instruments if you expect to perform your future job function in a professional manner. Read the instruments carefully. The more accurate a reading, the more accurate the results obtained." +
                                      "One final word of caution. For obvious reasons, do not make network changes with the power on! If you have any questions about the procedure, be sure to contact your instructor.",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    
    # Ohms law simulation test
    ohms_law_simulation_test = add_simulation_test(lab=ohms_law,
                                                   name="Ohms Law Simulation Test")
    
    add_simulation_test_question(simulationtest=ohms_law_simulation_test,
                                 question="What is the measured current through IR when VB = 2 V?",
                                 answer_one="5 mA", answer_two="10 mA",
                                 answer_three="15 mA", answer_four="20 mA",
                                 correct_answer_number=4,
                                 correct_response="This is why...",
                                 incorrect_response="This is a hint why...")
    add_simulation_test_question(simulationtest=ohms_law_simulation_test,
                                 question="What is the measured current through IR when VB = 4 V?",
                                 answer_one="5 mA", answer_two="10 mA",
                                 answer_three="15 mA", answer_four="20 mA",
                                 correct_answer_number=3,
                                 correct_response="This is why...",
                                 incorrect_response="This is a hint why...")
    add_simulation_test_question(simulationtest=ohms_law_simulation_test,
                                 question="What is the measured current through IR when VB = 6 V?",
                                 answer_one="5 mA", answer_two="10 mA",
                                 answer_three="15 mA", answer_four="20 mA",
                                 correct_answer_number=2,
                                 correct_response="This is why...",
                                 incorrect_response="This is a hint why...")
    add_simulation_test_question(simulationtest=ohms_law_simulation_test,
                                 question="What is the measured current through IR when VB = 8 V?",
                                 answer_one="5 mA", answer_two="10 mA",
                                 answer_three="15 mA", answer_four="20 mA",
                                 correct_answer_number=1,
                                 correct_response="This is why...",
                                 incorrect_response="This is a hint why...")
    
    # Ohms law hardware
    ohms_law_hardware = add_hardware(lab=ohms_law, name="Ohms Law Hardware")

    add_hardware_element(hardware=ohms_law_hardware, name="ohms law simulation 1", number=1,
                         text_input="In this section, the current of a dc series circuit will be determined by a direct measurement and using Ohm's law. In practice, most current levels are determined using Ohm's law and a measured voltage level to avoid having to break the circuit to insert the ammeter. However, one should be aware of the procedure associated with using an ammeter, and one should feel confident that the measured value" +
                         " and that calculated using Ohm's law are very close in magnitude.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')

    # Print out what we have added to the user.
    for c in Course.objects.all():
        for l in Laboratory.objects.filter(course=c):
            print "- {0} - {1}".format(str(c), str(l))

# Add course, lab, lab section (theory, simulation, hardware)
def add_course(name, crn, subj, course_number, section_number, start_date,
               end_date, lecture_time, lecture_days, lecture_location,
               lab_time, lab_days, lab_location, course_description,
               course_overview, website, instructor_name, instructor_email,
               instructor_office_hours, instructor_office_days,
               instructor_office_location, instructor_phone, TA_name, TA_email,
               TA_office_hours, TA_office_days, TA_office_location, TA_phone):
    c = Course.objects.get_or_create(name=name, subj=subj, course_number=course_number,
                                     section_number=section_number, start_date=start_date,
                                     end_date=end_date, lecture_time=lecture_time,
                                     lecture_days=lecture_days, lecture_location=lecture_location,
                                     lab_time=lab_time, lab_days=lab_days,
                                     lab_location=lab_location, course_description=course_description,
                                     course_overview=course_overview, website=website,
                                     instructor_name=instructor_name, instructor_email=instructor_email,
                                     instructor_office_hours=instructor_office_hours,
                                     instructor_office_days=instructor_office_days,
                                     instructor_office_location=instructor_office_location,
                                     instructor_phone=instructor_phone, TA_name=TA_name,
                                     TA_email=TA_email, TA_office_hours=TA_office_hours,
                                     TA_office_days=TA_office_days,
                                     TA_office_location=TA_office_location, TA_phone=TA_phone)[0]
    return c

def add_lab(course, name, start_date, due_date, lab_number):
    l = Laboratory.objects.get_or_create(course=course, name=name,
                                         start_date=start_date,
                                         due_date=due_date,
                                         lab_number=lab_number)[0]
    return l

def add_lab_objective(lab, objective):
    lo = LabObjective.objects.get_or_create(lab=lab, objective=objective)[0]
    return lo

def add_lab_equipment(lab, equipment):
    le = LabEquipment.objects.get_or_create(lab=lab, equipment=equipment)[0]
    return le

def add_theory(lab, name):
    t = Theory.objects.get_or_create(lab=lab, name=name)[0]
    return t

def add_theory_element(theory, name, number, text_input, image_input,
                       equation_input, element_type, video_input):
    te = TheoryElement.objects.get_or_create(theory=theory, name=name,
                                             number=number,
                                             text_input=text_input,
                                             image_input=image_input,
                                             equation_input=equation_input,
                                             element_type=element_type,
                                             video_input=video_input)[0]
    return te

def add_theory_test(lab, name):
    tt = TheoryTest.objects.get_or_create(lab=lab, name=name)[0]
    return tt

def add_theory_test_question(theorytest, question, answer_one, answer_two,
                             answer_three, answer_four, correct_answer_number,
                             correct_response, incorrect_response):
    ttq = TheoryTestQuestion.objects.get_or_create(theorytest=theorytest,
                                                   question=question,
                                                   answer_one=answer_one,
                                                   answer_two=answer_two,
                                                   answer_three=answer_three,
                                                   answer_four=answer_four,
                                                   correct_answer_number=correct_answer_number,
                                                   correct_response= correct_response,
                                                   incorrect_response=incorrect_response)[0]
    return ttq

def add_simulation(lab, name):
    s = Simulation.objects.get_or_create(lab=lab, name=name)[0]
    return s

def add_simulation_element(simulation, name, number, text_input, image_input,
                           equation_input, element_type, video_input):
    se = SimulationElement.objects.get_or_create(simulation=simulation,
                                                 name=name, number=number,
                                                 text_input=text_input,
                                                 image_input=image_input,
                                                 equation_input=equation_input,
                                                 element_type=element_type,
                                                 video_input=video_input)[0]
    return se

def add_simulation_test(lab, name):
    st = SimulationTest.objects.get_or_create(lab=lab, name=name)[0]
    return st

def add_simulation_test_question(simulationtest, question, answer_one,
                                 answer_two, answer_three, answer_four,
                                 correct_answer_number, correct_response,
                                 incorrect_response):
    stq = SimulationTestQuestion.objects.get_or_create(simulationtest=simulationtest,
                                                       question=question,
                                                       answer_one=answer_one,
                                                       answer_two=answer_two,
                                                       answer_three=answer_three,
                                                       answer_four=answer_four,
                                                       correct_answer_number=correct_answer_number,
                                                       correct_response= correct_response,
                                                       incorrect_response=incorrect_response)[0]
    return stq

def add_hardware(lab, name):
    h = Hardware.objects.get_or_create(lab=lab, name=name)[0]
    return h

def add_hardware_element(hardware, name, number, text_input, image_input,
                         equation_input, element_type, video_input):
    he = HardwareElement.objects.get_or_create(hardware=hardware, name=name,
                                               number=number,
                                               text_input=text_input,
                                               image_input=image_input,
                                               equation_input=equation_input,
                                               element_type=element_type,
                                               video_input=video_input)[0]
    return he

def add_results(lab, name):
    r = Results.objects.get_or_create(lab=lab, name=name)[0]
    return r

def add_results_questions(lab, name):
    rq = ResultsQuestions.objects.get_or_create(lab=lab, name=name)[0]
    return rq

# Start execution here!
if __name__ == '__main__':
    print "Starting VLA population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VLA_project.settings')
    from VLA.models import *
    populate()