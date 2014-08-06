# -*- coding: utf-8 -*-
import os
from django.utils import timezone

'''
Script to populate the complete Vocabulary Domain Database for Circuits

Creates one VocabDomain, 11 VocabTopics:
1.  Circuit elements and equipment (resistor, breadboard, dc source)
2.  Action word (compute, change, use)
3.  Question word (why, what, how)
4.  Problem word (wrong, don't, cannot)
5.  Circuit concepts (resistance, power, energy)
6.  Other (positive, gain, division, unit)
7.  Circuit Laws (thevenin, conservation, superposition)
8.  Circuit diagram and measurements (series, parallel, rms, ground)
9.  Math words (sum, difference, equivalent)
10. Units (ohm, watt, joule)
11. Help

Also adds Synonyms, Defintions, and current list of instructional Videos
'''

def populate():
    
    circuits_domain = add_vocab_domain(name = 'Circuits')
    
    # Circuit ELements and Equipment
    topic_elements = add_vocab_topic(domain=circuits_domain,
                    topic="Circuit Elements and Equipment",
                    def_useful=True)
    
    resistor_node = add_node("Resistor",
                    definition="A resistor is a passive two-terminal electrical component that implements electrical resistance " +
                    "as a circuit element. Resistors act to reduce current flow, and, at the same time, act to lower voltage " +
                    "levels within circuits. Resistors may have fixed resistances or variable resistances, such as those found " +
                    "in thermistors, varistors, trimmers, photoresistors, humistors, piezoresistors and potentiometers.",
                    topic=topic_elements)
    add_synonym("Res", node=resistor_node)
    add_synonym("R", node=resistor_node)
    add_synonym("Ohm", node=resistor_node)
    add_synonym("Conductor", node=resistor_node)
    
    capacitor_node = add_node("Capacitor",
                    definition="A capacitor (originally known as a condenser) is a passive two-terminal electrical component used " +
                    "to store energy electrostatically in an electric field. The forms of practical capacitors vary widely, " +
                    "but all contain at least two electrical conductors (plates) separated by a dielectric (i.e., insulator). " +
                    "The conductors can be thin films of metal, aluminum foil or disks, etc. The 'nonconducting' dielectric acts to " +
                    "increase the capacitor's charge capacity. A dielectric can be glass, ceramic, plastic film, air, paper, mica, etc. " +
                    "Capacitors are widely used as parts of electrical circuits in many common electrical devices. Unlike a " +
                    "resistor, an ideal capacitor does not dissipate energy. Instead, a capacitor stores energy in the form of an electrostatic field between its plates.",
                    topic=topic_elements)
    add_synonym("Cap", node=capacitor_node)
    add_synonym("F", node=capacitor_node)
    add_synonym("Farad", node=capacitor_node)
    
    inductor_node = add_node("Inductor",
                    definition="An inductor, also called a coil or reactor, is a passive two-terminal electrical component which " +
                    "resists changes in electric current passing through it. It consists of a conductor such as a wire, usually " +
                    "wound into a coil. When a current flows through it, energy is stored temporarily in a magnetic field in the " +
                    "coil. When the current flowing through an inductor changes, the time-varying magnetic field induces a voltage " +
                    "in the conductor, according to Faraday's law of electromagnetic induction, which opposes the change in current that created it.",
                    topic=topic_elements)
    add_synonym("Ind", node=inductor_node)
    add_synonym("L", node=inductor_node)
    add_synonym("Henry", node=inductor_node)
    add_synonym("H", node=inductor_node)
    
    dc_source_node = add_node("DC Source",
                              definition="A power supply is an electronic device that supplies electric energy to an electrical load." + 
                              "The primary function of a power supply is to convert one form of electrical energy to another and, as a result, power supplies are sometimes referred to as electric power converters." + 
                              "Some power supplies are discrete, stand-alone devices, whereas others are built into larger devices along with their loads." + 
                              "Examples of the latter include power supplies found in desktop computers and consumer electronics devices." + 
                              "A DC power supply is one that supplies a voltage of fixed polarity (either positive or negative) to its load." +
                              "Depending on its design, a DC power supply may be powered from a DC source or from an AC source such as the power mains.",
                              topic=topic_elements)
    add_synonym("DC Supply", node=dc_source_node)
    add_synonym("Supply", node=dc_source_node)
    add_synonym("Source", node=dc_source_node)
    add_synonym("DCS", node=dc_source_node)
    add_synonym("Battery", node=dc_source_node)
    add_synonym("Cell", node=dc_source_node)
    
    multimeter_node = add_node("Multimeter",
                    definition="A multimeter or a multitester, also known as a VOM (Volt-Ohm meter), is an electronic measuring instrument " +
                    "that combines several measurement functions in one unit. A typical multimeter would include basic features such " +
                    "as the ability to measure voltage, current, and resistance. Analog multimeters use a microammeter whose pointer moves " +
                    "over a scale calibrated for all the different measurements that can be made. Digital multimeters (DMM, DVOM) display the " +
                    "measured value in numerals, and may also display a bar of a length proportional to the quantity being measured. Digital " +
                    "multimeters are now far more common than analog ones, but analog multimeters are still preferable in some cases, for " +
                    "example when monitoring a rapidly varying value.",
                    topic=topic_elements)
    add_synonym("Voltmeter", node=multimeter_node)
    add_synonym("Ammeter", node=multimeter_node)
    add_synonym("Ohmmeter", node=multimeter_node)
    add_synonym("Meter", node=multimeter_node)
    add_synonym("Multim", node=multimeter_node)
    
    func_gen_node = add_node("Function Generator",
                    definition="A function generator is usually a piece of electronic test equipment or software used to generate different " +
                    "types of electrical waveforms over a wide range of frequencies. Some of the most common waveforms produced by the " +
                    "function generator are the sine, square, triangular and sawtooth shapes. These waveforms can be either repetitive or " +
                    "single-shot (which requires an internal or external trigger source). Integrated circuits used to generate waveforms " +
                    "may also be described as function generator ICs.",
                    topic=topic_elements)
    add_synonym("AC Supply", node=func_gen_node)
    add_synonym("Generator", node=func_gen_node)
    add_synonym("AC Source", node=func_gen_node)
    add_synonym("Func Gen", node=func_gen_node)
    
    oscilloscope_node = add_node("Oscilloscope",
                    definition="An oscilloscope, previously called an oscillograph, and informally known as a scope, CRO (for " +
                    "cathode-ray oscilloscope), or DSO (for the more modern digital storage oscilloscope), is a type of " +
                    "electronic test instrument that allows observation of constantly varying signal voltages, usually as a " +
                    "two-dimensional plot of one or more signals as a function of time. Non-electrical signals (such as sound " +
                    "or vibration) can be converted to voltages and displayed.",
                    topic=topic_elements)
    add_synonym("Oscope", node=oscilloscope_node)
    add_synonym("Display", node=oscilloscope_node)
    add_synonym("CRT", node=oscilloscope_node)
    add_synonym("Cathode", node=oscilloscope_node)
    
    spect_anal_node = add_node("Spectrum Analyzer",
                    definition="A spectrum analyzer measures the magnitude of an input signal versus frequency within the full " +
                    "frequency range of the instrument. The primary use is to measure the power of the spectrum of known and " +
                    "unknown signals. The input signal that a spectrum analyzer measures is electrical, however, spectral " +
                    "compositions of other signals, such as acoustic pressure waves and optical light waves, can be considered " +
                    "through the use of an appropriate transducer. Optical spectrum analyzers also exist, which use direct optical " +
                    "techniques such as a monochromator to make measurements.",
                    topic=topic_elements)
    add_synonym("Spectrum", node=spect_anal_node)
    add_synonym("Analyzer", node=spect_anal_node)
    add_synonym("Sweep", node=spect_anal_node)
    add_synonym("SA", node=spect_anal_node)
    
    diode_node = add_node("Diode",
                    definition="In electronics, a diode is a two-terminal electronic component with asymmetric conductance; it has " +
                    "low (ideally zero) resistance to current in one direction, and high (ideally infinite) resistance in the other. " +
                    "A semiconductor diode, the most common type today, is a crystalline piece of semiconductor material with a p-n " +
                    "junction connected to two electrical terminals. A vacuum tube diode has two electrodes, a plate (anode) and a " +
                    "heated cathode. Semiconductor diodes were the first semiconductor electronic devices. The discovery of crystals' " +
                    "rectifying abilities was made by German physicist Ferdinand Braun in 1874. The first semiconductor diodes, " +
                    "called cat's whisker diodes, developed around 1906, were made of mineral crystals such as galena. Today, most " +
                    "diodes are made of silicon, but other semiconductors such as selenium or germanium are sometimes used.",
                    topic=topic_elements)
    add_synonym("Rectifier", node=diode_node)
    add_synonym("Semiconductor", node=diode_node)
    add_synonym("Junction", node=diode_node)
    
    wire_node = add_node("Wire",
                         definition="A wire is a single, usually cylindrical, flexible strand or rod of metal."+  
                         " Wires are used to bear mechanical loads or electricity and telecommunications signals."+
                         " Wire is commonly formed by drawing the metal through a hole in a die or draw plate."+ 
                         " Wire gauges come in various standard sizes, as expressed in terms of a gauge number." + 
                         " The term wire is also used more loosely to refer to a bundle of such strands, as in 'multistranded wire', which is more correctly termed a wire rope in mechanics, or a cable in electricity."+
                         " Wire comes in solid core, stranded, or braided forms.",
                    topic=topic_elements)
    add_synonym("Cable", node=wire_node)
    add_synonym("Line", node=wire_node)
    add_synonym("Short", node=wire_node)
    add_synonym("Connector", node=wire_node)
    
    potentiometer_node = add_node("Potentiometer",
                    definition="A potentiometer, informally a pot, is a three-terminal resistor with a sliding or rotating contact " +
                    "that forms an adjustable voltage divider. If only two terminals are used, one end and the wiper, it acts as a " +
                    "variable resistor or rheostat.",
                    topic=topic_elements)
    
    element_node = add_node("Element",
                    definition="Electrical elements are conceptual abstractions representing idealized electrical components, such as " +
                    "resistors, capacitors, and inductors, used in the analysis of electrical networks. Any electrical network can " +
                    "be analysed as multiple, interconnected electrical elements in a schematic diagram or circuit diagram, each of " +
                    "which affects the voltage in the network or current through the network. These ideal electrical elements represent " +
                    "real, physical electrical or electronic components but they do not exist physically and they are assumed to have " +
                    "ideal properties according to a lumped element model, while components are objects with less than ideal properties, " +
                    "a degree of uncertainty in their values and some degree of nonlinearity, each of which may require a combination of " +
                    "multiple electrical elements in order to approximate its function.",
                    topic=topic_elements)
    add_synonym("Component", node=element_node)
    add_synonym("Entity", node=element_node)
    add_synonym("Instrument", node=element_node)
    add_synonym("Device", node=element_node)
    
    breadboard_node = add_node("Breadboard",
                    definition="A breadboard (or protoboard) is usually a construction base for prototyping of electronics. The term " +
                    "'breadboard' is commonly used to refer to a solderless breadboard (plugboard).",
                    topic=topic_elements)
    add_synonym("Board", node=breadboard_node)
    
    switch_node = add_node("Switch",
                    definition="In electrical engineering, a switch is an electrical component that can break an electrical circuit, interrupting the current or diverting it from one conductor to another.",
                    topic=topic_elements)
    
    transistor_node = add_node("Transistor",
                    definition="A transistor is a semiconductor device used to amplify and switch electronic signals and electrical power. " +
                    "It is composed of semiconductor material with at least three terminals for connection to an external circuit. A " +
                    "voltage or current applied to one pair of the transistor's terminals changes the current through another pair of " +
                    "terminals. Because the controlled (output) power can be higher than the controlling (input) power, a transistor " +
                    "can amplify a signal. Today, some transistors are packaged individually, but many more are found embedded in " +
                    "integrated circuits.",
                    topic=topic_elements)
    add_synonym("BJT", node=transistor_node)
    
    ammeter_node = add_node("Ammeter",
                    definition="An ammeter is a measuring instrument used to measure the electric current in a circuit. Electric " +
                    "currents are measured in amperes (A), hence the name. Instruments used to measure smaller currents, in the " +
                    "milliampere or microampere range, are designated as milliammeters or microammeters. Early ammeters were laboratory " +
                    "instruments which relied on the Earth's magnetic field for operation. By the late 19th century, improved " +
                    "instruments were designed which could be mounted in any position and allowed accurate measurements in electric " +
                    "power systems.",
                    topic=topic_elements)
    
    voltmeter_node = add_node("Voltmeter",
                    definition="A voltmeter is an instrument used for measuring electrical potential difference between two points in " +
                    "an electric circuit. Analog voltmeters move a pointer across a scale in proportion to the voltage of the " +
                    "circuit; digital voltmeters give a numerical display of voltage by use of an analog to digital converter.",
                    topic=topic_elements)
    
    ohmmeter_node = add_node("Ohmmeter",
                    definition="An ohmmeter is an electrical instrument that measures electrical resistance, the opposition to an " +
                    "electric current. Micro-ohmmeters (microhmmeter or microohmmeter) make low resistance measurements. Megohmmeters " +
                    "(aka megaohmmeter or in the case of a trademarked device Megger) measure large values of resistance. The " +
                    "unit of measurement for resistance is ohms.",
                    topic=topic_elements)
    
    # Action Words
    topic_action = add_vocab_topic(domain=circuits_domain,
                    topic="Action Words",
                    def_useful=False)
    measure_node = add_node("Measure", definition="", topic=topic_action)
    add_synonym("Know", node=measure_node)
    add_synonym("Get", node=measure_node)
    add_synonym("See", node=measure_node)
    add_synonym("Take", node=measure_node)
    add_synonym("Find", node=measure_node)
    add_synonym("Quantify", node=measure_node)
    add_synonym("Need", node=measure_node)
    add_synonym("Bill", node=measure_node)
    
    compute_node = add_node("Compute", definition="", topic=topic_action)
    add_synonym("Calculate", node=compute_node)
    add_synonym("Evaluate", node=compute_node)
    add_synonym("Build", node=compute_node)
    add_synonym("Verify", node=compute_node)
    add_synonym("Formula", node=compute_node)
    
    change_node = add_node("Change", definition="", topic=topic_action)
    add_synonym("Set", node=change_node)
    add_synonym("Reverse", node=change_node)
    add_synonym("Tune", node=change_node)
    add_synonym("Vary", node=change_node)
    
    use_node = add_node("Use", definition="", topic=topic_action)
    add_synonym("Place", node=use_node)
    add_synonym("Connect", node=use_node)
    add_synonym("Create", node=use_node)
    add_synonym("Drag Drop", node=use_node)
    add_synonym("Bill", node=use_node)
    
    move_node = add_node("Move", definition="", topic=topic_action)
    
    remove_node = add_node("Remove", definition="", topic=topic_action)
    add_synonym("Erase", node=remove_node)
    add_synonym("Delete", node=remove_node)
    add_synonym("Take Off", node=remove_node)
    add_synonym("Eliminate", node=remove_node)
    add_synonym("Clear", node=remove_node)
    
    save_node = add_node("Save", definition="", topic=topic_action)
    
    open_node = add_node("Open", definition="", topic=topic_action)
    
    work_node = add_node("Work", definition="", topic=topic_action)
    add_synonym("Does", node=work_node)
    add_synonym("Define", node=work_node)
    add_synonym("Definition", node=work_node)
    add_synonym("Mean", node=work_node)
    add_synonym("Signify", node=work_node)
    add_synonym("Understand", node=work_node)
    add_synonym("Whats", node=work_node)
    add_synonym("Whys", node=work_node)
    add_synonym("Hows", node=work_node)
    add_synonym("Wheres", node=work_node)
    add_synonym("Do", node=work_node)
    add_synonym("Is", node=work_node)
    add_synonym("Be", node=work_node)
    add_synonym("Are", node=work_node)
    add_synonym("This", node=work_node)
    add_synonym("That", node=work_node)
    add_synonym("Bill", node=work_node)
    
    read_node = add_node("Read", definition="", topic=topic_action)
    
    # Question Words
    topic_question = add_vocab_topic(domain=circuits_domain,
                                    topic="Question Words",
                                    def_useful=False)
    how_node = add_node("How", definition="", topic=topic_question)
    add_synonym("Hows", node=how_node)
    add_synonym("Howz", node=how_node)
    
    what_node = add_node("What", definition="", topic=topic_question)
    add_synonym("Whats", node=what_node)
    add_synonym("Whatz", node=what_node)
    
    why_node = add_node("Why", definition="", topic=topic_question)
    add_synonym("Whys", node=why_node)
    add_synonym("Whyz", node=why_node)
    
    when_node = add_node("When", definition="", topic=topic_question)
    add_synonym("Whens", node=when_node)
    add_synonym("Whenz", node=when_node)
    
    # Problem Words
    topic_problems = add_vocab_topic(domain=circuits_domain,
                                    topic="Problem Words",
                                    def_useful=False)
    wrong_node = add_node("Wrong", definition="", topic=topic_problems)
    add_synonym("Incorrect", node=wrong_node)
    add_synonym("Not Correct", node=wrong_node)
    add_synonym("Error", node=wrong_node)
    add_synonym("Mistake", node=wrong_node)
    add_synonym("Not Right", node=wrong_node)
    add_synonym("Not", node=wrong_node)
    add_synonym("Fault", node=wrong_node)
    add_synonym("Do Not", node=wrong_node)
    add_synonym("Dont", node=wrong_node)
    add_synonym("Cant", node=wrong_node)
    add_synonym("Cannot", node=wrong_node)
    add_synonym("Cant", node=wrong_node)
    add_synonym("Doesnt", node=wrong_node)
    add_synonym("Isnt", node=wrong_node)
    
    # Circuit Concepts
    topic_concepts = add_vocab_topic(domain=circuits_domain,
                                    topic="Circuit Concepts",
                                    def_useful=True)
    voltage_node = add_node("Voltage", 
                            definition="Voltage, electrical potential difference, electric tension or electric pressure (denoted ∆V and measured in units of electric potential: volts, or joules per coulomb) is the electric potential difference between two points, or the difference in electric potential energy of a unit charge transported between two points." + 
                            " Voltage is equal to the work done per unit charge against a static electric field to move the charge between two points."+ 
                            " A voltage may represent either a source of energy (electromotive force), or lost, used, or stored energy (potential drop)."+
                            " A voltmeter can be used to measure the voltage (or potential difference) between two points in a system; often a common reference potential such as the ground of the system is used as one of the points."+ 
                            " Voltage can be caused by static electric fields, by electric current through a magnetic field, by time-varying magnetic fields, or some combination of these three.", 
                            topic=topic_concepts)
    add_synonym("Volt", node=voltage_node)
    add_synonym("Volts", node=voltage_node)
    add_synonym("V", node=voltage_node)
    add_synonym("Potential", node=voltage_node)
    add_synonym("PD", node=voltage_node)
    add_synonym("KVL", node=voltage_node)
    
    current_node = add_node("Current", definition="An electric current is a flow of electric charge." +  
                            " In electric circuits this charge is often carried by moving electrons in a wire." + 
                            " It can also be carried by ions in an electrolyte, or by both ions and electrons such as in a plasma." +
                            " The SI unit for measuring an electric current is the ampere, which is the flow of electric charge across a surface at the rate of one coulomb per second." + 
                            " Electric current is measured using a device called an ammeter." + 
                            " Electric currents can have many effects, notably heating, but they also create magnetic fields, which are used in motors, inductors and generators.", 
                            topic=topic_concepts)
    add_synonym("Amp", node=current_node)
    add_synonym("Amps", node=current_node)
    add_synonym("Ampere", node=current_node)
    add_synonym("KCL", node=current_node)
    add_synonym("DC", node=current_node)
    add_synonym("AC", node=current_node)
    
    resistance_node = add_node("Resistance",
                               definition="The electrical resistance of an electrical conductor is the opposition to the passage of an electric current through that conductor." +  
                               " The inverse quantity is electrical conductance, the ease with which an electric current passes."+
                               " Electrical resistance shares some conceptual parallels with the mechanical notion of friction." + 
                               " The SI unit of electrical resistance is the ohm (Ω), while electrical conductance is measured in siemens (S).",
                               topic=topic_concepts)
    add_synonym("Ohm", node=resistance_node)
    add_synonym("Ohms", node=resistance_node)
    
    capacitance_node = add_node("Capacitance", 
                                definition="Capacitance is the ability of a body to store an electrical charge." + 
                                " Any object that can be electrically charged exhibits capacitance." +  
                                " A common form of energy storage device is a parallel-plate capacitor." + 
                                " In a parallel plate capacitor, capacitance is directly proportional to the surface area of the conductor plates and inversely proportional to the separation distance between the plates.", 
                                topic=topic_concepts)
    add_synonym("Farad", node=capacitance_node)
    add_synonym("F", node=capacitance_node)
    
    inductance_node = add_node("Inductance", 
                               definition="In electromagnetism and electronics, inductance is the property of a conductor by which a change in current flowing through it 'induces' (creates) a voltage (electromotive force) in both the conductor itself (self-inductance) and in any nearby conductors (mutual inductance)." + 
                               "The term 'inductance' was coined by Oliver Heaviside in February 1886." + 
                               "It is customary to use the symbol L for inductance, in honour of the physicist Heinrich Lenz." + 
                               "In the SI system the measurement unit for inductance is the henry, H, named in honor of the scientist who discovered inductance, Joseph Henry.", 
                               topic=topic_concepts)
    add_synonym("Henry", node=inductance_node)
    add_synonym("H", node=inductance_node)
    
    power_node = add_node("Power",
                          definition="Electric power is the rate at which electric energy is transferred by an electric circuit." + 
                          " The SI unit of power is the watt, one joule per second." + 
                          " Electric power is usually produced by electric generators, but can also be supplied by sources such as electric batteries." + 
                          " Electric power is generally supplied to businesses and homes by the electric power industry." + 
                          " Electric power is usually sold by the kilowatt hour (3.6 MJ) which is the product of power in kilowatts multiplied by running time in hours." + 
                          " Electric utilities measure power using an electricity meter, which keeps a running total of the electric energy delivered to a customer.", 
                          topic=topic_concepts)
    add_synonym("Watt", node=power_node)
    add_synonym("W", node=power_node)
    
    time_node = add_node("Time", 
                         definition="",
                         topic=topic_concepts)
    add_synonym("Term", node=time_node)
    add_synonym("Second", node=time_node)
    add_synonym("MS", node=time_node)
    add_synonym("S", node=time_node)
    
    frequency_node = add_node("Frequency", 
                              definition="Frequency is the number of occurrences of a repeating event per unit time." +  
                              " It is also referred to as temporal frequency, which emphasizes the contrast to spatial frequency and angular frequency." + 
                              " The period is the duration of one cycle in a repeating event, so the period is the reciprocal of the frequency." + 
                              " For example, if a newborn baby's heart beats at a frequency of 120 times a minute, its period – the interval between beats – is half a second (60 seconds (i.e. a minute) divided by 120 beats).",
                              topic=topic_concepts)
    add_synonym("Hetz", node=frequency_node)
    add_synonym("CPS", node=frequency_node)
    add_synonym("Hz", node=frequency_node)
    
    waveform_node = add_node("Waveform",
                             definition="A waveform is the shape and form of a signal such as a wave moving in a physical medium or an abstract representation." + 
                             " In many cases the medium in which the wave is being propagated does not permit a direct visual image of the form."+
                             " In these cases, the term 'waveform' refers to the shape of a graph of the varying quantity against time or distance."+
                             " An instrument called an oscilloscope can be used to pictorially represent a wave as a repeating image on a screen.", 
                             topic=topic_concepts)
    add_synonym("Wave", node=waveform_node)
    add_synonym("Crest", node=waveform_node)
    add_synonym("Trough", node=waveform_node)
    add_synonym("Sine", node=waveform_node)
    add_synonym("Sinusoid", node=waveform_node)
    add_synonym("Square", node=waveform_node)
    
    amplitude_node = add_node("Amplitude",
                              definition="Peak-to-peak amplitude is the change between peak (highest amplitude value) and trough (lowest amplitude value, which can be negative)."+
                              " With appropriate circuitry, peak-to-peak amplitudes of electric oscillations can be measured by meters or by viewing the waveform on an oscilloscope.", 
                              topic=topic_concepts)
    add_synonym("Value", node=amplitude_node)
    add_synonym("Magnitude", node=amplitude_node)
    add_synonym("Reading", node=amplitude_node)
    add_synonym("Entry", node=amplitude_node)
    add_synonym("Meter", node=amplitude_node)
    add_synonym("Metre", node=amplitude_node)
    add_synonym("Y", node=amplitude_node)
    
    reactance_node = add_node("Reactance", 
                              definition="In electrical and electronic systems, reactance is the opposition of a circuit element to a change of electric current or voltage, due to that element's inductance or capacitance."+
                              " A built-up electric field resists the change of voltage on the element, while a magnetic field resists the change of current."+
                              " The notion of reactance is similar to electrical resistance, but they differ in several respects." + 
                              " An ideal resistor has zero reactance, while ideal inductors and capacitors consist entirely of reactance."+
                              " The magnitude of the reactance of an inductor is proportional to frequency, while the magnitude of the reactance of a capacitor is inversely proportional to frequency.",
                              topic=topic_concepts)
    add_synonym("XC", node=reactance_node)
    add_synonym("XL", node=reactance_node)
    
    impedance_node = add_node("Impedance", 
                              definition="Electrical impedance is the measure of the opposition that a circuit presents to a current when a voltage is applied." +
                              "In quantitative terms, it is the complex ratio of the voltage to the current in an alternating current (AC) circuit."+
                              " Impedance extends the concept of resistance to AC circuits, and possesses both magnitude and phase, unlike resistance, which has only magnitude."+
                              " When a circuit is driven with direct current (DC), there is no distinction between impedance and resistance; the latter can be thought of as impedance with zero phase angle.", 
                              topic=topic_concepts)
    add_synonym("Z", node=impedance_node)
    
    conductance_node = add_node("Conductance",
                                definition="The electrical resistance of an electrical conductor is the opposition to the passage of an electric current through that conductor."+
                                " The inverse quantity is electrical conductance, the ease with which an electric current passes."+
                                " Electrical resistance shares some conceptual parallels with the mechanical notion of friction."+
                                " The SI unit of electrical resistance is the ohm (Ω), while electrical conductance is measured in siemens (S).",
                                topic=topic_concepts)
    add_synonym("G", node=conductance_node)
    add_synonym("Mho", node=conductance_node)
    add_synonym("Mhos", node=conductance_node)
    
    energy_node = add_node("Energy", definition="Electrical energy is energy newly derived from electrical potential energy."+
                           " When loosely used to describe energy absorbed or delivered by an electrical circuit (for example, one provided by an electric power utility) 'electrical energy' refers to energy which has been converted from electrical potential energy."+
                           " This energy is supplied by the combination of electric current and electrical potential that is delivered by the circuit."+
                           " At the point that this electrical potential energy has been converted to another type of energy, it ceases to be electrical potential energy."+
                           " Thus, all electrical energy is potential energy before it is delivered to the end-use."+
                           " Once converted from potential energy, electrical energy can always be described as another type of energy (heat, light, motion, etc.).", topic=topic_concepts)
    add_synonym("Joule", node=energy_node)
    add_synonym("J", node=energy_node)
    
    cycle_node = add_node("Cycle", 
                          definition="A turn is a unit of angle measurement equal to 360° or 2π radians."+
                          " A turn is also referred to as a revolution or complete rotation or full circle or cycle or rev or rot.",
                          topic=topic_concepts)
    
    period_node = add_node("Period",
                           definition="The period is the duration of one cycle in a repeating event, so the period is the reciprocal of the frequency."+
                          " For example, if a newborn baby's heart beats at a frequency of 120 times a minute, its period – the interval between beats – is half a second (60 seconds (i.e. a minute) divided by 120 beats).",  
                           topic=topic_concepts)
    
    wabelength_node = add_node("Wavelength", 
                               definition="In physics, the wavelength of a sinusoidal wave is the spatial period of the wave—the distance over which the wave's shape repeats."+
                               " It is usually determined by considering the distance between consecutive corresponding points of the same phase, such as crests, troughs, or zero crossings, and is a characteristic of both traveling waves and standing waves, as well as other spatial wave patterns."+
                               " Wavelength is commonly designated by the Greek letter lambda (λ)."+
                               " The concept can also be applied to periodic waves of non-sinusoidal shape."+
                               " The term wavelength is also sometimes applied to modulated waves, and to the sinusoidal envelopes of modulated waves or waves formed by interference of several sinusoids."+
                               " The SI unit of wavelength is the meter.", 
                               topic=topic_concepts)
    add_synonym("Wave Length", node=wabelength_node)
    
    circuit_node = add_node("Circuit",
                            definition="An electrical network is an interconnection of electrical elements such as resistors, inductors, capacitors, voltage sources, current sources and switches."+
                            " An electrical circuit is a network consisting of a closed loop, giving a return path for the current.", 
                            topic=topic_concepts)
    add_synonym("Loop", node=circuit_node)
    
    button_node = add_node("Button",
                           definition="A push-button (also spelled pushbutton) or simply button is a simple switch mechanism for controlling some aspect of a machine or a process."+
                           " Buttons are typically made out of hard material, usually plastic or metal."
                           , topic=topic_concepts)
    
    phasor_node = add_node("Phasor",
                           definition="In physics and engineering, a phase vector, or phasor, is a complex number representing a sinusoidal function whose amplitude (A), frequency (ω), and phase (θ) are time-invariant."+
                           " It is a subset of a more general concept called analytic representation. Phasors separate the dependencies on A, ω, and θ into three independent factors."+
                           " This can be particularly useful because the frequency factor (which includes the time-dependence of the sinusoid) is often common to all the components of a linear combination of sinusoids.",
                           topic=topic_concepts)
    
    phase_node = add_node("Phase",
                          definition="Phase in sinusoidal functions or in waves has two different, but closely related, meanings."+
                          " One is the initial angle of a sinusoidal function at its origin and is sometimes called phase offset or phase difference."+
                          " Another usage is the fraction of the wave cycle which has elapsed relative to the origin.", 
                          topic=topic_concepts)
    add_synonym("Angle", node=phase_node)
    
    # Other
    topic_other = add_vocab_topic(domain=circuits_domain,
                                  topic="Other",
                                  def_useful=True)
    positive_node = add_node("Positive", 
                             definition=" In DC circuits, the positive pole is usually marked red (or '+'). Electrons flow from the negative pole to the positive pole."+
                             " In a direct current (DC) circuit, one pole is always negative, the other pole is always positive and the electrons flow in one direction only."+
                             " In an alternating current (AC) circuit the two poles alternate between negative and positive and the direction of the electron flow reverses.",
                                topic=topic_other)
    
    negative_node = add_node("Negative", 
                             definition=" In DC circuits, the negative pole is usually marked black (or '-'). Electrons flow from the negative pole to the positive pole."+
                             " In a direct current (DC) circuit, one pole is always negative, the other pole is always positive and the electrons flow in one direction only."+
                             " In an alternating current (AC) circuit the two poles alternate between negative and positive and the direction of the electron flow reverses."
                            , topic=topic_other)
    
    polarity_node = add_node("Polarity", definition="Electrical polarity (positive and negative) is present in every electrical circuit. Electrons flow from the negative pole to the positive pole."+
                             " In a direct current (DC) circuit, one pole is always negative, the other pole is always positive and the electrons flow in one direction only."+
                             " In an alternating current (AC) circuit the two poles alternate between negative and positive and the direction of the electron flow reverses."+
                             " In DC circuits, the positive pole is usually marked red (or '+') and the negative pole is usually marked black (or '−'), but other color schemes are sometimes used in automotive and telecommunications systems."
                            , topic=topic_other)
    add_synonym("Sign", node=polarity_node)
    
    law_node = add_node("Law", definition="A scientific law is a statement based on repeated experimental observations that describes some aspect of the universe."+
                        " A scientific law always applies under the same conditions, and implies that there is a causal relationship involving its elements."+
                        " Factual and well-confirmed statements like 'Mercury is liquid at standard temperature and pressure' are considered too specific to qualify as scientific laws. "+
                        "Laws differ from scientific theories in that they do not posit a mechanism or explanation of phenomena: they are merely distillations of the results of repeated observation."+
                        " As such, a law is limited in applicability to circumstances resembling those already observed, and may be found false when extrapolated."+
                        " Ohm's law only applies to linear networks, Newton's law of universal gravitation only applies in weak gravitational fields, the early laws of aerodynamics such as Bernoulli's principle do not apply in case of compressible flow such as occurs in transonic and supersonic flight, Hooke's law only applies to strain below the elastic limit, etc."+
                        " These laws remain useful, but only under the conditions where they apply."
                        , topic=topic_other)
    add_synonym("Rule", node=law_node)
    add_synonym("Principle", node=law_node)
    add_synonym("Theorem", node=law_node)
    
    gain_node = add_node("Gain", definition="In electronics, gain is a measure of the ability of a circuit (often an amplifier) to increase the power or amplitude of a signal from the input to the output by adding energy converted from some power supply to the signal."+
                         " It is usually defined as the mean ratio of the signal output of a system to the signal input of the same system."+
                         " It is often expressed using the logarithmic decibel (dB) units ('dB gain')."+
                         " A gain greater than one (zero dB), that is, amplification, is the defining property of an active component or circuit, while a passive circuit will have a gain of less than one."
                         , topic=topic_other)
    
    loss_node = add_node("Loss", definition="Joule heating, also known as ohmic heating and resistive heating, is the process by which the passage of an electric current through a conductor releases heat. "+
                         "Joule heating is referred to as ohmic heating or resistive heating because of its relationship to Ohm's Law. "+
                         "It forms the basis for the large number of practical applications involving electric heating."+
                         " However, in applications where heating is an unwanted by-product of current use (e.g., load losses in electrical transformers) the diversion of energy is often referred to as resistive loss."+
                         " The use of high voltages in electric power transmission systems is specifically designed to reduce such losses in cabling by operating with commensurately lower currents."
                         , topic=topic_other)
    
    division_node = add_node("Division", 
                             definition="In electronics or EET, a voltage divider (also known as a potential divider) is a linear circuit that produces an output voltage (Vout) that is a fraction of its input voltage (Vin)."+
                             " Voltage division refers to the partitioning of a voltage among the components of the divider."
                             , topic=topic_other)
    
    unit_node = add_node("Unit",
                         definition="The International System of Units (abbreviated SI from French: Le Système international d'unités) is the modern form of the metric system and is the world's most widely used system of measurement, used in both everyday commerce and science."+
                         " It comprises a coherent system of units of measurement built around seven base units, 22 named and an indeterminate number of unnamed coherent derived units, and a set of prefixes that act as decimal-based multipliers."
                         , topic=topic_other)
    
    color_code_node = add_node("Color Code",
                               definition="The electronic color code is used to indicate the values or ratings of electronic components, very commonly for resistors, but also for capacitors, inductors, and others."+
                               " A separate code, the 25-pair color code, is used to identify wires in some telecommunications cables."
                               , topic=topic_other)
    add_synonym("Colorcode", node=color_code_node)
    add_synonym("Color", node=color_code_node)
    
    # Circuit Laws
    topic_laws = add_vocab_topic(domain=circuits_domain,
                                 topic="Circuit Laws",
                                 def_useful=True)
    ohms_law_node = add_node("Ohms Law", definition="Ohm's law states that the current through a conductor between two points is directly proportional to the potential difference across the two points. "+
                             " Introducing the constant of proportionality, the resistance, one arrives at the usual mathematical equation that describes this relationship: V = IR."+
                             " Where I is the current through the conductor in units of amperes, V is the potential difference measured across the conductor in units of volts, and R is the resistance of the conductor in units of ohms.", topic=topic_laws)
    add_synonym("Ohmic", node=ohms_law_node)
    
    kirchoffs_node = add_node("Kirchoffs Law", 
                              definition="Kirchoff's Current Law (KCL)  is also called Kirchhoff's first law, Kirchhoff's point rule, or Kirchhoff's junction rule (or nodal rule)."+
                              "The principle of conservation of electric charge implies that at any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node, or the algebraic sum of currents in a network of conductors meeting at a point is zero."
                              " Kirchoff's Voltage Law (KVL) is also called Kirchhoff's second law, Kirchhoff's loop (or mesh) rule, and Kirchhoff's second rule." + 
                              " The principle of conservation of energy implies that the directed sum of the electrical potential differences (voltage) around any closed network is zero, or"+
                              "more simply, the sum of the emfs in any closed loop is equivalent to the sum of the potential drops in that loop."
                            , topic=topic_laws)
    add_synonym("Kirchoffs", node=kirchoffs_node)
    add_synonym("Kirchoff", node=kirchoffs_node)
    add_synonym("Kircho", node=kirchoffs_node)
    
    thevenin_node = add_node("Thevenins Law",
                             definition="Thévenin's theorem and its dual, Norton's theorem, are widely used for circuit analysis simplification and to study circuit's initial-condition and steady-state response."+
                             " Thévenin's theorem can be used to convert any circuit's sources and impedances to a Thévenin equivalent; use of the theorem may in some cases be more convenient than use of Kirchhoff's circuit laws."
                             , topic=topic_laws)
    add_synonym("Thevenins", node=thevenin_node)
    add_synonym("Thevenin", node=thevenin_node)
    
    norton_node = add_node("Nortons Law", 
                           definition="Norton's Theorem states that it is possible to simplify any linear circuit, no matter how complex, to an equivalent circuit with just a single current source and parallel resistance connected to a load."+
                           " Just as with Thevenin's Theorem, the qualification of “linear” is identical to that found in the Superposition Theorem: all underlying equations must be linear (no exponents or roots). ",
                           topic=topic_laws)
    add_synonym("Nortons", node=norton_node)
    add_synonym("Norton", node=norton_node)
    
    max_power_node = add_node("Max Power Transfer",
                              definition="In electrical engineering, the maximum power transfer theorem states that, to obtain maximum external power from a source with a finite internal resistance, the resistance of the load must equal the resistance of the source as viewed from its output terminals."+
                              " Moritz von Jacobi published the maximum power (transfer) theorem around 1840; it is also referred to as 'Jacobi's law'."
                              , topic=topic_laws)
    add_synonym("Power Transfer", node=max_power_node)
    
    node_node = add_node("Node",
                         definition="In electrical engineering, node refers to any point on a circuit where two or more circuit elements meet."+
                         " For two nodes to be different, their voltages must be different."+
                         " Without any further knowledge, it is easy to establish how to find a node by using Ohm's Law: V=IR."+
                         " When looking at circuit schematics, ideal wires have a resistance of zero."+
                         " Since it can be assumed that there is no change in the potential across any part of the wire, all of the wire in between any components in a circuit is considered part of the same node.", 
                         topic=topic_laws)
    add_synonym("Nodes", node=node_node)
    
    conservation_node = add_node("Conservation",
                                 definition="In physics, charge conservation is the principle that electric charge can neither be created nor destroyed."+
                                 " The net quantity of electric charge, the amount of positive charge minus the amount of negative charge in the universe, is always conserved."+
                                 " The first written statement of the principle was by American scientist and statesman Benjamin Franklin in 1747.",
                                 topic=topic_laws)
    
    transformation_node = add_node("Transformation",
                                   definition="Source transformation is simplifying a circuit solution, especially with mixed sources, by transforming a voltage into a current source, and vice versa."+
                                   " Finding a solution to a circuit can be difficult without using methods such as this to make the circuit appear simpler."+
                                   " Source transformation is an application of Thévenin's theorem and Norton's theorem."+
                                   " Performing a source transformation consists of using Ohm's law to take an existing voltage source in series with a resistance, and replace it with a current source in parallel with the same resistance. ",
                                   topic=topic_laws)
    add_synonym("Conversion", node=transformation_node)
    
    superposition_node = add_node("Superposition",
                                  definition="The superposition theorem for electrical circuits states that for a linear system the response (voltage or current) in any branch of a bilateral linear circuit having more than one independent source equals the algebraic sum of the responses caused by each independent source acting alone, where all the other independent sources are replaced by their internal impedances.",
                                  topic=topic_laws)
    add_synonym("Super Position", node=superposition_node)
    
    linear_node = add_node("Linear", 
                           definition="In common usage, linearity refers to a mathematical relationship or function that can be graphically represented as a straight line, as in two quantities that are directly proportional to each other, such as voltage and current in a simple DC circuit, or the mass and weight of an object."+
                           " A crude but simple example of this concept can be observed in the volume control of an audio amplifier."+
                           " While our ears may (roughly) perceive a relatively even gradation of volume as the control goes from 1 to 10, the electrical power consumed in the speaker is rising geometrically with each numerical increment."+
                           " The 'loudness' is proportional to the volume number (a linear relationship), while the wattage is doubling with every unit increase (a non-linear, exponential relationship).", 
                           topic=topic_laws)
    
    nonlinear_node = add_node("Nonlinear", 
                              definition="In physics and other sciences, a nonlinear system, in contrast to a linear system, is a system which does not satisfy the superposition principle – meaning that the output of a nonlinear system is not directly proportional to the input.",
                              topic=topic_laws)
    add_synonym("Non Linear", node=nonlinear_node)
    
    variable_node = add_node("Variable", definition="In elementary mathematics, a variable is an alphabetic character representing a number, the value of the variable, which is either arbitrary or not fully specified or unknown."+
                             " Making algebraic computations with variables as if they were explicit numbers allows one to solve a range of problems in a single computation."
                             "Alternatively, a variable is an element, feature, or factor that is able to be changed or adapted, such as a variable resistor (see: potentiometer).",
                             topic=topic_laws)
    
    dc_node = add_node("Direct Current", 
                       definition="Direct current (DC) is the unidirectional flow of electric charge."+
                       " Direct current is produced by sources such as batteries, thermocouples, solar cells, and commutator-type electric machines of the dynamo type."+
                       " Direct current may flow in a conductor such as a wire, but can also flow through semiconductors, insulators, or even through a vacuum as in electron or ion beams."+
                       " The electric current flows in a constant direction, distinguishing it from alternating current (AC)."+
                       " A term formerly used for direct current was galvanic current.",
                       topic=topic_laws)
    add_synonym("DC", node=dc_node)
    
    ac_node = add_node("Alternating Current", definition="In alternating current (AC, also ac), the flow of electric charge periodically reverses direction."+
                       " In direct current (DC, also dc), the flow of electric charge is only in one direction."+
                       " The abbreviations AC and DC are often used to mean simply alternating and direct, as when they modify current or voltage.",
                       topic=topic_laws)
    add_synonym("AC", node=ac_node)
    add_synonym("Alternate", node=ac_node)
    
    channel_node = add_node("Channel", definition="a means of communication or expression: as (1) :  a path along which information (as data or music) in the form of an electrical signal passes (2) plural :  a fixed or official course of communication <went through established military channels with his grievances> ", topic=topic_laws)
    add_synonym("Chanel", node=channel_node)
    
    dualtrace_node = add_node("Dualtrace", 
                              definition="A dual trace oscilloscope is an oscilloscope which can compare two waveforms on the face of a single cathode-ray tube, using any one of several methods.",
                              topic=topic_laws)
    add_synonym("Dual", node=dualtrace_node)
    
    
    # Circuit Diagrams and Measurement
    topic_diagrams = add_vocab_topic(domain=circuits_domain,
                                     topic="Circuit Diagrams and Measurement",
                                     def_useful=True)
    combination_node = add_node("Series Parallel Combination",
                                definition="Circuit elements can be connected by means of series connections or by means of parallel connections."+
                                " When all the devices in a circuit are connected by series connections, then the circuit is referred to as a series circuit."+
                                " When all the devices in a circuit are connected by parallel connections, then the circuit is referred to as a parallel circuit."+
                                " A third type of circuit involves the dual use of series and parallel connections in a circuit; such circuits are referred to as compound circuits or combination circuits.",
                                topic=topic_diagrams)
    add_synonym("Combination", node=combination_node)
    add_synonym("Bill", node=combination_node)
    
    series_node = add_node("Series", 
                           definition=" In a series circuit, each device is connected in a manner such that there is only one pathway by which charge can traverse the external circuit." + 
                           " In series, components share the same current but have different voltages."  ,
                           topic=topic_diagrams)
    add_synonym("Serial", node=series_node)
    
    parallel_node = add_node("Parallel", definition="In a parallel circuit, each device is placed in its own separate branch."+
                             " The presence of branch lines means that there are multiple pathways by which charge can traverse the external circuit" + 
                             " In a parellel circuit, components share the same voltage but have different currents. " , topic=topic_diagrams)
    
    peak_node = add_node("Peak", definition="A peak is the greatest or highest point of a waveform. A peak represents a maximum of a signal."
                         , topic=topic_diagrams)
    add_synonym("Maximum", node=peak_node)
    add_synonym("Bill", node=peak_node)
    
    instantaneous_node = add_node("Instantaneous", 
                                  definition="Instantaneous represents a single moment in time." + 
                                  " When used in reference to a measurement, it represents a value at a specific point in time, as opposed to average or RMS measurements." ,
                                  topic=topic_diagrams)
    
    rms_node = add_node("RMS", 
                        definition="In mathematics, the root mean square (abbreviated RMS or rms), also known as the quadratic mean, is a statistical measure of the magnitude of a varying quantity."+
                        " It is especially useful when variates are positive and negative, e.g., sinusoids."+
                        " In the field of electrical engineering, the effective (RMS) value of a periodic current is equal to the DC current that delivers the same average power to a resistor as the periodic current.",
                        topic=topic_diagrams)
    add_synonym("Mean", node=rms_node)
    
    average_node = add_node("Average", 
                            definition="In mathematics and statistics, the arithmetic mean,  or simply the mean or average when the context is clear, is the sum of a collection of numbers divided by the number of numbers in the collection."+
                            " The collection is often a set of results of an experiment, or a set of results from a survey."+
                            " The term 'arithmetic mean' is preferred in some contexts in mathematics and statistics because it helps distinguish it from other means, such as the geometric mean and the harmonic mean.",
                            topic=topic_diagrams)
    add_synonym("Mean", node=average_node)
    
    ground_node = add_node("Ground", 
                           definition="In electrical engineering, ground or earth can refer to the reference point in an electrical circuit from which voltages are measured, a common return path for electric current, or a direct physical connection to the Earth.",
                           topic=topic_diagrams)
    add_synonym("Grnd", node=ground_node)
    add_synonym("Gnd", node=ground_node)

    peaktopeak_node = add_node("Peak to Peak", 
                               definition="Peak-to-peak (pk-pk) is the difference between the maximum positive and the maximum negative amplitudes of a waveform."+
                               " If there is no direct current ( DC ) component in an alternating current ( AC ) wave, then the pk-pk amplitude is twice the peak amplitude.",
                               topic=topic_diagrams)
    add_synonym("Bill", node=peaktopeak_node)
    
    xy_node = add_node("XY", definition="A Cartesian coordinate system is a coordinate system that specifies each point uniquely in a plane by a pair of numerical coordinates, which are the signed distances from the point to two fixed perpendicular directed lines, measured in the same unit of length."+
                       " Each reference line is called a coordinate axis or just axis of the system, and the point where they meet is its origin, usually at ordered pair (0, 0)."+
                       " The coordinates can also be defined as the positions of the perpendicular projections of the point onto the two axes, expressed as signed distances from the origin.",
                       topic=topic_diagrams)
    
    # Math words
    topic_math = add_vocab_topic(domain=circuits_domain,
                                 topic="Math",
                                 def_useful=True)
    net_node = add_node("Net", 
                        definition="The difference from the final resting point and the initial starting point."
                        , topic=topic_math)
    add_synonym("Total", node=net_node)
    add_synonym("Overall", node=net_node)
    add_synonym("Sum", node=net_node)
    add_synonym("Equivalent", node=net_node)
    
    difference_node = add_node("Difference",
                               definition="The result of subtracting one number from another. ", 
                               topic=topic_math)
    
    # Units
    topic_units = add_vocab_topic(domain=circuits_domain,
                                  topic="Units",
                                  def_useful=True)
    ohm_node = add_node("Ohm",
                        definition="An ohm is the SI unit of electrical resistance, expressing the resistance in a circuit transmitting a current of one ampere when subjected to a potential difference of one volt.", 
                        topic=topic_units)
    add_synonym("Ohms", node=ohm_node)
    
    farad_node = add_node("Farad", 
                          definition="A farad is the SI unit of electrical capacitance, equal to the capacitance of a capacitor in which one coulomb of charge causes a potential difference of one volt.",
                          topic=topic_units)
    add_synonym("F", node=farad_node)
    
    henry_node = add_node("Henry",
                          definition="A henry is the SI unit of inductance, equal to an electromotive force of one volt in a closed circuit with a uniform rate of change of current of one ampere per second."
                          , topic=topic_units)
    add_synonym("H", node=henry_node)
    
    volt_node = add_node("Volt", 
                         definition="A volt is the SI unit of electromotive force, the difference of potential that would drive one ampere of current against one ohm resistance.", 
                         topic=topic_units)
    add_synonym("V", node=volt_node)
    
    ampere_node = add_node("Ampere",
                           definition="An ampere is a unit of electric current equal to a flow of one coulomb per second.",
                           topic=topic_units)
    add_synonym("Amps", node=ampere_node)
    add_synonym("Amp", node=ampere_node)
    add_synonym("A", node=ampere_node)
    
    watt_node = add_node("Watt", 
                         definition="A watt is the SI unit of power, equivalent to one joule per second, corresponding to the power in an electric circuit in which the potential difference is one volt and the current one ampere.",
                         topic=topic_units)
    add_synonym("W", node=watt_node)
    
    joule_node = add_node("Joule", 
                          definition="A joule is the SI unit of work or energy, equal to the work done by a force of one newton when its point of application moves one meter in the direction of action of the force, equivalent to one 3600th of a watt-hour.",
                          topic=topic_units)
    add_synonym("J", node=joule_node)
    
    second_node = add_node("Second", 
                           definition="The second (symbol: s) is the base unit of time in the International System of Units (SI) and is also a unit of time in other systems of measurement (abbreviated s or sec); it is the second division of the hour by sixty, the first division by 60 being the minute.", 
                           topic=topic_units)
    add_synonym("S", node=second_node)
    add_synonym("MS", node=second_node)
    
    hertz_node = add_node("Hertz", 
                          definition="A hertz is the SI unit of frequency, equal to one cycle per second.",
                          topic=topic_units)
    add_synonym("Hz", node=hertz_node)
    add_synonym("Cps", node=hertz_node)
    add_synonym("Cycles", node=hertz_node)
    
    inverse_ohm_node = add_node("Inverse Ohm", 
                                definition="A mho is the reciprocal of an ohm, a former unit of electrical conductance. (See: Siemens)", 
                                topic=topic_units)
    add_synonym("mho", node=inverse_ohm_node)
    add_synonym("mhos", node=inverse_ohm_node)
    add_synonym("1/ohm", node=inverse_ohm_node)
    
    # Help
    topic_help = add_vocab_topic(domain=circuits_domain,
                                 topic="Help",
                                 def_useful=False)
    help_node = add_node("Help", definition="", topic=topic_help)
    safety_node = add_node("Safety", definition="", topic=topic_help)
    

    # add rulebase
    rb = add_rulebase(name='Circuits')
    
    # add answer topics
    general = add_answer_topic(rulebase=rb, topic='General')
    safety = add_answer_topic(rulebase=rb, topic='Safety')
    equipment = add_answer_topic(rulebase=rb, topic='Equipment')
    VLA = add_answer_topic(rulebase=rb, topic='VLA')
    simulation = add_answer_topic(rulebase=rb, topic='Simulation')
    hardware = add_answer_topic(rulebase=rb, topic='Hardware')
    theory = add_answer_topic(rulebase=rb, topic='Theory')
    
    # add answers with questions
    awq1 = add_answer_with_question(rulebase=rb,
                                    question="What is a capacitor")
    awq1.topic.add(theory, hardware, simulation)
    add_answer_keyword(answer_with_question=awq1,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq1,
                       node=capacitor_node)


    awq2 = add_answer_with_question(rulebase=rb,
                                    question="What is a resistor")
    awq2.topic.add(theory, hardware, simulation)
    add_answer_keyword(answer_with_question=awq2,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq2,
                       node=resistor_node)
    
    awq3 = add_answer_with_question(rulebase=rb,
                                    question="What is an inductor")
    awq3.topic.add(theory, hardware, simulation)
    add_answer_keyword(answer_with_question=awq3,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq3,
                       node=inductor_node)
    
    add_answer_element(answer_with_question=awq3, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="https://www.youtube.com/embed/NgwXkUt3XxQ",
                       element_type="video")
    
    awq4 = add_answer_with_question(rulebase=rb,
                                    question="How to use a multimeter")
    awq4.topic.add(equipment, hardware, simulation)
    add_answer_keyword(answer_with_question=awq4,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq4,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq4,
                       node=multimeter_node)
    
    awq5 = add_answer_with_question(rulebase=rb,
                                    question="What is superposition")
    awq5.topic.add(theory)
    add_answer_keyword(answer_with_question=awq5,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq5,
                       node=superposition_node)
    
    awq6 = add_answer_with_question(rulebase=rb,
                                    question="How to read resistor color code")
    awq6.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq6,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq6,
                       node=resistor_node)
    add_answer_keyword(answer_with_question=awq6,
                       node=color_code_node)
    
    awq7 = add_answer_with_question(rulebase=rb,
                                    question="How to use a Breadboard")
    awq7.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq7,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq7,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq7,
                       node=breadboard_node)
    add_answer_element(answer_with_question=awq7, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/cf6XZ4gs7Ao",
                       element_type="video")
    
    awq8 = add_answer_with_question(rulebase=rb,
                                    question="How to use a DC Power Supply")
    awq8.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq8,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq8,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq8,
                       node=dc_source_node)
    add_answer_element(answer_with_question=awq8, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/mOpCxeqXWEI",
                       element_type="video")
    add_answer_element(answer_with_question=awq8, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    awq9 = add_answer_with_question(rulebase=rb,
                                    question="How to use a Multimeter")
    awq9.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq9,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq9,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq9,
                       node=multimeter_node)
    add_answer_element(answer_with_question=awq9, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/_o8M34NbXpk",
                       element_type="video")
    add_answer_element(answer_with_question=awq9, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    awq10 = add_answer_with_question(rulebase=rb,
                                    question="How to measure Current")
    awq10.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq10,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq10,
                       node=measure_node)
    add_answer_keyword(answer_with_question=awq10,
                       node=current_node)
    add_answer_element(answer_with_question=awq10, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/wLA6Wkb-TLQ",
                       element_type="video")
    add_answer_element(answer_with_question=awq10, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    awq11 = add_answer_with_question(rulebase=rb,
                                    question="How to measure Voltage")
    awq11.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq11,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq11,
                       node=measure_node)
    add_answer_keyword(answer_with_question=awq11,
                       node=voltage_node)
    add_answer_element(answer_with_question=awq11, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/wLA6Wkb-TLQ",
                       element_type="video")
    add_answer_element(answer_with_question=awq11, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    awq12 = add_answer_with_question(rulebase=rb,
                                    question="How to use a Function Generator")
    awq12.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq12,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq12,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq12,
                       node=func_gen_node)
    add_answer_element(answer_with_question=awq12, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/uBm7veURIFk",
                       element_type="video")
    add_answer_element(answer_with_question=awq12, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    awq13 = add_answer_with_question(rulebase=rb,
                                    question="How to use an Oscilloscope")
    awq13.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq13,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq13,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq13,
                       node=oscilloscope_node)
    add_answer_element(answer_with_question=awq13, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/uBm7veURIFk",
                       element_type="video")
    add_answer_element(answer_with_question=awq13, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    awq14 = add_answer_with_question(rulebase=rb,
                                    question="Safety Measures")
    awq14.topic.add(hardware, safety)
    add_answer_keyword(answer_with_question=awq14,
                       node=safety_node)
    add_answer_element(answer_with_question=awq14, 
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="http://www.youtube.com/embed/Uck73jLjy7E",
                       element_type="video")
    add_answer_element(answer_with_question=awq14, 
                       text_input="This video refers to the equipment in the Temple University ECE Circuits laboratory.",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="text")
    
    # Print out what we have added to the user.
    for vd in VocabDomain.objects.all():
        for vt in VocabTopic.objects.filter(domain=vd):
            print "- {0} - {1}".format(str(vd), str(vt))

# Add Vocab Domain, Vocab Topics, Words, definitions, and synonyms
def add_vocab_domain(name):
    vd = VocabDomain.objects.get_or_create(name=name)[0]
    return vd

def add_vocab_topic(topic, domain, def_useful):
    vt = VocabTopic.objects.get_or_create(topic=topic, domain=domain,
                                          def_useful=def_useful)[0]
    return vt

def add_node(word, definition, topic, views=0):
    n = Node.objects.get_or_create(word=word, definition=definition,
                                   topic=topic, views=views,
                                   date_added=timezone.now())[0]
    return n

def add_synonym(word, node):
    s = Synonym.objects.get_or_create(word=word, node=node)[0]
    return s

# Add Rulebase, answers, answer topics, etc.
def add_rulebase(name):
    rb = Rulebase.objects.get_or_create(name=name)[0]
    return rb

def add_answer_with_question(rulebase, question, views=0):
    awq = AnswerWithQuestion.objects.get_or_create(rulebase=rulebase,
                                                   question=question,
                                                   views=views,
                                                   date_added=timezone.now())[0]
    return awq

def add_answer_topic(rulebase, topic):
    at = AnswerTopic.objects.get_or_create(rulebase=rulebase,
                                           topic=topic)[0]
    return at

def add_answer_keyword(answer_with_question, node):
    ak = AnswerKeyword.objects.get_or_create(answer_with_question=answer_with_question,
                                             node=node)[0]
    return ak

 # element_type must be one of: 'text', 'image', 'equation', 'latex', 'video', 'table'
def add_answer_element(answer_with_question, text_input, image_input,
                         equation_input, video_input, element_type):
     ae = AnswerElement.objects.get_or_create(answer_with_question=answer_with_question,
                                              text_input=text_input,
                                              image_input=image_input,
                                              equation_input=equation_input,
                                              video_input=video_input,
                                              element_type=element_type)[0]
     return ae

# Start execution here!
if __name__ == '__main__':
    print "Starting VOCAB DOMAIN population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VLA_project.settings')
    from VLA.models import VocabDomain, VocabTopic, Node, Synonym
    from VLA.models import Rulebase, AnswerWithQuestion, AnswerTopic, AnswerElement, AnswerKeyword
    populate()
