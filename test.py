class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = 0
        r = 31
        while(l <= r):
            mid = (r - l) // 2 + l
            if (2**mid == n):
                # print(mid)
                return True
            elif (2**mid > n):
                r = mid - 1
            elif (2**mid < n):
                l = mid + 1

        return False

#test
a = Solution()
# print("ans = ", a.isPowerOfTwo(1))
list = [2**i for i in range(31)]
for i in list:
    print("i = ", i , "ans = ", a.isPowerOfTwo(i - 2))





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