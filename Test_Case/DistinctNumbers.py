import sys
input = sys.stdin.readline

def Search(A, k):
    left = 0
    right = len(A) -1
    while left <= right:
        mid = (left + right)//2
        if A[mid] == k:
            return k
        elif (A[mid] < k):
            left = mid + 1
        else:
            right = mid - 1
    return -1
def Count(A):
    count = 0
    dis = 0
    for i in range(len(A)):
        if i == Search(A, i):
            count +=1
        dis = dis + count//count
    return dis

n = int(input())
A = list(map(int, input().split()))
# In kết quả
print(Count(A))