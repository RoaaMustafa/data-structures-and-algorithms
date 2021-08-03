from .linked_list import Node,LinkedList


def zipLists(llist1, llist2):
    current1 = llist1.head
    current2 = llist2.head

    if current1 == None or current2 == None:
        if current1:
            return llist1.__str__()
        elif current2:
            return llist2.__str__()
        else:
         return "Linked lists are both Empty "

    zip_list = []
    while current1 or current2:
        if(current1):
            zip_list+=[current1.value]
            current1 = current1.next
        if(current2):
            zip_list+=[current2.value]
            current2 = current2.next
    inital=''
    for item in zip_list:
      inital+=f'( {item} ) -> '
    inital+='None'
    return inital



if __name__ == "__main__":
    llist1 = LinkedList()
    llist1.append(1)
    llist1.append(3)
    llist1.append(5)
    llist1 = LinkedList()
    llist2.append(2)
    llist2.append(4)
    llist2.append(6)
    print(llist1.__str__())
    print(llist2.__str__())
    print(zipLists(llist1, llist2))
