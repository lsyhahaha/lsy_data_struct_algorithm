class Solution:
    def check(self, s):
        i = 0
        j = len(s) - 1
        while (i < j):
            if (s[i] != s[j]):
                return False
            i = i + 1
            j = j - 1

        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        if n == 1:
            return s
        ret = 0
        res = ""
        for i in range(n):
            for j in range(i, n):
                cur_s = s[i:j+1]
                if self.check(cur_s):
                    if ret < j - i + 1:
                        ret = j - i + 1
                        res = cur_s

        return res

a = Solution()
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(a.longestPalindrome(s))

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class LinkList:
#     def __init__(self, list):
#         self.head = ListNode()
#         ret = self.head
#         for a in list:
#             ret = ListNode(a)
#             ret = ret.next
#
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         ret = ListNode(0, head)
#         pre = ListNode(0, head)
#         cur = head
#         next = cur.next
#
#         while (next):
#             while (next is not None and cur.val == next.val):
#                 next = next.next
#             pre.next = next
#             # cur.next = next
#
#             print(next.val)
#             cur = next
#             next = cur.next
#
#         return ret.next
# a = Solution()
# linklist = LinkList([1,2,3,3,4,4,5])
# a.deleteDuplicates(linklist.head)
# head = linklist.head
# while head:
#     print(head.val)
#     head = head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         behind = head
#         ret = ListNode(0, head)
#         pre = ListNode(0, head)
#         while n > 1:
#             behind = behind.next
#             n = n - 1
#
#         while True:
#             if (behind.next is None):
#                 pre.next = head.next
#                 break
#
#             behind = behind.next
#             pre = pre.next
#             head = head.next
#
#         return ret.next
# a = Solution()
#
# print(a.removeNthFromEnd(ListNode(1), 1))

# from collections import deque
# class TreeNode:
#     def __init__(self, val = 0, child = []):
#         self.val = val
#         self.child = child
# class Solution:
#     def minimumOperations(self, nums, start, goal):
#         q = deque()
#         q.append(TreeNode(start))
#         ret = 0
#         aa = 0
#         while len(q):
#             n = len(q)
#             for i in range(n):
#                 cur = q.pop()
#                 print(cur.val)
#                 if cur.val == goal:
#                     return ret
#                 for num in nums:
#                     q.append(TreeNode(cur.val + num))
#                     q.append(TreeNode(cur.val - num))
#                     q.append(TreeNode(cur.val ^ num))
#
# a = Solution()
# print(a.minimumOperations([1, 3], start=6, goal=4))
# import random
# ret = []
# for i in range(10000):
#     ret.append(random.randint(1,100))
#
# print(ret)


# class Solution:
#     def smallestEqual(self, nums):
#         ret = []
#         for i in range(len(nums)):
#             if i % 10 == nums[i]:
#                 ret.append(i)
#         if (len(ret) == 0):
#             return -1
#         ret.sort()
#         return ret[0]




# class Solution(object):
#     def findWords(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         one = "qwertyuiop"
#         two = "asdfghjkl"
#         three = "zxcvbnm"
#
#         a_dict = dict()
#         for i in one:
#             a_dict[i] = 1
#         for i in two:
#             a_dict[i] = 2
#         for i in three:
#             a_dict[i] = 3
#         ret = []
#         for word in words:
#             flag = True
#             for i in range(len(word) - 1):
#                 s = word[i].lower()
#                 s_next  = word[i+1].lower()
#                 if (a_dict[s] != a_dict[s_next]):
#                     flag = False
#                     break
#             if flag:
#                 ret.append(word)
#
#         return ret
#
# a = Solution()
# print(a.findWords(words=["Hello","Alaska","Dad","Peace"]))

# a = set([1,2,3,4])
# print(a[0])
# # for i in a:
# #     print(i)

# for i in range(15):
#     print(i)
#     i = i + 1
#
# for name in ['lsy', 'aaa', 'bbb', 'ccc']:
#     print(name)
#     name = 'dddd'



# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         if n == 2:
#             return nums
#         nums.sort()
#         ret = []
#         i = 0
#         while i < n:
#             if (i == n-1):
#                 ret.append(nums[i])
#                 break
#             if (nums[i] == nums[i+1]):
#                 i = i + 1
#             else:
#                 ret.append(nums[i])
#
#             i = i + 1
#
#         return ret
#
# #test
# a = Solution()
# print(a.singleNumber([1,1,2,2,3,4,5,5]))


# class Solution:
#     def permuteUnique(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#
#         visit = [True for i in range(len(nums))]
#         print(visit)
#         tmp = nums[:] #  值传递
#         # tmp = nums # 引用传递
#
#         def dfs(position):
#             if position == len(nums):
#                 res.append(tmp[:])
#                 return
#
#             for index in range(0, len(nums)):
#                 if visit[index]:
#                     tmp[position] = nums[index]
#                     visit[index] = False
#                     dfs(position + 1)
#                     visit[index] = True
#
#         res = []
#         dfs(0)
#         return res
# #test
# a = Solution()
# print(a.permuteUnique([0,1,2]))




# class Solution(object):
#     def isPowerOfTwo(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         l = 0
#         r = 31
#         while(l <= r):
#             mid = (r - l) // 2 + l
#             if (2**mid == n):
#                 # print(mid)
#                 return True
#             elif (2**mid > n):
#                 r = mid - 1
#             elif (2**mid < n):
#                 l = mid + 1
#
#         return False
#
# #test
# a = Solution()
# # print("ans = ", a.isPowerOfTwo(1))
# list = [2**i for i in range(31)]
# for i in list:
#     print("i = ", i , "ans = ", a.isPowerOfTwo(i - 2))





# class Solution(object):
#     def reorderedPowerOf2(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         alist = []
#         for i in range(30):
#             set = dict()
#             for s in str(2 ** i):
#                 # print(s)
#                 if s in set.keys():
#                     set[s] = set[s] + 1
#                 else:
#                     set[s] = 1
#             alist.append(set)
#         # print(alist)
#
#         ret = dict()
#         for s in str(n):
#             if s in ret.keys():
#                 ret[s] = ret[s] + 1
#             else:
#                 ret[s] = 1
#
#         # print(ret)
#
#         return ret in alist
#
# a = Solution()
# print(a.reorderedPowerOf2(1521))