# Import docx NOT python-docx
#import docx
import os
#from docx.shared import Inches
import sys

from PIL import Image

# Get the list of all files and directories
path = "E:\\shar\\share\\"
dir_list = os.listdir(path)
dir_list.sort(reverse=True)

im = Image.open("E:\\shar\\share\\2022-01-28_Fri.png")

# Size of the image in pixels (size of original image)
# (This is not mandatory)s
width, height = im.size
print(width, height)

# Setting the points for cropped image
left = 220
top = 300
right = 950
bottom = 950

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))

# Shows the image in image viewer
#im1.show()

print("Files and directories in '", path, "' :")

# prints all files
#print(dir_list)

# Create an instance of a word document
#doc = docx.Document()

# Add a Title to the document
#doc.add_heading('Trade chart', 0)
day = sys.argv[1]
print(f'{day}')
for x in dir_list:
    if x.endswith(f"{day}"+".png"):
        im2 = Image.open(f"E:\\shar\\share\\{x}")
        im3 = im2.crop((left, top, right, bottom))
        im3.save(f"E:\\shar\\cropped\\{x}")
        #doc.add_picture(f"E:\\shar\\cropped\\{x}", width=Inches(5), height=Inches(3))
        print(x)

# Now save the document to a location
#doc.save('chart.docx')
