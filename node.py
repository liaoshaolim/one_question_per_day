class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = next


class TreeNode:
    ''' 二叉树节点 '''

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LinkListUtil(object):
    def isEmpty(self, head):
        ''' 链表是否为空 '''
        return head == None

    def length(self, head):
        ''' 链表长度 '''
        current = head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def printAll(self, head):
        ''' 打印链表所有元素 '''
        current = head
        while current != None:
            print(current.value, end='\t')
            current = current.next
        print()

    # fast slow point
    def isHasCycle(self, head):
        ''' 链表中是否有环 '''
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # is 与 == 的区别：is 不仅值相同，id() 出来的值也相同
            if slow is fast:
                return True
        return False

    # fast slow point
    # 快指针是慢指针一倍的步幅，当快指针指向 None 时，慢指针刚好满足条件
    def middleNode(self, head):
        ''' 876. 链表的中间结点 '''
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # fast slow point
    def removeNthFromEnd(self, head, n):
        ''' 19. 删除链表的倒数第 N 个节点 （给定的 n 保证是有效的。）'''
        slow = head
        fast = head
        # 快指针前进 n 个节点
        while n > 0:
            fast = fast.next
            n -= 1
        # 快指针如果为 None 则代表 n 为链表长度，删除第一个节点即可
        if fast == None:
            return head.next
        # 快慢指针同步向前，当快指针走到最后一个节点跳出循环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        # slow.next 就是倒数第 n 个节点，删除即可
        slow.next = slow.next.next
        return head

    def reverse(self, head):
        ''' 翻转链表 '''
        cur = head
        newH = None
        while cur:
            temp = cur.next
            cur.next = newH
            newH = cur
            cur = temp
        return newH
