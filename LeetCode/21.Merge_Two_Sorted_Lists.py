# @Time    : 2021/7/8 13:25
# @Author  : lucas
# @File    : 21.Merge_Two_Sorted_Lists.py
# @Project : locust demo
# @Software: PyCharm
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: ListNode, l2: ListNode):
    current_node = ListNode()
    ml = current_node
    while l1 and l2:
        if l1.val > l2.val:
            current_node.next = l2
            l2 = l2.next
        else:
            current_node.next = l1
            l1 = l1.next
        current_node = current_node.next

    if l1:
        current_node.next = l1
    if l2:
        current_node.next = l2

    return ml.next


def create_link_list(list_: List) -> ListNode:
    point = ListNode()
    link = point
    for i in list_:
        point.next = ListNode(i)
        point = point.next
    return link.next


l1 = create_link_list([1, 2, 4])
l2 = create_link_list([1, 3, 4])

r = merge_two_lists(l1, l2)
while r:
    print(r.val)
    r = r.next
