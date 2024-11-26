stack = []
undo_stack = []  
redo_stack = []  

stack.append(10)
undo_stack.append(('push', 10))
stack.append(20)
undo_stack.append(('push', 20))
stack.append(30)
undo_stack.append(('push', 30))
print("Stack setelah push:", stack)

elemen = stack.pop()
undo_stack.append(('pop', elemen))
print("Elemen yang di-pop pertama:", elemen)
print("Stack setelah pop pertama:", stack)

if undo_stack:
    action, elemen = undo_stack.pop()
    if action == 'push':
        stack.pop()  
    elif action == 'pop':
        stack.append(elemen)  
    redo_stack.append((action, elemen))
    print("Stack setelah undo:", stack)

if redo_stack:
    action, elemen = redo_stack.pop()
    if action == 'push':
        stack.append(elemen)  
    elif action == 'pop':
        stack.pop()  
    undo_stack.append((action, elemen))
    print("Stack setelah redo:", stack)

print("Stack akhir:", stack)
