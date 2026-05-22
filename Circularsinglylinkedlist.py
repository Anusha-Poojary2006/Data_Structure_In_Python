class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class circularlinkedlist:
    def __init__(self):
        self.tail=None
    def insert_at_beginning(self,data):
        new_node=node(data)
        if(self.tail==None):
            self.tail=new_node
            new_node.next=new_node
            return
        new_node.next=self.tail.next
        self.tail.next=new_node

    def insert_at_end(self,data):
        new_node=node(data)
        if(self.tail==None):
            self.tail=new_node
            new_node.next=new_node
            return
        new_node.next=self.tail.next
        self.tail.next=new_node
        self.tail=new_node

    def delete_at_end(self):
        if(self.tail==None):
            print("List is empty")
            return
        if(self.tail.next==self.tail):
            self.tail=None
            return
        current_node=self.tail.next
        while(current_node.next!=self.tail):
            current_node=current_node.next
        current_node.next=self.tail.next
        self.tail=current_node

    def delete_at_start(self):
        if(self.tail==None):
            print("List is empty")
            return
        if(self.tail.next==self.tail):
            self.tail=None
            return
        temp=self.tail.next
        self.tail.next=temp.next
        temp=None


    def printList(self):
        if(self.tail==None):
            print("List is empty")
            return
        current_node=self.tail.next
        while(True):
            print(f"{current_node.data}->",end="")
            current_node=current_node.next
            if(current_node==self.tail.next):
                break
        print("\n")
    
    def search(self,key):
        if(self.tail==None):
            print("List is empty")
            return
        current_node=self.tail.next
        while(True):
            if(current_node.data==key):
                print("key found")
                return
            current_node=current_node.next
            if(current_node==self.tail.next):
                break
        print("Key not found")


if __name__=="__main__":
    list=circularlinkedlist()
    while(1):
        print("\n-----Circular linked list demo-----")
        print("1.Insert a node at start")
        print("2.Insert a node at end")
        print("3.Delete a node at start")
        print("4.Delete a node at end")
        print("5.Search key in list")
        print("6.print list")
        print("7.Exit")

        choise=int(input("Enter your choise:"))
        match choise:
            case 1:
                data=int(input("Enter a data:"))
                list.insert_at_beginning(data)
            case 2:
                data=int(input("Enter a data:"))
                list.insert_at_end(data)
            case 3:
                list.delete_at_start()
            case 4:
                list.delete_at_end()
            case 5:
                key=int(input("Enter a key element to search:"))
                list.search(key)
            case 6:
                print("Elements of the list:")
                list.printList()
            case 7:
                exit(0)
            case _:
                print("Enter a valid choice")

    
        


        