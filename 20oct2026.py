#circular queue
#part a
class SaleData:
    def __init__(self, SaleIDp, Quantityp):
        self.SaleID = SaleIDp
        self.Quantity = Quantityp

#part b
NumberOfItems = 0
Head = 0
Tail = 0
CircularQueue = []
for x in range(5):
    CircularQueue.append(SaleData("",-1))

#part c
def Enqueue(Record):
    global NumberOfItems, Tail
    if NumberOfItems == len(CircularQueue):
        return -1
    CircularQueue[Tail] = Record
    Tail = 0 if Tail == len(CircularQueue) - 1 else Tail + 1
    NumberOfItems += 1
    return 1

#part d
def Dequeue():
    global Head, NumberOfItems
    if NumberOfItems == 0:
        return SaleData("",-1)
    removed = CircularQueue[Head]
    CircularQueue[Head] = SaleData("",-1)
    Head = 0 if Head == len(CircularQueue) - 1 else Head + 1
    NumberOfItems -= 1
    return removed

#part e
def EnterRecord():
    id = input("ID: ")
    quantity = int(input("Quantity: "))
    inp = SaleData(id, quantity)
    if Enqueue(inp)==-1:
        print("Full")
    else:
        print("Stored")

#part f
def main():
    EnterRecord()
    EnterRecord()
    EnterRecord()
    EnterRecord()
    EnterRecord()
    EnterRecord()

    returnval = Dequeue()
    print(returnval.SaleID,returnval.Quantity)

    EnterRecord()

    for x in CircularQueue:
        print(x.SaleID, x.Quantity)

if __name__=="__main__":
    main()