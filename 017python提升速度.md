####
python的效率比一般的编译语言，在效率和速度方面有一些不足，在涉及
性能瓶颈的时候，需要对特定部分进行性能优化。

####避免全局变量
定义为全局变量范围内的代码运行速度会比在函数中慢不少，将脚本放在函数中，通常会带来15%的速度提升。

例子1：
from time import time
import math

t1 = time()
size = 1000
for x in range(size):
    for y in range(size):
        z = math.sqrt(x)+math.sqrt(y)
print("使用全局变量：%f"%(time() - t1))

def calc():
    t1 = time()
    size = 1000
    for x in range(size):
        for y in range(size):
            z = math.sqrt(x) + math.sqrt(y)
    print("使用局部变量：%f"%(time() - t1))

calc()

例子2:
from time import time
import math

t1 = time()
size = 1000
for x in range(size):
    for y in range(size):
        z = math.sqrt(x)+math.sqrt(y)
print("使用sqrt全局变量：%f"%(time() - t1))

def calc():
    t1 = time()
    sqrt = math.sqrt
    for x in range(size):
        for y in range(size):
            z = sqrt(x) + sqrt(y)
    print("使用sqrt局部变量：%f"%(time() - t1))

calc()


####尽量用from xxx import XXX
因为使用.的方法时，会触发特定的方法，如__getattribute__()和__getattr__()，这些方法会进行字典操作，因此会带来额外的开销。

####避免类内属性访问
将频繁访问的类内属性赋值给一个局部变量，可以提升代码运行速度。

例子：
from time import time
import math

class DemoClass():
    def __init__(self,value):
        self.value = value

    def computeSqrt(self,size):
        result = []
        for i in range(size):
            for j in range(self.value):
                result.append(math.sqrt(self.value))

def main():
    t1 = time()
    demo = DemoClass(100)
    print(demo.computeSqrt(1000))
    print("类内属性全局调动时间消耗：%f"%(time()-t1))

main()


class DemoClass2():
    def __init__(self, value):
        self.value = value

    def computeSqrt2(self, size):
        result = []
        value = self.value
        for i in range(size):
            for i in range(value):
                result.append(math.sqrt(value))


def main2():
    t1 = time()
    demo = DemoClass2(100)
    print(demo.computeSqrt2(1000))
    print("类内属性局部调动时间消耗：%f" % (time() - t1))

main2()

 ####使用.join拼接字符串而不是+=
 当使用a + b拼接字符串时，由于 Python 中字符串是不可变对象，其会申请一块内存空间，将a和b分别复制到该新申请的内存空间中。
 因此，如果要拼接  个字符串，会产生  个中间结果，每产生一个中间结果都需要申请和复制一次内存，严重影响运行效率。
 而使用join()拼接字符串时，会首先计算出需要申请的总的内存空间，然后一次性地申请所需内存，并将每个字符串元素复制到该内存中去。

 例子：
 from time import time

def concatString(string):
    result = ''
    for str_i in string:
        result += str_i

def main():

    t1 = time()
    for _ in range(1000):
        result = concatString('this is a testing'*100)
    print("使用+=拼接字符串所耗费时间：%f"%(time() - t1))

main()

def concatString2(string):
    return ''.join(string)


def main2():
    t1 = time()
    for _ in range(1000):
        result = concatString2('this is a testing' * 100)
    print("使用join拼接字符串所耗费时间：%f" % (time() - t1))

main2()

####使用for循环，而不是while循环
在python中，for循环一般比while循环要快

例子：
from time import time

def computeSum(size):
    sum = 0
    i = 0
    while i < size:
        sum += i
        i += 1

def main():
    t1 = time()
    size = 1000*100
    for _ in range(100):
        computeSum(size)
    print("while 循环的消耗时间：%f"%(time()-t1))

main()

def computeSum2(size):
    sum = 0
    for i in range(size):
        sum += i

def main2():
    t1 = time()
    size = 1000*100
    for _ in range(100):
        computeSum(size)
    print("while 循环的消耗时间：%f"%(time()-t1))

main2()

####使用numba.git
使用numba模块可以将python函数jit编译为机器码执行，大大提高代码运行速度。

例子：
from time import time
import numba

def computeSum(size):
    sum = 0
    i = 0
    while i < size:
        sum += i
        i += 1

def main():
    t1 = time()
    size = 1000*100
    for _ in range(100):
        computeSum(size)
    print("不使用numba.git的消耗时间：%f"%(time()-t1))

main()


@numba.jit
def computeSum2(size):
    sum = 0
    i = 0
    while i < size:
        sum += i
        i += 1

def main2():
    t1 = time()
    size = 1000*100
    for _ in range(100):
        computeSum(size)
    print("使用numba.jit的消耗时间：%f"%(time()-t1))

main2()


####选择合适的数据结构
Python 内置的数据结构如str, tuple, list, set, dict底层都是 C 实现的，速度非常快，自己实现新的数据结构想在性能上达到内置的速度几乎是不可能的。

list类似于 C++ 中的std::vector，是一种动态数组。其会预分配一定内存空间，当预分配的内存空间用完，又继续向其中添加元素时，会申请一块更大的内存空间，然后将原有的所有元素都复制过去，之后销毁之前的内存空间，再插入新元素。删除元素时操作类似，当已使用内存空间比预分配内存空间的一半还少时，会另外申请一块小内存，做一次元素复制，之后销毁原有大内存空间。因此，如果有频繁的新增、删除操作，新增、删除的元素数量又很多时，list的效率不高。此时，应该考虑使用collections.deque。collections.deque是双端队列，同时具备栈和队列的特性，能够在两端进行  复杂度的插入和删除操作。

list的查找操作也非常耗时。当需要在list频繁查找某些元素，或频繁有序访问这些元素时，可以使用bisect维护list对象有序并在其中进行二分查找，提升查找的效率。

另外一个常见需求是查找极小值或极大值，此时可以使用heapq模块将list转化为一个堆，使得获取最小值的时间复杂度是  。