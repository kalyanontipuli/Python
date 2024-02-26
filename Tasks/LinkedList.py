class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():

    def __init__(self):
        self.head=None
    
    def print_linkedlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data,end=' ')
            curr=curr.next
        print()
    
    def add(self,e):
        temp=Node(e)
        
        if self.head==None:
            self.head = temp
            
        else:
            curr=self.head
            while(curr.next !=None):
                curr=curr.next
            curr.next=temp

    def addFirst(self,ele):
        temp=Node(ele)

        if self.head==None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp

    def addAll(self,elements):
        for element in elements:
            self.add(element)

    def addIndex(self,index,ele):
        try:
            if index==0:
                self.addFirst(ele)
            else:
                temp=Node(ele)
                count=0
                curr=self.head
                while count<index-1:
                    curr=curr.next
                    count+=1
                
                temp.next=curr.next
                curr.next=temp
        except AttributeError:
            raise IndexError("Index {} does not exist".format(index))
        
    def removeFirst(self):
        if self.head==None:
            print('No elements in linkedlist')
        elif self.head.next==None:
            head=None
        else:
            curr=self.head
            self.head=self.head.next
            curr.next=None

    def removeLast(self):
        if self.head==None:
            print('No elements in linked list ')
        elif self.head.next==None:
            self.head=None
        else:
            curr=self.head
            while(curr.next.next!=None):
                curr=curr.next
            curr.next=None 


    def remove(self,ele):
        self.isRemoved=False
        if self.head==None:
            print('No elements in Linkedlist')
        elif self.head.next==None:
            if self.head.data==ele:
                self.removeFirst()
                self.isRemoved=True
        else:
            if(self.head.data==ele):
               self.removeFirst()
               self.isRemoved=True
            else:
                curr=self.head
                while(curr.next!=None):
                    if curr.next.data==ele:
                        if curr.next.next==None:
                            self.removeLast()
                            self.isRemoved=True
                            break
                        else:
                            temp=curr.next
                            curr.next=curr.next.next
                            temp.next=None
                            self.isRemoved=True
                            break
                    curr=curr.next
        if self.isRemoved==False:
            print('No such element found to delete :')    


def main():
    l = LinkedList()
    list=[10,20,30,40]
    l.addAll(list)
    l.print_linkedlist()
    l.remove(10)
    l.print_linkedlist()

    
main()
