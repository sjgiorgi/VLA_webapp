
                          Virtual Lab Assistant (VLA)

  What is it?
  -----------

  The Virtual Lab Assistant is designed to be an intelligent Electrical
  Engineering laboratory assistant. The goal is to introduce students to,
  and guide them through theory and simulations BEFORE entering the lab,
  where they will be exposed to hardware. This should give them a better
  understanding of the hardware and free up the instructor to focus more
  on presenting the hardware and debugging any problems.

  The Latest Version
  ------------------
  
  LASTEST COMMIT:
  - allow TextFields to contain HTML
  - added 'video' option for TheoryElement, SimulationElement, and HardElement
  - added equipment to Laboratory
  - added powerset search for Q&A
  
  PREVIOUS COMMITS:
  - fully commented views.py
  - fixed bugs found by Zach
    - Size of green check marks
    - Selecting 'Yes' at end of Theory, Simulation, and Hardware sections now working
  
  TODO:
  - change 'VLA.* import' to more general import (remove VLA)
  - fix password confirmation field
  - create user profiles / track user data 
  - fix image uploading for 'element' classes
  - add Results section
  - add Results Questions section (is this actually needed???)
  - generate Word file
  - add 'question category' to Rulebase 
  - finish Rulebase search
    - include synonyms in search
  - finish python script for filling Vocab Domain and Rulebase database
  - finish python script for Ohms Law Lab
  - switch database to PostgreSQL
  - make help module app and VLA app separate
  - include mathjax.js instead of url (in base.html)
  - allow Course, Lab, etc. names to include symbols (example: Ohm's Law)
  - customize admin panel
  - create class "nav pull-left" to align Temple and CSNAP logo
  - add table option to TheoryElement, SimulationElement, and HardwareElement
  - use South for porting databases
  - add user panel
  - add forum
  - add multisim page
  - add OneToOne fields for Laboratory and Theory, TheoryTest, etc. (in general, check where we can use OneToOne fields)

 USABILITY IMPROVEMENTS:
  - Do something to fill white space on larger pages (Consider having the side bar scroll down with the page)
  - Make about page better (Add pictures, change formatting)
  - Fix alignment along top bar
  - Redirect /vla/ to /VLA/ to reduce 404s
  - Reduce uneven or unsymmetrical white space
  - Analyze good ranking websites to get a good idea of what constitutes good design
    - See: BitBucket top bar, Facebook/YouTube white space management, icon placement, etc. 
    - List of high ranking websites: http://www.alexa.com/topsites

 BUGS:
  - 

  Documentation
  -------------
  
  Python version 2.7.1
  Django version 1.6.5
  

  Installation
  ------------

  

  Licensing
  ---------



  Contacts
  --------
  
  sal.giorgi@gmail.com