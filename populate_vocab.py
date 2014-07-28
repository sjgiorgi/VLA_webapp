import os


def populate():
    
    circuits_domain = add_vocab_domain(name = 'Circuits')
    
    # Circuit ELements and Equipment
    topic_elements = add_vocab_topic(domain=circuits_domain,
                    topic="Circuit Elements and Equipment",
                    def_useful=True)
    
    n101 = add_node("Resistor",
            definition="A resistor is a passive two-terminal electrical component that implements electrical resistance " +
            "as a circuit element. Resistors act to reduce current flow, and, at the same time, act to lower voltage " +
            "levels within circuits. Resistors may have fixed resistances or variable resistances, such as those found " +
            "in thermistors, varistors, trimmers, photoresistors, humistors, piezoresistors and potentiometers.",
            topic=topic_elements)
    add_synonym("Res", node=n101)
    add_synonym("R", node=n101)
    add_synonym("Ohm", node=n101)
    add_synonym("Conductor", node=n101)
    
    n102 = add_node("Capacitor",
            definition="A capacitor (originally known as a condenser) is a passive two-terminal electrical component used " +
            "to store energy electrostatically in an electric field. The forms of practical capacitors vary widely, " +
            "but all contain at least two electrical conductors (plates) separated by a dielectric (i.e., insulator). " +
            "The conductors can be thin films of metal, aluminum foil or disks, etc. The 'nonconducting' dielectric acts to " +
            "increase the capacitor's charge capacity. A dielectric can be glass, ceramic, plastic film, air, paper, mica, etc. " +
            "Capacitors are widely used as parts of electrical circuits in many common electrical devices. Unlike a " +
            "resistor, an ideal capacitor does not dissipate energy. Instead, a capacitor stores energy in the form of an electrostatic field between its plates.",
            topic=topic_elements)
    add_synonym("Cap", node=n102)
    add_synonym("F", node=n102)
    add_synonym("Farad", node=n102)
    
    n103 = add_node("Inductor",
            definition="An inductor, also called a coil or reactor, is a passive two-terminal electrical component which " +
            "resists changes in electric current passing through it. It consists of a conductor such as a wire, usually " +
            "wound into a coil. When a current flows through it, energy is stored temporarily in a magnetic field in the " +
            "coil. When the current flowing through an inductor changes, the time-varying magnetic field induces a voltage " +
            "in the conductor, according to Faraday's law of electromagnetic induction, which opposes the change in current that created it.",
            topic=topic_elements)
    add_synonym("Ind", node=n103)
    add_synonym("L", node=n103)
    add_synonym("Henry", node=n103)
    add_synonym("H", node=n103)
    
    n104 = add_node("DC Source",
            definition="",
            topic=topic_elements)
    add_synonym("DC Supply", node=n104)
    add_synonym("Supply", node=n104)
    add_synonym("Source", node=n104)
    add_synonym("DCS", node=n104)
    add_synonym("Battery", node=n104)
    add_synonym("Cell", node=n104)
    
    n105 = add_node("Multimeter",
            definition="A multimeter or a multitester, also known as a VOM (Volt-Ohm meter), is an electronic measuring instrument " +
            "that combines several measurement functions in one unit. A typical multimeter would include basic features such " +
            "as the ability to measure voltage, current, and resistance. Analog multimeters use a microammeter whose pointer moves " +
            "over a scale calibrated for all the different measurements that can be made. Digital multimeters (DMM, DVOM) display the " +
            "measured value in numerals, and may also display a bar of a length proportional to the quantity being measured. Digital " +
            "multimeters are now far more common than analog ones, but analog multimeters are still preferable in some cases, for " +
            "example when monitoring a rapidly varying value.",
            topic=topic_elements)
    add_synonym("Voltmeter", node=n105)
    add_synonym("Ammeter", node=n105)
    add_synonym("Ohmmeter", node=n105)
    add_synonym("Meter", node=n105)
    add_synonym("Multim", node=n105)
    
    n106 = add_node("Function Generator",
            definition="A function generator is usually a piece of electronic test equipment or software used to generate different " +
            "types of electrical waveforms over a wide range of frequencies. Some of the most common waveforms produced by the " +
            "function generator are the sine, square, triangular and sawtooth shapes. These waveforms can be either repetitive or " +
            "single-shot (which requires an internal or external trigger source). Integrated circuits used to generate waveforms " +
            "may also be described as function generator ICs.",
            topic=topic_elements)
    add_synonym("AC Supply", node=n106)
    add_synonym("Generator", node=n106)
    add_synonym("AC Source", node=n106)
    add_synonym("Func Gen", node=n106)
    
    n107 = add_node("Oscilloscope",
            definition="An oscilloscope, previously called an oscillograph, and informally known as a scope, CRO (for " +
            "cathode-ray oscilloscope), or DSO (for the more modern digital storage oscilloscope), is a type of " +
            "electronic test instrument that allows observation of constantly varying signal voltages, usually as a " +
            "two-dimensional plot of one or more signals as a function of time. Non-electrical signals (such as sound " +
            "or vibration) can be converted to voltages and displayed.",
            topic=topic_elements)
    add_synonym("Oscope", node=n107)
    add_synonym("Display", node=n107)
    add_synonym("CRT", node=n107)
    add_synonym("Cathode", node=n107)
    
    n108 = add_node("Spectrum Analyzer",
            definition="A spectrum analyzer measures the magnitude of an input signal versus frequency within the full " +
            "frequency range of the instrument. The primary use is to measure the power of the spectrum of known and " +
            "unknown signals. The input signal that a spectrum analyzer measures is electrical, however, spectral " +
            "compositions of other signals, such as acoustic pressure waves and optical light waves, can be considered " +
            "through the use of an appropriate transducer. Optical spectrum analyzers also exist, which use direct optical " +
            "techniques such as a monochromator to make measurements.",
            topic=topic_elements)
    add_synonym("Spectrum", node=n108)
    add_synonym("Analyzer", node=n108)
    add_synonym("Sweep", node=n108)
    add_synonym("SA", node=n108)
    
    n109 = add_node("Diode",
            definition="In electronics, a diode is a two-terminal electronic component with asymmetric conductance; it has " +
            "low (ideally zero) resistance to current in one direction, and high (ideally infinite) resistance in the other. " +
            "A semiconductor diode, the most common type today, is a crystalline piece of semiconductor material with a p-n " +
            "junction connected to two electrical terminals. A vacuum tube diode has two electrodes, a plate (anode) and a " +
            "heated cathode. Semiconductor diodes were the first semiconductor electronic devices. The discovery of crystals' " +
            "rectifying abilities was made by German physicist Ferdinand Braun in 1874. The first semiconductor diodes, " +
            "called cat's whisker diodes, developed around 1906, were made of mineral crystals such as galena. Today, most " +
            "diodes are made of silicon, but other semiconductors such as selenium or germanium are sometimes used.",
            topic=topic_elements)
    add_synonym("Rectifier", node=n109)
    add_synonym("Semiconductor", node=n109)
    add_synonym("Junction", node=n109)
    
    n110 = add_node("Wire",
            definition="",
            topic=topic_elements)
    add_synonym("Cable", node=n110)
    add_synonym("Line", node=n110)
    add_synonym("Short", node=n110)
    add_synonym("Connector", node=n110)
    
    n111 = add_node("Potentiometer",
            definition="A potentiometer, informally a pot, is a three-terminal resistor with a sliding or rotating contact " +
            "that forms an adjustable voltage divider. If only two terminals are used, one end and the wiper, it acts as a " +
            "variable resistor or rheostat.",
            topic=topic_elements)
    
    n112 = add_node("Element",
            definition="Electrical elements are conceptual abstractions representing idealized electrical components, such as " +
            "resistors, capacitors, and inductors, used in the analysis of electrical networks. Any electrical network can " +
            "be analysed as multiple, interconnected electrical elements in a schematic diagram or circuit diagram, each of " +
            "which affects the voltage in the network or current through the network. These ideal electrical elements represent " +
            "real, physical electrical or electronic components but they do not exist physically and they are assumed to have " +
            "ideal properties according to a lumped element model, while components are objects with less than ideal properties, " +
            "a degree of uncertainty in their values and some degree of nonlinearity, each of which may require a combination of " +
            "multiple electrical elements in order to approximate its function.",
            topic=topic_elements)
    add_synonym("Component", node=n112)
    add_synonym("Entity", node=n112)
    add_synonym("Instrument", node=n112)
    add_synonym("Device", node=n112)
    
    n113 = add_node("Breadboard",
            definition="A breadboard (or protoboard) is usually a construction base for prototyping of electronics. The term " +
            "'breadboard' is commonly used to refer to a solderless breadboard (plugboard).",
            topic=topic_elements)
    add_synonym("Board", node=n113)
    
    n114 = add_node("Switch",
            definition="In electrical engineering, a switch is an electrical component that can break an electrical circuit, interrupting the current or diverting it from one conductor to another.",
            topic=topic_elements)
    
    n115 = add_node("Transistor",
            definition="A transistor is a semiconductor device used to amplify and switch electronic signals and electrical power. " +
            "It is composed of semiconductor material with at least three terminals for connection to an external circuit. A " +
            "voltage or current applied to one pair of the transistor's terminals changes the current through another pair of " +
            "terminals. Because the controlled (output) power can be higher than the controlling (input) power, a transistor " +
            "can amplify a signal. Today, some transistors are packaged individually, but many more are found embedded in " +
            "integrated circuits.",
            topic=topic_elements)
    add_synonym("BJT", node=n115)
    
    n116 = add_node("Ammeter",
            definition="An ammeter is a measuring instrument used to measure the electric current in a circuit. Electric " +
            "currents are measured in amperes (A), hence the name. Instruments used to measure smaller currents, in the " +
            "milliampere or microampere range, are designated as milliammeters or microammeters. Early ammeters were laboratory " +
            "instruments which relied on the Earth's magnetic field for operation. By the late 19th century, improved " +
            "instruments were designed which could be mounted in any position and allowed accurate measurements in electric " +
            "power systems.",
            topic=topic_elements)
    
    n117 = add_node("Voltmeter",
            definition="A voltmeter is an instrument used for measuring electrical potential difference between two points in " +
            "an electric circuit. Analog voltmeters move a pointer across a scale in proportion to the voltage of the " +
            "circuit; digital voltmeters give a numerical display of voltage by use of an analog to digital converter.",
            topic=topic_elements)
    
    n118 = add_node("Ohmmeter",
            definition="An ohmmeter is an electrical instrument that measures electrical resistance, the opposition to an " +
            "electric current. Micro-ohmmeters (microhmmeter or microohmmeter) make low resistance measurements. Megohmmeters " +
            "(aka megaohmmeter or in the case of a trademarked device Megger) measure large values of resistance. The " +
            "unit of measurement for resistance is ohms.",
            topic=topic_elements)
    
    # Action Words
    topic_action = add_vocab_topic(domain=circuits_domain,
                    topic="Action Words",
                    def_useful=False)
    n201 = add_node("Measure", definition="", topic=topic_action)
    add_synonym("Know", node=n201)
    add_synonym("Get", node=n201)
    add_synonym("See", node=n201)
    add_synonym("Take", node=n201)
    add_synonym("Find", node=n201)
    add_synonym("Quantify", node=n201)
    add_synonym("Need", node=n201)
    add_synonym("Bill", node=n201)
    
    n202 = add_node("Compute", definition="", topic=topic_action)
    add_synonym("Calculate", node=n202)
    add_synonym("Evaluate", node=n202)
    add_synonym("Build", node=n202)
    add_synonym("Verify", node=n202)
    add_synonym("Formula", node=n202)
    
    n203 = add_node("Change", definition="", topic=topic_action)
    add_synonym("Set", node=n203)
    add_synonym("Reverse", node=n203)
    add_synonym("Tune", node=n203)
    add_synonym("Vary", node=n203)
    
    n204 = add_node("Use", definition="", topic=topic_action)
    add_synonym("Place", node=n204)
    add_synonym("Connect", node=n204)
    add_synonym("Create", node=n204)
    add_synonym("Drag Drop", node=n204)
    add_synonym("Bill", node=n204)
    
    n205 = add_node("Move", definition="", topic=topic_action)
    
    n206 = add_node("Remove", definition="", topic=topic_action)
    add_synonym("Erase", node=n206)
    add_synonym("Delete", node=n206)
    add_synonym("Take Off", node=n206)
    add_synonym("Eliminate", node=n206)
    add_synonym("Clear", node=n206)
    
    n207 = add_node("Save", definition="", topic=topic_action)
    
    n208 = add_node("Open", definition="", topic=topic_action)
    
    n209 = add_node("Work", definition="", topic=topic_action)
    add_synonym("Does", node=n209)
    add_synonym("Define", node=n209)
    add_synonym("Definition", node=n209)
    add_synonym("Mean", node=n209)
    add_synonym("Signify", node=n209)
    add_synonym("Understand", node=n209)
    add_synonym("Whats", node=n209)
    add_synonym("Whys", node=n209)
    add_synonym("Hows", node=n209)
    add_synonym("Wheres", node=n209)
    add_synonym("Do", node=n209)
    add_synonym("Is", node=n209)
    add_synonym("Be", node=n209)
    add_synonym("Are", node=n209)
    add_synonym("This", node=n209)
    add_synonym("That", node=n209)
    add_synonym("Bill", node=n209)
    
    # Question Words
    topic_question = add_vocab_topic(domain=circuits_domain,
                    topic="Question Words",
                    def_useful=False)
    n301 = add_node("How", definition="", topic=topic_question)
    add_synonym("Hows", node=n301)
    add_synonym("Howz", node=n301)
    
    n302 = add_node("What", definition="", topic=topic_question)
    add_synonym("Whats", node=n302)
    add_synonym("Whatz", node=n302)
    
    n303 = add_node("Why", definition="", topic=topic_question)
    add_synonym("Whys", node=n303)
    add_synonym("Whyz", node=n303)
    
    n304 = add_node("When", definition="", topic=topic_question)
    add_synonym("Whens", node=n304)
    add_synonym("Whenz", node=n304)
    
    # Problem Words
    topic_problems = add_vocab_topic(domain=circuits_domain,
                    topic="Problem Words",
                    def_useful=False)
    n401 = add_node("Wrong", definition="", topic=topic_problems)
    add_synonym("Incorrect", node=n401)
    add_synonym("Not Correct", node=n401)
    add_synonym("Error", node=n401)
    add_synonym("Mistake", node=n401)
    add_synonym("Not Right", node=n401)
    add_synonym("Not", node=n401)
    add_synonym("Fault", node=n401)
    add_synonym("Do Not", node=n401)
    add_synonym("Dont", node=n401)
    add_synonym("Cant", node=n401)
    add_synonym("Cannot", node=n401)
    add_synonym("Cant", node=n401)
    add_synonym("Doesnt", node=n401)
    add_synonym("Isnt", node=n401)
    
    # Circuit Concepts
    topic_concepts = add_vocab_topic(domain=circuits_domain,
                    topic="Circuit Concepts",
                    def_useful=True)
    n501 = add_node("Voltage", definition="", topic=topic_concepts)
    add_synonym("Volt", node=n501)
    add_synonym("Volts", node=n501)
    add_synonym("V", node=n501)
    add_synonym("Potential", node=n501)
    add_synonym("PD", node=n501)
    add_synonym("KVL", node=n501)
    
    n502 = add_node("Current", definition="", topic=topic_concepts)
    add_synonym("Amp", node=n502)
    add_synonym("Amps", node=n502)
    add_synonym("Ampere", node=n502)
    add_synonym("KCL", node=n502)
    add_synonym("DC", node=n502)
    add_synonym("AC", node=n502)
    
    n503 = add_node("Resistance", definition="", topic=topic_concepts)
    add_synonym("Ohm", node=n503)
    add_synonym("Ohms", node=n503)
    
    n504 = add_node("Capacitance", definition="", topic=topic_concepts)
    add_synonym("Farad", node=n504)
    add_synonym("F", node=n504)
    
    n505 = add_node("Inductance", definition="", topic=topic_concepts)
    add_synonym("Henry", node=n505)
    add_synonym("H", node=n505)
    
    n506 = add_node("Power", definition="", topic=topic_concepts)
    add_synonym("Watt", node=n506)
    add_synonym("W", node=n506)
    
    n507 = add_node("Time", definition="", topic=topic_concepts)
    add_synonym("Term", node=n507)
    add_synonym("Second", node=n507)
    add_synonym("MS", node=n507)
    add_synonym("S", node=n507)
    
    n508 = add_node("Frequency", definition="", topic=topic_concepts)
    add_synonym("Hetz", node=n508)
    add_synonym("CPS", node=n508)
    add_synonym("Hz", node=n508)
    
    n509 = add_node("Waveform", definition="", topic=topic_concepts)
    add_synonym("Wave", node=n509)
    add_synonym("Crest", node=n509)
    add_synonym("Trough", node=n509)
    add_synonym("Sine", node=n509)
    add_synonym("Sinusoid", node=n509)
    add_synonym("Square", node=n509)
    
    n510 = add_node("Amplitude", definition="", topic=topic_concepts)
    add_synonym("Value", node=n510)
    add_synonym("Magnitude", node=n510)
    add_synonym("Reading", node=n510)
    add_synonym("Entry", node=n510)
    add_synonym("Meter", node=n510)
    add_synonym("Metre", node=n510)
    add_synonym("Y", node=n510)
    
    n511 = add_node("Reactance", definition="", topic=topic_concepts)
    add_synonym("XC", node=n511)
    add_synonym("XL", node=n511)
    
    n512 = add_node("Impedance", definition="", topic=topic_concepts)
    add_synonym("Z", node=n512)
    
    n513 = add_node("Conductance", definition="", topic=topic_concepts)
    add_synonym("G", node=n513)
    add_synonym("Mho", node=n513)
    add_synonym("Mhos", node=n513)
    
    n514 = add_node("Energy", definition="", topic=topic_concepts)
    add_synonym("Joule", node=n514)
    add_synonym("J", node=n514)
    
    n515 = add_node("Cycle", definition="", topic=topic_concepts)
    
    n516 = add_node("Period", definition="", topic=topic_concepts)
    
    n517 = add_node("Wavelength", definition="", topic=topic_concepts)
    add_synonym("Wave Length", node=n517)
    
    n518 = add_node("Circuit", definition="", topic=topic_concepts)
    add_synonym("Loop", node=n518)
    
    n519 = add_node("Button", definition="", topic=topic_concepts)
    
    n520 = add_node("Phasor", definition="", topic=topic_concepts)
    
    n521 = add_node("Phase", definition="", topic=topic_concepts)
    add_synonym("Angle", node=n521)
    
    # Other
    topic_other = add_vocab_topic(domain=circuits_domain,
                    topic="Other",
                    def_useful=True)
    n601 = add_node("Positive", definition="", topic=topic_other)
    
    n602 = add_node("Negative", definition="", topic=topic_other)
    
    n603 = add_node("Polarity", definition="", topic=topic_other)
    add_synonym("Sign", node=n603)
    
    n604 = add_node("Law", definition="", topic=topic_other)
    add_synonym("Rule", node=n603)
    add_synonym("Principle", node=n603)
    add_synonym("Theorem", node=n603)
    
    n605 = add_node("Gain", definition="", topic=topic_other)
    
    n606 = add_node("Loss", definition="", topic=topic_other)
    
    n607 = add_node("Division", definition="", topic=topic_other)
    
    n608 = add_node("Unit", definition="", topic=topic_other)
    
    # Circuit Laws
    topic_laws = add_vocab_topic(domain=circuits_domain,
                    topic="Circuit Laws",
                    def_useful=True)
    n701 = add_node("Ohms Law", definition="", topic=topic_laws)
    add_synonym("Ohmic", node=n701)
    
    n702 = add_node("Kirchoffs Law", definition="", topic=topic_laws)
    add_synonym("Kirchoffs", node=n702)
    add_synonym("Kircho", node=n702)
    
    n703 = add_node("Thevenin Law", definition="", topic=topic_laws)
    
    n704 = add_node("Norton Law", definition="", topic=topic_laws)
    
    n705 = add_node("Max Power Transfer", definition="", topic=topic_laws)
    add_synonym("Power Transfer", node=n705)
    
    n706 = add_node("Node", definition="", topic=topic_laws)
    add_synonym("Nodes", node=n706)
    
    n707 = add_node("Conservation", definition="", topic=topic_laws)
    
    n708 = add_node("Transformation", definition="", topic=topic_laws)
    add_synonym("Conversion", node=n708)
    
    n709 = add_node("Superposition", definition="", topic=topic_laws)
    add_synonym("Super Position", node=n709)
    
    n710 = add_node("Linear", definition="", topic=topic_laws)
    
    n711 = add_node("Nonlinear", definition="", topic=topic_laws)
    add_synonym("Non Linear", node=n711)
    
    n712 = add_node("Variable", definition="", topic=topic_laws)
    
    n713 = add_node("Direct Current", definition="", topic=topic_laws)
    add_synonym("DC", node=n713)
    
    n714 = add_node("Alternating Current", definition="", topic=topic_laws)
    add_synonym("AC", node=n714)
    add_synonym("Alternate", node=n714)
    
    n715 = add_node("Channel", definition="", topic=topic_laws)
    add_synonym("Chanel", node=n715)
    
    n716 = add_node("Dualtrace", definition="", topic=topic_laws)
    add_synonym("Dual", node=n716)
    
    n717 = add_node("Lissaj", definition="", topic=topic_laws)
    add_synonym("Pattern", node=n717)
    
    # Circuit Diagrams and Measurement
    topic_diagrams = add_vocab_topic(domain=circuits_domain,
                    topic="Circuit Diagrams and Measurement",
                    def_useful=True)
    n801 = add_node("Series Parallel Combination", definition="", topic=topic_diagrams)
    add_synonym("Combination", node=n801)
    add_synonym("Bill", node=n801)
    
    n802 = add_node("Series", definition="", topic=topic_diagrams)
    add_synonym("Serial", node=n802)
    
    n803 = add_node("Parallel", definition="", topic=topic_diagrams)
    
    n804 = add_node("Peak", definition="", topic=topic_diagrams)
    add_synonym("Maximum", node=n804)
    add_synonym("Bill", node=n804)
    
    n805 = add_node("Instantaneous", definition="", topic=topic_diagrams)
    
    n806 = add_node("RMS", definition="", topic=topic_diagrams)
    add_synonym("Mean", node=n806)
    
    n807 = add_node("Average", definition="", topic=topic_diagrams)
    add_synonym("Mean", node=n807)
    
    n808 = add_node("Ground", definition="", topic=topic_diagrams)
    add_synonym("Grnd", node=n808)
    
    n809 = add_node("Peak to Peak", definition="", topic=topic_diagrams)
    add_synonym("Bill", node=n809)
    
    n810 = add_node("XY", definition="", topic=topic_diagrams)
    
    # Math words
    topic_math = add_vocab_topic(domain=circuits_domain,
                    topic="Math",
                    def_useful=True)
    n901 = add_node("Net", definition="", topic=topic_math)
    add_synonym("Total", node=n901)
    add_synonym("Overall", node=n901)
    add_synonym("Sum", node=n901)
    add_synonym("Equivalent", node=n901)
    
    n902 = add_node("Difference", definition="", topic=topic_math)
    
    # Units
    topic_units = add_vocab_topic(domain=circuits_domain,
                    topic="Units",
                    def_useful=True)
    n1001 = add_node("Ohm", definition="", topic=topic_units)
    add_synonym("Ohms", node=n1001)
    
    n1002 = add_node("Farad", definition="", topic=topic_units)
    add_synonym("F", node=n1002)
    
    n1003 = add_node("Henry", definition="", topic=topic_units)
    add_synonym("H", node=n1003)
    
    n1004 = add_node("Volt", definition="", topic=topic_units)
    add_synonym("V", node=n1004)
    
    n1005 = add_node("Ampere", definition="", topic=topic_units)
    add_synonym("Amps", node=n1005)
    add_synonym("Amp", node=n1005)
    add_synonym("A", node=n1005)
    
    n1006 = add_node("Watt", definition="", topic=topic_units)
    add_synonym("W", node=n1006)
    
    n1007 = add_node("Joule", definition="", topic=topic_units)
    add_synonym("J", node=n1007)
    
    n1008 = add_node("Second", definition="", topic=topic_units)
    add_synonym("S", node=n1008)
    add_synonym("MS", node=n1008)
    
    n1009 = add_node("Hertz", definition="", topic=topic_units)
    add_synonym("Hz", node=n1009)
    add_synonym("Cps", node=n1009)
    add_synonym("Cycles", node=n1009)
    
    n1010 = add_node("Inverse Ohm", definition="", topic=topic_units)
    add_synonym("mho", node=n1010)
    add_synonym("mhos", node=n1010)
    add_synonym("1/ohm", node=n1010)
    
    # Help
    topic_help = add_vocab_topic(domain=circuits_domain,
                    topic="Help",
                    def_useful=False)
    n1101 = add_node("Help", definition="", topic=topic_help)
    
    # Add videos
    add_video(name="How to use a Breadboard",
              video_link="http://www.youtube.com/embed/cf6XZ4gs7Ao")
    add_video(name="How to use a DC Power Supply",
              video_link="http://www.youtube.com/embed/mOpCxeqXWEI")
    add_video(name="How to use a Multimeter",
              video_link="http://www.youtube.com/embed/_o8M34NbXpk")
    add_video(name="How to measure Current and Voltage",
              video_link="http://www.youtube.com/embed/wLA6Wkb-TLQ")

    # Print out what we have added to the user.
    for vd in VocabDomain.objects.all():
        for vt in VocabTopic.objects.filter(domain=vd):
            print "- {0} - {1}".format(str(vd), str(vt))

# Add Vocab Domain, Vocab Topics, Words, definitions, and synonyms
def add_vocab_domain(name):
    vd = VocabDomain.objects.get_or_create(name=name)[0]
    return vd

def add_vocab_topic(topic, domain, def_useful):
    vt = VocabTopic.objects.get_or_create(topic=topic, domain=domain, def_useful=def_useful)[0]
    return vt

def add_node(word, definition, topic):
    n = Node.objects.get_or_create(word=word, definition=definition, topic=topic)[0]
    return n

def add_synonym(word, node):
    s = Synonym.objects.get_or_create(word=word, node=node)[0]
    return s

def add_video(name, video_link):
    v = Video.objects.get_or_create(name=name, video_link=video_link)[0]
    return v

# Start execution here!
if __name__ == '__main__':
    print "Starting VOCAB DOMAIN population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VLA_project.settings')
    from VLA.models import *
    populate()