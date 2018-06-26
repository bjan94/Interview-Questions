import common.Node as ListNode


class Solver:
    """
    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

    Example:

    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
    """
    def merge_two_lists(self, l1, l2):
        node = ListNode(-1)
        start = node

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1 is not None:
            node.next = l1

        if l2 is not None:
            node.next = l2

        return start.next


def main():
    solver = Solver()
    print(solver.merge_two_lists(ListNode(1), ListNode(2)))


if __name__ == "__main__":
    main()
