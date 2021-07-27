import csv
  
def write_into_csv(info_list):
    with open("studentinfo.csv", 'a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        
        #condition to add the following only once when the list is empty 
        if csv_file.tell()==0:                                  
          writer.writerow(["Name","Age","Contact no","Email id"])
        writer.writerow(info_list)


if __name__=="__main__":
  condition = True
  Studentno = 1
  
  
  while(condition):
       studentinfo=input("\nEnter the information for Student{} in the following format (Name,Age,ContactNo,E-mail id):".format(Studentno))
      
      #split function       
       studentinfo_list=studentinfo.split(' ')

       print("\nEntered student information is: \n Name:{}\n Age:{}\n ContactNo:{}\n E-mail id:{}"
             .format (studentinfo_list[0],studentinfo_list[1],studentinfo_list[2],studentinfo_list[3] ))
    
     
      
       con_check=input("Is the information given is right ? (yes/no):")
       if con_check =="yes":
          write_into_csv(studentinfo_list)
          
          check=input("Enter (yes/no) whether you want to add more students information: ")
          if check == "yes":
            condition = True
            Studentno = Studentno + 1
          elif check== "no":
            condition = False  
     
       elif con_check == "no":
            print("Re-enter the information")
                

