import sys
import spacy
nlp = spacy.load("en_core_web_sm")
#get file name from user
filename = input("what is the filename? please input the full path.\n")
#read user input
try:
    file = open(filename, "r")
except FileNotFoundError:
    print(f"File {filename} not found.  Aborting")
    sys.exit(1)
except OSError:
    print(f"OS error occurred trying to open {filename}")
    sys.exit(1)
except Exception as err:
    print(f"Unexpected error opening {filename} is",repr(err))
    sys.exit(1)
else:
  with file:
    #create tokens for each sentence
    #isolate important struct?
    #rephrase to generate question?
    #get answer from user
    #strip answer of spaces, capatilization, etc.
    #compare to known answer taken from user notes
for line in file:
    for token in line:
        print(token.text, token.pos_, token.dep_)
