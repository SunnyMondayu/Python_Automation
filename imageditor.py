from PIL import Image, ImageEnhance, ImageFilter
import os 
path='./imgs'
pathout='/editedimgs'
for filename in os.listdir(path):
    img=Image.open(f"{path}/{filename}")

    edit=img.filter(ImageFilter.SHARPEN)
    edit=img.filter(ImageFilter.CONTOUR)
    edit=img.filter(ImageEnhance.Brightness)
    edit=img.filter(ImageFilter.SMOOTH)
    clean_name=os.path.splitext(filename)
    edit.save(f'.{pathout}/{clean_name}_edited.jpg')
    