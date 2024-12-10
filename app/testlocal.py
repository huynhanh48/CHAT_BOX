# Python program to explain os.path.dirname() method 
	
# importing os.path module 
import os.path 

# Path 


# Path 
path = 'file.txt'

# Get the directory name 
# from the specified path 
dirname = os.path.dirname(__file__) 
print(dirname)

path = os.path.join(os.path.abspath(dirname),'haha.txt')
print(path)


# Get the directory name where the current script is located
dirname = os.path.dirname(__file__)

# Move one directory up (to the 'Chat_box' directory)
parent_dir = os.path.dirname(dirname)
test = os.path.dirname(parent_dir)
print('test: ',test)

# Join the parent directory with 'haha.txt'
path = os.path.join(parent_dir, 'haha.txt')

print(path)
