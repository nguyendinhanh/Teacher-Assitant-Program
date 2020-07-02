

def main():
     students = []
     student_ID = []
     gradebook = []
     gradebook_int = []
     number_ID = []
     list_ID = []
     usr = 'O'

     while usr != 'X':
          option = input('''Welcome to the Teacher’s Simple Class Calculator. Here’s the list of options:
          1- Enter student records (Name, ID, and 6 marks separated by commas)
          2- Display the class average.
          3- Display the information for a given student
          4- List the entire class by name and ID.
          X- Exit

Select an option by entering its number or X to exit: ''')
          if option == 'X':
               break

          
#OPTION 1:          
          if option == '1':
               user_input = 'continue'  #set user_input as something different than "done"
               while user_input != 'done':
                    user_input = input('Enter student record (separate fields by commas) or done: ')
                    if user_input == "done":
                         pass
                    else:
                         new = user_input.split(',')
                         if len(new) < 8:
                              print('Record incomplete. Record rejected.')
                         if len(new) > 8:
                              print('Record overload. Record rejected.')
                         elif len(new) == 8:
                              #student_name:
                              stu_name = new[:1]

                              #student_ID:
                              student_ID.append(new[1:2])  #create a list for student ID
                              count_ID = 0
                              for each_ID in student_ID: #check if any student ID has already been entered
                                   if student_ID.count(each_ID) > 1:
                                        count_ID += 1
                              if count_ID != 0:
                                   print('Duplicate ID number. Record rejected. ')
                                   student_ID.pop()
                              elif count_ID == 0:
                                    
                              
                              #grades
                                   input_grades = new[2:] #store the last 6 input's value (marks) into "input_grades"
                                   correct_num = 0
                                   for each_grade in new[1:]: #check if any grade is wrongly entered as string
                                        if each_grade.isdigit():
                                             correct_num += 1
                                   if correct_num == 7:
                                        print('Record accepted. ')
                                        students.append(new)
                                        for i in input_grades:
                                             gradebook.append(int(i)) #if all inputted data is correct, convert it into integers and store all students' grades in "gradebook"
                                   else:
                                        print('Invalid data. Record rejected. ')
                                        student_ID.pop() #remove student's ID if inputted data was invalid
                                        
               
                    print(students)
                         
                         
                              

#OPTION 2:                  
          if option == '2':
               average = sum(gradebook) / len(student_ID)
               print('Class average is: ', average)

#OPTION 3:
          if option == '3':
               input_3 = input('Enter the ID of the student: ')
               if input_3.isdigit():
                    ID = int(input_3)
                    found = False
                    newlist = []
                    for a in students:
                         name = a[0]
                         for element in a[1:]:
                              if int(element) == ID:
                                   for i in a[1:]:
                                        newlist.append(int(i))
                                   found = True
                                   break
                              
                    total = sum(newlist[1:])
                    
                    # Define Letter Grade
                    if   total >= 87:
                         letter = 'A'
                    elif total >= 75 and total <= 86:
                         letter = 'B'
                    elif total >= 65 and total <= 74:
                         letter = 'C'
                    else :
                         letter = 'F'
                    
                    if found:
                         print('Information for', name, ID,'total grade', total, "letter grade", letter)
                    else:
                         print('Invalid ID')
               else:
                    print('Please enter a numeric ID')
                             
                                    
#OPTION 4:
          if option == '4':
               for i in range(len(students)):
                    print(",".join(students[i][0:1]),"",",".join(students[i][1:2]))
               
main()
