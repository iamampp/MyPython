"""二分搜索是一种在有序数组中查找某一特定元素的搜索算法。搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半。"""

def search(arr,left,right,x):
    if right >= left:
        mid = int(left+(right-left)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return search(arr,left,mid-1,x)
        elif arr[mid] < x:
            return search(arr,mid+1,right,x)
    else:
        return -1
a = [1,2,3,4,5,6,7,8,9]
b = []
print(search(a, 0, right=len(a)-1, x=9))



