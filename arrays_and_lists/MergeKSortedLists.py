from queue import PriorityQueue
from common.Node import ListNode

class Solver:
    """
    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

    Example:

    Input:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    Output: 1->1->2->3->4->4->5->6
    """
    def merge_k_lists(self, lists):
        head = point = ListNode(-1)
        pq = PriorityQueue()

        for l in lists:
            if l:
                pq.put((l.val, l))

        while not pq.empty():
            val, node = pq.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next

            if node:
                pq.put((node.val, node))

        return head.next


def main():
    solver = Solver()
    x = ListNode(1)
    x.next = ListNode(3)
    x.next.next = ListNode(5)

    y = ListNode(2)
    y.next = ListNode(7)
    y.next.next = ListNode(15)

    z = ListNode(1)
    z.next = ListNode(5)
    z.next.next = ListNode(10)
    z.next.next.next = ListNode(12)

    combined = [x, y, z]

    print(solver.merge_k_lists(combined))


if __name__ == "__main__":
    main()

