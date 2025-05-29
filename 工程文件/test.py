def Grade_input_and_out_put():
    
    #路径获取
    path = input("请拖入成绩文件，并回车确定")
    
    #成绩获取
    data = Data_get(path)
    
    #数据获取
    course_num = data[0]
    course_list = data[1]
    course_grade = data[2]
    course_point = data[3]

    #课程输出|排版不够整齐|改喽！(现在使用全角空格解决中英文字符大小不一致的问题，希望后续用动态算法解决^-^)
    print("课程信息如下：")
    for i in range(course_num):
        print("{:\u3000^10} | {:2} | {:^3}".format(course_list[i],course_grade[i],course_point[i]))
    boor = input("请确认课程(有误请输入“1”，无误直接回车)")

    #返回值
    return boor,course_num,course_list,course_grade,course_point

data = Grade_input_and_out_put()

boor = data[0]
while boor != "":
    data = Grade_input_and_out_put()
    boor = data[0]

#数据输出
course_num = data[1]
course_list = data[2]
course_grade = data[3]
course_point = data[4]