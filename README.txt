
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
  - built Rulebase database
  - implemented initial question search
  - added 'views' to definitions/questions
  - track number of times definition/question is viewed and present top 5 on Help page
  - added 'date_added' to definitions/questions
  - present top 5 recent definitions/questions on Help page
  - added Answer topics
  
  PREVIOUS COMMITS:
  - changed models for TheoryElement, SimulationElement, and HardwareElement (removed multiple Booleans, added choice list)
  - added password confirmation field to register page
  - added first name, last name, TUid field to register page
  - added instructional videos to help module
  - added YouTube page link to menu bar
  
  TODO:
  - change 'VLA.* import' to more general import (remove VLA)
  - fix password confirmation field
  - create user profiles / track user data 
  - fix image uploading for 'element' classes
  - add Results section
  - add Results Questions section
  - generate Word file
  - add 'question category' to Rulebase 
  - finish Rulebase search
    - include synonyms in search
    - search for all subsets of input keywords
    - search substrings of keywords (ex: 'res' for 'resistor')
  - finish python script for filling Vocab Domain and Rulebase database
  - finish python script for Ohms Law Lab
  - switch database to PostgreSQL
  - make help module app and VLA app separate
  - make 'top 5 viewed definition' list on help page
  - include mathjax.js instead of url (in base.html)
  - allow Course, Lab, etc. names to include symbols (example: Ohm's Law)
  - customize admin panel
  - create class="nav pull-left" to align Temple and CSNAP logo
  - add table option to TheoryElement, SimulationElement, and HardwareElement
  - use South for porting databases

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