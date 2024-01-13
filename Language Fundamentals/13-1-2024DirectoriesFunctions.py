# To Know Current Working Directory:
import os
cwd=os.getcwd()
print("Current Working Directory:",cwd)

#To create a sub directory in the current working directory:
import os
os.mkdir("mysub")
print("mysub directory created in cwd")

#. To remove a directory:
import os
os.rmdir("mysub/mysub2")
print("mysub2 directory deleted")

#To rename a directory
import os
os.rename("mysub","newdir")
print("mysub directory renamed to newdir")
