from PIL import Image
from PIL import ImageFilter
img=Image.open(r"C:\Users\keren\OneDrive\Pictures\Screenshots\Screenshot 2024-04-03 225245.png")
img.show()#Display the image
width = img.width
height = img.height
print("The height of the image is: ", height)
print("The width of the image is: ", width)
wid=width//2
hei=height//2
newimg=img.resize((hei,wid))
newimg.show()#Reduce the Image size of its half size
rotatedimg=img.rotate(145)
rotatedimg.show()#Rotate the image 145 degrees
nimg=img.resize((50,70))
nimg.show()#Resize the image with 50 units in x direction and 70 units in y direction
limg=img.transpose(Image.FLIP_TOP_BOTTOM)
limg.show()#Flip the image (Top to Bottom)
fimg=img.transpose(Image.FLIP_LEFT_RIGHT)
fimg.show()#Flip the image (Left to Right)
area=(60,215,124,278)
crpimg=img.crop(area)
crpimg.show()#Crop the image
bwimg=img.convert('L')
bwimg.show()#Change the color image to  Black and White
bimg=img.convert('LA')
bimg.show()#Change the color image to GrayScale
blur=img.filter(ImageFilter.GaussianBlur(radius=8))
blur.show()#Apply blur effect on the image