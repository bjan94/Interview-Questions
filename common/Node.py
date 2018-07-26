class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        node_list = ""
        while self is not None:
            node_list += str(self.val) + " -> " if self.next else str(self.val)
            self = self.next

        return node_list

    def __eq__(self, other):
        return self.val == other.val

    def __gt__(self, other):
        return self.val > other.val

    def __ge__(self, other):
        return self.val >= other.val

    def __lt__(self, other):
        return self.val < other.val

    def __le__(self, other):
        return self.val <= other.val
