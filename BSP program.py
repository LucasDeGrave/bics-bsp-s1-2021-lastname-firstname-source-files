
# user name - nom de l'utilisateur
user_name = input("Please enter your user name:")
print("Your user name is", user_name)



# program start - démarrage du programme
program_start = input("Would you start the program ?")

if program_start == "yes":
    print("the program starts")
    from datetime import datetime
    start_date = datetime.now()
    print ("You starts at", start_date.year, "-",  start_date.month, "-", start_date.day, "at",
           start_date.hour, ":", start_date.minute, ":", start_date.second,
           )
elif program_start == "no":
    print("the program isn't going to start")
else:
    print("you entered an invalid answer")



# program stop - arrêt du programme
program_stop = input("Would you stop the program ?")

if program_stop == "yes":
    print("the program stops")
    stop_date = datetime.now()
    print ("You stops at", stop_date.year, "-",  stop_date.month, "-", stop_date.day, "at",
           stop_date.hour, ":", stop_date.minute, ":", stop_date.second,
           )
    time_delta = stop_date - start_date
    print("the program ran for", time_delta)
if program_stop == "no":
    print("the program isn't going to stop")

# data date file - fichier de dates

convert_start_date = str(start_date)
convert_stop_date = str(stop_date)
convert_time_delta = str(time_delta)

file = open("programdatadate.txt", "a+")
file.write("User name: ")
file.write(user_name)
file.write("\n")
file.write("Start: ")
file.write(convert_start_date)
file.write("\n")
file.write("Stop: ")
file.write(convert_stop_date)
file.write("\n")
file.write("Duration: ")
file.write(convert_time_delta)
file.write("\n")
file.close()
