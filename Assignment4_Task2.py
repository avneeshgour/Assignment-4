#Assignment 4 Task 2: Write and Append Data to a File
user_input = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input)

print("Data successfully written to output.txt")
print("Enter additional text to append:")
file1=open('output.txt','a')
writing_file=file1.write('\nLearning File Handling in Python.')
print(writing_file)
file1.close()
print("Data Successfully appended")

print("Final Content of output.text: ")
file1=open('output.txt','r')
reading_file=file1.read()
print(reading_file)
file1.close()
