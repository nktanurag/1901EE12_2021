import os
import re
import shutil
os.system("cls")

#making folder structure for all 3 webseries
def make_folder():

	corrected_srt_dir="corrected_srt"
	if not os.path.exists(corrected_srt_dir):
		os.makedirs(corrected_srt_dir)
	series1_path=os.path.join(corrected_srt_dir,"Breaking Bad")
	series2_path=os.path.join(corrected_srt_dir,"Game Of Thrones")
	series3_path=os.path.join(corrected_srt_dir,"Lucifer")

	if not os.path.exists(series1_path):
		os.makedirs(series1_path)
	if not os.path.exists(series2_path):
		os.makedirs(series2_path)
	if not os.path.exists(series3_path):
		os.makedirs(series3_path)

	return




def rename_webseries_BreakingBad(season_padding,episode_padding):
	wrong_dir_path = r"./wrong_srt/Breaking Bad"
	corrected_dir_path = r"./corrected_srt/Breaking Bad/"
	
	for file in os.listdir(wrong_dir_path):
		# arr=file.split(' ')
		arr=re.split(r"\s+",file)
		season_no=arr[2][1:arr[2].index('e')]
		episode_no=arr[2][arr[2].index('e')+1: ]
		# episode_name=arr[2][0:arr[2].index('.')]

		while season_padding > len(season_no):
			season_no='0'+season_no
		
		while episode_padding > len(episode_no):
			episode_no='0'+episode_no
		
		if  (episode_padding < len(episode_no)):
			episode_no = episode_no[-1* episode_padding:]
		
		if  season_padding < len(season_no):
			season_no = season_no[-1*season_padding:]

		if file.endswith(".mp4"):
			new_dest_file_name="Breaking Bad - Season "+season_no+" Episode "+episode_no +".mp4"
			
			if not os.path.exists("./corrected_srt/Breaking Bad/"+new_dest_file_name):
				src_file=os.path.join(wrong_dir_path,file)
				dest_file=shutil.copy(src_file,corrected_dir_path)
				os.rename(corrected_dir_path+file,corrected_dir_path+new_dest_file_name)
			
		if file.endswith(".srt"):
			new_dest_file_name="Breaking Bad - Season "+season_no+" Episode "+episode_no+".srt"
			
			if not os.path.exists("./corrected_srt/Breaking Bad/"+new_dest_file_name):
				src_file=os.path.join(wrong_dir_path,file)
				dest_file=shutil.copy(src_file,corrected_dir_path)
				os.rename(corrected_dir_path+file,corrected_dir_path+new_dest_file_name)
	return

def rename_webseries_GameOfThrones(season_padding,episode_padding):
	wrong_dir_path = r"./wrong_srt/Game Of Thrones"
	corrected_dir_path = r"./corrected_srt/Game Of Thrones/"
	
	for file in os.listdir(wrong_dir_path):
		# arr=file.split(' - ')
		arr=re.split(" - ",file)
		season_no=arr[1][0:arr[1].index('x')]
		episode_no=arr[1][arr[1].index('x')+1: ]
		episode_name=arr[2][0:arr[2].index('.')]

		while season_padding > len(season_no):
			season_no='0'+season_no
		while episode_padding > len(episode_no):
			episode_no='0'+episode_no

		if  (episode_padding < len(episode_no)):
			episode_no = episode_no[-1* episode_padding:]
		
		if  season_padding < len(season_no):
			season_no = season_no[-1*season_padding:]
		
		if file.endswith(".mp4"):
			new_dest_file_name="Game of Thrones - Season "+season_no+" Episode "+episode_no+" - "+episode_name+".mp4"

			if not os.path.exists("./corrected_srt/Game of Thrones/"+new_dest_file_name):
				src_file=os.path.join(wrong_dir_path,file)
				dest_file=shutil.copy(src_file,corrected_dir_path)
				os.rename(corrected_dir_path+file,corrected_dir_path+new_dest_file_name)
			
		if file.endswith(".srt"):
			new_dest_file_name="Game of Thrones - Season "+season_no+" Episode "+episode_no+" - "+episode_name+".srt"

			if not os.path.exists("./corrected_srt/Game of Thrones/"+new_dest_file_name):
				src_file=os.path.join(wrong_dir_path,file)
				dest_file=shutil.copy(src_file,corrected_dir_path)
				os.rename(corrected_dir_path+file,corrected_dir_path+new_dest_file_name)
	return




def rename_webseries_Lucifier(season_padding,episode_padding):
	wrong_dir_path = r"./wrong_srt/Lucifer"
	corrected_dir_path = r"./corrected_srt/Lucifer/"
	
	for file in os.listdir(wrong_dir_path):
		# arr=file.split(' - ')
		arr=re.split(" - ",file)
		season_no=arr[1][0:arr[1].index('x')]
		episode_no=arr[1][arr[1].index('x')+1: ]
		episode_name=arr[2][0:arr[2].index('.')]

		while season_padding > len(season_no):
			season_no='0'+season_no
		while episode_padding > len(episode_no):
			episode_no='0'+episode_no

		if  (episode_padding < len(episode_no)):
			episode_no = episode_no[-1* episode_padding:]
		
		if  season_padding < len(season_no):
			season_no = season_no[-1*season_padding:]
		
		if file.endswith(".mp4"):
			new_dest_file_name="Lucifer - Season "+season_no+" Episode "+episode_no+" - "+episode_name+".mp4"
			
			if not os.path.exists("./corrected_srt/Lucifer/"+new_dest_file_name):
				src_file=os.path.join(wrong_dir_path,file)
				dest_file=shutil.copy(src_file,corrected_dir_path)
				os.rename(corrected_dir_path+file,corrected_dir_path+new_dest_file_name)
			
		if file.endswith(".srt"):
			new_dest_file_name="Lucifer - Season "+season_no+" Episode "+episode_no+" - "+episode_name+".srt"
			
			if not os.path.exists("./corrected_srt/Lucifer/"+new_dest_file_name):
				src_file=os.path.join(wrong_dir_path,file)
				dest_file=shutil.copy(src_file,corrected_dir_path)
				os.rename(corrected_dir_path+file,corrected_dir_path+new_dest_file_name)
	return






def regex_renamer():

	# Taking input from the user

	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")

	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))

	#making folder structure for all 3 webseries
	make_folder()

	if (webseries_num==1):
		rename_webseries_BreakingBad(season_padding,episode_padding)
	elif (webseries_num==2):
		rename_webseries_GameOfThrones(season_padding,episode_padding)
	elif (webseries_num==3):
		rename_webseries_Lucifier(season_padding,episode_padding)
	else:
		print("WebSeries Not Available, try again !")



regex_renamer()