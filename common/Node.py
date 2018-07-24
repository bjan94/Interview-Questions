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

