import xlrd

#函数定义
def Data_get(path):
    #打开Excel文件
    data = xlrd.open_workbook(path)

    #获取工作表-sheet1
    table = data.sheets()[0]
    
    #课程计数
    name_list = table.col_values(1)
    course_number = len(name_list)-2

    #课程列表
    course_list = table.col_values(1)[2:course_number+2]

    #课程成绩
    course_grade = table.col_values(2)[2:course_number+2]

    #课程学分
    course_point = table.col_values(3)[2:course_number+2]
    return course_number,course_list,course_grade,course_point

#路径获取
path = input("请给出成绩文件路径(！！请确保路径及文件内格式正确)")

#函数调用
data = Data_get(path)

#数据获取
course_number = data[0]
course_list = data[1]
course_grade = data[2]
course_point = data[3]

