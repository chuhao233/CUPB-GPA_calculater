#本程序用于计算2024级本科生绩点，仅供参考，属自用模块
#平均学分绩=pjxfj
#课程绩点=kcjd
#平均学分绩点=pjxfjd
#五等级制支持：优秀，良好，中等，及格，不及格五等级
#2.0！！！新增Excel导入，避免重复输入以及输入错误等问题，目前为单人使用版本
#2.1解决路径问题，使用需复制Excel文件路径

#Excel导入
import xlrd

#参数定义
#课程学分和
total_points = 0
#课程*学分-求和
total_grade_and_point = 0
#课程绩点*学分-求和
total_kcjd_and_point = 0


#课程信息输入（基本弃用，希望后续版本删除）
def course_input() :
    for i in range(course_num):
        a = input("请输入课程名称：")
        course_list.append(a)
        b = input("请输入课程成绩：")
        course_grade.append(b)
        c = int(input("请输入课程对应学分："))
        course_point.append(c)
    return course_grade,course_list,course_point

#平均学分绩计算函数
def Pjxfj():
    m=[]
    for a in course_grade:
        if a < 60:
            #a =40
            m.append(40)
        else:
            m.append(a)    
        
    total_grade=0
    print(m)
    for i in range(course_num):
        total_grade += m[i]*course_point[i]
    pjxfj = total_grade/total_points
    print(f"平均学分绩为{pjxfj}")

#课程绩点计算
def Kcjd():
    kcjd_list = []
    for a in course_grade:
        m = a // 10
        n = a / 10 - m
        kcjd = m + n - 5
        kcjd_list.append(kcjd)
    return kcjd_list

#平均学分绩点计算
def Pjxfjd():
    kcjd_list = Kcjd()
    total_kcjd_and_point = 0
    for i in range(course_num):
        total_kcjd_and_point += kcjd_list[i] * course_point[i]
    pjxfjd = total_kcjd_and_point / total_points
    print(f"同学，你的平均学分绩点（GPA）为{pjxfjd}")

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


#程序开始！
print("欢迎使用绩点计算[2.1]")
#路径获取
path = input("请拖入成绩文件，并回车确定")

#成绩获取函数
data = Data_get(path)

#数据获取
course_num = data[0]
course_list = data[1]
course_grade = data[2]
course_point = data[3]

#课程输出
print("课程信息如下：")
for i in range(course_num):
    print(course_list[i]+"----"+course_grade[i]+"----"+str(course_point[i]))

#课程信息确认
boor = input("请确认课程(有误请修改课程信息后输入“1”并回车,无误直接回车):")
if boor == "0":
    print("请重新输入:")
    course_input()
elif boor == "1":
    course_num = int(input("请输入需要加入计算的课程数量："))
    course_input()

#五等级制百分制转换
for i in range(course_num):
    a = course_grade[i]
    try:
        m = int(a)
        course_grade[i]=m
    except ValueError:
        if a == "优秀":
            course_grade[i]=95
        elif a == "良好":
            course_grade[i]=85
        elif a == "中等":
            course_grade[i]=75
        elif a == "及格":
            course_grade[i]=65
        elif a == "不及格":
            course_grade[i]=0
#学分转换
    course_point[i] = float(course_point[i])
    
#数值计算
#课程成绩*学分计算,学分和计算--五等级百分制
for i in range(course_num):
    total_grade_and_point += course_grade[i]*course_point[i]
    total_points += course_point[i]

#平均学分绩计算
Pjxfj()

#课程绩点计算
kcjd_list = Kcjd()
for i in range(course_num):
    print(f"{course_list[i]}课程绩点为{kcjd_list[i]}")

#平均学分绩点计算
Pjxfjd()

#防止程序运行完成关闭窗口
running = True
while running:
    user_input = input("回车退出程序")
    if user_input == "":
        running = False