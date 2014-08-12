import os
from django.utils import timezone

'''
Script to populate VLA with:

COURSE:
-EE Science II Course

LABORATORIES:
-Digilent Board Intro and RC Time Constant
-First Order Filters
-Second Order Step Response I
-Second Order Low-pass Filters
-Second Order Step Response II
-Complex Impedances
-Bass Booster
-Op-Amps
-Amplitude Modulation
-Boost Converter
'''

def populate():
    # Add EE Science II Course
    ee_science_ii = add_course("EE Science II", subj='ECE',
                                 course_number=2323, crn=999999,
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

    ###
    # EE Science II Lab 1: Digilent Board Intro & RC Time Constant
    ###
    digilent_board_intro = add_lab(course=ee_science_ii, name="Digilent Board Intro and RC Time Constant",
                                   start_date=timezone.now(), due_date=timezone.now(),
                                   lab_number=1)
    add_lab_objective(lab=digilent_board_intro,
                      objective="The purpose of this week's lab is two-fold. The first goal is to introduce you to " +
                                "the Digilent Explorer board and the second is to give you experience measuring the " +
                                "time constant of an RC circuit. If you are planning on bringing your laptop to lab, " +
                                "make sure you have the Waveforms software installed ahead of time. You can download " +
                                "it <a href=\"http://www.digilentinc.com/Products/Detail.cfm?Prod=WAVEFORMS\" target=\"new\">here</a>.")
    
    # Digilent Board Intro & RC Time Constant Simulation
    digilent_board_simulation = add_simulation(lab=digilent_board_intro, name="Digilent Board Simulation")
    
    add_simulation_element(simulation=digilent_board_simulation,
                           name="digilent intro simulation 1", number=1,
                           text_input="Using a circuit similator, build and simulate the following circuit. To view the scope screen, " +
                           "right click the object during the simulation and select 'Properties'. Adjust the scope knobs as " +
                           "necessary in order to visualize two complete cycles of the signals. Bring either a screenshot of " +
                           "the virtual oscilloscope or your laptop with the running simulation to lab.",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=digilent_board_simulation,
                           name="digilent intro simulation 2", number=2,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab01/fig01.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=digilent_board_simulation,
                           name="digilent intro simulation 3", number=3,
                           text_input="Figure 1",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')
    
    # Digilent Board Intro & RC Time Constant Hardware
    digilent_board_hardware = add_hardware(lab=digilent_board_intro, name="Digilent Board Hardware")
    
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 1", number=1,
                         text_input="<h4>Part 1. MEET YOUR DILIGENT BOARD</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 2", number=2,
                         text_input="The Digilent board is shown below. Note that in addition to the standard beadboard " +
                         "(which is wired normally just like every other breadboard), there are extra modules to the " +
                         "left and right. For this semester, you can ignore the digital modules on the right. On the " +
                         "left we have:",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 3", number=3,
                         text_input="<b>SCOPE</b>: Four channel oscilloscope. Each channel can be used as either AC or DC coupled. You should stick to DC coupled scope usage unless otherwise directed",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 4", number=4,
                         text_input="<b>ANALOG</b>: Analog voltages, including two reference voltages (VREF), two channels of arbitrary waveform generators (AWG) and a four-input voltage meter (VMTR)",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 5", number=5,
                         text_input="<b>POWER</b>: Power supplies including analog positive (VP+), analog negative (VP-) and digital supply (VCC).",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 6", number=6,
                         text_input="Note that every row marked with a down arrow is ground. All the grounds are wired internally so you don't have to bother wiring your power supply ground to your scope ground like you would have to if you were using the bench instruments.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 7", number=7,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab01/fig02.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 8", number=8,
                         text_input="Figure 2",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 9", number=9,
                         text_input="To get started, plug in the power supply, connect your board to a PC with the supplied USB cable, and turn the power switch to 'on'.  Then, run the Waveforms software.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 10", number=10,
                         text_input="The first screen you will see should look like this:",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 11", number=11,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab01/fig03.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 12", number=12,
                         text_input="Figure 3",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 13", number=13,
                         text_input="This screen lets you navigate to the individual instruments we'll need for this course. We'll be using Scope, WaveGen, and Voltage. ",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 14", number=14,
                         text_input="<h4>Part 2. VOLTAGE SUPPLY</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 15", number=15,
                         text_input="Click on Voltage to get started. This will bring up the voltage source screen.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 16", number=16,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab01/fig04.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 17", number=17,
                         text_input="Figure 4",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 18", number=18,
                         text_input="Here you can determine how you want your voltage sources to be set up. Set your positive supply to +5V and your negative supply " +
                         "to -3V. If your current limit is set to 0A, make sure to increase it to something modest like \(\\pm\)50 mA as shown in the picture. Finally, " +
                         "turn on the power by clicking the Power button at top left. You can now take a wire and connect your positive supply pin to one of the voltage " +
                         "meter pins. The volt meter reading on the screen should change and read 5V accordingly. Do the same with your negative supply to make sure its working.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 19", number=19,
                         text_input="<h4>Part 3. WAVEFORM GENERATOR</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 20", number=20,
                         text_input="Go back to the Waveforms selector window and click  'WaveGen'. This will bring you to the following screen:",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 21", number=21,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab01/fig05.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 22", number=22,
                         text_input="Figure 5",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 23", number=23,
                         text_input="As you can see, this screen will let you select what kind of waveform to generate as well as all the relevant parameters. Set the system " +
                         "up to create a 1 \(V_{pp}\) sine wave with frequency 1kHz. Make sure to click on 'Run AWG' to actually turn on the signal. The sine wave should now be " +
                         "available on channel 1 of the AWG module on the board. In order to tell whether its working, you can either connect the AWG module to a bench top " +
                         "oscilloscope or you can use the on-board Digilent oscilloscope. To do so, start by running a wire from AWG channel 1 to input 'DC 1' on the Scope " +
                         "module. Then, follow the steps in Section 4 to turn on the oscilloscope.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 24", number=24,
                         text_input="<h4>Part 4. OSCILLOSCOPE</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 25", number=25,
                         text_input="Go back to the Waveforms selector window and click 'Scope'. This will bring up the oscilloscope screen which should look like this:",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 26", number=26,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab01/fig06.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 27", number=27,
                         text_input="Figure 6",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 28", number=28,
                         text_input="Click the 'Run' button to turn on the oscilloscope. The interface should work just like a regular bench top scope. You can adjust " +
                         "voltage and time settings in order to visualize your signal. You can also adjust trigger settings as necessary. Visualize your signal and " +
                         "verify that you have created a 1 \(V_{pp}\) sine wave at 1kHz. You can now go back to the Waveform Generator and change the signal type or the voltage " +
                         "or frequency and verify that you can see the expected changes on the oscilloscope. For example, try creating a square wave, since you'll " +
                         "need one for the following section.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 29", number=29,
                         text_input="<h4>Part 5. RC TIME CONSTANT</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=digilent_board_hardware, name="digilent board hardware 30", number=30,
                         text_input="Build the circuit from the simulation on your board. Use the AWG module to create an input square wave at 50 Hz. Run both the input " +
                         "and output signals to the oscilloscope (on different channels). You should be able to watch your capacitor charging and discharging. We will " +
                         "be learning in class that this first order circuit is governed by a time constant, \(\\tau=RC\). We will also be learning that the capacitor will " + 
                         "charge 63% of the way from its initial to its final value in one time constant. Calculate the time constant using your resistor and capacitor " + 
                         "values. Now, for comparison, measure how much time it takes for your capacitor charges to 63%. You might like to use the 'cursor' feature " +
                         "on your oscilloscope to help you measure exactly. Ask your TA how to do this. Ideally, this time should be exactly equal to your RC time " +
                         "constant but more likely than not, there will be some error. What are the sources of error?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    ###
    # EE Science II Lab 2: First Order Filters
    ###
    first_order_filters = add_lab(course=ee_science_ii, name="First Order Filters",
                                  start_date=timezone.now(), due_date=timezone.now(),
                                  lab_number=2)
    add_lab_objective(lab=first_order_filters,
                      objective="The purpose of this week's lab is to build and test your first ever filter. Filters are " +
                                "circuits that allow certain frequencies to pass through while blocking others. Here " +
                                "you will be building two circuits and determining what types of filters they are and " +
                                "what ranges of frequencies they allow to pass.")
    
    # First Order Filters Simulation
    fof_simulation = add_simulation(lab=first_order_filters, name="First Order Filters Simulation")
    
    add_simulation_element(simulation=fof_simulation,
                           name="first order filters simulation 1", number=1,
                           text_input="Using a circuit similator, build the following circuit. Allow the input to be a 1V sine wave " +
                           "and the output to be the voltage across the capacitor. This is exactly the same circuit that " +
                           "you worked with in Lab 1 except we are using a sine wave for input instead of a square wave. " +
                           "With the sine wave frequency equal to 10Hz, determine the peak voltage of the output sine wave. " +
                           "Then, keeping the input amplitude at 1V, repeat this measurement for the following frequencies: " +
                           "10Hz, 20Hz, 50Hz, 100Hz, 200Hz, 500Hz, 1kHz, 2kHz. Finally make a plot of the amplitude of the " +
                           "output signal versus frequency. Bring this plot with you to lab. What kind of filter have you built?",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=fof_simulation,
                           name="first order filters simulation 2", number=2,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab02/fig01.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=fof_simulation,
                           name="first order filters simulation 3", number=3,
                           text_input="Figure 1",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')
    
    # First Order Filters  Hardware
    fof_hardware = add_hardware(lab=first_order_filters, name="First Order Filters Hardware")
    
    add_hardware_element(hardware=fof_hardware, name="first order filters hardware 1", number=1,
                         text_input="<h4>Part 1. FILTER 1</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=fof_hardware, name="first order filters hardware 2", number=2,
                         text_input="In this section you will repeat the steps of the simualtion on your Digilent board. Using a sine " +
                         "wave input, measure the peak voltage of the output sine wave and create a plot of peak amplitude versus " +
                         "frequency (use the same frequencies as the simulation). Overlay this plot with the simulation plot. Do they agree? " +
                         "If not, how far off are they? Why?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=fof_hardware, name="first order filters hardware 3", number=3,
                         text_input="<h4>Part 2. FILTER 2</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=fof_hardware, name="first order filters hardware 4", number=4,
                         text_input="Repeat the steps of the previous section with the circuit shown below. The output voltage is the " +
                         "voltage across the resistor. In this case, use the following range of frequencies: 100Hz, 200Hz, 500Hz, 1kHz, " +
                         "2kHz, 5kHz, 10kHz, 20kHz. Plot peak amplitude versus frequency. What kind of filter have you built?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=fof_hardware, name="first order filters hardware 5", number=5,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab02/fig02.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=fof_hardware, name="first order filters hardware 6", number=6,
                         text_input="Figure 2",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    ###
    # EE Science II Lab 3: Second Order Step Response I
    ###
    second_order_step_i = add_lab(course=ee_science_ii, name="Second Order Step Response I",
                                  start_date=timezone.now(), due_date=timezone.now(),
                                  lab_number=3)
    add_lab_objective(lab=second_order_step_i,
                      objective="The purpose of this week's lab is to look at second order step responses.")
    
    # Second Order Step Response I Simulation
    sos1_simulation = add_simulation(lab=second_order_step_i, name="Second Order Step Response I Simulation")
    add_simulation_element(simulation=sos1_simulation,
                           name="second order step response I simulation 1", number=1,
                           text_input="Using  a circuit similator, build the following circuit. Allow \(V_{in}\) to be a 1kHz square wave. " +
                           "Let R=100 \(\\Omega\), C=4.7nF, and L=1mH. Run your simulation (1ms should be enough) and sketch or " +
                           "print out what the step response (i.e. \(V_{out}\)) looks like. Using the cursors, determine the " +
                           "frequency of oscillation (i.e. the reciprocal of the time between peaks) and the time it " +
                           "takes for the oscillations to damp out completely more or less. Then, repeat this process " + 
                           "with R=1.5k \(\\Omega\). In this case, the circuit will not oscillate, so just measure the rise time " +
                           "(the time it takes for the signal to charge or discharge more or less completely).",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=sos1_simulation,
                           name="second order step response I simulation 2", number=2,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab03/fig01.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=sos1_simulation,
                           name="second order step response I simulation 3", number=3,
                           text_input="Figure 1",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')
    
    # Second Order Step Response I Hardware
    sos1_hardware = add_hardware(lab=second_order_step_i, name="Second Order Step Response I Hardware")
    
    add_hardware_element(hardware=sos1_hardware, name="second order step response I hardware 1", number=1,
                         text_input="<h4>Part 1. FILTER 1</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=sos1_hardware, name="second order step response I hardware 2", number=2,
                         text_input="Using your Digilent board, build the circuit from the simulation using R=100 \(\\Omega\). Make " +
                         "a sketch or a printout of the step response. Measure the oscillation frequency and damping time, " +
                         "and confirm that these values match (i.e. are in the same ballpark) as in the simulation.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=sos1_hardware, name="second order step response I hardware 3", number=3,
                         text_input="<h4>Part 2. FILTER 2</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=sos1_hardware, name="second order step response I hardware 4", number=4,
                         text_input="Repeat the steps for Filter 1 using R=1.5 \(\\Omega\).",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    ###
    # EE Science II Lab 4: Second Order Low-pass Filters
    ###
    second_order_lowpass = add_lab(course=ee_science_ii, name="Second Order Lowpass Filters",
                                   start_date=timezone.now(), due_date=timezone.now(),
                                   lab_number=4)
    add_lab_objective(lab=second_order_lowpass,
                      objective="The purpose of this week's lab is to look at second order filters.")
    
    # Second Order Low-pass Filters Simulation
    solpf_simulation = add_simulation(lab=second_order_lowpass, name="Second Order Lowpass Filters Simulation")
    add_simulation_element(simulation=solpf_simulation,
                           name="second order lowpass filters simulation 1", number=1,
                           text_input="Using a circuit simulator, build the following circuit. Allow \(V_{in}\) to be a 1V " +
                           "2kHz sine wave. Let R=1500 \(\\Omega\), C=4.7nF, and L=1mH. Run your simulation (5ms should " +
                           "be enough) and determine the amplitude of the output cosine. Repeat this process for the " +
                           "following frequencies: f=2k, 5k, 10k, 20k, 30k, 40k, 50k, 60k, 70k, 80k, 90k, " +
                           "100k, 200k, 300kHz. Make a plot with frequency f on the x-axis and the \(V_{out}\) " +
                           "amplitude on the y-axis. What kind of filter is this?",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=solpf_simulation,
                           name="second order lowpass filters  simulation 2", number=2,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab04/fig01.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=solpf_simulation,
                           name="second order lowpass filters  simulation 3", number=3,
                           text_input="Figure 1",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')
    
    # Second Order Low-pass Filters Hardware
    solpf_hardware = add_hardware(lab=second_order_lowpass, name="Second Order Lowpass Filters Hardware")
    
    add_hardware_element(hardware=solpf_hardware, name="second order lowpass filters hardware 1", number=1,
                         text_input="<h4>Part 1. FILTER 1</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=solpf_hardware, name="second order lowpass filters hardware 2", number=2,
                         text_input="Using your Digilent board, build the circuit from the simulation. Generate a " +
                         "1V cosine input, apply it as \(V_{in}\), and measure the amplitude of \(V_{out}\). Do this measurement " +
                         "for all of the frequencies in the simulation. Create a plot of \(V_{out}\) vs f and superimpose it " +
                         "on the simulation plot. How well do they agree?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=solpf_hardware, name="second order lowpass filters hardware 3", number=3,
                         text_input="<h4>Part 2. FILTER 2</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=solpf_hardware, name="second order lowpass filters hardware 4", number=4,
                         text_input="Create a first order RC low-pass filter with the same cutoff frequency as " +
                         "the Filter 1 circuit. Measure the \(V_{out}\) at all the same frequencies as with Filter 1 " +
                         "and superimpose the frequency plot with that of Filter 1. How are the two filters similar? " +
                         "How are they different? Which is the better filter?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=solpf_hardware, name="second order lowpass filters hardware 5", number=5,
                         text_input="<h4>Part 3. FILTER 3</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=solpf_hardware, name="second order lowpass filters hardware 6", number=6,
                         text_input="Repeat the steps for Filter 1 but using R=100 \(\\Omega\). How does the filter " +
                         "response for this filter differ from that of Filter 1?",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    
    ###
    # EE Science II Lab 5: Second Order Step Response II
    ###
    second_order_step_ii = add_lab(course=ee_science_ii, name="Second Order Step Response II",
                                   start_date=timezone.now(), due_date=timezone.now(),
                                   lab_number=5)
    add_lab_objective(lab=second_order_step_ii,
                      objective="The purpose of this week's lab is to take another look at second order circuit step responses.")
    
    # Second Order Step Response II Simulation
    sos2_simulation = add_simulation(lab=second_order_step_ii, name="Second Order Step Response II Simulation")
    add_simulation_element(simulation=sos2_simulation,
                           name="second order step response 2 simulation 1", number=1,
                           text_input="Determine the characteristic equation for the following circuit:",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=sos2_simulation,
                           name="second order step response 2 simulation 2", number=2,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab05/fig01.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=sos2_simulation,
                           name="second order step response 2 simulation 3", number=3,
                           text_input="Figure 1",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')
    
    # Second Order Step Response II Hardware
    sos2_hardware = add_hardware(lab=second_order_step_ii, name="Second Order Step Response II Hardware")
    
    add_hardware_element(hardware=sos2_hardware, name="second order step response 2 hardware 1", number=1,
                         text_input="<h4>Part 1. CIRCUIT 1</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=sos2_hardware, name="second order step response 2 hardware 2", number=2,
                         text_input="For the circuit in the simulation, select values for \(R_1\), \(L_1\), and \(C_1\) that " +
                         "give you the step response shown here. Build your circuit and demonstrate that you have " +
                         "successfully recreated this step response.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=sos2_hardware, name="second order step response 2 hardware 3", number=3,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab05/fig02.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=sos2_hardware, name="second order step response 2 hardware 4", number=4,
                         text_input="Figure 2",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    add_hardware_element(hardware=sos2_hardware, name="second order step response 2 hardware 5", number=5,
                         text_input="<h4>Part 2. CIRCUIT 2</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=sos2_hardware, name="second order step response 2 hardware 6", number=6,
                         text_input="For the circuit in the prelab, select values for \(R_1\), \(L_1\), and \(C_1\) " +
                         "that give you the step response shown here. Build your circuit and demonstrate that " +
                         "you have successfully recreated this step response.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=sos2_hardware, name="second order step response 2 hardware 7", number=7,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab05/fig03.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=sos2_hardware, name="second order step response 2 hardware 8", number=8,
                         text_input="Figure 3",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')

    ###
    # EE Science II Lab 6: Complex Impedances
    ###
    complex_impedances = add_lab(course=ee_science_ii, name="Complex Impedances",
                                 start_date=timezone.now(), due_date=timezone.now(),
                                 lab_number=6)
    add_lab_objective(lab=complex_impedances,
                      objective="The purpose of this week's lab is to measure impedances.")
    
    # Complex Impedances Simulation
    ci_simulation = add_simulation(lab=complex_impedances, name="Complex Impedances Simulation")
    add_simulation_element(simulation=ci_simulation,
                           name="complex impedances simulation 1", number=1,
                           text_input="For each of the two circuits shown below, solve for the equation " +
                           "of the equivalent impedance looking left into <i>AA'</i>. The equations should " +
                           "both be functions of frequency.",
                           image_input=None, equation_input="", video_input="", 
                           element_type='text')
    add_simulation_element(simulation=ci_simulation,
                           name="complex impedances simulation 2", number=2,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab06/fig01.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=ci_simulation,
                           name="complex impedances simulation 3", number=3,
                           text_input="Figure 1",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')
    add_simulation_element(simulation=ci_simulation,
                           name="complex impedances simulation 4", number=4,
                           text_input="",
                           image_input='VLA/courses/EE_Science_II/Lab06/fig02.jpg', equation_input="", video_input="", 
                           element_type='image')
    add_simulation_element(simulation=ci_simulation,
                           name="complex impedances simulation 5", number=5,
                           text_input="Figure 2",
                           image_input=None, equation_input="", video_input="", 
                           element_type='caption')
    
    # Complex Impedances Hardware
    ci_hardware = add_hardware(lab=complex_impedances, name="Complex Impedances Hardware")
    
    add_hardware_element(hardware=ci_hardware, name="complex impedances hardware 1", number=1,
                         text_input="<h4>Part 1. CIRCUIT 1</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ci_hardware, name="complex impedances hardware 2", number=2,
                         text_input="Build the LR circuit from the simulation. Your task is to create a plot " +
                         "with frequency on the x-axis and impedance magnitude on the y-axis. You will have " +
                         "to do some thinking about how you can measure the impedance of the LR circuit at " +
                         "any given frequency. Measure the impedance magnitude at the following frequencies to " +
                         "create your plot. These frequencies are log-spaced so be sure to use log-spacing on " +
                         "your x-axis.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ci_hardware, name="complex impedances hardware 3", number=3,
                         text_input="f = 100Hz, 200Hz, 500Hz, 1kHz, 2kHz, 5kHz, 10kHz, 20kHz, 50kHz, 100kHz, 200kHz, 500kHz, 1mHz",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ci_hardware, name="complex impedances hardware 4", number=4,
                         text_input="When you turn in your report, be sure to superimpose a plot of your hand " +
                         "calculation values (from the simulation) onto your data points that you collect in " +
                         "lab. Comment on how well the predicted (theoretical simulation) values match to the " +
                         "measured data points.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ci_hardware, name="complex impedances hardware 5", number=5,
                         text_input="<h4>Part 2. CIRCUIT 2</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ci_hardware, name="complex impedances hardware 6", number=6,
                         text_input="Repeat the previous section using the RC circuit from the simulation " +
                         "(use the same list of frequencies too). Note that the ceramic capacitor " +
                         "labeled '104' should be 100nF.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ci_hardware, name="complex impedances hardware 7", number=7,
                         text_input="<h4>Part 3. CIRCUIT 3</h4>",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ci_hardware, name="complex impedances hardware 8", number=8,
                         text_input="Build the circuit shown below and apply a 0.1V cosine at \(V_{in}\). " +
                         "Start with a frequency of 100Hz. Measure the amplitude of the resulting " +
                         "cosine at the output. Your <i>gain</i> is defined as the ratio of the " +
                         "cosine amplitude at \(V_{out}\) to \(V_{in}\). Make a plot of gain versus frequency " +
                         "(using the same list of frequencies as the two previous parts). What kind " +
                         "of filter do you think this is? Note: be sure to apply power to your op-amp: " +
                         "\(\\pm\)5 Volts should be sufficient.",
                         image_input=None, equation_input="", video_input="", 
                         element_type='text')
    add_hardware_element(hardware=ci_hardware, name="complex impedances hardware 9", number=9,
                         text_input="",
                         image_input='VLA/courses/EE_Science_II/Lab06/fig03.jpg', equation_input="", video_input="", 
                         element_type='image')
    add_hardware_element(hardware=ci_hardware, name="complex impedances hardware 10", number=10,
                         text_input="Figure 3",
                         image_input=None, equation_input="", video_input="", 
                         element_type='caption')
    
    ###
    # EE Science II Lab 7: Bass Booster
    ###
    bass_booster = add_lab(course=ee_science_ii, name="Bass Booster",
                       start_date=timezone.now(), due_date=timezone.now(),
                       lab_number=7)
    add_lab_objective(lab=bass_booster,
                      objective="A stereo amplifier is essential a bunch of really good filters designed to isolate specific " +
                      "frequencies (i.e. treble, bass), and amplify those signals for their respective speaker components.  " +
                      "In this week's lab, you will essentially be building a bass booster.  ")
    
    ###
    # EE Science II Lab 8: Op-Amps
    ###
    opp_amps = add_lab(course=ee_science_ii, name="Op Amps",
                       start_date=timezone.now(), due_date=timezone.now(),
                       lab_number=8)
    add_lab_objective(lab=opp_amps,
                      objective="Op-Amps have some interesting characteristics which we have to take into account when we design " +
                                "AC circuits. Specifically, there is a limit to what frequencies they can operate at. Beyond these " +
                                "limits, the transistors inside the opamp can't charge or discharge fast enough to produce the " +
                                "desired output. This week we will be investigating gain-bandwidth product and slew rate. You " +
                                "should read about both these phenomena on Wikipedia at <a href=\"http://en.wikipedia.org/wiki/Gain-bandwidth_product\">Gain Bandwidth Product</a> "+
                                "and <a href=\"http://en.wikipedia.org/wiki/Slew_rate\">Slew Rate</a> respectively. You should also use Google to find " +
                                "the data sheet for your opamp and look up the gain-bandwidth product and the slew rate. Be mindful " +
                                "that different students seem to have different model opamps so don't assume that yours is the same " +
                                "as everyone else's. Finally, note that bandwidth refers to the frequency at which output is " +
                                "reduced to 0.707 times the low-frequency output value.")
    
    ###
    # EE Science II Lab 9: Amplitude Modulation
    ###
    amplitude_modulation = add_lab(course=ee_science_ii, name="Amplitude Modulation",
                                   start_date=timezone.now(), due_date=timezone.now(),
                                   lab_number=9)
    add_lab_objective(lab=amplitude_modulation,
                      objective="")
    
    ###
    # EE Science II Lab 10: Boost Converter
    ###
    boost_converter = add_lab(course=ee_science_ii, name="Boost Converter",
                              start_date=timezone.now(), due_date=timezone.now(),
                              lab_number=10)
    add_lab_objective(lab=boost_converter,
                      objective="The goal of this laboratory is to introduce you to power supply design. Power supply design is a very important part of both analog and digital electronics. Though we haven't formally studied this topic yet, we have learned about many of the basic elements that go into power supply design. In this laboratory, we will introduce you to the basic concepts, and then provide you an opportunity to build a more complex circuit using transformers.")

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