from tkinter import *
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

# Global variable for QR code color
qr_color = "black"

def generate_qr():
    data = textentery.get()  # Get the text from the input field
    if not data:  # Check if input is empty
        messagebox.showerror("Error", "Please enter some text!")
        return

    # Generate QR code with selected color
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=qr_color, back_color="white")
    img.save("qrcode.png")  # Save the QR code image

    # Display QR code
    img = Image.open("qrcode.png")
    img = img.resize((200, 200))  # Resize for display
    img = ImageTk.PhotoImage(img)

    imglabel.config(image=img)
    imglabel.image = img


def save_qr():
    try:
        img = Image.open("qrcode.png")
        img.save("saved_qrcode.png")
        messagebox.showinfo("Saved", "QR Code saved successfully as 'saved_qrcode.png' lol")
    except:
        messagebox.showerror("Error", "No QR code generated to save!")

def set_color(color):
    global qr_color
    qr_color = color

root = Tk()
root.title("QR Forge")
root.iconbitmap('QR_GEN/1.ico')
root.geometry('520x310')
root.resizable(False, False)

title = Label(text="QR CODE Generator by Kamekazi ⭐",font=("cosmicsansms",19, "bold"))
title.pack(pady=(15, 0))

img = Image.open("QR_GEN/kamekazi.png") 
img_resized = img.resize((200, 200))  
img_tk = ImageTk.PhotoImage(img_resized)

image_frame = Frame(root)
image_frame.pack(side=RIGHT, padx=(0, 40), pady=(20, 0))

imglabel = Label(image_frame, image=img_tk)
imglabel.pack()

textvar = StringVar()
colorvar = StringVar()
title = Label(text="Enter Link or Plain Text: ",font=("",10, "bold")).pack(anchor=NW,padx=(20, 0),pady=(15, 0))
textentery = Entry(root, textvariable=textvar,font=("Helvetica", 13), width=25)
textentery.pack(anchor=NW,padx=(20, 0),ipady=3)
title = Label(text="Boder Color: ",font=("",10, "bold")).pack(anchor=NW,padx=(20, 0),pady=(5, 0))

frame5 = Frame(root, bg="", bd=6)
frame5.pack(side=BOTTOM, anchor=W, padx=(21, 0), pady=(0, 10), fill=X)

Createbutton = Button(frame5, text="Create", width=8, height=1, bg="white", bd=2, relief="solid", 
                      font=("cosmicsansms", 14, ''), command=generate_qr)
Createbutton.pack(side=LEFT, padx=4, pady=0)

savebutton = Button(frame5, text="Save", width=8, height=1, bg="white", bd=2, relief="solid", 
                    font=("cosmicsansms", 14, ''), command=save_qr)
savebutton.pack(side=LEFT, padx=10, pady=0)

# Color Buttons
frame1 = Frame(root, bg="",bd=6)
frame1.pack(side=LEFT, anchor=NW,padx=(18, 0),pady=(0, 0))

redbutton = Button(frame1, width=5, height=2, bg="red",bd=3, command=lambda: set_color("red"))
redbutton.pack(anchor=NW,padx=(0, 0),pady=(0, 0))
greenbutton = Button(frame1, width=5, height=2, bg="green",bd=3, command=lambda: set_color("green"))
greenbutton.pack(anchor=NW,padx=(0, 0),pady=(5, 0))

frame2 = Frame(root, bg="",bd=6)
frame2.pack(side=LEFT, anchor=NW,padx=(0, 0),pady=(0, 0))

bluebutton = Button(frame2, width=5, height=2, bg="blue",bd=3, command=lambda: set_color("blue"))
bluebutton.pack(anchor=NW,padx=(0, 0),pady=(0, 0))
blackbutton = Button(frame2, width=5, height=2, bg="black",bd=3, command=lambda: set_color("black"))
blackbutton.pack(anchor=NW,padx=(0, 0),pady=(5, 0))

frame3 = Frame(root, bg="",bd=6)
frame3.pack(side=LEFT, anchor=NW,padx=(0, 0),pady=(0, 0))

yellowbutton = Button(frame3, width=5, height=2, bg="yellow",bd=3, command=lambda: set_color("yellow"))
yellowbutton.pack(anchor=NW,padx=(0, 0),pady=(0, 0))
pinkbutton = Button(frame3, width=5, height=2, bg="pink",bd=3, command=lambda: set_color("pink"))
pinkbutton.pack(anchor=NW,padx=(0, 0),pady=(5, 0))

frame4 = Frame(root, bg="",bd=6)
frame4.pack(side=LEFT, anchor=NW,padx=(0, 0),pady=(0, 0))

greybutton = Button(frame4, width=5, height=2, bg="grey",bd=3, command=lambda: set_color("grey"))
greybutton.pack(anchor=NW,padx=(0, 0),pady=(0, 0))
orangebutton = Button(frame4, width=5, height=2, bg="orange",bd=3, command=lambda: set_color("orange"))
orangebutton.pack(anchor=NW,padx=(0, 0),pady=(5, 0))

root.mainloop()
