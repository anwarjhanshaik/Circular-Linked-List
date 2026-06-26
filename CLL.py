class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class CLL:
  def __init__(self, tail=None):
    self.tail = tail
    self.size = 0

  def __len__(self):
    return self.size
    
  def __str__(self):
    if self.is_empty():
      return "List is empty"
    current = self.tail.next
    outPut = "=== LIST ITEMS ===\n"
    while True:
      outPut += f"{current.data} --> "
      current = current.next
      if current == self.tail.next:
        break
    outPut += "(Head)"
    return outPut
  
  def __iter__(self):
    if self.is_empty():
      return 
    current = self.tail.next
    while True:
      yield current 
      current = current.next
      if current == self.tail.next:
        break
  
  def is_empty(self):
    return self.tail == None
  
  def insert_at_start(self, item):
    node = Node(item)
    if self.is_empty():
      self.tail = node
      self.tail.next = self.tail
    else:
      node.next = self.tail.next
      self.tail.next = node
    self.size += 1
  
  def insert_at_last(self, item):
    self.insert_at_start(item)
    self.tail = self.tail.next
  
  def search(self, item):
    for node in self:
      if node.data == item:
        return node
    return None
  
  def insert_after(self, address, item):
    if address:
      node = Node(item, address.next)
      address.next = node
      if address == self.tail:
        self.tail = node
      self.size += 1
  
  def delete_first(self):
    if self.is_empty():
      return 
    if self.tail.next == self.tail:
      self.tail = None
    else:
      self.tail.next = self.tail.next.next
    self.size -= 1
  
  def delete_last(self):
    if self.is_empty():
      return 
    if self.tail.next == self.tail:
      self.tail = None
    else:
      current = self.tail.next
      while current.next != self.tail:
        current = current.next
      current.next = current.next.next
      self.tail = current 
    self.size -= 1
    
  def delete_after(self, address):
    if address:
      if address.next == address:
        return 
      deleted_node = address.next
      address.next = address.next.next
      if deleted_node == self.tail:
        self.tail = address
      self.size -= 1
      
  def delete_item(self, item):
    if self.is_empty():
      return 
    if self.tail.data == item and self.tail.next == self.tail:
      self.tail = None
      self.size = 0
      return 
    current = self.tail
    while True:
      if current.next.data == item:
        deleted_node = current.next
        current.next = current.next.next
        if deleted_node == self.tail:
          self.tail = current 
        self.size -= 1
        return 
      current = current.next
      if current == self.tail:
        break
  
  def reverse_list(self):
    if self.is_empty():
      return 
    if self.tail.next == self.tail:
      return self.tail
    old_head = self.tail.next
    next = None
    current = self.tail.next
    prev = self.tail
    while True:
      next = current.next
      current.next = prev
      prev = current 
      current = next
      if current == old_head:
        break
    self.tail = current 
    return self.tail
    
  def get_index(self, item):
    if not self.is_empty():
      index = 0
      current = self.tail.next
      while True:
        if current.data == item:
          return index
        current = current.next
        index += 1
        if current == self.tail.next:
          break
    return -1

  def get_item_at_index(self, index):
    if (self.is_empty() or (index < 0) or (index >= len(self))):
      raise IndexError("list index out of range")
    current = self.tail.next
    for i in range(index):
      current = current.next
    return current

  def insert_at_index(self, index, item):
    if index < 0:
      raise IndexError("list index out of range")
    if index == 0:
      self.insert_at_start(item)
    elif index >= len(self):
      self.insert_at_last(item)
    else:
      prev_node = self.get_item_at_index(index-1)
      node = Node(item, prev_node.next)
      prev_node.next = node
      self.size += 1

  def delete_at_index(self, index):
    if (self.is_empty() or (index < 0) or (index >= len(self))):
      raise IndexError("list index out of range")
    if index == 0:
      self.delete_first()
    elif index == len(self)-1:
      self.delete_last()
    else:
      prev_node = self.get_item_at_index(index-1)
      prev_node.next = prev_node.next.next
      self.size -= 1 

  def findMiddle(self):
    if self.is_empty():
      return 
    if self.tail.next == self.tail:
      return self.tail
    slow = self.tail.next
    fast = self.tail.next
    while fast.next != self.tail.next and fast.next.next != self.tail.next:
      slow = slow.next
      fast = fast.next.next
    return slow

  def delete_middle(self):
    if self.is_empty():
      return 
    if self.tail.next == self.tail:
      self.tail = None
    elif self.tail.next.next == self.tail:
      self.tail.next = self.tail
    else:
      prev = None
      slow = self.tail.next
      fast = self.tail.next
      while fast.next != self.tail.next and fast.next.next != self.tail.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
      prev.next = slow.next
    self.size -= 1

  def clear(self):
    self.tail = None
    self.size = 0
