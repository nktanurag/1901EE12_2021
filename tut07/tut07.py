import os
import csv
import os.path

import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook

os.system("cls")

def feedback_not_submitted():

	#storing file addresses for each csv file
	student_info_file="studentinfo.csv"
	course_info_file="course_master_dont_open_in_excel.csv"
	course_registered_file="course_registered_by_all_students.csv"
	course_feedback_file="course_feedback_submitted_by_students.csv"
	
	ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3:'practical'}
	output_file_name = "course_feedback_remaining.xlsx" 
	if os.path.isfile(output_file_name):
		return
	
	#student_info[roll]=[name,email,email,contactno]
	student_info={}
	with open(student_info_file,'r') as file:
		reader=csv.reader(file)
		counter=0
		for row in reader:
			counter+=1
			if(counter==1):
				continue
			student_info[row[1]]=[row[0],row[8],row[9],row[10]]
	
	#courses_info[course code]=[L,T,P]
	course_info={}
	with open(course_info_file,'r') as file:
		reader=csv.reader(file)
		counter=0
		for row in reader:
			counter+=1
			if(counter==1):
				continue
			LTP_list=row[2].split('-')
			course_info[row[0]]=LTP_list

	#student_course_registered[roll]=[ [reg_sem1,sch_sem1,coursecode1,L1,T1,P1],[reg_sem2,sch_sem2,coursecode2,L2,T2,P2],[reg_sem_nth,sch_sem_nth,coursecode_nth,L2_nth,T2_nth,P2_nth] ]
	student_course_registered={}
	with open(course_registered_file,'r') as file:
		reader=csv.reader(file)
		header=[]
		counter=0
		for row in reader:
			counter+=1
			if counter<=1:
				continue
			#3 zero/one indicate boolean type feedback submitted/not_submitted for L,T,P respectively 
			if row[0] in student_course_registered:
				student_course_registered[row[0]].append([row[1],row[2],row[3],0,0,0])
			else:
				student_course_registered[row[0]]=[]
				student_course_registered[row[0]].append([row[1],row[2],row[3],0,0,0])

	#now traverse the course_feedback_file and mark the course (L,T,P) in which feedback given as "1"
	with open(course_feedback_file,'r') as file:
		reader=csv.reader(file)
		header=[]
		counter=0
		for row in reader:
			counter+=1
			if counter<=1:
				continue
			course_code=row[4]
			roll_no=row[3]
			feedback_type=int(row[5])
			if roll_no in student_course_registered:
				for r in student_course_registered[roll_no]:
					#marking feedback as submitted
					if course_code == r[2]:
						r[2+feedback_type]=1

	#now traverse the student_course_registered again and check about the course for all rollno in which feedback not given
	wb=Workbook()
	sheet=wb.active
	sheet.append(["rollno","register_sem","schedule_sem","subno","Name","email","aemail","contact"])
	for rollno,courses in student_course_registered.items():
		for course_list_info in courses:

			register_sem=course_list_info[0]
			schedule_sem=course_list_info[1]
			course_code=course_list_info[2]

			
			L_status=course_list_info[3]
			T_status=course_list_info[4]
			P_status=course_list_info[5]

			if not course_code in course_info:
				continue
			#Logic for feedback not submission- if anyone of L,T,P is required for a course and its feedback not taken and it has to be present in output file
			if (course_info[course_code][0]!="0" and L_status==0) or (course_info[course_code][1]!="0" and T_status==0) or (course_info[course_code][2]!="0" and P_status==0) :
				stud_name=""
				email=""
				aemail=""
				contact=""
				if not rollno in student_info:
					stud_name="NA_IN_STUDENTINFO"
					email="NA_IN_STUDENTINFO"
					aemail="NA_IN_STUDENTINFO"
					contact="NA_IN_STUDENTINFO"
				else:
					stud_name=student_info[rollno][0]
					email=student_info[rollno][1]
					aemail=student_info[rollno][2]
					contact=student_info[rollno][3]
				sheet.append([rollno,register_sem,schedule_sem,course_code,stud_name,email,aemail,contact])
	wb.save(output_file_name)
	#end of	function ->def feedback_not_submitted():


#task
feedback_not_submitted()
