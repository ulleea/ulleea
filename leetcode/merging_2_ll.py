# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# # list1=ListNode(1,ListNode(2,ListNode(4)))
# # list2=ListNode(1,ListNode(3,ListNode(4)))
# list1=ListNode()
# list2=ListNode()
# print(list1.val)
# merged=ListNode()
# prev=merged
# while list1 and list2:
#     cur=ListNode()
#     prev.next=cur
#     if list1.val<list2.val:
#         prev.val=list1.val
#         list1=list1.next
#     else:
#         prev.val=list2.val
#         list2=list2.next
#     prev=prev.next
#
# if 'cur' in locals():
#     if list1:
#         cur.val=list1.val
#         cur.next=list1.next
#     elif list2:
#         cur.val=list2.val
#         cur.next=list2.next
# else:
#     if list1:
#         merged.val=list1.val
#         merged.next=list1.next
#     elif list2:
#         merged.val=list2.val
#         merged.next=list2.next
#
# while merged:
#     print(merged.val)
#     merged=merged.next
a=[5,4,3,2,1]
a.sort()
print(a)