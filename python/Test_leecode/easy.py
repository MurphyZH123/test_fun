"""
对于字符串S 和T，只有在 S = T + ... + T（T 自身连接 1 次或多次）时，我们才认定“T 能除尽 S”。
返回最长字符串X，要求满足X 能除尽 str1 且X 能除尽 str2。

示例1
输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"

示例2
输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"

示例3
输入：str1 = "LEET", str2 = "CODE"
输出：""
"""
from math import gcd


# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if str1+str2 == str2+str1:
#             Max_Introduction = gcd(len(str1), len(str2))
#         return str1[:Max_Introduction]


# solution = Solution()
# print(solution.gcdOfStrings("ABABAB", "ABAB"))


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        if str1 + str2 != str2 + str1: return ''

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        return str1[:gcd(m, n)]


"""
给出第一个词first 和第二个词second，考虑在某些文本text中可能以 "first second third" 形式出现的情况，其中second紧随first出现，third紧随second出现。

对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。

输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
输出：["girl","student"]

输入：text = "we will we will rock you", first = "we", second = "will"
输出：["we","rock"]
"""


class SolutionThirdOfStrings:
    def thirdOfStrings(self, text: str, first: str, second: str) -> list[str]:
        res = []
        text_list = text.split(' ')
        first_list = first.split(' ')
        second_list = second.split(' ')
        for each in range(len(text_list) - 1):
            if first_list[0] == text_list[each] and second_list[0] == text_list[each + 1]:
                res.append(text_list[each + 2])
        return res


"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
例子：
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
"""

""" 解法1 暴力解法"""


class Solution:
    def num_target(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        target_data = []
        for i in range(0, length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    target_data.append(i)
                    target_data.append(j)
        return list(set(target_data))


""" 解法2 排序加双指针,两遍哈希数 """


# class Solution2:
#     def sums_target(self, nums:list[int], target:int) -> list[int]:

class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        temp = nums.copy()
        temp.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            if (temp[i] + temp[j]) > target:
                j = j - 1
            elif (temp[i] + temp[j]) < target:
                i = i + 1
            else:
                break
        p = nums.index(temp[i])
        nums.pop(p)
        k = nums.index(temp[j])
        if k >= p:
            k = k + 1
        return [p, k]


""" 一遍哈希数 """


class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], idx]
            else:
                hashmap[num] = idx


class Solution3:
    def sumTwo(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], idx]
            else:
                hashmap[num] = idx


"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−2**31, 2**31− 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
"""


class Solution:
    def reverse_int(self, nums: int) -> int:
        if nums < 0:
            res_nums = str(nums)[:0:-1]
            return int('-' + res_nums)
        else:
            res_nums = str(nums)[::-1]
            return int(res_nums)


# data_int = '1234'
# print(data_int[:0:-1])


def reverse_better(self, x: int) -> int:
    y, res = abs(x), 0
    # 则其数值范围为 [−2^31,  2^31 − 1]
    boundry = (1 << 31) - 1 if x > 0 else 1 << 31
    while y != 0:
        res = res * 10 + y % 10
        if res > boundry:
            return 0
        y //= 10
    return res if x > 0 else -res


"""
习题：回文数
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
示例 1：
输入：x = 121
输出：true

示例2：
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
"""


# 将正数转为字符串
class SolutionPalindrome:
    def isPalindrome(self, nums: int) -> int:
        if nums < 0:
            return False
        elif nums > 0:
            if str(nums) == str(nums)[::-1]:
                return True
            else:
                return False


# 不将整数转为字符串

class SolutionPalindrome2:
    def isPalindrome(self, nums: int) -> int:
        res, y = 0, abs(nums)
        if nums < 0:
            return False
        while y != 0:
            res = res * 10 + y % 10
            y //= 10
        return res == nums


"""
例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给定一个罗马数字，将其转换成整数。输入确保在 1到 3999 的范围内。
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
示例 1:
输入: "III"
输出: 3

示例 2:
输入: "IV"
输出: 4
"""


class SolutionRomanToInt:
    def romanToInt(self, s: str) -> int:
        dict_str = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s) - 1):
            if dict_str[s[i]] < dict_str[s[i + 1]]:
                res = res - dict_str[s[i]]
            else:
                res = res + dict_str[s[i]]
        return res + dict_str[s[-1]]


"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

备注：
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
"""


class SolutionLongestCommonPrefix:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

    def longestCommonPrefix2(self, s: list[str]) -> str:
        res = ''
        if len(s) == 0: return ''  # 判断当前字符串是否为空，如果为空则返回空
        ss = list(zip(*s))  # 将s进行解压
        for each in ss:
            if len(set(each)) == 1:  # 将解压后的s转化为元组
                res = res + each[0]
            else:
                return res
        return res


"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例2：
输入：s = "()[]{}"
输出：true

示例3：
输入：s = "(]"
输出：false

示例4：
输入：s = "([)]"
输出：false

示例5：
输入：s = "{[]}"
输出：true

"""


class SolutionIsValid:
    def IsValid(self, s: str) -> bool:
        reference = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if stack and i in reference:
                if stack[-1] == reference[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack


"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例2：
输入：l1 = [], l2 = []
输出：[]

示例3：
输入：l1 = [], l2 = [0]
输出：[0]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def vauleOfListCode(lists):
    val = []
    while lists:
        val.append(lists.val)
        lists = lists.next
    return val


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class SolutionAddTwoListCode:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建哑节点作为 结果链表 的开头
        dummy = ListNode(0)
        # 有个游标，标识 结果链表 的结尾
        move = dummy
        # l1 和 l2 都未遍历结束
        while l1 and l2:
            # 如果 l1 的数值比较小
            if l1.val <= l2.val:
                # 把 l1 头部节点拼接到 结果链表 的结尾
                move.next = l1
                # l1 指向下一个节点
                l1 = l1.next
            else:
                # 把 l2 头部节点拼接到 结果链表 的结尾
                move.next = l2
                # l2 指向下一个节点
                l2 = l2.next
            # 移动 结果链表 的结尾指针
            move = move.next
        # l1 或者 l2 尚未使用完，拼接到 结果链表 的最后
        move.next = l1 if l1 else l2
        # 返回哑节点的下一个位置
        # res = dummy.next
        return move


"""
汉诺塔的问题
在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
(1) 每次只能移动一个盘子;
(2) 盘子只能从柱子顶端滑出移到下一根柱子;
(3) 盘子只能叠在比它大的盘子上。
请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。

示例1
输入：A = [2, 1, 0], B = [], C = []
输出：C = [2, 1, 0]

示例2
输入：A = [1, 0], B = [], C = []
输出：C = [1, 0]
"""


class SolutionOfhanota:
    def hanota(self, A: list[int], B: list[int], C: list[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        stk = [(len(A), A, B, C, 0)]
        while stk:
            n, src, tmp, dest, which = stk.pop()
            if which == 0:  # 调用者
                if n == 1:  # 递归出口
                    dest.append(src.pop())
                else:  # 将两个子函数放入栈内
                    # stk.append((n - 1, src, tmp, dest, 2))  # 子函数②执行完毕退栈后（这里没必要写）
                    stk.append((n - 1, tmp, src, dest, 0))  # 先放子函数②

                    stk.append((n - 1, src, tmp, dest, 1))  # 子函数①执行完毕退栈，保留原调用函数信息
                    stk.append((n - 1, src, dest, tmp, 0))  # 后放子函数①
            elif which == 1:  # 子函数①结束，打印移动信息
                dest.append(src.pop())


class SolutionOfHanota:
    def hanota(self, A: list[int], B: list[int], C: list[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        self.move(n, A, B, C)

    def move(self, n, A, B, C):
        if n == 1:
            C.append(A.pop())
        else:
            self.move(n - 1, A, C, B)
            C.append(A.pop())
            self.move(n - 1, B, A, C)
        return C


if __name__ == '__main__':
    # l1 = ListNode(2)
    # l2 = ListNode(3)
    # s = SolutionAddTwoListCode()
    # print(vauleOfListCode(s.mergeTwoLists(l1, l2)))
    # # print(valueListCode(s.mergeListCode(3,4)))
    # # print(lengthListCode(s.mergeListCode(3,4)))
    s = SolutionOfHanota()
    print(s.move(3,A=[2, 1, 0], B=[], C=[]))
