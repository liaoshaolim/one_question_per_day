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
