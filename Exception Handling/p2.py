
# open a file and read display if the file content in this directory  from console 
# otherwise print "sorry file is not exisitng in this directory"  using try n except+

try:
    with open(input("enter the filename: ")) as file:

     print(file.read())


except FileNotFoundError:

   print("sorry file is not exisitng in this directory")     
 
    