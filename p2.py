# p2.py: Medical Diagnostic System
# Created By: Jae Cho
# E-mail: jhcho@email.wm.edu
#
# The program performs as a basic tool for medical diagnosis. This tool behaves as a human expert for a particular application domain.
# This program is essentially a rule-based system that performs a series of queries to determine the situation at hand so that it can determine which of its rules apply. 
# The queries are performed using the strings from previous queries to determine future queries, enabling the program to quickly determine the specifics of the situation.
# The domain in the case study contains the likely causes of a fever.

print ("Fever Diagnostic Tool")
print ("---------------------")
print()
print ("Please note that this program performs no true diagnostic \n activity. No decisitions should be made based upon the tool\'s \n analysis. If you have a fever, you should contact your doctor.\n")

# Assign a variable to the string "y" as a string.
string = "y" 

# Create a loop where the program prompts queries that follow a sequence of other queries and set variables.
while string == "y":
    # Fever condition
    string = (input ("\nDo you have a fever (y,n): "))
    print(string)
    symptoms = " "
    diagnosis = " "
    
    if string.lower() == 'y':
        # Coughing condition.
        string = (input ("Are you coughing (y,n): "))
        print (string)
        
        if string.lower() == 'y':
            #Breathing condition.
            string = (input ("Are you short of breath or wheezing or coughing up phlegm (y,n): "))
            print (string)
            
            if string.lower() == 'y':
                symptoms = ("\nSymptoms\n* Fever \n* Coughing \n* Short of breath or wheezing or coughing up phlegm")
                diagnosis = ("\nDiagnosis\n        Possibilities include pneumonia or infection of airways.")
            
            else:
                #Headache condition.
                string = input ("Do you have a headache (y,n): ")
                print (string)
                
                if string.lower() == 'y':
                    symptoms = ("\n* None")
                    diagnosis = ("Diagnosis\n        Possibilities include viral infection.")
                
                else:
                    # Sore throat condition.
                    string = input ("Do you have a sore throat (y,n): ")
                    print (string)
                    
                    if string.lower() == 'y':
                        symptoms = ("* None" + '\n')
                        diagnosis = ("Diagnosis\n        Possibilities include throat infection.")
                        
                    else:
                        # Back pain with fever condition.
                        string = input ("Do you have back pain just above the waist with chills and fever (y,n): ")
                        print (string)
                        
                        if string.lower() == 'y':
                            symptoms = ("Symptoms\n* Fever\n* Coughing\n* Back pain just above the waist with chills and fever")
                            diagnosis = ("\nDiagnosis\n        Possibilities include kidney infection.")
                            
                        else:
                            # Urinating condition.
                            string = input ("Do you have pain urinating or are urinating more often (y,n): ")
                            print (string)
                            
                            if string.lower() == 'y':
                                symptoms = ("* None" + '\n')
                                diagnosis = ("Diagnosis\n        Possibilities include urinary tract infection.")
                                
                            else:
                                symptoms = ("* None" + '\n')
                                diagnosis = ("Diagnosis\n        Insufficient information to list possibilities.")
                                
# Continue with the loop now starting with the teh answer as no to the queries. 
        else:
            # Headache condition.
            string = input ("Do you have a headache (y,n): ")
            print (string)
            
            if string.lower() == 'y':
                # Pain and vomiting condition.
                string = input ("Are you experiencing any of the following:\npain when bending your head forward,\nnausea or vomiting,\nbright light hurting your eyes,\ndrowsiness, or confusion (y,n): ")
                print (string)
                
                if string.lower() == 'y':
                    symptoms = ("\nSymptoms\n* Fever\n* Headache\n* Pain when bending head forward, nausea or vomiting, bright light hurting eyes, drowsiness, or confusion")
                    diagnosis = ("\nDiagnosis\n        Possibilities include meningitis.")
                    
                else:
                    # Vomiting or diarrhea condition.
                    string = input ("Are you vomiting or have you had diarrhea (y,n): ")
                    print (string)
                    
                    if string.lower() == 'y':
                        symptoms = ("Symptoms\n* Vomitting\n* Diarrhea" + '\n')
                        diagnosis = ("Diagnosis\n        Possibilities include digestive tract infection.")
                        
                    else:
                        symptoms = ("\n* None" + '\n')
                        diagnosis = ("Diagnosis\n        Insufficient information to list possibilities.")
                        
            else:
                # Vomiting or Diarrhea condition.
                string = input ("Are you vomiting or have you had diarrhea (y,n): ")
                print (string)
                
                if string.lower() == 'y':
                    symptoms = ("\n* None" + '\n')
                    diagnosis = ("Diagnosis\n        Possibilities include digestive tract infection.")
                    
                else:
                    symptoms = ("\n* None" + '\n')
                    diagnosis = ("Diagnosis\n        Insufficient information to list possibilities.")
                    
    else:
        symptoms = ("\nSymptoms\n* None\n")
        diagnosis = ("Diagnosis\n        Insufficient information to list possibilities")
        
    print (symptoms)
    print (diagnosis)
    
    string = input ("\n\nWould you to input another set of symptoms?: ")
    print (string)
    string = string.lower()
    
    
        
