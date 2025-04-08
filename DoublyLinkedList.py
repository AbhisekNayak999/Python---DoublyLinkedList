class Node:
    def __init__(self , data = None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertAtFirst(self , data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def appendAtLast(self , data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            current = self.head
            while current:
                if current.next is None:
                    current.next = node
                    break
                current = current.next

            node.prev = self.tail
            self.tail = node
        self.size += 1

    def InsertAtIndex(self , data , index):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = self.head
        elif self.size == index:
            self.appendAtLast(data)
        else:
            count = 0
            current = self.head

            while current.next is not None and count < index:
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node

        self.size += 1

    def InsertAfterAnElement(self, data,  element):

        if self.head is None:
            self.insertAtFirst(data)
        elif element == self.tail.data:
            self.appendAtLast(data)
        else:
            node = Node(data)
            current = self.head

            while current.data != element:
                current = current.next

            if current is None:
                print(f"The element {element} is not present in the Linked List")
            else:
                node.next = current.next
                node.prev = current
                current.next.prev = node
                current.next = node
        self.size += 1

    def InsertBeforeAnElement(self , data , element):

        if self.head is None or element == self.head.data:
            self.insertAtFirst(data)

        else:
            node = Node(data)
            current = self.head
            prev = self.head

            while current.data != element:
                if current.data != element:
                    prev = current
                current = current.next

            if current is None:
                print(f"The element {element} is not present in the Linked List")
            else:
                node.next = current
                node.prev = prev
                prev.next = node
                current.prev = node

        self.size += 1

    def Display(self):
        if self.head is None:
            print("There is no element in the linked list")
        else:
            current =  self.head

            while current:
                print(current.data , end=" -> ")
                current = current.next
            print()

    def Search(self , element):
        if self.head is None:
            print("There is no element in the linked list")
        else:
            current = self.head
            count = 1
            while current:
                if current.data == element:
                    print(f"The element {element} is present in the linked list at position {count}.")
                    break
                count += 1
                current = current.next

    def DeleteFromTheBeginning(self):
        current = self.head
        current.next.prev = None
        self.head = current.next
        self.size -= 1


    def DeleteAtTheEnd(self):
        current = self.tail
        current.prev.next = None
        self.tail = current.prev
        self.size -= 1

    def DeleteAtPosition(self , position):
        if position == 1:
            self.DeleteFromTheBeginning()
        elif position == self.size:
            self.DeleteAtTheEnd()
        else:
            count = 1
            current = self.head

            while count < position:
                if count+1 == position:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                current = current.next

    def DeleteTheElement(self , element):
        if element == self.head.data:
            self.DeleteFromTheBeginning()
        elif element == self.tail.data:
            self.DeleteAtTheEnd()
        else:
            current = self.head
            while current is not None:
                if current.data == element:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                current = current.next


obj = DoublyLinkedlist()

while True:
    print("The size of the current linked list is : ",obj.size)
    print('1>>Insert at beginning')
    print("2>>Insert at end")
    print("3>>Insert at any position")
    print("4>>Insert after a element")
    print("5>>Insert before a element")
    print("6>>Display the list")
    print("7>>Search element")
    print("8>>Delete from the beginning")
    print("9>>Delete at the end")
    print("10>>Delete at position")
    print("11>>Delete the element")
    print("12>>Exit")
    choice = int(input("Enter your choice : "))

    match choice:
        case 1:
            data = int(input("Enter the data: "))
            obj.insertAtFirst(data)
        case 2:
            data = int(input("Enter the data: "))
            obj.appendAtLast(data)
        case 3:
            data = int(input("Enter the data: "))
            position = int(input("Enter the position: "))
            obj.InsertAtIndex(data, position)
        case 4:
            data = int(input("Enter the data: "))
            element = int(input("Enter the element: "))
            obj.InsertAfterAnElement(data ,element)
        case 5:
            data = int(input("Enter the data: "))
            element = int(input("Enter the element: "))
            obj.InsertBeforeAnElement(data, element)
        case 6:
            obj.Display()
        case 7:
            element = int(input("Enter the element: "))
            obj.Search(element)
        case 8:
            obj.DeleteFromTheBeginning()
        case 9:
            obj.DeleteAtTheEnd()
        case 10:
            position = int(input("Enter the position: "))
            obj.DeleteAtPosition(position)
        case 11:
            element = int(input("Enter the element: "))
            obj.DeleteTheElement(element)
        case 12:
            print("Exiting......")
            break






















