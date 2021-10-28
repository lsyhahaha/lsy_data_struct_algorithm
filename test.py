class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        alist = []
        for i in range(30):
            set = dict()
            for s in str(2 ** i):
                # print(s)
                if s in set.keys():
                    set[s] = set[s] + 1
                else:
                    set[s] = 1
            alist.append(set)
        # print(alist)

        ret = dict()
        for s in str(n):
            if s in ret.keys():
                ret[s] = ret[s] + 1
            else:
                ret[s] = 1

        # print(ret)

        return ret in alist

a = Solution()
print(a.reorderedPowerOf2(1521))