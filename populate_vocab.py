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
                              definition="",
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
                    definition="",
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
    voltage_node = add_node("Voltage", definition="", topic=topic_concepts)
    add_synonym("Volt", node=voltage_node)
    add_synonym("Volts", node=voltage_node)
    add_synonym("V", node=voltage_node)
    add_synonym("Potential", node=voltage_node)
    add_synonym("PD", node=voltage_node)
    add_synonym("KVL", node=voltage_node)
    
    current_node = add_node("Current", definition="", topic=topic_concepts)
    add_synonym("Amp", node=current_node)
    add_synonym("Amps", node=current_node)
    add_synonym("Ampere", node=current_node)
    add_synonym("KCL", node=current_node)
    add_synonym("DC", node=current_node)
    add_synonym("AC", node=current_node)
    
    resistance_node = add_node("Resistance", definition="", topic=topic_concepts)
    add_synonym("Ohm", node=resistance_node)
    add_synonym("Ohms", node=resistance_node)
    
    capacitance_node = add_node("Capacitance", definition="", topic=topic_concepts)
    add_synonym("Farad", node=capacitance_node)
    add_synonym("F", node=capacitance_node)
    
    inductance_node = add_node("Inductance", definition="", topic=topic_concepts)
    add_synonym("Henry", node=inductance_node)
    add_synonym("H", node=inductance_node)
    
    power_node = add_node("Power", definition="", topic=topic_concepts)
    add_synonym("Watt", node=power_node)
    add_synonym("W", node=power_node)
    
    time_node = add_node("Time", definition="", topic=topic_concepts)
    add_synonym("Term", node=time_node)
    add_synonym("Second", node=time_node)
    add_synonym("MS", node=time_node)
    add_synonym("S", node=time_node)
    
    frequency_node = add_node("Frequency", definition="", topic=topic_concepts)
    add_synonym("Hetz", node=frequency_node)
    add_synonym("CPS", node=frequency_node)
    add_synonym("Hz", node=frequency_node)
    
    waveform_node = add_node("Waveform", definition="", topic=topic_concepts)
    add_synonym("Wave", node=waveform_node)
    add_synonym("Crest", node=waveform_node)
    add_synonym("Trough", node=waveform_node)
    add_synonym("Sine", node=waveform_node)
    add_synonym("Sinusoid", node=waveform_node)
    add_synonym("Square", node=waveform_node)
    
    amplitude_node = add_node("Amplitude", definition="", topic=topic_concepts)
    add_synonym("Value", node=amplitude_node)
    add_synonym("Magnitude", node=amplitude_node)
    add_synonym("Reading", node=amplitude_node)
    add_synonym("Entry", node=amplitude_node)
    add_synonym("Meter", node=amplitude_node)
    add_synonym("Metre", node=amplitude_node)
    add_synonym("Y", node=amplitude_node)
    
    reactance_node = add_node("Reactance", definition="", topic=topic_concepts)
    add_synonym("XC", node=reactance_node)
    add_synonym("XL", node=reactance_node)
    
    impedance_node = add_node("Impedance", definition="", topic=topic_concepts)
    add_synonym("Z", node=impedance_node)
    
    conductance_node = add_node("Conductance", definition="", topic=topic_concepts)
    add_synonym("G", node=conductance_node)
    add_synonym("Mho", node=conductance_node)
    add_synonym("Mhos", node=conductance_node)
    
    energy_node = add_node("Energy", definition="", topic=topic_concepts)
    add_synonym("Joule", node=energy_node)
    add_synonym("J", node=energy_node)
    
    cycle_node = add_node("Cycle", definition="", topic=topic_concepts)
    
    period_node = add_node("Period", definition="", topic=topic_concepts)
    
    wabelength_node = add_node("Wavelength", definition="", topic=topic_concepts)
    add_synonym("Wave Length", node=wabelength_node)
    
    circuit_node = add_node("Circuit", definition="", topic=topic_concepts)
    add_synonym("Loop", node=circuit_node)
    
    button_node = add_node("Button", definition="", topic=topic_concepts)
    
    phasor_node = add_node("Phasor", definition="", topic=topic_concepts)
    
    phase_node = add_node("Phase", definition="", topic=topic_concepts)
    add_synonym("Angle", node=phase_node)
    
    # Other
    topic_other = add_vocab_topic(domain=circuits_domain,
                                  topic="Other",
                                  def_useful=True)
    positive_node = add_node("Positive", definition="", topic=topic_other)
    
    negative_node = add_node("Negative", definition="", topic=topic_other)
    
    polarity_node = add_node("Polarity", definition="", topic=topic_other)
    add_synonym("Sign", node=polarity_node)
    
    law_node = add_node("Law", definition="", topic=topic_other)
    add_synonym("Rule", node=law_node)
    add_synonym("Principle", node=law_node)
    add_synonym("Theorem", node=law_node)
    
    gain_node = add_node("Gain", definition="", topic=topic_other)
    
    loss_node = add_node("Loss", definition="", topic=topic_other)
    
    division_node = add_node("Division", definition="", topic=topic_other)
    
    unit_node = add_node("Unit", definition="", topic=topic_other)
    
    color_code_node = add_node("Color Code", definition="", topic=topic_other)
    add_synonym("Colorcode", node=color_code_node)
    add_synonym("Color", node=color_code_node)
    
    # Circuit Laws
    topic_laws = add_vocab_topic(domain=circuits_domain,
                                 topic="Circuit Laws",
                                 def_useful=True)
    ohms_law_node = add_node("Ohms Law", definition="", topic=topic_laws)
    add_synonym("Ohmic", node=ohms_law_node)
    
    kirchoffs_node = add_node("Kirchoffs Law", definition="", topic=topic_laws)
    add_synonym("Kirchoffs", node=kirchoffs_node)
    add_synonym("Kirchoff", node=kirchoffs_node)
    add_synonym("Kircho", node=kirchoffs_node)
    
    thevenin_node = add_node("Thevenins Law", definition="", topic=topic_laws)
    add_synonym("Thevenins", node=thevenin_node)
    add_synonym("Thevenin", node=thevenin_node)
    
    norton_node = add_node("Nortons Law", definition="", topic=topic_laws)
    add_synonym("Nortons", node=norton_node)
    add_synonym("Norton", node=norton_node)
    
    max_power_node = add_node("Max Power Transfer", definition="", topic=topic_laws)
    add_synonym("Power Transfer", node=max_power_node)
    
    node_node = add_node("Node", definition="", topic=topic_laws)
    add_synonym("Nodes", node=node_node)
    
    conservation_node = add_node("Conservation", definition="", topic=topic_laws)
    
    transformation_node = add_node("Transformation", definition="", topic=topic_laws)
    add_synonym("Conversion", node=transformation_node)
    
    superposition_node = add_node("Superposition", definition="", topic=topic_laws)
    add_synonym("Super Position", node=superposition_node)
    
    linear_node = add_node("Linear", definition="", topic=topic_laws)
    
    nonlinear_node = add_node("Nonlinear", definition="", topic=topic_laws)
    add_synonym("Non Linear", node=nonlinear_node)
    
    variable_node = add_node("Variable", definition="", topic=topic_laws)
    
    dc_node = add_node("Direct Current", definition="", topic=topic_laws)
    add_synonym("DC", node=dc_node)
    
    ac_node = add_node("Alternating Current", definition="", topic=topic_laws)
    add_synonym("AC", node=ac_node)
    add_synonym("Alternate", node=ac_node)
    
    channel_node = add_node("Channel", definition="", topic=topic_laws)
    add_synonym("Chanel", node=channel_node)
    
    dualtrace_node = add_node("Dualtrace", definition="", topic=topic_laws)
    add_synonym("Dual", node=dualtrace_node)
    
    lissaj_node = add_node("Lissaj", definition="", topic=topic_laws)
    add_synonym("Pattern", node=lissaj_node)
    
    # Circuit Diagrams and Measurement
    topic_diagrams = add_vocab_topic(domain=circuits_domain,
                                     topic="Circuit Diagrams and Measurement",
                                     def_useful=True)
    combination_node = add_node("Series Parallel Combination", definition="", topic=topic_diagrams)
    add_synonym("Combination", node=combination_node)
    add_synonym("Bill", node=combination_node)
    
    series_node = add_node("Series", definition="", topic=topic_diagrams)
    add_synonym("Serial", node=series_node)
    
    parallel_node = add_node("Parallel", definition="", topic=topic_diagrams)
    
    peak_node = add_node("Peak", definition="", topic=topic_diagrams)
    add_synonym("Maximum", node=peak_node)
    add_synonym("Bill", node=peak_node)
    
    instantaneous_node = add_node("Instantaneous", definition="", topic=topic_diagrams)
    
    rms_node = add_node("RMS", definition="", topic=topic_diagrams)
    add_synonym("Mean", node=rms_node)
    
    average_node = add_node("Average", definition="", topic=topic_diagrams)
    add_synonym("Mean", node=average_node)
    
    ground_node = add_node("Ground", definition="", topic=topic_diagrams)
    add_synonym("Grnd", node=ground_node)
    
    peaktopeak_node = add_node("Peak to Peak", definition="", topic=topic_diagrams)
    add_synonym("Bill", node=peaktopeak_node)
    
    xy_node = add_node("XY", definition="", topic=topic_diagrams)
    
    # Math words
    topic_math = add_vocab_topic(domain=circuits_domain,
                                 topic="Math",
                                 def_useful=True)
    net_node = add_node("Net", definition="", topic=topic_math)
    add_synonym("Total", node=net_node)
    add_synonym("Overall", node=net_node)
    add_synonym("Sum", node=net_node)
    add_synonym("Equivalent", node=net_node)
    
    difference_node = add_node("Difference", definition="", topic=topic_math)
    
    # Units
    topic_units = add_vocab_topic(domain=circuits_domain,
                                  topic="Units",
                                  def_useful=True)
    ohm_node = add_node("Ohm", definition="", topic=topic_units)
    add_synonym("Ohms", node=ohm_node)
    
    farad_node = add_node("Farad", definition="", topic=topic_units)
    add_synonym("F", node=farad_node)
    
    henry_node = add_node("Henry", definition="", topic=topic_units)
    add_synonym("H", node=henry_node)
    
    volt_node = add_node("Volt", definition="", topic=topic_units)
    add_synonym("V", node=volt_node)
    
    ampere_node = add_node("Ampere", definition="", topic=topic_units)
    add_synonym("Amps", node=ampere_node)
    add_synonym("Amp", node=ampere_node)
    add_synonym("A", node=ampere_node)
    
    watt_node = add_node("Watt", definition="", topic=topic_units)
    add_synonym("W", node=watt_node)
    
    joule_node = add_node("Joule", definition="", topic=topic_units)
    add_synonym("J", node=joule_node)
    
    second_node = add_node("Second", definition="", topic=topic_units)
    add_synonym("S", node=second_node)
    add_synonym("MS", node=second_node)
    
    hertz_node = add_node("Hertz", definition="", topic=topic_units)
    add_synonym("Hz", node=hertz_node)
    add_synonym("Cps", node=hertz_node)
    add_synonym("Cycles", node=hertz_node)
    
    inverse_ohm_node = add_node("Inverse Ohm", definition="", topic=topic_units)
    add_synonym("mho", node=inverse_ohm_node)
    add_synonym("mhos", node=inverse_ohm_node)
    add_synonym("1/ohm", node=inverse_ohm_node)
    
    # Help
    topic_help = add_vocab_topic(domain=circuits_domain,
                                 topic="Help",
                                 def_useful=False)
    help_node = add_node("Help", definition="", topic=topic_help)
    
    # Add videos
    add_video(name="How to use a Breadboard",
              video_link="http://www.youtube.com/embed/cf6XZ4gs7Ao",
              description="")
    add_video(name="How to use a DC Power Supply",
              video_link="http://www.youtube.com/embed/mOpCxeqXWEI",
              description="")
    add_video(name="How to use a Multimeter",
              video_link="http://www.youtube.com/embed/_o8M34NbXpk",
              description="")
    add_video(name="How to measure Current and Voltage",
              video_link="http://www.youtube.com/embed/wLA6Wkb-TLQ",
              description="")
    add_video(name="How to measure Function Generator and Oscilloscope",
              video_link="http://www.youtube.com/embed/uBm7veURIFk",
              description="")
    add_video(name="Safety Measures",
              video_link="http://www.youtube.com/embed/Uck73jLjy7E",
              description="")

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
                                    question="What is a capacitor?")
    awq1.topic.add(theory, hardware, simulation)
    add_answer_keyword(answer_with_question=awq1,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq1,
                       node=capacitor_node)
    add_answer_element(answer_with_question=awq1,
                       text_input="",
                       image_input=None,
                       equation_input="",
                       video_input="",
                       element_type="")
    
    awq2 = add_answer_with_question(rulebase=rb,
                                    question="What is a resistor?")
    awq2.topic.add(theory, hardware, simulation)
    add_answer_keyword(answer_with_question=awq2,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq2,
                       node=resistor_node)
    
    awq3 = add_answer_with_question(rulebase=rb,
                                    question="What is an inductor?")
    awq3.topic.add(theory, hardware, simulation)
    add_answer_keyword(answer_with_question=awq3,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq3,
                       node=inductor_node)
    
    awq4 = add_answer_with_question(rulebase=rb,
                                    question="How to use a multimeter?")
    awq4.topic.add(equipment, hardware, simulation)
    add_answer_keyword(answer_with_question=awq4,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq4,
                       node=use_node)
    add_answer_keyword(answer_with_question=awq4,
                       node=multimeter_node)
    
    awq5 = add_answer_with_question(rulebase=rb,
                                    question="What is a superposition?")
    awq5.topic.add(theory)
    add_answer_keyword(answer_with_question=awq5,
                       node=what_node)
    add_answer_keyword(answer_with_question=awq5,
                       node=superposition_node)
    
    awq6 = add_answer_with_question(rulebase=rb,
                                    question="How to read resistor color code?")
    awq5.topic.add(hardware)
    add_answer_keyword(answer_with_question=awq5,
                       node=how_node)
    add_answer_keyword(answer_with_question=awq5,
                       node=resistor_node)
    add_answer_keyword(answer_with_question=awq5,
                       node=color_code_node)
    
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

def add_video(name, video_link, description):
    v = Video.objects.get_or_create(name=name, video_link=video_link,
                                    description=description)[0]
    return v

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
    from VLA.models import VocabDomain, VocabTopic, Node, Synonym, Video
    from VLA.models import Rulebase, AnswerWithQuestion, AnswerTopic, AnswerElement, AnswerKeyword
    populate()