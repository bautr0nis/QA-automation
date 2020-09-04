#As I'm new with PyTest I was struggling to create a clean and working script to validate application, so
#I thought I could compare the output of a script and a compare it to existing file.

#Reading a files
file1 = open('betty.output.txt', 'r')
file2 = open('app_output.txt', 'r')

#Removing spaces
file1.discard('\n')
file2.discard('\n')

if file1 == file2:
    print ("Files are exactly the same")

else:
    print ("Files are not exactly the same")
