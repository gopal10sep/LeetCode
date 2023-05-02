# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. Add Two Numbers
# Medium

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.



# 1. Iterative Solution:
# In the iterative solution, we traverse both linked lists simultaneously, adding corresponding digits and carrying over any excess to the next place value. We keep track of the current digit and the carry.

# Time Complexity: O(max(N, M)), where N and M are the lengths of the two linked lists.
# Space Complexity: O(max(N, M)), as the new linked list will have at most max(N, M) + 1 nodes.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    

# 2. Recursive Solution:
# In the recursive solution, we recursively traverse the linked lists, adding corresponding digits and propagating any carry to the next recursive call.

# Time Complexity: O(max(N, M)), where N and M are the lengths of the two linked lists.
# Space Complexity: O(max(N, M)) for the recursive call stack.
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def helper(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None

            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            node = ListNode(sum % 10)
            carry = sum // 10

            l1_next = l1.next if l1 else None
            l2_next = l2.next if l2 else None

            node.next = helper(l1_next, l2_next, carry)
            return node

        return helper(l1, l2, 0)


# 3. Stack Solution:
# In the stack solution, we use two stacks to store the digits of the two linked lists in reverse order. We then pop digits from the stacks, adding them together while considering any carry, and construct the result linked list in reverse order.

# Time Complexity: O(max(N, M)), where N and M are the lengths of the two linked lists.
# Space Complexity: O(N + M), where N and M are the lengths of the two linked lists.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None



# It's worth noting that the time complexity is the same for all three approaches, as they all involve visiting each node once. The space complexity may vary slightly depending on the approach.


       
