import sys

print("File name",sys.argv[0])

if len(sys.argv)>1:
    print("Arguments given are:")
    for i in range(1,len(sys.argv)):
        print(sys.argv[i])

else:
    print("No arguments given")