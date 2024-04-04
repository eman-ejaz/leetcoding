# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_linklist(self, head):
        curr = head
        prev = None

        while curr:
            next = curr.next

            curr.next = prev
            prev = curr
            curr = next


        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverse_linklist(slow)

        l, r = head, second_half

        while r:
            if l.val != r.val:
                return False
            
            l = l.next
            r = r.next

        

        return True

        # Brute Force

        # arr = []

        # curr = head

        # while curr:
        #     arr.append(curr.val)
        #     curr = curr.next
         
        # left, right = 0, len(arr) - 1

        # while left <= right:
        #     if arr[left] != arr[right]:
        #         return False
            
        #     left += 1
        #     right -= 1

        # return True

        
        