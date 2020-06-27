
def menu():
    menu_info = '''            学籍管理系统
￥-------------------------------￥
￥                               ￥
￥   1.添加学生                  ￥
￥   2.删除学生                  ￥
￥   3.修改学生                  ￥
￥   4.查询学生                  ￥
￥   5.任意按键加回车退出        ￥
￥-------------------------------￥'''
    print(menu_info)


# 添加学生
def add_student():
    student_list = []
    while True:
        name = input("请输入姓名：")
        if not name:
            break
        try:
            age = int(input("请输入年龄："))
            results = int(input("请输入成绩："))
        except:
            print("输入数据格式有误，请重新输入：")
            continue
        student_info = {"name": name, "age": age, "results": results}
        student_list.append(student_info)
    return student_list


# 删除学生
def remove_student(student_list, remove_name=""):
    if not remove_name:
        remove_name = input("请输入需要删除的学生姓名：")
    for info in student_list:
        if remove_name == info.get("name"):
            return info
    raise IndexError(f"未找到学生信息{remove_name}")


# 修改学生信息
def amend_student(student_info):
    amend_name = input("请输入需要修改的学生信息：")
    for info in student_info:
        if amend_name == info.get("name"):
            age = input("请输入年龄：")
            results = input("请输入成绩：")
            student_info = {"name": amend_name, "age": age, "results": results}
            return student_info
    raise IndexError(f"学生信息不存在{amend_name}")


# 查询学生信息
def show_student(student_list):
    i = 1
    j = 0
    k = 1

    if not student_list:
        print("当前数据为空")
        return

    print("=================================")
    print("学生信息如下：")
    print("=================================")
    print("序号\t姓名\t年龄\t成绩")
    for info in student_list:  # 遍历列表
        for cla in info.values():  # 字典中的按值索引
            if j % 3 == 0:  # 第一个if用来实现：序号递增并换行
                print("\n")
                print(k, end='.\t')
                k += 1
            print(cla, end='\t')
            if i % 3 == 0:  # 第二个if用来实现：每输出一个字典就换行
                print("\n")
            i += 1
            j += 1
    print("\n")


# 储存信息
def save_student(student_list):
    if not student_list:
        return
    students_txt = open("students.txt", "w+")     # 以写模式打开，并清空文件内容
    for info in student_list:
        students_txt.write(str(info)+"\n")          # 按行存储，添加换行符
    students_txt.close()


def read_student():
    old_info = []
    try:
        students_txt = open("students.txt")
    except:
        print("暂未保存数据信息")                       # 打开失败，文件不存在说明没有数据保存
        return
    while True:
        info = students_txt.readline()
        if not info:
            break
        # print(info)
        info = info.rstrip()  # 　去掉换行符
        # print(info)
        info = info[1:-1]       # 去掉｛｝
        # print(info)
        student_dict = {}       # 单个学生字典信息
        for x in info.split(","):   # 以，为间隔拆分
            # print(x)
            key_value = []      # 开辟空间，key_value[0]存key,key_value[0]存value
            for k in x.split(":"):  # 以：为间隔拆分
                k = k.strip()  # 　去掉首尾空字符
                # print(k)
                if k[0] == k[-1] and len(k) > 2:        # 判断是字符串还是整数
                    key_value.append(k[1:-1])           # 去掉　首尾的＇
                else:
                    key_value.append(int(k))
                # print(key_value)
            student_dict[key_value[0]] = key_value[1]   # 学生信息添加
        # print(student_dict)
        old_info.append(student_dict)   # 所有学生信息汇总
    students_txt.close()
    return old_info


def main():
    student_list = read_student()
  #  print(student_list[0].get("age"))
    while True:
        menu()
        number = input("请输入你的选项：")
        if number == "1":
            student_list = student_list+add_student()
        elif number == "2":
            try:
                student_list.remove(remove_student(student_list))
                print("已删除")
            except Exception as e:
                print(e)
        elif number == "3":
            try:
                student = amend_student(student_list)
            except Exception as e:
                # 学生姓名不匹配
                print(e)
            else:
                # 首先按照根据输入信息的名字，从列表中删除该生信息，然后重新添加该学生最新信息
                student_list.remove(remove_student(
                    student_list,student.get("name")))
                student_list.append(student)
        elif number=="4":
            show_student(student_list)
        else:
            save_student(student_list)
            print("已保存")
            break
        input("回车返回菜单")

if __name__ == "__main__":
    main()
