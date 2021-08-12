
import pickle
import json
import send

with open("absent_students.pickle", 'rb') as f_3:
    data1 = pickle.load(f_3)
with open("present_students.pickle", 'rb') as f_3:
    data2 = pickle.load(f_3)					
with open("info.json") as all_students:
	all_students_dict = json.load(all_students)

present_studs_with_names = []
for present_student in data2:
	present_studs_with_names.append((present_student, all_students_dict[str(present_student)],"present"))
	
absent_studs_with_names = []
for absent_students in data1:
	absent_studs_with_names.append((absent_students, all_students_dict[str(absent_students)],"absent"))


all_students_presenty_status = present_studs_with_names+absent_studs_with_names
# print(len(all_students_presenty_status))

with open("all_students_presenty_status.pickle",'wb') as f:
	pickle.dump(all_students_presenty_status,f)




with open("all_students_presenty_status.pickle",'rb') as f:
	all_students_presenty_status = pickle.load(f)


for roll,name,status in all_students_presenty_status:
	print(roll,"\t",name,"\t",status)