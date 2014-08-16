
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
  - finished Rulebase search (now includes synonyms in search)
  - create user profiles / track user data
  - added populate_users.py script
  - added South
  - Make it so login page doesn't redirect on failure to login
  - Remove side bar on login page or add content to it
  - separate apps (tutor, VLA, and student)
  - changed question search to omit subsets consisting of just question words (what, how, etc.)
  - added OneToOne fields for Laboratory and Theory, TheoryTest, etc.
  - add Results section
  - added Ohm's Law lab to EE1 and all of Dr. Obeid's labs to EE2
  - add user profile page
  - fixed password confirmation field
  - change imports to explicit relative import type
  - Redirect /vla/ to /VLA/
  - allow saving of simulation image to be dynamic (save to folder titled after username and lab name)

  PREVIOUS COMMITS:
  - allow TextFields to contain HTML
  - added 'video' option for TheoryElement, SimulationElement, and HardwareElement
  - added equipment to Laboratory
  - added powerset search for Q&A
  
  TODO (PRIORITY):
  - add table option to TheoryElement, SimulationElement, and HardwareElement
  - generate Word file
  - add forum
  - add Zach's image processing script to the views
   
  TODO:
  - finish python script for filling Vocab Domain and Rulebase database
  - switch database to PostgreSQL
  - include mathjax.js instead of url (in base.html)
  - allow Course, Lab, etc. names to include symbols, ex: Ohm's Law
  - customize admin panel
  - create class "nav pull-left" to align Temple and CSNAP logo
  - ability for user to change profile info and password
  - add synonym for each word in multi-word nodes (ex: 'function' and 'generator' for 'function generator')

 USABILITY IMPROVEMENTS:
  - Do something to fill white space on larger pages (Consider having the side bar scroll down with the page)
  - Make about page better (Add pictures, change formatting)
  - Fix alignment along top bar
  - Reduce uneven or unsymmetrical white space
  - Analyze good ranking websites to get a good idea of what constitutes good design
    - See: BitBucket top bar, Facebook/YouTube white space management, icon placement, etc. 
    - List of high ranking websites: http://www.alexa.com/topsites

 BUGS:
  - Theory and Simulation Test don't store user responses when page is reloaded after test taken
  - if Element of image type is uploaded through admin panel, url does not point correctly to image

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