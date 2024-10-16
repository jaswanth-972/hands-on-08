class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [0] * capacity
        self.top = -1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow!")
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow!")
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def size(self):
        return self.top + 1

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack contents:", end=" ")
            for i in range(self.top + 1):
                print(self.stack[i], end=" ")
            print()


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [0] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow!")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow!")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def front_element(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue contents:", end=" ")
            for i in range(self.size):
                print(self.queue[(self.front + i) % self.capacity], end=" ")
            print()


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        if not self.head:
            print("Linked list is empty!")
            return
        current = self.head
        print("Linked list contents:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:

# Stack operations
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.display()  # Display stack contents
print("Popped from stack:", stack.pop())  # Output: 20
stack.display()  # Display stack contents after pop

# Queue operations
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.display()  # Display queue contents
print("Dequeued from queue:", queue.dequeue())  # Output: 10
queue.display()  # Display queue contents after dequeue

# Singly Linked List operations
linked_list = SinglyLinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.display()  # Output: 10 -> 20 -> None
