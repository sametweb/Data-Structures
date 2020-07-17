def reverse(ll):
    if ll.head is None:
        return ll

    if ll.head is ll.tail:
        return ll

    current = ll.head
    previous = None
    next_node = None
    while current is not None:
        next_node = current.get_next()

        current.set_next(previous)
        
        previous = current
        current = next_node
    
    ll.head, ll.tail = ll.tail, ll.head