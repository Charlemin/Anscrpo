from com.anscrpo.conf import Employee
#"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
#"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)
print("test")

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = 'John'  # 字符串

print(float(counter))
print(int(miles))
print(name)
