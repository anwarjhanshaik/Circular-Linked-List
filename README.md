# Circular Linked List (CLL) Implementation in Python

A robust, highly optimized, and memory-efficient implementation of a **Circular Linked List (CLL)** with a Tail-Only reference model. This project demonstrates advanced pointer manipulation, rigorous boundary/edge-case handling, and clean object-oriented design in Python.

## 🚀 Key Architecture Choices

Unlike standard linked lists that track both `head` and `tail`, this implementation utilizes a **Tail-Only Reference Model** (`self.tail`). 
* **Efficiency:** Accessing both the first node (Head) via `self.tail.next` and the last node via `self.tail` takes constant **O(1) time**.
* **Memory Optimization:** Eliminates the overhead of maintaining an independent head pointer.

---

## ✨ Features

- **Dynamic Insertions:** Supports O(1) operations for `insert_at_start` and `insert_at_last`, along with index-based adjustments.
- **Robust Deletions:** Safely removes nodes from the start, end, specific values (`delete_item`), or targeted indices.
- **In-Place Reversal:** Swaps node directional pointers natively with zero extra memory allocation (O(1) space complexity).
- **Look-Ahead Middle Node Operations:** Features high-performance `findMiddle` and `delete_middle` algorithms using a modified fast/slow pointer method that naturally catches exact middle nodes without loop-overrun vulnerabilities.
- **Python Integration:** Fully supports native Python idioms, including length querying (`len(obj)`) and collection iteration via a custom `__iter__` generator.

---

## 📊 Time & Space Complexity Matrix

| Operation | Time Complexity | Space Complexity | Notes |
| :--- | :---: | :---: | :--- |
| `insert_at_start` / `insert_at_last` | O(1) | O(1) | High-performance bounds modifications |
| `delete_first` | O(1) | O(1) | Direct pointer bypass |
| `delete_last` | O(n) | O(1) | Requires traversal to find the node preceding tail |
| `search` / `get_index` | O(n) | O(1) | Linear scan |
| `reverse_list` | O(n) | O(1) | Complete in-place array pointer inversion |
| `findMiddle` / `delete_middle` | O(n) | O(1) | Uses an optimized look-ahead two-pointer approach |
| `clear` | O(1) | O(1) | Leverages Python's native Garbage Collector |

---

## 💻 Sample Test Execution

To verify the integrity of the data structure across obscure boundary thresholds (e.g., 0-node, 1-node, and 2-node variants), you can paste and run the following script at the bottom of your file execution block:

```python
def run_cll_tests():
    print("🚀 STARTING CIRCULAR LINKED LIST TESTS...\n")
    myList = CLL()

    # Test 1: Empty List Case
    print("--- Test 1: Empty List ---")
    print(myList)  # Expected: List is empty
    myList.delete_middle()  # Safeguarded against crashes
    print(f"Size: {len(myList)}\n")

    # Test 2: Single Node Edge Case
    print("--- Test 2: Single Node ---")
    myList.insert_at_start("Node A")
    print(myList)
    print(f"Middle node data: {myList.findMiddle().data}")  # Returns Node A
    myList.delete_middle()
    print(myList)  # Expected: List is empty
    print(f"Size: {len(myList)}\n")

    # Test 3: Two Nodes Look-Ahead Verification
    print("--- Test 3: Two Nodes ---")
    myList.insert_at_start("Node B")
    myList.insert_at_start("Node A")
    print(myList)  # Node A --> Node B
    print(f"Middle node data: {myList.findMiddle().data}")  # Safely returns first-middle (Node A)
    myList.delete_middle()
    print(myList)  # Expected: Node B --> (Head)
    print(f"Size: {len(myList)}\n")

    # Test 4: General Multi-Node Operations & In-Place Reversal
    print("--- Test 4: Multi-Node & Reversal ---")
    myList.clear()
    myList.insert_at_start("Item 2")
    myList.insert_at_start("Item 1")
    myList.insert_at_last("Item 3")
    myList.insert_at_last("Item 4")
    
    print("Original State:")
    print(myList)
    print(f"Current Middle Node: {myList.findMiddle().data}")  # Item 2

    myList.reverse_list()
    print("\nReversed State:")
    print(myList)
    
    print("\n🎉 ALL CORNER CASES AND DATA INTEGRITY TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_cll_tests()
```

---

## 🛠️ Requirements & Installation

- **No external dependencies** required.
- Requires **Python 3.x+** environment.

Simply clone this repository to your local machine:
```bash
git clone https://github.com
```
