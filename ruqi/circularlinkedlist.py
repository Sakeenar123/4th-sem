# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:45:19 2024

@author: Language Lab
"""

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class circularlinkedlist:
    def __init__(self):
        self.first=None
    def insert (self,data):
        temp=node(data)
        if(self.first==None):
            self.first=temp
            self.first.next=temp
        else:
            cur=self.first
            while(cur.next!=self.first):
                cur=cur.next
            cur.next=temp
            temp.next=self.first
    def delete(self):
        if(self.first==None):
            print("list is empty")
        elif(self.first.next==self.first):
            print("the deleted item is",self.first.data)
            self.first=None
        else:
            cur=self.first
            while(cur.next!=self.first):
                pr=cur
                cur=cur.next
            pr.next=self.first
            print("the deleted item is",cur.data)
    def display(self):
        if(self.first==None):
            print("list is empty")
            return
        cur=self.first
        while(True):
            print(cur.data,end=" ")
            cur=cur.next
            if(cur==self.first): 
              break
c1=circularlinkedlist()
while(True):
    ch=int(input("enter your choice 1_insert 2_delete 3_display 4_exit:"))
    if(ch==1):
        item=input("enter the element to insert")
        c1.insert(item)
        c1.display()
        print()
    elif(ch==2):
        c1.delete()
        c1.display()
        print()
    elif(ch==3):
        c1.display()
        print()
    else:
        break
    