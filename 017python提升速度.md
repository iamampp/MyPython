####
python��Ч�ʱ�һ��ı������ԣ���Ч�ʺ��ٶȷ�����һЩ���㣬���漰
����ƿ����ʱ����Ҫ���ض����ֽ��������Ż���

####����ȫ�ֱ���
����Ϊȫ�ֱ�����Χ�ڵĴ��������ٶȻ���ں����������٣����ű����ں����У�ͨ�������15%���ٶ�������

����1��
from time import time
import math

t1 = time()
size = 1000
for x in range(size):
    for y in range(size):
        z = math.sqrt(x)+math.sqrt(y)
print("ʹ��ȫ�ֱ�����%f"%(time() - t1))

def calc():
    t1 = time()
    size = 1000
    for x in range(size):
        for y in range(size):
            z = math.sqrt(x) + math.sqrt(y)
    print("ʹ�þֲ�������%f"%(time() - t1))

calc()

����2:
from time import time
import math

t1 = time()
size = 1000
for x in range(size):
    for y in range(size):
        z = math.sqrt(x)+math.sqrt(y)
print("ʹ��sqrtȫ�ֱ�����%f"%(time() - t1))

def calc():
    t1 = time()
    sqrt = math.sqrt
    for x in range(size):
        for y in range(size):
            z = sqrt(x) + sqrt(y)
    print("ʹ��sqrt�ֲ�������%f"%(time() - t1))

calc()


####������from xxx import XXX
��Ϊʹ��.�ķ���ʱ���ᴥ���ض��ķ�������__getattribute__()��__getattr__()����Щ����������ֵ��������˻��������Ŀ�����

####�����������Է���
��Ƶ�����ʵ��������Ը�ֵ��һ���ֲ������������������������ٶȡ�

���ӣ�
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
    print("��������ȫ�ֵ���ʱ�����ģ�%f"%(time()-t1))

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
    print("�������Ծֲ�����ʱ�����ģ�%f" % (time() - t1))

main2()

 ####ʹ��.joinƴ���ַ���������+=
 ��ʹ��a + bƴ���ַ���ʱ������ Python ���ַ����ǲ��ɱ�����������һ���ڴ�ռ䣬��a��b�ֱ��Ƶ�����������ڴ�ռ��С�
 ��ˣ����Ҫƴ��  ���ַ����������  ���м�����ÿ����һ���м�������Ҫ����͸���һ���ڴ棬����Ӱ������Ч�ʡ�
 ��ʹ��join()ƴ���ַ���ʱ�������ȼ������Ҫ������ܵ��ڴ�ռ䣬Ȼ��һ���Ե����������ڴ棬����ÿ���ַ���Ԫ�ظ��Ƶ����ڴ���ȥ��

 ���ӣ�
 from time import time

def concatString(string):
    result = ''
    for str_i in string:
        result += str_i

def main():

    t1 = time()
    for _ in range(1000):
        result = concatString('this is a testing'*100)
    print("ʹ��+=ƴ���ַ������ķ�ʱ�䣺%f"%(time() - t1))

main()

def concatString2(string):
    return ''.join(string)


def main2():
    t1 = time()
    for _ in range(1000):
        result = concatString2('this is a testing' * 100)
    print("ʹ��joinƴ���ַ������ķ�ʱ�䣺%f" % (time() - t1))

main2()

####ʹ��forѭ����������whileѭ��
��python�У�forѭ��һ���whileѭ��Ҫ��

���ӣ�
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
    print("while ѭ��������ʱ�䣺%f"%(time()-t1))

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
    print("while ѭ��������ʱ�䣺%f"%(time()-t1))

main2()

####ʹ��numba.git
ʹ��numbaģ����Խ�python����jit����Ϊ������ִ�У������ߴ��������ٶȡ�

���ӣ�
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
    print("��ʹ��numba.git������ʱ�䣺%f"%(time()-t1))

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
    print("ʹ��numba.jit������ʱ�䣺%f"%(time()-t1))

main2()


####ѡ����ʵ����ݽṹ
Python ���õ����ݽṹ��str, tuple, list, set, dict�ײ㶼�� C ʵ�ֵģ��ٶȷǳ��죬�Լ�ʵ���µ����ݽṹ���������ϴﵽ���õ��ٶȼ����ǲ����ܵġ�

list������ C++ �е�std::vector����һ�ֶ�̬���顣���Ԥ����һ���ڴ�ռ䣬��Ԥ������ڴ�ռ����꣬�ּ������������Ԫ��ʱ��������һ�������ڴ�ռ䣬Ȼ��ԭ�е�����Ԫ�ض����ƹ�ȥ��֮������֮ǰ���ڴ�ռ䣬�ٲ�����Ԫ�ء�ɾ��Ԫ��ʱ�������ƣ�����ʹ���ڴ�ռ��Ԥ�����ڴ�ռ��һ�뻹��ʱ������������һ��С�ڴ棬��һ��Ԫ�ظ��ƣ�֮������ԭ�д��ڴ�ռ䡣��ˣ������Ƶ����������ɾ��������������ɾ����Ԫ�������ֺܶ�ʱ��list��Ч�ʲ��ߡ���ʱ��Ӧ�ÿ���ʹ��collections.deque��collections.deque��˫�˶��У�ͬʱ�߱�ջ�Ͷ��е����ԣ��ܹ������˽���  ���ӶȵĲ����ɾ��������

list�Ĳ��Ҳ���Ҳ�ǳ���ʱ������Ҫ��listƵ������ĳЩԪ�أ���Ƶ�����������ЩԪ��ʱ������ʹ��bisectά��list�������������н��ж��ֲ��ң��������ҵ�Ч�ʡ�

����һ�����������ǲ��Ҽ�Сֵ�򼫴�ֵ����ʱ����ʹ��heapqģ�齫listת��Ϊһ���ѣ�ʹ�û�ȡ��Сֵ��ʱ�临�Ӷ���  ��