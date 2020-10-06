
'''
===============================================================================
ENGR 133 Fa 2020

Assignment Information
	Assignment:     Py4 Task 1
	Author:         Kyle Nematz, knematz@purdue.edu
	Team ID:        LC4-09
	
Contributors:   Name, login@purdue 
                Name, login@purdue 
                Name, login@purdue 
                Name, login@purdue [repeat as needed]
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
last = input("Enter your last name:\n")
first = input("Enter your first name: \n")
ageYears = int(input("Enter your age in years: \n"))
daysB = int(input("Enter the days elapsed since your last birthday: \n"))
daysYear = 365.242199
realAge = ageYears + (daysB / daysYear)
def Seconds(ageYears,daysB,daysYear):
    ageSec = (ageYears + (daysB / daysYear)) * daysYear * 86400
    return(ageSec)
secondsOld = Seconds(ageYears,daysB,daysYear)
list1 = [first,last,round(realAge,10),round(secondsOld,0)]
with open("Py4_Task1_output.txt","w") as P:
    P.write(list1[0] + " " + list1[1] )





'''
==============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''

