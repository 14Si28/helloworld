append_me="\nThis is the appended part of the file." # For this we will open the file in append mode.
file=open('FileName.txt','a') #'a' denotes the append mode here
file.write(append_me)
file.close()