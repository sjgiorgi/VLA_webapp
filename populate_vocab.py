import os


def populate():
    
    circuits_domain = add_vocab_domain(name = 'Circuits')
    
    # Circuit ELements and Equipment
    topic_elements = add_vocab_topic(domain=circuits_domain,
                    topic="Circuit Elements and Equipment",
                    def_useful=True)
    add_node("Resistor", definition="", topic=topic_elements)
    add_node("Capacitor", definition="", topic=topic_elements)
    add_node("Inductor", definition="", topic=topic_elements)
    add_node("DC Source", definition="", topic=topic_elements)
    add_node("Multimeter", definition="", topic=topic_elements)
    add_node("Function Generator", definition="", topic=topic_elements)
    add_node("Oscilloscope", definition="", topic=topic_elements)
    add_node("Spectrum Analyzer", definition="", topic=topic_elements)
    add_node("Diode", definition="", topic=topic_elements)
    add_node("Wire", definition="", topic=topic_elements)
    add_node("Potentiometer", definition="", topic=topic_elements)
    add_node("Element", definition="", topic=topic_elements)
    add_node("Breadboard", definition="", topic=topic_elements)
    add_node("Switch", definition="", topic=topic_elements)
    add_node("Transistor", definition="", topic=topic_elements)
    add_node("Ammeter", definition="", topic=topic_elements)
    add_node("Voltmeter", definition="", topic=topic_elements)
    add_node("Ohmmeter", definition="", topic=topic_elements)
    
    # Action Words
    topic_action = add_vocab_topic(domain=circuits_domain,
                    topic="Action Words",
                    def_useful=False)
    add_node("Measure", definition="", topic=topic_action)
    add_node("Compute", definition="", topic=topic_action)
    add_node("Change", definition="", topic=topic_action)
    add_node("Use", definition="", topic=topic_action)
    add_node("Move", definition="", topic=topic_action)
    add_node("Remove", definition="", topic=topic_action)
    add_node("Save", definition="", topic=topic_action)
    add_node("Open", definition="", topic=topic_action)
    add_node("Work", definition="", topic=topic_action)
    
    # Question Words
    topic_question = add_vocab_topic(domain=circuits_domain,
                    topic="Question Words",
                    def_useful=False)
    add_node("How", definition="", topic=topic_question)
    add_node("What", definition="", topic=topic_question)
    add_node("Why", definition="", topic=topic_question)
    add_node("When", definition="", topic=topic_question)
    
    # Problem Words
    topic_problems = add_vocab_topic(domain=circuits_domain,
                    topic="Problem Words",
                    def_useful=False)
    add_node("Wrong", definition="", topic=topic_problems)
    
    # Circuit Concepts
    topic_concepts = add_vocab_topic(domain=circuits_domain,
                    topic="Circuit Concepts",
                    def_useful=True)
    add_node("Voltage", definition="", topic=topic_concepts)
    add_node("Current", definition="", topic=topic_concepts)
    add_node("Resistance", definition="", topic=topic_concepts)
    add_node("Capacitance", definition="", topic=topic_concepts)
    add_node("Inductance", definition="", topic=topic_concepts)
    add_node("Power", definition="", topic=topic_concepts)
    add_node("Time", definition="", topic=topic_concepts)
    add_node("Frequency", definition="", topic=topic_concepts)
    add_node("Waveform", definition="", topic=topic_concepts)
    add_node("Amplitude", definition="", topic=topic_concepts)
    add_node("Reactance", definition="", topic=topic_concepts)
    add_node("Impedance", definition="", topic=topic_concepts)
    add_node("Conductance", definition="", topic=topic_concepts)
    add_node("Energy", definition="", topic=topic_concepts)
    add_node("Cycle", definition="", topic=topic_concepts)
    add_node("Period", definition="", topic=topic_concepts)
    add_node("Wavelength", definition="", topic=topic_concepts)
    add_node("Circuit", definition="", topic=topic_concepts)
    add_node("Button", definition="", topic=topic_concepts)
    add_node("Phasor", definition="", topic=topic_concepts)
    add_node("Phase", definition="", topic=topic_concepts)
    
    # Other
    topic_other = add_vocab_topic(domain=circuits_domain,
                    topic="Other",
                    def_useful=True)
    add_node("Positive", definition="", topic=topic_other)
    add_node("Negative", definition="", topic=topic_other)
    add_node("Polarity", definition="", topic=topic_other)
    add_node("Law", definition="", topic=topic_other)
    add_node("Gain", definition="", topic=topic_other)
    add_node("Loss", definition="", topic=topic_other)
    add_node("Division", definition="", topic=topic_other)
    add_node("Unit", definition="", topic=topic_other)
    
    # Circuit Laws
    topic_laws = add_vocab_topic(domain=circuits_domain,
                    topic="Circuit Laws",
                    def_useful=True)
    add_node("Ohms Law", definition="", topic=topic_laws)
    add_node("Kirchoffs Law", definition="", topic=topic_laws)
    add_node("Thevenin Law", definition="", topic=topic_laws)
    add_node("Norton Law", definition="", topic=topic_laws)
    add_node("Max Power Transfer", definition="", topic=topic_laws)
    add_node("Node", definition="", topic=topic_laws)
    add_node("Conservation", definition="", topic=topic_laws)
    add_node("Transformation", definition="", topic=topic_laws)
    add_node("Superposition", definition="", topic=topic_laws)
    add_node("Linear", definition="", topic=topic_laws)
    add_node("Nonlinear", definition="", topic=topic_laws)
    add_node("Variable", definition="", topic=topic_laws)
    add_node("Direct Current", definition="", topic=topic_laws)
    add_node("Alternating Current", definition="", topic=topic_laws)
    add_node("Channel", definition="", topic=topic_laws)
    add_node("Dualtrace", definition="", topic=topic_laws)
    add_node("Lissaj", definition="", topic=topic_laws)
    
    # Circuit Diagrams and Measurement
    topic_diagrams = add_vocab_topic(domain=circuits_domain,
                    topic="Circuit Diagrams and Measurement",
                    def_useful=True)
    add_node("Series Parallel Combination", definition="", topic=topic_diagrams)
    add_node("Series", definition="", topic=topic_diagrams)
    add_node("Parallel", definition="", topic=topic_diagrams)
    add_node("Peak", definition="", topic=topic_diagrams)
    add_node("Instantaneous", definition="", topic=topic_diagrams)
    add_node("RMS", definition="", topic=topic_diagrams)
    add_node("Average", definition="", topic=topic_diagrams)
    add_node("Ground", definition="", topic=topic_diagrams)
    add_node("Peak to Peak", definition="", topic=topic_diagrams)
    add_node("XY", definition="", topic=topic_diagrams)
    
    # Math words
    topic_math = add_vocab_topic(domain=circuits_domain,
                    topic="Math",
                    def_useful=True)
    add_node("Net", definition="", topic=topic_math)
    add_node("Difference", definition="", topic=topic_math)
    
    # Units
    topic_units = add_vocab_topic(domain=circuits_domain,
                    topic="Units",
                    def_useful=True)
    add_node("Ohm", definition="", topic=topic_units)
    add_node("Farad", definition="", topic=topic_units)
    add_node("Henry", definition="", topic=topic_units)
    add_node("Volt", definition="", topic=topic_units)
    add_node("Ampere", definition="", topic=topic_units)
    add_node("Watt", definition="", topic=topic_units)
    add_node("Joule", definition="", topic=topic_units)
    add_node("Second", definition="", topic=topic_units)
    add_node("Hertz", definition="", topic=topic_units)
    add_node("Inverse Ohm", definition="", topic=topic_units)
    
    # Help
    topic_help = add_vocab_topic(domain=circuits_domain,
                    topic="Help",
                    def_useful=False)
    add_node("Help", definition="", topic=topic_help)

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