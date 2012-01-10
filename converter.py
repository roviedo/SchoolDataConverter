import sys
import csv
import os

class CSV(object):
    def __init__(self):
        pass

    def parse_csv(self, filename):
        data = csv.reader(open(filename, 'r'))
        data_dict_list = []
        for x in data:
            if x:
                data_dict = {'classroom_id': x[0] , 'classroom_name': x[1], 'teacher_1_id': x[2], 'teacher_1_lastname': x[3], 'teacher_1_firstname': x[4], 'teacher_2_id': x[5], 'teacher_2_last_name': x[6], 'teacher_2_first_name': x[7],'student_id':x[8],'student_last_name': x[9], 'student_first_name':x[10], 'student_grade':x[11]} 
                data_dict_list.append(data_dict)
        return data_dict_list
    
    def write_csv(self,data, filenameWOext):
        writer = csv.writer(open(filenameWOext + '.csv', 'wb'))
        for x in data:
            writer.writerow([x['classroom_id'], x['classroom_name'], x['teacher_1_id'], x['teacher_1_lastname'],x['teacher_1_firstname'],x['teacher_2_id'],x['teacher_2_last_name'], x['teacher_2_first_name'], x['student_id'], x['student_last_name'] , x['student_first_name'], x['student_grade']])
        print writer

def main():
    pass
    if len(sys.argv) < 3:
        print "Please follow program running scheme is incorrect"
        exit(0)
    filename = sys.argv[1]
    types = sys.argv[2].split('2')
    read_type = types[0][1:]
    write_type = types[1]
    if read_type == "csv":
        x = CSV()
        result = x.parse_csv(filename)
    else:
        print "Not a valid format"
    if write_type == "csv":
        y = CSV()
        filenameWOext, fileExt = os.path.splitext(filename)
        y.write_csv(result, filenameWOext)
    else:
        print "No other valid format for this file"
if __name__ == "__main__":
    main()
