# Table of content

1. [Tuple](#tuple)
    1. [Top 5 methods](#top-5-methods)

---
# Tuple

A tuple in Python is an ordered collection of items that is immutable, meaning its elements cannot be changed after the tuple is created. Tuples are defined by enclosing elements in parentheses `()`, with elements separated by commas. They can hold items of different data types (heterogeneous). 

Methods and Built-in Functions Applicable to Tuples:

While tuples are immutable and therefore do not have methods that modify their contents, several built-in functions and methods can be used with them for information retrieval or manipulation of their elements (by creating new objects).

# Top 5 methods

1. `count(value)` Count specified element occurence.
### Example:
```python
tup=(1,2,3,'A', "Rohit",'A')
count=tup.count('A')
print(count) # Output: 2
```
### Output:
```python
2
```

2. `index(value, start, end)`: Searches the tuple for a specified value and returns the index of its first occurrence. Optional `start` and `end` arguments can limit the search range.
### Example:
```python
tup=(1,2,3,'A', "Rohit",'A')
index=tup.index('A')
print(index) # Output: 3
```
### Output:
```python
3
```

3. `sorted(iterable, key=None, reverse=False)`: A built-in function that returns a new sorted **list** from the items in the tuple. The original tuple remains unchanged.
### Syntax:
```python
sorted(iterable, key=None, reverse=False)
```
#### Parameters:
1. **`iterable`** *(required)*  
   - The sequence (tuple, list, string, etc.) to be sorted.  
   - Example:  
     ```python
     my_tuple = (3, 1, 4, 2)
     sorted_list = sorted(my_tuple)  # Returns [1, 2, 3, 4]
     ```

2. **`key=None`** *(optional)*  
   - A function that specifies a custom sorting criterion.  
   - The `key` function is applied to each element before sorting.  
   - Example (sorting strings by length):  
     ```python
     names = ("Alice", "Bob", "Charlie")
     sorted_names = sorted(names, key=len)  # Sorts by length: ['Bob', 'Alice', 'Charlie']
     ```

3. **`reverse=False`** *(optional)*  
   - If `True`, sorts in **descending** order.  
   - Default is `False` (ascending order).  
   - Example:  
     ```python
     numbers = (5, 2, 9, 1)
     sorted_desc = sorted(numbers, reverse=True)  # Returns [9, 5, 2, 1]
     ```

3. `max(tuple)` To get max value out of tuple.
#### Example:
```python
tup=(1,2,3)
maxNum=max(tup)
print(maxNum) # Output: 3
```
#### Output:
```python
3
```
> `max()` function won't work with different data types, only need single data type like `int` or `float`. Result in `TypeError`.

4. `min(tuple)` Find minimum value out of tuple.
#### Example:
```python
tup=(1,2,3)
minNum=min(tup)
print(minNum) # Output: 1
```
#### Output:
```python
1
```
> `max()` function won't work with different data types, only need single data type like `int` or `float`. Result in `TypeError`

5. `sum(tuple)` Return total sum of elements.
#### Example:
```python
tup=(1,2,3,4,5)
sumValue=sum(tup)
print(sumValue)
```
#### Output:
```css
15
```