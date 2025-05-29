#成绩获取（Excel）【2.1加入】
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