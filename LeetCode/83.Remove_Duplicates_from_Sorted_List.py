# @Time    : 2021/8/12 15:18
# @Author  : lucas
# @File    : 83.Remove_Duplicates_from_Sorted_List.py
# @Project : locust demo
# @Software: PyCharm
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        point = head
        current = head.next
        new = point

        while point and current:
            if point.val != current.val:
                point = current
                new.next = current
                new = new.next
            current = current.next
        if not current:
            new.next = None
        return head


def create_link_list(list_: List) -> ListNode:
    point = ListNode()
    link = point
    for i in list_:
        point.next = ListNode(i)
        point = point.next
    return link.next


def print_nodes(node):
    while node:
        print(node.val)
        node = node.next
