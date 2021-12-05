# Delete alternate nodes of a Linked List

# Given a Singly Linked List, starting from the second node delete all alternate nodes of it. For example, if the given linked list is 1->2->3->4->5 then your function should convert it to 1->3->5, and if the given linked list is 1->2->3->4 then convert it to 1->3.

class Node :
    def __init__ ( self, data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
        
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next
            
    def deleteAlt ( self ) :
        if self.head.next != None :
            find_alt = self.head.next
            prev_alt = self.head
            while ( find_alt ) :
                prev_alt.next = find_alt.next
                if find_alt.next != None :
                    find_alt = find_alt.next.next
                    prev_alt = prev_alt.next
                else : break
                #find_alt.next = None

    def add ( self , data ) :
        if self.head != None :
            last = self.head
            end = self.head
            while ( end ) : 
                last = end
                end = end.next
            last.next = Node ( data )
        else : self.head = Node ( data )

llist = LinkedList()
llist.add ( 1 )
llist.add ( 2 )
llist.add ( 3 )
llist.add ( 4 )
llist.add ( 5 )
llist.deleteAlt ()
llist.printList()