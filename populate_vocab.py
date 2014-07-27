import os


def populate():
    
    circuits_domain = add_vocab_domain(name = 'Circuits')
    
    # Circuit ELements and Equipment
    topic_elements = add_vocab_topic(domain=circuits_domain,
                    topic="Circuit Elements and Equipment",
                    def_useful=True)
    n101 = add_node("Resistor", definition="", topic=topic_elements)
    add_synonym("Res", node=n101)
    add_synonym("R", node=n101)
    add_synonym("Ohm", node=n101)
    add_synonym("Conductor", node=n101)
    
    n102 = add_node("Capacitor", definition="", topic=topic_elements)
    add_synonym("Cap", node=n102)
    add_synonym("F", node=n102)
    add_synonym("Farad", node=n102)
    
    n103 = add_node("Inductor", definition="", topic=topic_elements)
    add_synonym("Ind", node=n103)
    add_synonym("L", node=n103)
    add_synonym("Henry", node=n103)
    add_synonym("H", node=n103)
    
    n104 = add_node("DC Source", definition="", topic=topic_elements)
    add_synonym("DC Supply", node=n104)
    add_synonym("Supply", node=n104)
    add_synonym("Source", node=n104)
    add_synonym("DCS", node=n104)
    add_synonym("Battery", node=n104)
    add_synonym("Cell", node=n104)
    
    n105 = add_node("Multimeter", definition="", topic=topic_elements)
    add_synonym("Voltmeter", node=n105)
    add_synonym("Ammeter", node=n105)
    add_synonym("Ohmmeter", node=n105)
    add_synonym("Meter", node=n105)
    add_synonym("Multim", node=n105)
    
    n106 = add_node("Function Generator", definition="", topic=topic_elements)
    add_synonym("AC Supply", node=n106)
    add_synonym("Generator", node=n106)
    add_synonym("AC Source", node=n106)
    add_synonym("Func Gen", node=n106)
    
    n107 = add_node("Oscilloscope", definition="", topic=topic_elements)
    add_synonym("Oscope", node=n107)
    add_synonym("Display", node=n107)
    add_synonym("CRT", node=n107)
    add_synonym("Cathode", node=n107)
    
    n108 = add_node("Spectrum Analyzer", definition="", topic=topic_elements)
    add_synonym("Spectrum", node=n108)
    add_synonym("Analyzer", node=n108)
    add_synonym("Sweep", node=n108)
    add_synonym("SA", node=n108)
    
    n109 = add_node("Diode", definition="", topic=topic_elements)
    add_synonym("Rectifier", node=n109)
    add_synonym("Semiconductor", node=n109)
    add_synonym("Junction", node=n109)
    
    n110 = add_node("Wire", definition="", topic=topic_elements)
    add_synonym("Cable", node=n110)
    add_synonym("Line", node=n110)
    add_synonym("Short", node=n110)
    add_synonym("Connector", node=n110)
    
    n111 = add_node("Potentiometer", definition="", topic=topic_elements)
    
    n112 = add_node("Element", definition="", topic=topic_elements)
    add_synonym("Component", node=n112)
    add_synonym("Entity", node=n112)
    add_synonym("Instrument", node=n112)
    add_synonym("Device", node=n112)
    
    n113 = add_node("Breadboard", definition="", topic=topic_elements)
    add_synonym("Board", node=n113)
    
    n114 = add_node("Switch", definition="", topic=topic_elements)
    
    n115 = add_node("Transistor", definition="", topic=topic_elements)
    add_synonym("BJT", node=n115)
    
    n116 = add_node("Ammeter", definition="", topic=topic_elements)
    n117 = add_node("Voltmeter", definition="", topic=topic_elements)
    n118 = add_node("Ohmmeter", definition="", topic=topic_elements)
    
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

# Start execution here!
if __name__ == '__main__':
    print "Starting VOCAB DOMAIN population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VLA_project.settings')
    from VLA.models import *
    populate()