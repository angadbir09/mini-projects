School = raw_input("Enter School name\n")
Province = raw_input ("Enter your Province\n")
City = raw_input ("Enter your City\n")
SchoolAddress = School + ", " + City + ", " + Province
FirstName = raw_input("Enter First name\n")
LastName = raw_input("Enter Last name\n")
Student = FirstName + " " + LastName
Mark1 = raw_input ("Enter the name of your First period class\n")
Mark1avg = input ("Enter your Mark for " + Mark1 + "\n")
Mark2 = raw_input ("Enter the name of your Second period class\n")
Mark2avg = input ("Enter your Mark for " + Mark2 + "\n")
Mark3 = raw_input ("Enter the name of your Third period class\n")
Mark3avg = input ("Enter your Mark for " + Mark3 + "\n")
Mark4 = raw_input ("Enter the name of your Fourth period class\n")
Mark4avg = input ("Enter your Mark for " + Mark4 + "\n")
Overall = (Mark1avg + Mark2avg + Mark3avg + Mark4avg)/4
Comment = raw_input ("Enter comments on student success here")
print "\nStudent Report Card"
print School
print Student
print "\nSemester 1 marks for " + Student
print Mark1
print Mark2
print Mark3
print Mark4
print "Overall average for " + FirstName + " is:"
print Overall
print Comment
print "\nAll student Report Cards are to be returned to:"
print SchoolAddress
print "\nThank you"

