
A = [5, 10, 15, 20]
B = [3, 7, 13, 60]

# C now equals [3, 5, 7, 10, 13, 15, 20, 60]


def mergeLists(sorted_list_a, sorted_list_b):
    merged_list = []
    while len(sorted_list_a) > 0 and len(sorted_list_b) > 0:
        if sorted_list_a [0] < sorted_list_b[0]:
            merged_list.append(sorted_list_a.pop(0))
        else:
            merged_list.append(sorted_list_b.pop(0))
    if len(sorted_list_b) > 0:
        merged_list += sorted_list_b
    if len(sorted_list_a) > 0:
        merged_list += sorted_list_a
    return merged_list

C = mergeLists(A, B)
print(C)


#---Problem 2 ---------------


class Node:
    def __init__ (self,value):
        self.value = value
        self.next = None

class LList:
    def __init__(self):
        self.head = None
    def AddNode (self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def PrintReverse (self):
        temp = self.head
        while temp:
            print (temp.value)
            temp = temp.next

Linked_List = LList()
Linked_List.AddNode(1)
Linked_List.AddNode(2)
Linked_List.AddNode(3)
Linked_List.PrintReverse()



#---Problem 3 ---------------

class Node:
    def __init__ (self,value):
        self.value = value
        self.next = None

class LList:
    def __init__(self):
        self.head = None
    def AddNode (self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def PrintReverse (self):
        temp = self.head
        while temp:
            print (temp.value)
            temp = temp.next
    def reverse(self):
        list = LList()
        templ = self.head
        while templ:
            list.AddNode(templ.value)
            templ = templ.next
        return list

Linked_List = LList()
Linked_List.AddNode(1)
Linked_List.AddNode(2)
Linked_List.AddNode(3)
Linked_List.PrintReverse()
Reversed_Linked_List = Linked_List.reverse()
#Reversed_Linked_List.PrintReverse()

#Note: can create a function print later and print the values without the reverse
