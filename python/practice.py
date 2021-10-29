"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

输入：strs = ["flower","flow","flight"]
输出："fl"

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''
        new_strs = zip(*strs)
        for i in new_strs:
            if len(set(i)) == 1:
                res += i[0]
            else:
                return res
        return str(res)


if __name__=='__main__':
    strs = ["flower","flow","flight"]
    s = Solution()
    print(s.longestCommonPrefix(strs))