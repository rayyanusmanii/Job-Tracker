import pandas as pd
import matplotlib.pyplot as plt
import os

while True: #options show up after each decision the user makes
    #opening options
    options = input ("Which of the following would you like to do today? (Reply with the number) \n"
        "1. Add a new application\n"
        "2. View all applications\n"
        "3. View analytics\n"
        "4. Quit \n")

    #if user decides to go with adding a new application, ask for specfic data related to the application
    if options == "1" or options == "1.":
        companyname = input ("Input company name: ")
        role = input ("Input role: ")
        dateapplied = input ("Input date applied (YYYY-MM-DD): ")
        status = input ("Input status (Applied/Interview/Rejected/Offer): ")
        print()

        #first check if the csv exists, if it does, add a new row at the end of the df with the inputted application data and save it
        if os.path.isfile ('applications.csv'):
            df = pd.read_csv ('applications.csv')
            df.loc[len (df)] = [companyname, role, dateapplied, status]
            df.to_csv('applications.csv', index=False)

        #if csv doesn't exist, create a new df with just that one row of inputted application data and save it
        else:
            data = { #df must be a dictionary
                "company" : [companyname],
                "role" : [role],
                "dateapplied" : [dateapplied],
                "status" : [status]
            }

            df = pd.DataFrame(data)
            df.to_csv ('applications.csv', index=False)
        
   #if user chooses view all applications, to prevent crashing, applications.csv must exist and if so, print all user applications in a table     
    elif options == "2" or options == "2.":
        if os.path.isfile ('applications.csv'):
            df = pd.read_csv ('applications.csv')
            print()
            print (df)
            print()

            input("Press Enter to continue...")
        
        else:
            print ("applications.csv not found. Please create one and try again. ")
            print()

    #if user chooses view analytics, same safeguard as before to ensure applications.csv exists
    elif options == "3" or options == "3.":
        if os.path.isfile ('applications.csv'):
            df = pd.read_csv ('applications.csv') 

            totalapplications = len(df) #total applications is determined by row count

            statusbreakdown = df.groupby ("status") ["company"].count() #status is given for each company inputted

            notapplied = df [df["status"] != "Applied"] #any application status that isn't "Applied"
            responserate = (len (notapplied) / totalapplications) * 100 #response rate calculation
            result = f"{responserate}%"

            applied = df [df["status"] == "Applied"] #any application status that is "Applied"
            convertcol = pd.to_datetime (applied ["dateapplied"])
            timedelta = (pd.Timestamp.now() - convertcol).dt.days #subtract today's date with the date the user applied 
            averagetimewaiting = round (timedelta.mean())

            statusbreakdown.plot (kind='bar')
            plt.xticks(rotation=45, ha='right')
            plt.title("Job Application Status Breakdown")
            plt.xlabel("Application Status")
            plt.ylabel("Number of applications ")
            plt.show()

            print()
            print ("--- Your Analytics Report ---")
            print ()
            print ("Total applications sent: ", totalapplications)
            print ("Breakdown by status: ")
            statusbreakdown.index.name = None
            print (statusbreakdown.to_string())
            print("Response rate: ", result)
            print("Average days waiting: ", averagetimewaiting)
            print()

            input("Press Enter to continue...")


        else:
            print ("applications.csv not found. Please create one and try again. ")
            print()

    elif options == "4" or options == "4.":
        break
    print()

