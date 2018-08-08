########################################################################
#   LAB_06____6-6-2018
#       Takes a text file with student exam scores and 
#       returns the student's exams in alphabetical order,
#       exam average for each exam, and the total exam average
#       for a student.
########################################################################

scores_file = open("scores.txt","r")        #opens text file with scores
print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format(\
      "Name","Exam1","Exam2","Exam3","Exam4","Mean"))
      
def get_mean(exam_scores_list):
    '''returns average of list of ints'''
    exam_scores = []
    for exam in exam_scores_list:
        exam_scores.append(int(exam))
    mean = sum(exam_scores)/len(exam_scores)
    
    return(mean)


def number_exams(exam_scores_list):
    '''converts string exam scores to int'''
    exam1 = int(exam_scores_list[0])
    exam2 = int(exam_scores_list[1])
    exam3 = int(exam_scores_list[2])
    exam4 = int(exam_scores_list[3])
      
    return(exam1,exam2,exam3,exam4)

lines = scores_file.readlines()
lines.sort()

exam1_scores = []
exam2_scores = []
exam3_scores = []
exam4_scores = []

for item in lines:
    
    item.replace("\n","")   #sorting the line creates '\n' chars, removing 
                            #for calulations
    name = item[:20]
    total_exam_scores = item[20:].split()
    
    exam1_scores.append(total_exam_scores[0])
    exam2_scores.append(total_exam_scores[1])
    exam3_scores.append(total_exam_scores[2])
    exam4_scores.append(total_exam_scores[3])
            
    
    exam1_mean = get_mean(exam1_scores)
    exam2_mean = get_mean(exam2_scores)
    exam3_mean = get_mean(exam3_scores)
    exam4_mean = get_mean(exam4_scores)
    total_mean = get_mean(total_exam_scores)
        #returns all the mean values needed
    
    exam1,exam2,exam3,exam4 = number_exams(total_exam_scores)
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(\
          name,exam1,exam2,exam3,exam4,total_mean))
print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format(\
      "Exam Mean",exam1_mean,exam2_mean,exam3_mean,exam4_mean))
      
      
      
      