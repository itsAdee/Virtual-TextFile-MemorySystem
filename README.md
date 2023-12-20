# Virtual File System

We have developed a Virtual File System that replicates all the functionalities of a typical file system in an operating system. This document provides an in-depth exploration of the file and directory structure, memory allocation, memory map, system functionalities, system requirements, and limitations.

![Virtual File System](https://github.com/itsAdee/VirtualTextFileMemorySystem/assets/104891437/a64c1f7a-6fa5-42c6-b6e0-df2d7149d68d)

The `File Management System` class is responsible for executing all the functionalities to meet the requirements of the virtual file system. This class incorporates instances of the `File` class, representing text files in the virtual file system, as well as instances of the `Directory` class, representing directories, and the `Memory` object, symbolizing the main memory of our virtual file system where all files are loaded.

The `File Management System` object is saved in the `filesystem.pickle` file, encompassing critical information about the virtual file management system, such as the root, subdirectories, and files.

## File and Directory Structure

A hierarchical implementation resembling a tree data structure is utilized to store files and directories. From the UML diagram above, observe that each file has a unique ID and name, while a directory has a list of files and subdirectories. All these functions are overseen and called by the `File Management` class, which is saved in a pickle file when the virtual file system is closed.

## Memory Allocation

The `Memory` class represents the logical main memory of the file system, depicting the RAM. It consists of a specific number of blocks and a block size, where the block size signifies the number of bytes a block can store. During writing, truncating, and appending, a `File` object directly accesses these memory blocks using the allocated and free block methods. Each file system has its own unique blocks of memory, which are freed when the file is deleted.

## Memory Map

The `Memory` class has a list of blocks, and each block has a unique index associated with it. Based on its index, each block is allocated to a file or is left empty.

## Accessing Data from the Main Memory

The program allocates memory to a file when the user enters data, with the data assigned to memory blocks that do not already have data allocated to them. Memory is deallocated when the file is deleted or data is removed, freeing the associated memory blocks.

## Data Structure

The `Directory` class contains a list of files and subdirectories, facilitating file system traversal. The `File` class comprises a list of blocks that store the data of the file.

## System Functionalities

The `File Management System` offers a range of functionalities, including:

- Reading and writing files, appending data, or overwriting files.
- Changing the current working directory.
- Displaying the memory map.
- Opening and closing files for operations.
- Listing files and directories.
- Deleting files and directories.
- Truncating files.
- Moving data within a file.
- Moving files from one directory to another.
- Creating and deleting files.

## System Requirements

The system requirements include:

- Maximum robustness.
- Proper data storage mechanism (files, directories, memories).
- User-friendly terminal interface.
- Complete file system operations support.
- A mechanism for storing and loading data to/from files.
- Efficient data management.

## System Limitations

Despite its capabilities, our system has a few limitations:

- The system may be challenging to use initially without referring to a manual.
- The system lacks a Graphical User Interface, only providing a Terminal interface.
- Loading and reloading data can be slow.
- Currently, the system only supports text files and does not accommodate other formats such as binary data or images.

