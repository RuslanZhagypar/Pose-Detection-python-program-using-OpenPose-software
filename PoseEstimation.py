
import csv  # a library to read csv files
from statistics import mean # a library to find the mean value
from moviepy.editor import VideoFileClip
fields = [] # To store the headings of each column in a .csv file;
rows = []	# to store all the rows of a file
xarr = []	# to store x coordinate of each point
yarr = []	# to store y coordinate of each point
carr = []	# to store confidence index of each point

clip = VideoFileClip("VideoSample.mp4")
length_of_video = clip.duration # determining the length of the video

filename = "VideoSample.csv"
with open(filename, 'r') as csvfile: 
	csvVar = csv.reader(csvfile)	# creating a csv reader object 
	fields = next(csvVar)
	for row in csvVar: 			# extracting each data row one by one 
		rows.append(row) 
  
    # get total number of rows 
	print("Total no. of rows: %d"%(csvVar.line_num)) 

sec_per_frame = length_of_video / (csvVar.line_num-1)# calculating sec/frame for determining the total time for each pose 

prev_state		=0 		# the value of 0 means no pose;

happy_count		=0		# to count the occurence of HAPPY pose
surprise_count	=0		# to count the occurence of SURPRISE pose
sad_count		=0		# to count the occurence of SAD pose
garbage_count	=0		# to count the occurence of GARBAGE pose

total_happy		=0		# total number of frames will be recorder independently of previous state;
total_surprise	=0
total_sad		=0
total_garbage	=0
	
dur_happy		=0		# durations for each emotion represent the number of successive frames/rows showing the same emotion;
dur_surprise	=0
dur_sad			=0
dur_garbade		=0

DURATION=6			# the emotion will get recognized only if DURATION number of successive frames show the same emotion;

for row in rows[:csvVar.line_num]: # A loop to iterate through all the rows/frames
	col_count = 0		# simple int counter for column indexing					
	for col in row: 				# A loop to iterate through all columns in a row / frame;
		if 'x' in fields[col_count]:	# if the corresponding column number represents x coordinates, the value at this row and column will get parsed in "xarr" list ;
			xarr.append(col)  		
		if 'y' in fields[col_count]:	# if the corresponding column number represents y coordinates, the value at this row and column will get parsed in "yarr" list ;
			yarr.append(col)  
		if 'c' in fields[col_count]:	# if the corresponding column number represents index of confidence, the value at this row and column will get parsed in "carr" list ;
			carr.append(col)  	
		col_count = col_count+1

	carr_int = [float(i) for i in carr] # converting all string values in the carr list into float numbers
	th = mean(carr_int)					# for calculating the mean value of confidence;

	#Condition for HAPPY pose
	if ((yarr[4]<yarr[0] and yarr[7]<yarr[0]) and carr[4]>str(th) and carr[7]>str(th) and carr[0]>str(th)): # the conditions will be satisfied only if the confidences are higher than the mean
		if dur_happy ==DURATION: #count until DURATION number of rows/frames show HAPPY pose															   					 				
			if prev_state==1:	 # checks if the previous state was HAPPY state (prev_state = 1)
				total_happy=total_happy+1	# if the previous state was HAPPY, there is no need to count it as new pose, just add to total happy time;
			else:							
				happy_count= happy_count+1	# if the previous state was NOT HAPPY, then increment the HAPPY counter
				total_happy=total_happy+6	# and add it to total happy time;
				prev_state=1				# now update the previous state to HAPPY;
		else:
			dur_happy=dur_happy+1			# Increment until the dur_happy reaches the DURATION;

	else:									# If a row does not show HAPPY,
		dur_happy=0							# then the duration counter of successive HAPPY frames is interupted; so, set it back to zero;
		#Condition for SURPRISE pose
		if (((yarr[4]<yarr[1] and yarr[4]>yarr[0] and xarr[4]>xarr[2] and xarr[7]<xarr[5])  ) and  carr[4]>str(th) and carr[7]>str(th) and  carr[5]>str(th) and carr[6]>str(th)): 
			if dur_surprise==DURATION:
				if prev_state==2:
					total_surprise=total_surprise+1
				else:
					surprise_count=surprise_count+1
					total_surprise=total_surprise+6
					prev_state=2
			else:
				dur_surprise=dur_surprise+1
		else:
			dur_surprise=0
			#Condition for SAD pose
			if ((yarr[15] > yarr[16] and xarr[4]>xarr[9] and xarr[7]<xarr[12]) and carr[4]>str(th) and carr[7]>str(th) and carr[0]>str(th) and carr[1]>str(th) and carr[16]>str(th)): 
				if dur_sad==DURATION:
					if prev_state==3:
						total_sad=total_sad+1
					else:
						sad_count=sad_count+1
						total_sad=total_sad+6
						prev_state=3
				else:
					dur_sad=dur_sad+1;
			else:
				dur_sad=0
				#Condition for DISGUST/Garbage pose
				if (xarr[4]>xarr[1] and xarr[7]>xarr[5] and yarr[7]>yarr[0] and carr[4]>str(th) and carr[7]>str(th) and carr[1]>str(th) and carr[5]>str(th)): 
					if dur_garbade==DURATION:

						if prev_state==4:
							total_garbage=total_garbage+1
							prev_state=4
						else:
							garbage_count=garbage_count+1
							total_garbage=total_garbage+6
							prev_state=4
					else:
						dur_garbade=dur_garbade+1;		
				else:
					dur_garbade=0
					prev_state=0	# if no condition was satisfied (i.e. no pose was detected), then previous state remains as zero (no state)


	xarr.clear()	# the lists containing x, y and confidence values are cleared after each row/frame
	yarr.clear()
	carr.clear()

print("Total number of happy moments: ",happy_count,' \n')
print("Time the user was in the happy state: ",round(total_happy*sec_per_frame,2),'sec \n')
print("Total number of surprise moments: ",surprise_count,' \n')
print("Time the user was in the surprise state: ",round(total_surprise*sec_per_frame,2),'sec \n')
print("Total number of sad moments: ",sad_count,' \n')
print("Time the user was in the sad state: ",round(total_sad*sec_per_frame,2),'sec \n')

print("Total number of garbade moments: ",garbage_count,' \n')
print("Time the user was in the garbade state: ",round(total_garbage*sec_per_frame,2),'sec \n')

