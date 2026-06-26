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

    

# ==========================================
# ANONYMISED TEST SCRIPT FOR YOUR CLL IMPLEMENTATION
# ==========================================

def run_cll_tests():
    print("🚀 STARTING CIRCULAR LINKED LIST TESTS...\n")
    myList = CLL()

    # Test 1: Empty List Case
    print("--- Test 1: Empty List ---")
    print(myList)  # Should print "List is empty"
    print(f"Middle of empty list: {myList.findMiddle()}")  # Should print None
    myList.delete_middle()  # Should not crash
    print(f"Size: {len(myList)}\n")

    # Test 2: Single Node Case
    print("--- Test 2: Single Node ---")
    myList.insert_at_start("Node A")
    print(myList)
    print(f"Middle node data: {myList.findMiddle().data}")  # Should be Node A
    print("Deleting middle of single-node list...")
    myList.delete_middle()
    print(myList)  # Should print "List is empty"
    print(f"Size: {len(myList)}\n")

    # Test 3: Two Nodes Case
    print("--- Test 3: Two Nodes ---")
    myList.insert_at_start("Node B")
    myList.insert_at_start("Node A")
    print(myList)  # Node A --> Node B
    print(f"Middle node data: {myList.findMiddle().data}")  # Should be Node A
    print("Deleting middle node...")
    myList.delete_middle()
    print(myList)  # Should leave only Node B --> (Head)
    print(f"Size: {len(myList)}\n")

    # Test 4: General Multi-Node Operations
    print("--- Test 4: General Multi-Node Operations ---")
    myList.clear()
    myList.insert_at_start("Item 2")
    myList.insert_at_start("Item 1")
    myList.insert_at_last("Item 3")
    myList.insert_at_last("Item 4")
    
    x = myList.search("Item 4")
    myList.insert_after(x, "Item 5")
    
    print("Original List:")
    print(myList)  # Expected: Item 1 --> Item 2 --> Item 3 --> Item 4 --> Item 5
    print(f"Current Size: {len(myList)}")
    print(f"Current Middle Node: {myList.findMiddle().data}\n")  # Expected: Item 3

    # Test 5: Reversal
    print("--- Test 5: Reversing List ---")
    myList.reverse_list()
    print("Reversed List:")
    print(myList)  # Expected: Item 5 --> Item 4 --> Item 3 --> Item 2 --> Item 1
    print(f"Middle Node after reversal: {myList.findMiddle().data}\n")  # Expected: Item 3

    # Test 6: Deleting Middle Node on Odd List (Size 5)
    print("--- Test 6: Deleting Middle Node ---")
    myList.delete_middle()
    print("List after deleting middle ('Item 3'):")
    print(myList)  # Expected: Item 5 --> Item 4 --> Item 2 --> Item 1
    print(f"New Size: {len(myList)}")
    print(f"New Middle Node: {myList.findMiddle().data}\n")  # Expected: Item 4

    # Test 7: Indexing and Boundary Checks
    print("--- Test 7: Index Access ---")
    print(f"Item at index 0: {myList.get_item_at_index(0).data}")  # Item 5
    print(f"Item at index 2: {myList.get_item_at_index(2).data}")  # Item 2
    print(f"Index of 'Item 1': {myList.get_index('Item 1')}")  # 3
    print(f"Index of missing item 'Missing': {myList.get_index('Missing')}\n")  # -1

    # Test 8: Index-Based Insertion & Deletion
    print("--- Test 8: Index Operations ---")
    print("Inserting 'New Mid' at index 2...")
    myList.insert_at_index(2, "New Mid")
    print(myList)
    print("Deleting item at index 0 (Item 5)...")
    myList.delete_at_index(0)
    print(myList)
    print(f"Final Size: {len(myList)}\n")

    print("🎉 ALL TESTS EXECUTED SUCCESSFULLY WITHOUT CRASHES!")

# Execute the test function
run_cll_tests()


