#### python语言进阶

####排序算法（选择、冒泡和归并）和查找算法（顺序和折半）：

冒泡排序
name_list = [1,20,34,11,90,23,34,21,66,77,44]
def select_sort(origin_items, cmp = lambda x,y:x>y):
    items = origin_items.copy()
    for i in range(len(items)-1):
        for j in range(len(items)-i-1):
            if cmp(items[j],items[j+1]):
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
    return items
print(select_sort(name_list))

顺序查找
name_list = [1,20,34,11,90,23,34,21,66,77,44]
def seq_search(items, key):
    for index, item in enumerate(items):
        if item == key:
            return index
    return 'there is no'


print(seq_search(name_list, 44))

生成式语法生成新的字典
prices = {
         'AAPL': 191.88,
         'GOOG': 1186.96,
         'IBM': 149.24,
         'ORCL': 48.44,
         'ACN': 166.89,
         'FB': 208.09,
         'SYMC': 21.29
     }

prices2 = {key:value for key,value in prices.items() if value > 100}
print(prices2)

找出最大或者最小的几个元素
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(heapq.nlargest(2,list1))
print(heapq.nsmallest(3,list1))
print(heapq.nlargest(2,list2,key=lambda x:x['shares']))
print(heapq.nlargest(3,list2,key=lambda x:x['price']))


####常用算法
- 穷举法 - 又称为暴力破解法，对所有的可能性进行验证，直到找到正确答案。
- 贪婪法 - 在对问题求解时，总是做出在当前看来
- 最好的选择，不追求最优解，快速找到满意解。
- 分治法 - 把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，直到可以直接求解的程度，最后将子问题的解进行合并得到原问题的解。
- 回溯法 - 回溯法又称为试探法，按选优条件向前搜索，当搜索到某一步发现原先选择并不优或达不到目标时，就退回一步重新选择。
- 动态规划 - 基本思想也是将待求解问题分解成若干个子问题，先求解并保存这些子问题的解，避免产生大量的重复运算。

穷举法例子：
公鸡5元一只 母鸡3元一只 小鸡1元三只
用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
for i in range(20):
    for j in range(33):
        for k in [k*3 for k in range(101)]:
            if i*5 + j*3 + k//3 == 100 and i+j+k == 100:
                print(i,j,k)
				
				
####函数的使用方式
高阶函数的用法，map，filter
items1 = list(map(lambda x:x **2,filter(lambda x:x % 2,range(1,10))))
items2 = [i ** 2 for i in range(1,10) if i % 2]
print(items1)
print(items2)

####面对对象的相关知识
例子：月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成

from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):

    def get_salary(self):
        return 15000


class Programmer(Employee):
    def __init__(self, name, working_hours=0):
        self.working_hours = working_hours
        super().__init__(name)

    def get_salary(self):
        return 200*self.working_hours


class Salesman(Employee):
    def __init__(self, name, sales=0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return self.sales*0.05


class EmployeeFactory():
    @staticmethod
    def create(emp_type,*args,**kwargs):
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args,**kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args,**kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args,**kwargs)
        return emp


emps = [
             EmployeeFactory.create('M', 'joey'),
             EmployeeFactory.create('P', 'monica', 120),
             EmployeeFactory.create('P', 'phybee', 85),
             EmployeeFactory.create('S', 'ross', 123000),
         ]

for emp in emps:
    print(f'{emp.name},his salary is {emp.get_salary()}')
	

