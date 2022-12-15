class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# def mergeKLists(lists):
#     """
#     :type lists: List[ListNode]
#     :rtype: ListNode
#     """
#     if lists==[] or lists==[[]]:
#         return[]
#     start = ListNode()
#     cur = start
#     k = len(lists)
#     while k!=1:
#         min = 0
#         for i in range(k):
#             if lists[i]:
#                 if lists[i].val < lists[min].val:
#                     min = i
#         cur.next = lists[min]
#         cur = cur.next
#         lists[min] = lists[min].next
#         if not lists[min]:
#             lists.pop(min)
#         k = len(lists)
#     cur.next = lists[0]
#     return start.next

list1=ListNode(1,ListNode(4,ListNode(5)))
list2=ListNode(1,ListNode(3,ListNode(4)))
list3=ListNode(2,ListNode(6,None))
# lists=[list1,list2,list3]
lists=[]
# for i in range(3):
#     print(lists[0].val)
#     lists[0]=lists[0].next
# print(lists[0].next)
# a=mergeKLists(lists)
# while a:
#     print(a.val)
#     a=a.next

from operator import attrgetter
def mergeKLists( lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    sorted_list = []
    for head in lists:
        curr = head
        while curr is not None:
            sorted_list.append(curr)
            curr = curr.next

    sorted_list = sorted(sorted_list, key=attrgetter('val'))
    for i, node in enumerate(sorted_list):
        try:
            node.next = sorted_list[i + 1]
        except:
            node.next = None

    if sorted_list:
        return sorted_list[0]
    else:
        print('-')
        return None
a=mergeKLists(lists)
while a:
    print(a.val)
    a=a.next