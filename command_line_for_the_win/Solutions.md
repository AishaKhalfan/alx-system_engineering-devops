# CMD CHALLENGE SOLUTIONS

- This File contains some of the solutions to the CMD Challenge

- 1 -> hello_world
Your first challenge is to print "hello world" on the terminal in a single command.
```console
> echo 'hello world'
```
- 2 -> current_working_directory
Print the current working directory.
```console
> pwd
```
- 3 -> list_files
List names of all the files in the current directory, one file per line.
```console
> ls
```
- 4 ->Print_contents
There is a file named access.log in the current directory. Print the contents.
```console
> cat access.log 
```
- 5 ->Print_last lines
Print the last 5 lines of "access.log".
```console
> tail -5 access.log 
```
- 6 ->Empty_file
Create an empty file named take-the-command-challenge in the current working directory.
```console
> touch take-the-command-challenge 
```
- 7 ->create_dir
Create a directory named tmp/files in the current working directory
```console
> mkdir tmp && cd tmp &&  mkdir files 
```
- 8 ->Copy_file
Copy the file named take-the-command-challenge to the directory tmp/files
```console
> cp take-the-command-challenge tmp/files 
```
- 9 ->Move_file
Move the file named take-the-command-challenge to the directory tmp/files
```console
> mv take-the-command-challenge tmp/files 
```
- 10 ->Create_symlink
A symbolic link is a type of file that is a reference to another file.
Create a symbolic link named take-the-command-challenge that points to the file tmp/files/take-the-command-challenge.
```console
> tail -5 access.log 
```
- 11 ->Delete_files
Delete all of the files in this challenge directory including all subdirectories and their contents.
```console
> find . -delete 
```
- 12 ->Remove_files_with_extension
There are files in this challenge with different file extensions. Remove all files with the .doc extension recursively in the current working directory.
```console
> find . -name '*.doc' -delete 
```
- 13 ->Find_string
There is a file named access.log in the current working directory. Print all lines in this file that contains the string "GET".
```console
> grep "GET" ./access.log 
```
- 14 ->Search_for_string
Print all files in the current directory, one per line (not the path, just the filename) that contain the string "500".
```console
> grep -l '500' * 
```
- 15 ->Search_for_extension
Print the relative file paths, one path per line for all filenames that start with "access.log" in the current directory.
```console
> find . -name "access.log*" 
```
- 16 ->Search_recursive
Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500".
```console
grep -r -h "500"
```
- 17 ->Find_IP_address
Extract all IP addresses from files that start with "access.log" printing one IP address per line.
```console
> grep -ro ^[0-9.]* 
```
- 18 ->Count_files
Count the number of files in the current working directory. Print the number of files as a single integer.
```console
> ls -l | wc -l 
```
- 19 ->simple_sort
Print the contents of access.log sorted.
```console
> sort access.log
```
- 20 ->count_the_strings
Print the number of lines in access.log that contain the string "GET".
```console
> grep -c GET access.log
```
- 21 ->Split_on_a_char
The file split-me.txt contains a list of numbers separated by a ; character.

Split the numbers on the ; character, one number per line.
```console
> tr ';' '\n' < split-me.txt
```
- 22 ->Generate_a_number_sequence
Print the numbers 1 to 100 separated by spaces.
```console
> echo {1..100} 
```
- 23 ->Replace_text_in_files
This challenge has text files (with a .txt extension) that contain the phrase "challenges are difficult". Delete this phrase from all text files recursively.
```console
> sed -i 'challenge are difficult/d' **/*.txt 
```
- 24 ->sum_the_numbers
The file sum-me.txt has a list of numbers, one per line. Print the sum of these numbers
```console
> cat sum-me.txt | paste -sd+ | bc 
```
- 25 ->Only_the_file_names
Print all files in the current directory recursively without the leading directory path.
```console
> find . -type f -printf "%f\n"
```
- 26 ->remove_extensions
Rename all files removing the extension from them in the current directory recursively.
```console
> find * -type f | rename 's/\..*//' 
```
- 27 ->Replace_spaces
List all of the files (filenames only) in the current directory but replace all spaces with a '.' character.
```console
> ls | tr ' ' '.' 
```
- 28 ->Directories_containing_files
Print all directories, one per line without duplicates that contain one or more files with a ".tf" extension.
```console
> dirname **/*.tf | uniq
```
- 29 ->Files_starting_with_a+number
There are a mix of files in this directory that start with letters and numbers. Print the filenames (just the filenames) of all files that start with a number recursively in the current directory.
```console
> find -type f -printf "%f\n" | grep ^[0-9]
```
- 30 ->nth_line
Print the 25th line of the file faces.txt
```console
> head -25 faces.txt | tail -1
```
