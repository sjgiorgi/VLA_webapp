
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
  - added South
  - make help ('tutor') module app and VLA app separate
  - changed question search to omit subsets consisting of just question words (what, how, etc.)
  - added OneToOne fields for Laboratory and Theory, TheoryTest, etc.
  - add Results section
  - added Ohm's Law lab to EE1 and all of Dr. Obeid's labs to EE2
  - add user profile page
  - fixed password confirmation field
  - change imports to explicit relative import type
  - Redirect /vla/ to /VLA/
  
  PREVIOUS COMMITS:
  - allow TextFields to contain HTML
  - added 'video' option for TheoryElement, SimulationElement, and HardwareElement
  - added equipment to Laboratory
  - added powerset search for Q&A
  
  TODO (PRIORITY):
  - create user profiles / track user data 
  - add table option to TheoryElement, SimulationElement, and HardwareElement
  - generate Word file
  - finish Rulebase search
    - include synonyms in search
    - search for pairs of words, ex: 'function generator', 'dc source'
                          (is this needed? will searching synonyms take care of this?)
    
  TODO:
  - fix image uploading for 'element' classes
  - finish python script for filling Vocab Domain and Rulebase database
  - switch database to PostgreSQL
  - include mathjax.js instead of url (in base.html)
  - allow Course, Lab, etc. names to include symbols, ex: Ohm's Law
  - customize admin panel
  - create class "nav pull-left" to align Temple and CSNAP logo
  - add forum
  - ability for user to change profile info and password

 USABILITY IMPROVEMENTS:
  - Do something to fill white space on larger pages (Consider having the side bar scroll down with the page)
  - Make about page better (Add pictures, change formatting)
  - Fix alignment along top bar
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
  South version 1.0
  

  Installation
  ------------

  

  Licensing
  ---------



  Contacts
  --------
  
  sal.giorgi@gmail.com