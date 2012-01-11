import sys
import csv
import os
import xml.dom.minidom as minidom
from xml.dom.minidom import Document

class CSV(object):
    def __init__(self):
        pass

    def parse_csv(self, filename):
        """
        This function takes in as a parameter the filename which it opens with
        the csv reader and parses the csv data that is in the file row by row 
        and creates a dicitionary (data_dict) and returns a list of dictionaries (data_dict_list)
        """
        data = csv.reader(open(filename, 'r'))
        data_dict_list = []
        for row in data:
            if row:
                data_dict = {
                                'classroom_id': row[0].strip(), 
                                'classroom_name': row[1].strip(), 
                                'teacher_1_id': row[2].strip(), 
                                'teacher_1_lastname': row[3].strip(), 
                                'teacher_1_firstname': row[4].strip(), 
                                'teacher_2_id': row[5].strip(), 
                                'teacher_2_last_name': row[6].strip(), 
                                'teacher_2_first_name': row[7].strip(),
                                'student_id':row[8].strip(),
                                'student_last_name': row[9].strip(), 
                                'student_first_name':row[10].strip(), 
                                'student_grade':row[11].strip(),
                            }
 
                data_dict_list.append(data_dict)
        return data_dict_list
    
    def write_csv(self,data_dict_list, output_file):
        """
        This function takes in as parameters the list of dictionaries(data_dict_list) 
        and the file name we want to write to without the extension where then a file 
        is opened for writing the data to be written to in the csv schema, then we 
        write each row for the csv file using each dictionary from the list of dicts.
        """
        writer = csv.writer(open(output_file + '.csv', 'wb'))
        for data_dict in data_dict_list:
            writer.writerow([
                                data_dict['classroom_id'], 
                                data_dict['classroom_name'], 
                                data_dict['teacher_1_id'], 
                                data_dict['teacher_1_lastname'],
                                data_dict['teacher_1_firstname'],
                                data_dict['teacher_2_id'],
                                data_dict['teacher_2_last_name'], 
                                data_dict['teacher_2_first_name'], 
                                data_dict['student_id'], 
                                data_dict['student_last_name'] , 
                                data_dict['student_first_name'], 
                                data_dict['student_grade']
                           ])


class XML(object):
    def __init__(self):
        pass
    
    def parse_xml(self, filename):
        """
        This function takes as parameter the filename and the xml.dom.mindiom module is
        used to parse the xml file the xml is traversed recursively until the lowest level
        is reached of students where then the dictionary is created and it is appended to
        the list of dictionaries once finished the list of dicts (data_dict_list) is 
        returned
        """
        data_dict_list = []
        doc = minidom.parse(filename)
        node = doc.documentElement
        schools = doc.getElementsByTagName("school")
        for school in schools:
            grades = school.getElementsByTagName("grade")
            
            for grade in grades:
                classrooms = grade.getElementsByTagName("classroom")
                student_grade = grade.getAttribute("id")
                for classroom in classrooms:
                    classroom_id = classroom.getAttribute("id")    
                    classroom_name = classroom.getAttribute("name")
                    teachers = classroom.getElementsByTagName("teacher")
                    
                    """This condition statement checks to see if there is either 2 teachers at most or 1 teacher at very least"""
                    if len(teachers) == 2:
                        teacher1 = teachers[0]
                        teacher_1_id = teacher1.getAttribute("id")
                        teacher_1_last_name = teacher1.getAttribute("last_name")
                        teacher_1_first_name = teacher1.getAttribute("first_name")
                        teacher2 = teachers[1]
                        teacher_2_id = teacher2.getAttribute("id")
                        teacher_2_last_name = teacher2.getAttribute("last_name")
                        teacher_2_first_name = teacher2.getAttribute("first_name")
                        students = classroom.getElementsByTagName("student")
                        if students:

                            for student in students:
                                student_id = student.getAttribute("id")
                                student_last_name = student.getAttribute("last_name")
                                student_first_name = student.getAttribute("first_name")
                                data_dict =     {
                                                'classroom_id': classroom_id , 
                                                'classroom_name': classroom_name, 
                                                'teacher_1_id': teacher_1_id, 
                                                'teacher_1_lastname': teacher_1_last_name, 
                                                'teacher_1_firstname': teacher_1_first_name, 
                                                'teacher_2_id': teacher_2_id, 
                                                'teacher_2_last_name': teacher_2_last_name, 
                                                'teacher_2_first_name': teacher_2_first_name,
                                                'student_id':student_id,
                                                'student_last_name': student_last_name, 
                                                'student_first_name': student_first_name, 
                                                'student_grade': student_grade,
                                                } 
                                data_dict_list.append(data_dict)
                        else:
                            student_id = ""
                            student_last_name = ""
                            student_first_name = ""
                            data_dict =     {
                                            'classroom_id': classroom_id , 
                                            'classroom_name': classroom_name, 
                                            'teacher_1_id': teacher_1_id, 
                                            'teacher_1_lastname': teacher_1_last_name, 
                                            'teacher_1_firstname': teacher_1_first_name, 
                                            'teacher_2_id': teacher_2_id, 
                                            'teacher_2_last_name': teacher_2_last_name, 
                                            'teacher_2_first_name': teacher_2_first_name,
                                            'student_id':student_id,
                                            'student_last_name': student_last_name, 
                                            'student_first_name': student_first_name, 
                                            'student_grade': student_grade,
                                            } 
                            data_dict_list.append(data_dict)
                    else:
                        teacher1 = teachers[0]
                        teacher_1_id = teacher1.getAttribute("id")
                        teacher_1_last_name = teacher1.getAttribute("last_name")
                        teacher_1_first_name = teacher1.getAttribute("first_name")
                        teacher_2_id = ""
                        teacher_2_last_name = ""
                        teacher_2_first_name = ""
                        students = classroom.getElementsByTagName("student")
                        if students:
                            
                            for student in students:
                                student_id = student.getAttribute("id")
                                student_last_name = student.getAttribute("last_name")
                                student_first_name = student.getAttribute("first_name")
                                data_dict =     {
                                                'classroom_id': classroom_id , 
                                                'classroom_name': classroom_name, 
                                                'teacher_1_id': teacher_1_id, 
                                                'teacher_1_lastname': teacher_1_last_name, 
                                                'teacher_1_firstname': teacher_1_first_name, 
                                                'teacher_2_id': teacher_2_id, 
                                                'teacher_2_last_name': teacher_2_last_name, 
                                                'teacher_2_first_name': teacher_2_first_name,
                                                'student_id':student_id,
                                                'student_last_name': student_last_name, 
                                                'student_first_name': student_first_name, 
                                                'student_grade': student_grade,
                                                } 
                                data_dict_list.append(data_dict)
                        else:
                            student_id = ""
                            student_last_name = ""
                            student_first_name = ""
                            data_dict =     {
                                            'classroom_id': classroom_id , 
                                            'classroom_name': classroom_name, 
                                            'teacher_1_id': teacher_1_id, 
                                            'teacher_1_lastname': teacher_1_last_name, 
                                            'teacher_1_firstname': teacher_1_first_name, 
                                            'teacher_2_id': teacher_2_id, 
                                            'teacher_2_last_name': teacher_2_last_name, 
                                            'teacher_2_first_name': teacher_2_first_name,
                                            'student_id':student_id,
                                            'student_last_name': student_last_name, 
                                            'student_first_name': student_first_name, 
                                            'student_grade': student_grade
                                            } 
                            data_dict_list.append(data_dict)
        return data_dict_list        
        
            
    def write_xml(self,data_dict_list,output_file):
        """
        This function takes in as parameter the list of dictionaries(data_dict_list 
        and the output file name without the extension, first we set the id, name
        and xmlns of the school and then we traverse the list of dicts (data_dict_list)
        dictionary by dictionary and create the elements and attributes of the xml 
        we check if the element tag was created, otherwise we created and set the 
        set the attribute to the element and we do this for every element of the xml,
        and finally we write our doc to a output file (out_file) using the name passed
        in (output_file) plus the extension 'xml'.
        """
        doc = Document()
        school = doc.createElement("school")
        school.setAttribute("id" , "100")
        school.setAttribute("name" , "WGen School")
        school.setAttribute("xmlns" , "http://www.wirelessgeneration.com/wgen.xsd")
        doc.appendChild(school)
        for data_dict in data_dict_list:
            current_grade = None
            current_classroom_id = None
            current_teacher_id = None
            current_teacher2_id = None
            current_student_id = None
            grades = school.getElementsByTagName("grade")
            if grades:
                for grade in grades:
                    if grade.getAttribute("id") == data_dict['student_grade']:
                        current_grade = grade
            if not current_grade:
                current_grade = doc.createElement("grade")
                current_grade.setAttribute("id", data_dict['student_grade'])
                school.appendChild(current_grade)
                
            classrooms = current_grade.getElementsByTagName("classroom")
            if classrooms:
                for classroom in classrooms:
                    if classroom.getAttribute("id") == data_dict['classroom_id']:
                        current_classroom_id = classroom
            if not current_classroom_id:
                current_classroom_id = doc.createElement("classroom")
                current_classroom_id.setAttribute("id", data_dict['classroom_id'])
                current_classroom_id.setAttribute("name" , data_dict['classroom_name'])                           
                current_grade.appendChild(current_classroom_id)
                
            teachers = current_classroom_id.getElementsByTagName("teacher")
            if teachers:
                for teacher in teachers:
                    if teacher.getAttribute("id") == data_dict['teacher_1_id']:
                        current_teacher_id = teacher
            if not current_teacher_id:
                current_teacher_id = doc.createElement("teacher")
                current_teacher_id.setAttribute("id", data_dict['teacher_1_id'])
                current_teacher_id.setAttribute("first_name", data_dict['teacher_1_firstname'])
                current_teacher_id.setAttribute("last_name", data_dict['teacher_1_lastname'])
                current_classroom_id.appendChild(current_teacher_id)

            """Checking to see if there is a second teacher"""
            if data_dict['teacher_2_id']:
                teachers = current_classroom_id.getElementsByTagName("teacher")
                if teachers:
                    for teacher in teachers:
                        if teacher.getAttribute("id") == data_dict['teacher_2_id']:
                            current_teacher2_id = teacher
                if not current_teacher2_id:
                    current_teacher2_id = doc.createElement("teacher")
                    current_teacher2_id.setAttribute("id", data_dict['teacher_2_id'])
                    current_teacher2_id.setAttribute("first_name", data_dict['teacher_2_first_name'])
                    current_teacher2_id.setAttribute("last_name", data_dict['teacher_2_last_name'])
                    current_classroom_id.appendChild(current_teacher2_id)
            
            if data_dict['student_id']:
                students = current_classroom_id.getElementsByTagName("student")
                if students:
                    for student in students:
                        if student.getAttribute("id") == data_dict['student_id']:
                            current_student_id = student
                if not current_student_id:
                    current_student_id = doc.createElement("student")
                    current_student_id.setAttribute("id", data_dict['student_id'])
                    current_student_id.setAttribute("first_name", data_dict['student_first_name']) 
                    current_student_id.setAttribute("last_name", data_dict['student_last_name'])
                    current_classroom_id.appendChild(current_student_id)
                
        out_file = open(output_file + ".xml" , "w")
        out_file.write(doc.toprettyxml(indent="  "))
        out_file.close()


def main():
    if len(sys.argv) < 3:
        print "Please follow program running scheme is incorrect"
        exit(0)
    filename = sys.argv[1]
    types = sys.argv[2].split('2')
    read_type = types[0][1:]
    write_type = types[1]

    if read_type == "csv" and (filename[-3:] == "csv" or filename[-3:] == "txt"):
        x = CSV()
        result = x.parse_csv(filename)
    elif read_type == "xml" and filename[-3:] == "xml":
        x = XML()
        result = x.parse_xml(filename)
    else:
        print "Not a valid format, try again, (input formats have to match)"
        exit(0)
        
    output_file = raw_input("Type the path of the output file without extension: ")
    
    if write_type == "csv":
        y = CSV()
        y.write_csv(result,output_file)
    elif write_type == "xml":
        y = XML()
        y.write_xml(result, output_file)
    else:
        print "No other valid output format for this file at the moment only csv or xml"

if __name__ == "__main__":
    main()
