from PIL import Image
import sys
from tkinter import filedialog
import tkinter
global UNIT
UNIT = 100

root = tkinter.Tk()

def find_path():
    global img_path

    img_path = filedialog.askopenfilename(initialdir ="Samples/", title ="Choose a image file", filetypes=(("jpg Files", "*.jpg"),("png Files", "*.png"), ))
    

    img = Image.open(img_path)

    width, height = img.size
    ratio = height/width

    new_width = UNIT
    new_height = ratio*new_width

    img = img.resize((new_width,int(new_height)))

    img = img.convert("L")
    pixel = img.getdata()

    characters = ["@",'#',"S","%","?","*","+",";",":",",","."]

    new_pixel = [characters[pixels//25] for pixels in pixel]
    new_height = "".join(new_pixel)

    count = len(new_pixel)

    final_image = [new_pixel[index:index+new_width] for index in range(0,count,new_width)]
    txt_file = ""
    for i in final_image:

        txt_file += "".join(i)
        txt_file += "\n"

    print(txt_file)
    with open("2.txt","w+") as f:
        
        f.write(txt_file)


my_lable = tkinter.Label(root,text="Select an image")
my_lable.pack(pady = 10,padx=10)



my_button = tkinter.Button(root, text="Click to select", command= find_path)
my_button.pack(pady = 10,padx=10)


root.mainloop()





