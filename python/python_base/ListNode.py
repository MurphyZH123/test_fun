class Node():
    def __init__(self,value,next = None):
        self.value = value
        self.next = next


head = Node(100)  # 定义第一个值100，第二个值99
head.next = Node(99)
head.next.next = Node(88)


# 获取链表中的值
def get_Node_value(head):
    linklist = []
    while head:
        linklist.append(head.value)
        head = head.next
    return linklist


# print(get_Node_value(head))


# 在链表中增加一个值，head是头结点，value是要添加的值，target是在目标元素之前插入
# 插入的操作：1）找到目标结点target 2）将目标结点前一个结点指向新插入的结点 3）将新节点的指针向目标结点
# 插入的方式有三种： 1）在头结点前插入 2）在链表中间插入 3）在链表结尾插入
def add_node_in_linklist(head,value,target):
    newNode = Node(value)  # 定义一个目标链表值
    tempHead = head  # 复制一下链表
    previous = None  # 在插入结点的前结点默认为Node
    while tempHead:
        if tempHead.value == target:  # 如果target存在
            if previous is None:
                newNode.next = head
                return newNode
            previous.next = newNode
            newNode.next = tempHead
            return head
        else:
            previous = tempHead
            tempHead = tempHead.next
    previous.next = newNode  # 如果循环完后没有taret,那么把value插入链接结尾
    return head

#
# node_value = (get_Node_value(head))
# head = add_node_in_linklist(head,66,99)
# newNode = get_Node_value(head)
# print(node_value, newNode)


# 获取链表的长度
def linklist_length(head):
    length = 0
    while head:
        length = length+1
        head = head.next
    return length


# 链表删除方法
# 删除操作： 1）找到目标结点target 2）将目标结点的前一个结点指向删除结点的下一个结点
# 删除的三种情况 1）目标结点是头结点 2）目标结点是中间结点 3）目标结点是最后一个结点

def delete_target_from_linklist(head, target):
    previous = None
    result = head  # 复制一下结点
    while head:
        if head.value == target:
            if previous is None:  # 如果是删除头结点
                return head.next  # 那就直接返回头结点的下一个结点
            previous.next = head.next  # 否则删除中间的结点，那就让被删除结点的前一个结点指针指向被删除结点的下一个节点，来实现删除功能
            return result
        previous = head  # 如果删除的结点是最后一个结点，那么让前一个结点等于被删除的结点
        head = head.next  # 然后前一个结点的指针指向被删除结点的下一个结点，也就是空节点
    return result


result = delete_target_from_linklist(head,88)
# print(get_Node_value(result))
# print(linklist_length(result))


"""
习题：
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


class ListNode():
    def __init__(self,value,next = None):
        self.value = value
        self.next = next


def vauleOfListCode(lists):
    val = []
    while lists:
        val.append(lists.value)
        lists = lists.next
    return val


class SolutionAddTwoListCode:
    def mergeTwoLists(self,l1:ListNode,l2:ListNode)->ListNode:
        dummy = ListNode(0)
        previous = dummy
        while l1 and l2:
            if l1.value <= l2.value:
                previous.next = l1
                l1 = l1.next
            else:
                previous.next = l2
                l2 = l2.next
            previous = previous.next
        if l1:
            previous.next = l1
        else:
            previous.next = l2
        return dummy.next


if __name__=='__main__':
    l1 = ListNode([2, 3])
    l2 = ListNode([3, 4])
    s = SolutionAddTwoListCode()
    result = s.mergeTwoLists(l1, l2)
    print(vauleOfListCode(result))



