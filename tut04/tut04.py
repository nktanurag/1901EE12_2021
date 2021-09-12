import csv
import os
import os.path
os.system("cls")

def output_by_subject(csv_file):
    DIRECTORY = "output_by_subject"

    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    with open(csv_file,'r') as file:
        reader=csv.reader(file)
    
        counter=0
        header=[]
        for row in reader:
            counter+=1
            if counter==1:
                header=row
            else:
                course_path = os.path.join(DIRECTORY, row[3]+".csv")   
                #appending the new Row to its course file path
                if os.path.isfile(course_path):
                    with open(course_path,'a',newline='')as file:
                        writer=csv.writer(file)
                        writer.writerow([row[0],row[1],row[3],row[8]])
                #creating a file with the course code and writing header row and new row
                else:
                    with open(course_path,'w',newline='')as file:
                        writer=csv.writer(file)
                        writer.writerow([header[0],header[1],header[3],header[8]])
                        writer.writerow([row[0],row[1],row[3],row[8]])
        
    return

def output_individual_roll(csv_file):
    DIRECTORY = "output_individual_roll"

    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    with open(csv_file,'r') as file:
        reader=csv.reader(file)
    
        counter=0
        header=[]
        for row in reader:
            counter+=1
            if counter==1:
                header=row
            else:
                roll_path = os.path.join(DIRECTORY, row[0]+".csv")   
                #appending the new Row to its roll path
                if os.path.isfile(roll_path):
                    with open(roll_path,'a',newline='')as file:
                        writer=csv.writer(file)
                        writer.writerow([row[0],row[1],row[3],row[8]])           
                #creating a file with the roll code and writing header row and new row
                else:
                    with open(roll_path,'w',newline='')as file:
                        writer=csv.writer(file)
                        writer.writerow([header[0],header[1],header[3],header[8]])
                        writer.writerow([row[0],row[1],row[3],row[8]])
    return


csv_file="regtable_old.csv"

#task1
output_individual_roll(csv_file)

#task2
output_by_subject(csv_file)