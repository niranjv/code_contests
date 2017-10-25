# URL: https://leetcode.com/problems/add-two-numbers/description/
# 
# Description:
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return 'Node [{}, {}]'.format(self.val, self.next)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr_result = result_list = None
        ptr1 = l1
        ptr2 = l2

        quot = remainder = 0

        while ptr1 or ptr2 or quot:

            num1 = num2 = 0

            if ptr1:
                num1 = ptr1.val
                ptr1 = ptr1.next

            if ptr2:
                num2 = ptr2.val
                ptr2 = ptr2.next

            quot, remainder = divmod(quot + num1 + num2, 10)

            if ptr_result is None:
                result_list = ListNode(remainder)
                ptr_result = result_list
            else:
                ptr_result.next = ListNode(remainder)
                ptr_result = ptr_result.next

        return result_list


if __name__ == "__main__":

    o = Solution()
    l1 = ListNode(5)
    l1.next = ListNode(5)
    l1.next.next = ListNode(5)

    l2 = ListNode(5)
    l2.next = ListNode(5)
    # l2.next.next = ListNode(2)

    result = o.addTwoNumbers(l1, l2)
    print(result)

