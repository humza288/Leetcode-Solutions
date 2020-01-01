class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

x = ListNode(2)
x.next = ListNode(4)
x.next.next = ListNode(3)

y = ListNode(5)
y.next = ListNode(6)
y.next.next = ListNode(4)

z = []
s = ''
w = []
t = ''

current = x
while current:
    z.insert(0, str(current.val))
    current = current.next

current = y
while current:
    w.insert(0, str(current.val))
    current = current.next
    

s = int(s.join(z))
t = int(t.join(w))

l = str(s + t)
u = ''
for i in l:
    u = i + u

l = u

print(l)

final = ListNode(l[0])
current = final

for i in range(1, len(l)):
    current.next = ListNode(l[i])
    current = current.next


current = final
while current:
    print(current.val)
    current = current.next
        
    


