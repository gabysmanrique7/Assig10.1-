
#                                Assigment 10.1
#In this assignment, I implement my own class based on a real-world object.
#This is a  short demo program in the main function that highlights all your class variables and methods.
# Citation: Harikrishna Kuttivelil, Presentation 10/6/2021


#I imported random 
import random

#This is my class student 
class Student:
    # Class variable santa cruz and records 
    school = "Santa Cruz "
    records = {
        "john12": 3.4,
        "ron13": 3.5,
        "lisa14": 3.7,
        "aron15": 3.8
    }
    
    # Constructor | 5 Data variables self , name , age , gpa and std 
    def __init__(self, name, age, gpa, stid):
        self.__name = name
        self.__age = age
        self.__gpa = gpa
        self.__std = stid
        self.__programs = []
    
    # Getters are name , age, gpa , programs , stid 
    @property
    def name(self):
        return self.__name
        
    @property
    def age(self):
        return self.__age
    
    @property
    def gpa(self):
        return self.__gpa
    
    @property
    def programs(self):
        return self.__programs

    @property
    def stid(self):
        return self.__stid
    
    # Setters the setters are for name , age . gpa , newstid and programs
    
    @name.setter
    def name(self, newname):
        self.__name = newname
        
    @age.setter
    def age(self, newage):
        self.__age = newage

    @gpa.setter
    def gpa(self, newgpa):
        self.__gpa = newgpa
        
    @stid.setter
    def std(self, newstid):
        self.__std = newstid
        
    @programs.setter
    def programs(self, newprograms):
        self.__programs = newprograms


    #First method grade calc where you calculate the grade of the students depending on their GPA  
    def grade_calc(self):
        #if the gpa is between 3.5 and 4 the grade is A 
        if 3.5 <= self.gpa <= 4:
            grade = "A"
        #if the grade is between 3.5 and 2.75 the grade is B
        elif 2.75 <= self.gpa < 3.5:
            grade = "B"
        #if the grade is between 2.26 and 2.75 the grade is C 
        elif 2.26 <= self.gpa < 2.75:
            grade = "C"
        # if the grade is between 2 and 2.25 you receive the grade D 
        elif 2 <= self.gpa < 2.25:
            grade = "D"
        #if you receive a grade lower than 2 you receive a F 
        elif self.gpa < 2:
            grade = "F"
        return grade
    
#the second method is called program pick a program depending on the interest of the student 
    def program_pick(self):
        #while true for a loop to ask their main interest  
        while True:
            #intrest is for students to input their interest either in athletics or in Art 
            interest = input("What interests you the most:\n1. Athletics\n2. Art\n")
            #there are two interest to chose either 1 or 2 
            if interest in ["1", "2"]:
                break
            else:
                #just in case someone chooses another number they will have this message displayed 
                print("\n--Choose between these two.--\n")
        #if they choose 1 it wnter a true loop 
        if interest == "1":
            while True:
                #they offer two programs in athletics wither basketball or football 
                choice = input("We offer these programs in Athletics:\n\n1. Basketball\n2. Football\n")
                #there are 2 options again 1 or 2 
                if choice in ["1", "2"]:
                    break
                #just in case they choose the wrong one they receive a message to chose another number 
                else:
                    print("\n--Choose between these two.--\n")
            #if they chose 1 again that means that they want to play basketball  
            if choice == "1":
                    if "Basketball" in self.__programs:
                        #and we print that they are already enrolled  enrolled in the program 
                        print("\nYou're already enrolled in this program.\n")
                    else:
                        #if this is the first time it will say you are already enrolled 
                        self.__programs.append("Basketball")
                        print("\nYou successfully enrolled.\n")
            #if they choose 2 then they are chocing the option of footbal 
            elif choice == "2":
                    if "Football" in self.__programs:
                        #Then they get to print again that they are already enrolled in the program 
                        print("\nYou're already enrolled in this program.\n")
                    else:
                        #if this is the first time it will say that they are succesfully enrolled 
                        self.__programs.append("Football")
                        print("\nYou successfully enrolled.\n")
        #if they choose 2 is that they are intrested in option 2 through a true loop for art 
        elif interest == "2":
            while True:
                #the two options are painting and music 
                choice = input("We offer these programs in Art:\n\n1. Painting\n2. Music\n")
                #the choices are 1 and 2 
                if choice in ["1", "2"]:
                    break
                else:
                    #print if they didnt choose and option that was available 
                    print("\n--Choose between these two.--\n")
            # if they choose the option 1 then they are intrested in painting 
            if choice == "1":
                #if they are already enrolled to painting then it will print you are already enrolled 
                    if "Painting" in self.__programs:
                        print("\nYou're already enrolled in this program.\n")
                    else:
                        #otherwise it will say that you are enrolled 
                        self.__programs.append("Painting")
                        print("\nYou successfully enrolled.\n")
            # the other option is #2 means that you are choicing music 
            elif choice == "2":
                    if "Music" in self.__programs:
                        #if you already enrolled it will apear that you already have this program 
                        print("\nYou're already enrolled in this program.\n")
                    else:
                        #else you have sucesfully enrolled 
                        self.__programs.append("Music")
                        print("\nYou successfully enrolled.\n")



#this is the main funcition 
def main():
    #first it will salute the student 
    print("Hello Student from UC Santa Cruz. Congratulations on being one of the first five students to enroll")
    print ("To help you use your program please input any nickname you would like us to save in our system and your age") 
    print ("Just remember that you have to input your id exactly as we have it in the system")
    print ("Becouse there only 5 students you can find it here: john12 , ron13, lisa14 and aron15")
    #then it will ask them to enter their name and age 
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    
#a true loop is created to input your student if 
    while True:
        student_id = input("Enter your Student ID: ")
        # if the student id is in the student records then it will be able to display the info 
        if student_id in Student.records:
            break
        else:
            #if not it will print to please iter the correct student id 
            print("\nEnter a correct Student ID.\n")
    gpa = Student.records[student_id]
    
    s1 = Student(name, age, gpa, student_id)
    #while true you can chose what they want to do 
    while True:
        choice = input("Hello Student what do you wish to do ?:\n1. Check your grade\n2. Enroll in a program.")
        #they choose their option either 1 or 2 
        if choice in ["1", "2"]:
            break
        #then they get a answer if they didnt choose from those 2 they receive a message 
        else:
            print("\nChoose between these two.\n")
    #if they choose 1 then it calls the method and and you calculate the grade 
    if choice == "1":
        grade = s1.grade_calc()
        print("Your grade is", grade)
    else:
        #if not it calls the second method 
        s1.program_pick()
    

#closing main 
if __name__ == "__main__":
    main()
