import os
import os.path
os.system("cls")

def output_by_subject(csv_file):
    DIRECTORY = "output_by_subject"
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    with open(csv_file,'r') as f:
        head_line=""
        counter=0
        for line in f:
            counter+=1
            if counter==1:
                head_list=line.split(',')
                header=[head_list[0],head_list[1],head_list[3],head_list[8]]
                
                for word in header:
                    head_line+=word
                    head_line+=","
                head_line=head_line[:-1]
                continue
            else:
                word_list=line.split(',')
                words=[word_list[0],word_list[1],word_list[3],word_list[8]]

                new_line=""
                for word in words:
                    new_line+=word
                    new_line+=","
                new_line=new_line[:-1]

                course_path = os.path.join(DIRECTORY, words[2]+".csv")  
                if os.path.isfile(course_path):
                    roll_file=open(course_path,'a')
                    roll_file.write(new_line)
                    roll_file.close()
                else:  
                    roll_file=open(course_path,'w')
                    roll_file.write(head_line)
                    roll_file.write(new_line)
                    roll_file.close()
    return

def output_individual_roll(csv_file):
    DIRECTORY = "output_individual_roll"
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    with open(csv_file,'r') as f:
        head_line=""
        counter=0
        for line in f:
            counter+=1
            if counter==1:
                head_list=line.split(',')
                header=[head_list[0],head_list[1],head_list[3],head_list[8]]
                
                for word in header:
                    head_line+=word
                    head_line+=","
                head_line=head_line[:-1]
                continue
            else:
                word_list=line.split(',')
                words=[word_list[0],word_list[1],word_list[3],word_list[8]]

                new_line=""
                for word in words:
                    new_line+=word
                    new_line+=","
                new_line=new_line[:-1]

                roll_path = os.path.join(DIRECTORY, words[0]+".csv")  
                if os.path.isfile(roll_path):
                    roll_file=open(roll_path,'a')
                    roll_file.write(new_line)
                    roll_file.close()
                else:  
                    roll_file=open(roll_path,'w')
                    roll_file.write(head_line)
                    roll_file.write(new_line)
                    roll_file.close()

    return



csv_file="regtable_old.csv"

#task1
output_individual_roll(csv_file)

#task2
output_by_subject(csv_file)


