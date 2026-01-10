import os
print(os.getcwd())                                          #current working directory
print(os.listdir())                                         #List files in folder
#os.mkdir("test")                                           #Create folder
print(os.path.exists("test"))                               #Check if folder exists
os.rmdir("test")                                            #Delete folder
os.chdir("test")                                            #Change folder
os.system("echo Hello")                                     #Run system command


