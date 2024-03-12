class Node:
    def __init__ (self,data=None):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.first =None
    def insertAtEnd(self,data):
        temp=None(data)
        temp.next=self.first
        self.first=temp
    def removeFirst(self):
        if(self.first==None):
            print("list is empty")
        else:
            cur=self.first
            self.first=self.first.next
            print("the deleted item is ",cur.data)
    def display(self):
        if(self.first==None):
            print("list is empty")
            return
            cur=self.first
            while(cur):
                print(cur.data,end=" ")
                cur=cur.next
    def Search(self,item):
        if(self.first==None):
            print("list is empty")
            return
        cur=self.firs
        while cur!=None:
            if cur.data==item:
                print("item is present in the linked list")
                return
            else:
                cur=cur.next
                print("item is not present in the linked list")
s1=SinglyLinkedList()
while(True):
    ch=int(input("\nEnter your choice 1-insert 2-delete 3-Search 4-display 5-exit:"))
    if(ch==1):
        item=input("Enter the element to insert:")
        s1.insertfirst(item)
        s1.display()
    elif(ch==3):
        item=input("Enter the element to Search:")
        s1.Search(item)
    elif(ch==4):
        s1.display()
    else:
        break
            
        
        
                
                    
                
            

