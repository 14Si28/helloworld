import os
import io
import time
current_WD= os.getcwd() # To see the present working directory
print(current_WD)
test_text="Hi there"
try:
    os.mkdir("Test") # Making the directory
    # file=open('Testfile1.csv','w')
    # file.write("Test")
    # file.close()
    with io.FileIO("foobar.txt",'w') as file:  # why not writing or appending ?
        file.write(test_text)
        file.close()
except Exception:
    time.sleep(1)
    os.rename("Test","Test2") # Renaming the folder
    time.sleep(1)
    os.rmdir("Test2") # Removing the folder created