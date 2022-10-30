#Example1: writing data in to text file
# file=open("/Users/adithbala/Downloads/myfile.txt",'w')
# file.write("This is my first statement...\n")
# file.write("This is my second statement...\n")
# file.write("This is my third statement...\n")
# file.write("This is my fourth statement...\n")
# file.write("This is my fifth statement...")
# file.close()
# print("program completed....")

#Example2: reading data from text file
# file=open("/Users/adithbala/Downloads/myfile.txt",'r')
# print(file.read())
# #print(file.readline())
# file.close()
print("------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>")
#Example3 : appending data into text file
file=open("/Users/adithbala/Downloads/myfile.txt",'a')
file.write("\n this is my sixth line\n")
file.write(" this is my seventh line\n")
print(file.read())
file.close()

print("program is completed....")





