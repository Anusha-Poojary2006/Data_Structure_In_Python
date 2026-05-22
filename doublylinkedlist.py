class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class doublylinkedlist:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new_node=node(data)
        if(self.head==None):
            self.head=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    
    def insert_at_end(self,data):
        new_node=node(data)
        if(self.head==None):
            self.head=new_node
            return
        current_node=self.head
        while(current_node.next!=None):
            current_node=current_node.next
        current_node.next=new_node
        new_node.prev=current_node

    def insert_at_givenPosition(self,data,position):
        new_node=node(data)
        if(self.head==None and position!=1):
            print("list is empty")
            return
        if(position==1):
            insert_at_beginning(data)
            return
        current_node=self.head
        current_position=1
        while(current_position<position-1 and current_node!=None):
            current_node=current_node.next
            current_position+=1
        if(current_node==None):
            print("can't insert at this position,there are less nodes")
            return
        new_node.next=current_node.next
        new_node.prev=current_node
        if(current_node.next!=None):
            current_node.next.prev = new_node
        current_node.next=new_node
        
    def delete_at_start(self):
        if(self.head==None):
            print("List is empty")
            return
        if(self.head.next==None):
            self.head=None
            return
        self.head=self.head.next
        self.head.prev=None

    def delete_at_end(self):
        if(self.head==None):
            print("list is empty")
            return
        if(self.head.next==None):
            self.head=None
        current_node=self.head
        while(current_node.next.next!=None):
            current_node=current_node.next
        current_node.next=None

    def delete_at_givenPosition(self,position):
        if(self.head==None):
            print("List is empty")
            return
        if(position==1):
            self.delete_at_start()
            return
        current_node=self.head
        current_position=1
        while(current_node!=None and current_position<position):
            current_node=current_node.next
            current_position+=1
        if(current_node==None):
            print("can't delete at this position,there are less nodes")
            return
        current_node.prev.next=current_node.next
        if(current_node.next!=None):
            current_node.next.prev=current_node.prev

    def printList(self):
        if(self.head==None):
            print("list is empty")
            return
        current_node=self.head
        print("head->",end="")
        while(current_node!=None):
            print(f"<-{current_node.data}->",end="")
            current_node=current_node.next
        print("None")

    def search(self,key):
        if(self.head==None):
            print("list is empty")
            return
        current_node=self.head
        while(current_node!=None):
            if(current_node.data==key):
                print("key is fouund")
                return
            current_node=current_node.next
        print("key is not found")

if __name__ =="__main__":
    list=doublylinkedlist()
    while(1):
        print("\n-----Doubly linked list demo-----")
        print("1.Insert a node at start")
        print("2.Insert a node at end")
        print("3.Insert a node at given position")
        print("4.Delete a node at start")
        print("5.Delete a node at end")
        print("6.Delete a node at given position")
        print("7.Search key in list")
        print("8.print list")
        print("9.Exit")

        choise=int(input("Enter your choise:"))
        match choise:
            case 1:
                data=int(input("Enter a data:"))
                list.insert_at_beginning(data)
            case 2:
                data=int(input("Enter a data:"))
                list.insert_at_end(data)
            case 3:
                data=int(input("Enter a data:"))
                position=int(input("Enter a position to insert a data:"))
                list.insert_at_givenPosition(data,position)
            case 4:
                list.delete_at_start()
            case 5:
                list.delete_at_end()
            case 6:
                position=int(input("Enter a position to delete:"))
                list.delete_at_givenPosition(position)
            case 7:
                key=int(input("Enter a key element to search:"))
                list.search(key)
            case 8:
                print("Elements of the list:")
                list.printList()
            case 9:
                exit(0)
            case _:
                print("Enter a valid choice")

    
        
