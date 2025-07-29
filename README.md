# Table of content
1. [Syllabus overview](#syllabus-overview)
2. [Installation process](#installation-process)
3. [Why Python language?](#why-python-language)
4. [Command line basics](#Windows-command-line-basics)
5. [Data types](#data-types)
6. [Operators](#operators)
7. [Variable assignments](#Variable-assignments)
	- [Rules for variable assignment](#valid-rules-for-naming-variables-in-python)
8. [Strings](#strings)
	- [Top 10 string methods](#top-10-string-methods)
	- [Print formatting with string](#print-formatting-with-string)
	- [Float formatting with f-string](#float-formatting-with-f-string)
9. [List](#list)
	- [Top 10 list methods](#top-10-list-methods)
10. [Dictionary](#dictionary)
	- [Top 6 dictionary methods](#top-10-dictionary-methods)
11. [List](#list)
12. [Tuples](#tuples)
13. [Set](#set)
14. [Files](#files)
15. [Guess the number game](#guess-the-number-game)

---
# Syllabus overview

1. Python 2 vs Python 3
2. Python installation
3. Environment selection
4. Jupyter notebook
5. Git & Github
6. Object & data structure basics
    - Numbers
    - Strings
    - List
    - Dictionary
    - Tuples
    - Files
    - Sets
    - Booleans
7. Comparison operator
    - Basic operators
    - Chained comparison operators
8. Python statement
    - `if`, `elif`, `else`
    - `for` loops
    - `while` loops
    - `range()`
    - List comprehension
9. Methods & functions
    - Methods
    - Functions
    - Lambda expressions
    - Nested statement
    - Scope
10. Create a game in python
11. OOP
    - Objects
    - Classes
    - Methods
    - Inheritance
    - Special methods
12. Error and exceptional handling
    - Error
    - Exception
    - try
    - except
    - finally
13. Create a more complex game in python
14. Modules & packages
    - Create modules
    - Installing modules
    - Exploring python ecosystem
15. Build in functions
    - `map`
    - `reduce`
    - `filter`
    - `zip`
    - `enumerate`
    - `all, any`
    - Complex
16. Decorators in python
17. Python generators
    - Iteration vs generation
    - Creating generators
18. Final capstone project
19. Advance bonus contents
    - Advance python modules
    - Advance python objects and data structure

---
# Installation process

## :desktop_computer: For windows:

#### Step 1: Download Python

1. Go to the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
    
2. Click on the **Download Python 3.x.x** button (it detects your OS automatically).
#### Step 2: Run the Installer

1. Open the downloaded `.exe` file.
    
2. **Important**: Check the box that says **"Add Python to PATH"**.
    
3. Click **"Install Now"** (or choose "Customize Installation" if you want advanced options).
#### Step 3: Verify Installation

1. Open **Command Prompt**.
    
2. Type:
```python
python --version
```
or
```python
python3 --version
```
You should see something like:
```python
Python 3.12.0
```

## For macOS:

#### Step 1: Use the Official Installer (Recommended for Beginners)

1. Go to [https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/)
    
2. Download the latest `.pkg` installer.
    
3. Open it and follow the installation instructions.
    

#### Step 2: Add Python to PATH (if needed)

- macOS often includes Python, but it might be Python 2.x.
    
- Open **Terminal** and type:
```python
python3 --version
```
- If it’s not installed or outdated, consider using **Homebrew**:
#### Optional: Install with Homebrew (Advanced)
```python
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

### **For Linux (Ubuntu/Debian)**

#### Step 1: Check if Python is Installed

- Open Terminal and type:
```python
python3 --version
```
#### Step 2: Install (if needed)
```python
sudo apt update
sudo apt install python3
```
### Step 3: Install pip (Python package manager)
```python
sudo apt install python3-pip
```

## ✅ **Post-Installation: Check Everything**

1. **Open terminal/command prompt**
    
2. Run:
```python
python --version
pip --version
```

---
# Virtual environment

## **Step 1:** Open your project folder

1. Launch `vs code`
2. Open the folder where you want to create the virtual environment:
	- `File`>`Open folder`
## **Step 2:**

1. Open `terminal`
## Windows:
```python
python -m venv venv
```
> This creates a folder named `venv` in your project directory

## **Step 3**: Activate the `virtual environment`

### Windows(CMD):
```python
venv\Scripts\activate
```
### Windows(Powershell):
```python
.\venv\Scripts\Activate.ps1
```
> After activation, your terminal prompt should show something like: `(venv)`

## **Step 4:** Select the Interpreter in VS Code

1. Press `Ctrl+Shift+P` to open Command Palette.
    
2. Type and select: `Python: Select Interpreter`
    
3. Choose the interpreter from the `.venv` folder, usually like:
```python
.\venv\Scripts\python.exe
```

## **Step 5:** Install Packages Inside the Virtual Environment

Once activated, use pip as usual:
```python
pip install flask
```
> Packages will install only inside the virtual environment.

### File structure

your-project/
├── venv/                  # Virtual environment (usually ignored in version control)
├── main.py                # Your main Python script
├── .env                   # For environment variables like API keys
├── requirements.txt       # Dependency list
└── .gitignore             # Ignore files/folders in Git


---
# Why `python` language

**Python is a beginner-friendly and highly versatile programming language, making it easy to learn and implement across various domains.** From web development and automation to data science and machine learning, Python is used virtually everywhere. Its clean syntax and vast ecosystem of libraries make it suitable for both simple tasks and complex projects.

In real-life applications, Python can help you:

- **Organize your digital files**: Automatically sort documents, photos, videos, and other files into appropriate folders based on type, name, or creation date.
    
- **Automate repetitive tasks**: Clean temporary files, rename batches of files, or schedule regular backups of important data.
    
- **Build intelligent tools**: Create your own AI agents or chatbots using frameworks like `LangChain`, `OpenAI API`, or `Rasa`.
    
- **Detect faces or objects**: Use OpenCV to build face detection systems or security monitoring apps.
    
- **Scrape data from websites**: Collect product data, reviews, or prices from sites like Amazon or Flipkart using libraries like `BeautifulSoup`, `Scrapy`, or `Selenium`.
    
- **Analyze and visualize data**: Use `Pandas`, `NumPy`, and `Matplotlib` to process and visualize large datasets for insights and decision-making.
    
- **Create web apps**: Develop scalable web applications using frameworks like `Django` or `Flask`.
    
- **Develop games**: Use `Pygame` to build 2D games for learning and entertainment.
    
- **Build desktop applications**: Use `Tkinter`, `PyQt`, or `Kivy` to create user-friendly software interfaces.
    
- **Control IoT devices**: Integrate Python with Raspberry Pi to automate home appliances or build smart home solutions.
    
- **Automate browser actions**: Fill out forms, log into accounts, and perform web tasks with `Selenium` or `Playwright`.
    
- **Monitor stock prices or cryptocurrencies**: Pull real-time financial data and automate trading strategies.
    

For example, if your friend asks for a list of the best laptops under $5000, you can write a Python script to scrape laptop listings from Amazon or Flipkart, extract details like price, brand, and features, and save the results in an Excel file using the `openpyxl` or `pandas` library to share easily.

---
# Windows command line basics

## 🖥️ **1. Opening Command Prompt**

- Press `Win + R`, type `cmd`, and press `Enter`
    
- Or search “Command Prompt” from the Start menu

## 📁2. Navigation commands:

| Command | Description                                      |
| ------- | ------------------------------------------------ |
| `dir`   | Lists files and folders in the current directory |
| `cd`    | Changes directory (e.g., `cd foldername`)        |
| `cd ..` | Moves up one directory level                     |
| `cd \`  | Goes to the root directory                       |
| `cls`   | Clears the screen                                |
## 📂 3. Working with Files and Folders

| Command                    | Description                   |
| -------------------------- | ----------------------------- |
| `mkdir newfolder`          | Creates a new folder          |
| `rmdir foldername`         | Removes a folder (empty only) |
| `del filename.txt`         | Deletes a file                |
| `copy file1.txt file2.txt` | Copies file1 to file2         |
| `move file1.txt C:\Backup` | Moves a file to a folder      |
## ⚙️ 4.  Running Programs and Scripts

| Command         | Description                                    |
| --------------- | ---------------------------------------------- |
| `program.exe`   | Runs an executable (if in PATH or current dir) |
| `start notepad` | Opens Notepad                                  |
| `yourfile.bat`  | Runs a batch script                            |
| `exit`          | Closes the Command Prompt window               |

## 🔍 5. Helpful Tips

- Press **Tab** to auto-complete file or folder names.
    
- Use the **up/down arrow keys** to scroll through previous commands.
    
- Use `help` to get a list of available commands.

---
# Data types

| Name       | Type  | Description                                                            | Example                                                                                                                                                                                                   |
| ---------- | ----- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Integer    | `int` | Whole number such as 1,2,3,4 etc. which doesn't hold any fraction part | ```<br>age=20<br>print(age) # Output: 20<br>print(type(age)) # Output: <class 'int'><br>```                                                                                                               |
| Float      | float | Fraction number such as 1.5, 10.0                                      | ```<br>height=10.5<br><br>print(height) # Output: 10.5<br><br>print(type(height)) # Output: <class 'float'><br>```                                                                                        |
| String     | str   | Collection of characters such as `Ramesh`, `Pooja`                     | ```<br>name="Pooja"<br><br>print(name) # Output: Pooja<br><br>print(type(name)) # Output: <class 'str'><br>```                                                                                            |
| List       | list  | Collection of homogeneous or heterogeneous data types.                 | ```<br>cities=["Mumbai", "Pune", 200, 100]<br><br>print(cities) # Output: ['Mumbai', 'Pune', 200, 100]<br><br>print(type(cities)) # Output: <class 'list'><br>```                                         |
| Dictionary | dict  | Unordered `key:value` pair.                                            | ```<br>cityWithPopulation={"Mumbai": 100, "Pune": 200}<br><br>print(cityWithPopulation) # Output: {'Mumbai': 100, 'Pune': 200}<br><br>print(type(cityWithPopulation)) # Output: <class 'dict'><br>```     |
| Tuples     | tup   | Order immutable sequence of objects.                                   | ```<br>cities=("Mumbai", "Pune", 100, 200)<br><br>print(cities) # Output: ('Mumbai', 'Pune', 100, 200)<br><br>print(type(cities)) # Output: <class 'tuple'><br>```                                        |
| Sets       | set   | Unordered collection of unique objects.                                | ```<br>alpha={"a", "b", "c", "c"}<br><br>print(alpha) # Output: {'a', 'b', 'c'}<br><br>print(type(alpha)) # Output: <class 'set'><br>```                                                                  |
| Booleans   | bool  | Logical value indicate `True` or `False`                               | ```<br>yes=True<br><br>no=False<br><br>print(yes) # Output: True<br><br>print(type(yes)) # Output: <class 'bool'><br><br>print(no) # Output: False<br><br>print(type(no)) # Output: <class 'bool'><br>``` |

---
# Operators

Operators are special symbols or keywords used to perform operations on variables and values.

|Operator|Description|Example|Output|
|---|---|---|---|
|`+`|Addition|`5 + 3`|`8`|
|`-`|Subtraction|`5 - 2`|`3`|
|`*`|Multiplication|`4 * 3`|`12`|
|`/`|Division (float)|`10 / 4`|`2.5`|
|`//`|Floor Division|`10 // 4`|`2`|
|`%`|Modulus (remainder)|`10 % 3`|`1`|
|`**`|Exponentiation|`2 ** 3`|`8`|

# Variable assignments

Variable assignments means assigning name, number, string to variable. For example, if you have name called _Rohit_ that means _Rohit_ name assigned to you when you get born. Similarly in programming language assigning value to variable useful for future use.

#### Example 1:
```python
name="Rohit"

age=21

weight=65.80

print("Name:", name)

print("Age:", age)

print("Weight:", weight)
```
#### Output:
```python
Name: Rohit
Age: 21
Weight: 65.8
```

![Diagram_1](./Resources/Diagram_1.png)
*Diagram 1*

> When you assign particular value to 2 or more variable on that time single data reference is shared to that 2 variable instead of creating individual object. See above `Diagram 1`. To check reference number, you can use `id()` method.

#### Example:
```python
name="Rohit"

myName="Rohit"

print(id(name))

print(id(myName))
```
#### Output:
```python
2391358551936
2391358551936
```
---
# ✅ Valid Rules for Naming Variables in Python

1. **Must begin with a letter (A-Z, a-z) or an underscore `_`**
    
    - Examples: `name`, `_value`, `age1`
        
2. **Can contain letters, digits (0-9), and underscores**
    
    - Valid: `user_name`, `value1`, `x_2_y`
        
3. **Cannot start with a digit**
    
    - ❌ Invalid: `1name`, `3_value`
        
4. **Cannot be a Python keyword or reserved word**
    
    - ❌ Invalid: `class`, `def`, `for`, `if`, `while`, etc.
        
    - Use `import keyword; print(keyword.kwlist)` to see all keywords.
        
5. **Python is case-sensitive**
    
    - `score`, `Score`, and `SCORE` are three different variables.
        

---

#### ✅ **Best Practices (Conventions)**

- Use **lowercase letters** and **underscores** for readability (PEP 8 style guide):
```python
total_amount = 100
user_name = "Alice"
```
- Use **UPPER_CASE** for constants (by convention):
```python
MAX_USERS = 50
```

---
# Strings

String is collection of characters. It can your name, address, pet name etc. Written in single quote `''` or double quote `""`. For example `name='Ramesh'` or `name="Ramesh"`. Strings are ordered sequences so it can be accessed through indexing. Indexing start from `0` to `n-1`. Negative indexing also exist in python language. To access particular character from string you can use `[]` square brackets. For example `myName[0]`. `myName` variable contains `Rohit` string, if you print `myName[0]` this would result in  `R`, because `R` is stored at `0` index. If you give negative index like `-10`, `-20`, this would print character from back to front.

#### Example:
```python
myName="Rohit"

print(myName[0]) # Output: R

print(myName[1]) # Output: o

print(myName[2]) # Output: h

print(myName[3]) # Output: i

print(myName[4]) # Output: t

print(myName[5]) # Output: IndexError: string index out of range

print(myName[-1]) # Output: t

print(myName[-2]) # Output: i

print(myName[-3]) # Output: h

print(myName[-4]) # Output: o

print(myName[-5]) # Output: R

print(myName[-6]) # Output: IndexError: string index out of range

print(myName[0:3]) # Output: Roh

print(myName[1:4]) # Output: ohi

print(myName[2:5]) # Output: hit

print(myName[3:6]) # Output: it

print(myName[0:6]) # Output: Rohit

print(myName[0:7]) # Output: Rohit

print(myName[0:8]) # Output: Rohit

print(myName[0:9]) # Output: Rohit

print(myName[0:10]) # Output: Rohit

print(myName[0:11]) # Output: Rohit

print(myName[0:12]) # Output: Rohit

print(myName[0:13]) # Output: Rohit

print(myName[0:14]) # Output: Rohit
```

---
# Top 10 `String` methods

1. `upper()` Convert all characters into uppercase.
```python
name="rohit"
print(name.upper()) # Output: ROHIT
```
2. `lower()` Converts all characters in lower case.
```python
name="ROHIT"
print(name.lower()) # Output: rohit
```
3. `strip()` Removes leading(starting) & trailing(Ending) whitespaces.
```python
name="    Rohit    "
print(name.strip()) # Output: Rohit
```
4. `replace("old","new")` Replace all occurence of substring with another.
```python
name="Rohit"
print(name.replace("R","M")) # Output: Mohit
```
5. `split(separator)` Split the string into list of substring. `separator` can be`,`, `.`, ` `.
```python
name="Rohit,Sharma"
nameList=name.split(",")
print(nameList) # Output: ["Rohit", "Sharma"]
print(type(nameList)) # Output: <class 'list'>
```

6. `join(iterable)` Joins elements of an iterable into single string.
```python
source="D:/Country"
myFolderLocation="States"
fullPath="/".join([source, myFolderLocation])
print(fullPath) # Output: D:/Country/States
print(type(fullPath)) # Output: <class 'str'>
```

7. `find(substring)` Returns the lowest index where the substring is found, or `-1` if not found. If string contains `Rohit Roshan`, only first occurence of character's index value returned. You can see in the example.
```python
name="RohitRoshan"
print(name.find("R")) # Output: 0
print(name.find("d")) # Output: -1
```

8. `startswith(prefix)` Check if the string starts with a specified substring. It returns `boolean` value.
```python
name="Rohit"

print(name.startswith("R")) # Output: True

fullName="Rohit Sharma"

print(fullName.startswith("Rohit")) # Output: True

print(fullName.startswith("Sharma")) # Output: False

print(fullName.startswith("Rohit Sharma")) # Output: True

print(fullName.startswith("Roh")) # Output: True
```

9. `endswith(suffix)` Check if the string ends with a specified substring.
```python
name="Rohit"
print(name.endswith("t")) # Output: True
fullName="Rohit Sharma"
print(fullName.endswith("Rohit")) # Output: False
print(fullName.endswith("Sharma")) # Output: True
```

10. `isdigit()` Returns `True` if all characters in the string are **Digits**.
```python
age="20"
print(age.isdigit()) # Output: True
```

---
# Print formatting with string

```python
name="Rohit"
print(name) # Output: Rohit
```
In the above example just name being displayed; what if you wanna add `Hello Rohit` instead of `Rohit`? This done by `formating`. See the below example:
```python
name="Rohit"
print("Hello",name) # Output: Hello Rohit
```
Another way to do this (**recommended**):
```python
name="Rohit"
print(f"Hello {name}") # Output: Hello Rohit
```

>The `f` stands for **f-string**, which is short for **formatted string literal** — a powerful way to embed variables or expressions directly inside strings.

---
# Float formatting with f-string

You can control the **number of decimal places**, **alignment**, and more using **format specifiers** inside `{}`.

What's the answer of `12/7`? Answer is `1.714286`. This number is too long to print onto console, however you can crop it by following method and result would be `1.7142` or how much decimal point you want, it arbitrary choice.

```python
value = 1.714286
print(f"Value is {value:.2f}")  # Output: Value is 1.71
```
**Explanation:**

- `:.2f` means:
    
    - `:` → Start format spec
        
    - `.2` → 2 decimal places. If you type `.4` answer would be `1.7142`
        
    - `f` → Fixed-point number (float)


---
# List

`List` are ordered sequences that can hold a variety of object types. They use square brackets `[]` and commas `,` to separate object in the `list`. Example `List=[1,"A","Hello"]`. `List` support _indexing_ & _slicing_. `List` can be nested & also have a variety of useful methods.

# Top 10 `python` `list` methods

## 1. `append(item)`  
   - **Description**: Adds an item to the end of the list.  
   
#### Example: 
```python
cities=["Pune","Mumbai"]

  

for i in cities:

    print(i)

print("----")

  

cities.append("Solapur")

for i in cities:

    print(i)
```
#### Output:
```python
Pune
Mumbai
----
Pune
Mumbai
Solapur
```

## 2. `extend(iterable)`  
   - **Description**: Extends the list by appending elements from an iterable.  
#### Syntax:
```python
list1.extend(iterable)
```
-  `iterable` is any iterable object (like list, tuple, set, string, etc.).
- It modifies `list1` **in place** and returns `None`.
#### Example:
```python
List=[]

  

for i in range(1,10):

    List.extend([i,i*2])

  

for i in List:

    print(i)
```
#### Output:
```python
1
2
2
4
3
6
4
8
5
10
6
12
7
14
8
16
9
18
```
## 3. `insert(index, item)`  
   - **Description**: Inserts an item at a specified position.  
   - **Example**:  
```python
lst = [1, 3]
lst.insert(1, 2)  # [1, 2, 3]
```

## 4. `remove(item)`  
   - **Description**: Removes the first occurrence of an item (raises `ValueError` if not found).  
   - **Example**:  
```python
lst = [1, 2, 2, 3]
lst.remove(2)  # [1, 2, 3]
```

## 5. `pop([index])`  
   - **Description**: Removes and returns the item at the given index (default: last element).  
   - **Example**:  
```python
lst = [1, 2, 3]
last = lst.pop()  # Returns 3, lst becomes [1, 2]
```

## 6. `index(item)`  
   - **Description**: Returns the index of the first occurrence of an item.  
   - **Example**:  
```python
lst = [10, 20, 30]
idx = lst.index(20)  # 1
```

## 7. `count(item)`  
   - **Description**: Returns the count of occurrences of an item.  
   - **Example**:  
```python
lst = [1, 2, 2, 3]
cnt = lst.count(2)  # 2
```

## 8. `sort(key=None, reverse=False)`  
   - **Description**: Sorts the list in place (modifies the original list).  
#### Example:
```python
lst = [3, 1, 2]

lst.sort(reverse=False)

print(lst) # [1, 2, 3] Ascending order

lst.sort(reverse=True)

print(lst) # # [3,2,1] Descending order
```
#### Output:
```python
[1, 2, 3]
[3, 2, 1]
```

## 9. `reverse()`  
   - **Description**: Reverses the list in place.  
   - **Example**:  
```python
lst = [1, 2, 3]
lst.reverse()  # [3, 2, 1]
```

## 10. `clear()`  
   - **Description**: Removes all items from the list.  
   - **Example**:  
```python
lst = [1, 2, 3]
lst.clear()  # []
```

## 11.  `copy()`  
   - **Description**: Returns a shallow copy of the list.  
   - **Example**:  
```python
lst = [1, 2, 3]
lst_copy = lst.copy()  # New list [1, 2, 3]
```
## 12. Add list value through loop
#### Example:
```python
my_list=[i for i in range(1,10) if i % 2==0] # my_list=[x for x in range(1,100)]

for i in my_list:

    print(i) # 2 4 6 8
```

---
# Dictionary

A **Dictionary** in Python is an unordered, mutable, and indexed collection of key-value pairs. It is defined using curly braces `{}` or the `dict()` constructor.

## Key Features:

- **Unordered** – Elements are not stored in any particular order.
- **Mutable** – Can be modified after creation.
- **Indexed by Keys** – Values are accessed using unique keys (not by position).
- **No Duplicate Keys** – Each key must be unique; duplicate keys overwrite existing values.
- **Heterogeneous** – Keys and values can be of any data type.

#### Syntax:
```python
my_dict = {key1: value1, key2: value2, ...}
# or
my_dict = dict(key1=value1, key2=value2, ...)
```
#### Example 1:
```python
student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Physics"]
}

print(student["name"])  # Output: Alice
print(student["courses"][0]) # Output: Math
```
#### Output:
```python
Alice
Math
```

#### Example 2:
```python
ITCompanies=dict(Intel=1000,Google=2000)
print(ITCompanies["Intel"])
```
#### Output:
```python
1000
```

# Top 6 `dictionary` methods

1. `dict.keys()` Returns all keys
#### Example:
```python
cities={"Pune":1000, "Mumbai":2000}

keys=cities.keys()

print(keys)

print(type(keys))
```
#### Output:
```python
dict_keys(['Pune', 'Mumbai'])
<class 'dict_keys'>
```

2. `dict.values()` Return list of values.
#### Syntax:
```python
dict.values()
```
#### Example:
```python
cities={"Pune":1000, "Delhi":2000}

  

values=cities.values()

  

print(values)

print(type(values))

sum=0

  

for i in values:

    sum+=i

  

print(sum)
```
#### Output:
```python
dict_values([1000, 2000])
<class 'dict_values'>
3000
```

3. `dict.items()` Return `tuple` of *key-value* pair.
#### Syntax:
```python
dict.items()
```
#### Example:
```python
cities={"Pune":1000, "Delhi":2000}

values=cities.items()

for i in values:

    print(i)

    print(type(i))
```
#### Output:
```python
('Pune', 1000)
<class 'tuple'>
('Delhi', 2000)
<class 'tuple'>
```

4. `dict.get()` Retrieve value safely.
#### Syntax:
```python
dict.get(key)
```
#### Example:
```python
cities={"Pune":1000, "Delhi":2000}

print(cities.get("Pune"))
```
#### Output:
```python
1000
```

5. `update()` Add new *key-value* pair.
#### Syntax:
```python
dict.update({"key":value})
```
#### Example:
```python
cities={"Pune":1000, "Delhi":2000}
cities.update({"Kochi":10000})
print(cities)
```
#### Output:
```python
{'Pune': 1000, 'Delhi': 2000, 'Kochi': 10000}
```

6. `pop(key)` Remove and return value.
#### Syntax:
```python
removed_value=dict.pop(key)
```
#### Example:
```python
cities={"Pune":1000, "Delhi":2000}

removed_value=cities.pop("Delhi")

print(cities)
```
#### Output:
```python
{'Pune': 1000}
```

---
# Tuples

A **tuple** in Python is an ordered collection of elements that is immutable (cannot be changed after creation). Tuples are similar to lists, but unlike lists, their contents cannot be modified (you can't add, remove, or change elements once they are created).

### Key Characteristics of Tuples:

1. **Ordered**: Tuples maintain the order of the elements.
    
2. **Immutable**: Once created, the elements of a tuple cannot be modified.
    
3. **Heterogeneous**: Tuples can contain elements of different data types (integers, strings, lists, other tuples, etc.).
    
4. **Indexing and Slicing**: You can access elements using indexing or slicing, just like lists.
    
5. **Iterable**: Tuples can be iterated over in loops.
    
6. **Hashable**: Because they are immutable, tuples can be used as keys in dictionaries, unlike lists.

#### Syntax:
```python
tuple_name = (element1, element2, element3, ...)
```
#### Example 1:
```python
# Tuple with multiple elements
my_tuple = (1, 2, 3, 4)

# Tuple with a single element (note the trailing comma)
single_element_tuple = (5,)

# Empty tuple
empty_tuple = ()

# Tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)
```

> If you don't include the comma, Python will just consider the value inside the parentheses as a single element (Assume `int` ), not a tuple.

#### Example 2:
```python
# Tuple as a key in a dictionary
my_dict = {
    ('apple', 1): "Fruit",
    ('banana', 2): "Fruit",
    ('carrot', 3): "Vegetable"
}

# Accessing the value using the tuple as the key
print(my_dict[('apple', 1)])  # Output: Fruit
print(my_dict[('banana', 2)])  # Output: Fruit
```

---
# Set

A **set** in Python is an **unordered** collection of **unique** elements. It is a built-in data type that is similar to a list or tuple, but with some key differences. The most important distinction is that sets do **not** allow duplicate values and do not maintain any order of elements.

### Key Characteristics of Sets:

1. **Unordered**: The elements of a set are not stored in any particular order, and their order may change each time you interact with the set.
    
2. **Unique Elements**: Sets do not allow duplicates. If you try to add the same element multiple times, it will only appear once in the set.
    
3. **Mutable**: Sets are mutable, meaning you can add and remove elements from a set.
    
4. **No Indexing**: You cannot access elements in a set by index like you can with lists or tuples. You can only iterate over the set.
    
5. **Hashable Elements**: Elements inside a set must be hashable, meaning they must be immutable (like numbers, strings, or tuples). Mutable types like lists cannot be added to a set.

#### Syntax:
```python
# Creating a set
my_set = {1, 2, 3, 4}
empty_set = set()  # An empty set (note: {} creates an empty dictionary, not a set)
```

---
# Files

When you want to work with files like `Excel`, `CSV`, `text`, by editing and changing in it. There are tons of methods used to do so. `open()` method in used to open file for operation.
#### Syntax:
```python
file_pointer=open("file_name.extension","mode")
```

#### Example:
```python
fp=open("Sample.txt") # text file contains "Hello, dude"

print(fp.read())
```
#### File directory:
```python
Python-src-code/
    |---Playground.py
    |---Sample.txt
```
> `python` file and `text` file must be in same directory to perform operations.

How to move `cursor` up and down? You can do it by `seek()` method, which let you put your `cursor` where you want. When you read file by `read()` method, after reading it move `cursor` to next line, so if you want to move `cursor` back to top, you can do it by `seek()` method. After doing your file operation, please `close` file by `file_pointer.close()` method

> `read()` method read entire file content with escape characters.

#### Example:
```python
fp=open("Sample.txt")

print(fp.read())

fp.seek(0)  # Reset file pointer to the beginning

print(fp.readline())
fp.close()
```
#### Output:
```python
Hello, dude.
Hello, dude.
```

# Writing to file

By default, the `open()` function will only allow us to read the file. We need to pass the argument `'w'` to write over the file. Before writing data into file, we must know `mode` to work with files in better manner, check out following table.

| Mode | Description                                                                                                 |
| ---- | ----------------------------------------------------------------------------------------------------------- |
| `r`  | **Read** (default mode). Opens the file for reading. Error if the file doesn't exist.                       |
| `w`  | **Write**. Creates a new file or truncates the file if it exists.                                           |
| `a`  | **Append**. Creates a new file if it doesn’t exist, otherwise appends to the end.                           |
| `x`  | **Exclusive creation**. Creates a file, but fails if it already exists.                                     |
| `b`  | **Binary** mode. Used to handle binary files (e.g., images, audio). Add to other modes like `'rb'`, `'wb'`. |
| `t`  | **Text** mode (default). Used for text files. Combine with other modes like `'rt'`, `'wt'`.                 |
| `+`  | **Update**. Opens the file for reading and writing (e.g., `'r+'`, `'w+'`).                                  |
# File methods

|Method|Description|
|---|---|
|`read(size=-1)`|Reads entire file or up to `size` bytes.|
|`readline(size=-1)`|Reads one line from the file.|
|`readlines()`|Reads all lines and returns them as a list.|
|`write(string)`|Writes a string to the file.|
|`writelines(lines)`|Writes a list of strings to the file (no newline added automatically).|
|`seek(offset, whence=0)`|Moves the file pointer to a specific position.|
|`tell()`|Returns the current position of the file pointer.|
|`close()`|Closes the file. Always do this unless using `with`.|
|`flush()`|Forces the write buffer to be written to disk.|
|`truncate(size=None)`|Truncates the file to `size` bytes (or current position if not specified).|
1. `write()` Write data into file.
#### Example:
```python
fp=open("Sample.txt","w")

  

for i in range(65,91):

     fp.write(chr(i)+"\n") # fp.write(f"{chr(i)}\n") <-- Alternative way
```
#### Output:
```python
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z

```

> 1. Write program which print table from 1 to 100 into file.

#### Solution:
```python
with open('tables_1_to_100.txt', 'w') as f:

    for i in range(1, 101):  # Tables from 1 to 100

        f.write(f"Multiplication Table of {i}\n")

        f.write("-" * 30 + "\n")

        for j in range(1, 11):  # Each table up to 10

            f.write(f"{i} x {j} = {i * j}\n")

        f.write("\n")  # Blank line between tables
```

---
# Comparison operator

When you compare values by `==` operator on that time it compares value, if you wanna check object ID is same or not on that time you can use `is`.

#### Example:
```python
num_1=1

num_2=1

  

if(num_1==num_2):

    print("The numbers are equal.")

else:

    print("The numbers are not equal.")

if num_1 is num_2:

    print("The numbers are identical.")

else:

    print("The numbers are not identical.")
```
#### Output:
```python
The numbers are equal.
The numbers are identical.
```

---
# `enumerate` function

In Python, the `enumerate()` function is used to **loop over an iterable (like a list, tuple, or string) and keep track of the index** of the current item.

#### Syntax:
```python
enumerate(iterable, start=0)
```
#### Example:
```python
fruits = ['apple', 'banana', 'cherry']

  

for index, fruit in enumerate(fruits):

    print(index, fruit)
```
#### Output:
```python
0 apple
1 banana
2 cherry
```

> It eliminates the need to manually track indexes with a counter variable.
---
# Random module

Visit [here](https://docs.python.org/3/library/random.html#functions-for-integers) to see `random` package document.

# Top 10 `random` methods.

| Method                                   | Description                                                  |
| ---------------------------------------- | ------------------------------------------------------------ |
| `random()`                               | Returns a float between **0.0** and **1.0**                  |
| `randint(a, b)`                          | Returns a random **integer** between `a` and `b` (inclusive) |
| `randrange(start, stop[, step])`         | Returns a random **integer from a range**, like `range()`    |
| `uniform(a, b)`                          | Returns a **random float** between `a` and `b`               |
| `choice(seq)`                            | Returns a **random element** from a non-empty sequence       |
| `choices(population, k=1, weights=None)` | Returns a list of `k` random elements (with **replacement**) |
| `sample(population, k)`                  | Returns `k` unique random elements (**no replacement**)      |
| `shuffle(seq)`                           | **Shuffles** a list (in-place)                               |
| `seed(a=None)`                           | Sets the seed for reproducibility of random results          |
| `betavariate(alpha, beta)`               | Returns a random float from a **beta distribution**          |
#### Example:
```python
import random

print(random.random())          # 0.345... (float between 0 and 1)
print(random.randint(1, 10))    # e.g., 7
print(random.randrange(0, 100, 5))  # e.g., 25
print(random.uniform(1.5, 5.5)) # e.g., 3.87

colors = ['red', 'green', 'blue']
print(random.choice(colors))   # e.g., 'green'
print(random.choices(colors, k=2))  # e.g., ['red', 'red']
print(random.sample(colors, 2))     # e.g., ['blue', 'green']

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)  # e.g., [3, 1, 4, 5, 2]

random.seed(42)  # Sets seed for reproducible results
```

---
# Guess the number game
```python
import random

  

while True:

    user_input=int(input("Enter a number between 1 and 10 (or 0 to exit): "))

    if user_input == random.randint(1,10):

        print("Congratulations! You guessed the number correctly.")

    else:

        print("Sorry, that's not correct. Try again.")
```

---
