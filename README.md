# Virtual File System
In lab 6, we created a Virtual File System that does all the functionalities of a general file system in an operating system. This document will explore the file and directory structure, memory allocation and memory map, system functionalities, system requirements, and limitations.


![image](https://github.com/itsAdee/VirtualTextFileMemorySystem/assets/104891437/a64c1f7a-6fa5-42c6-b6e0-df2d7149d68d)


The File Management System Class is responsible for doing all the functionality to fulfill the requirements of the virtual file system. This class will contain many instances of File class which will represent a Txt file in the virtual file system, as well as many instances of Directory class which will represent directories in our file system, and lastly, the Memory object which represents the main memory of our virtual file system in which all files will be loaded upon.
This File Management System object is saved in the filesystem. pickle file, and basically represents all the information of the virtual file management system like root, subdirectories, and files.
File and Directory Structure:
 
A hierarchical implementation resembling a tree data structure has been used to store files and directories, from the UML diagram above see that each file will have its unique id and name, and the directory will have a list of files and subdirectories, all of these functions will be overseen and called by the File Management class, which is saved in a pickle file when the virtual file system is closed. 
## Memory Allocation:
The Memory Class represents the logical main memory of the file system, depicting the RAM it consists of a specific number of blocks and a block size, the block size will represent the number of bytes a block can store. A File Object during writing, truncating, and appending will directly access these memory blocks using the allocated blocks and free blocks methods and, in this way, each file system will have its own unique blocks of memory, these blocks will be freed when the file is deleted.
## Memory Map:
The Memory class as mentioned above has a list of blocks, and each block has a unique index associated with it. Each block based on its index will be allocated to a file or it will be empty.
## Accessing data from the main memory:
The Memory is allocated by the program to a file when the user enters any data in it. The data is then allocated as the value of memory blocks that do not have any data from before which have been allocated to that file. The memory is also deallocated when the file is deleted, or the data is removed from the file. In such a case, the data is removed from the memory blocks, and they are declared free.
## Data Structure:
The Directory class contains a list of files and subdirectories, which can be used to traverse the file system. The File class contains a list of blocks, which store the data of the file.
## System Functionalities
The File Management System offers a range of functionalities, including:
•	Reading and writing files, appending data, or overwriting files.
•	Changing the current working directory.
•	Displaying the memory map.
•	Opening and closing files for operations.
•	Listing files and directories.
•	Deleting files and directories.
•	Truncating files.
•	Moving data within a file.
•	Moving files from one directory to another.
•	Creating and deleting files.

## System Requirements:
The system requirements include:
•	Maximum robustness
•	Proper data storage mechanism (files, directories, memories)
•	User-friendly terminal interface
•	Complete file system operations support
•	A mechanism for storing and loading data to/from files.
•	Efficient data management
## System Limitations:
Our system has a few limitations, including:
•	The system may be difficult to use initially without referring to a manual to familiarize oneself with the commands.
•	The system does not provide a Graphical User Interface, only a Terminal.
•	Loading and reloading data can be slow.
•	Currently, the system only supports text files and does not support other formats such as binary data or images.

