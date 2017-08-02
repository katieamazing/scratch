# Definition for singly-linked list:
 class ListNode(object):
   def __init__(self, x):
     self.value = x
     self.next = None

    def filter_k_out(self, k):
        if self.next == None:
            if self.value == k:
                return None
            else:
                return self
        else:
            filtered = l.next.filter_k_out(k)
            if l.value == k:
                print(filtered)
                return filtered
            else:
                head = new ListNode(self.value)
                head.next = filtered
                return head

    def reverse(self):
        if self.next == None:
            return self
        else:
            rest_reversed = self.next.reverse()
            return rest_reversed.append(self.value)

    def append(self, new_value):
        if self.next == None:
            self.next = new ListNode(new_value)
            return self
        else:
            self.next.append(new_value)
            return self
