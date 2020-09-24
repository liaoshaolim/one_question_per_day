class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = next


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

    def reverse(self, head):
        # cur, pre = head, None
        # while cur:
        #     cur.next, pre, cur = pre, cur, cur.next
        # return pre
        cur = head
        newH = None
        while cur:
            temp = cur.next
            cur.next = newH
            newH = cur
            cur = temp
        return newH
