#-----------------FastQRgen-----------------
#-QRCode generator based in tkinter
#-Developed by Renato Braze at 27/11/2021
#-Feel free to use and modify

#Import area
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.colorchooser import askcolor
from tkinter import messagebox
import pyqrcode as pqr
import os
from PIL import Image

#Initial color set
color_fg = ((0,0,0), '#000000')
color_bg = ((255,255,255), '#ffffff')

#Button Functions
def generate():
  content = input_widget.get()
  downloads_folder = os.path.expanduser("~")+"/Downloads/"
  if content:
    qr = pqr.create(content)
    save_path = asksaveasfilename(initialdir=downloads_folder, defaultextension='.png', filetypes=[('Image File', '*.png')])
    qr.png(f'{save_path}', scale=scale_cfg.get(), module_color=color_fg[0], background=color_bg[0])
    img = Image.open(save_path)
    img.show()
  else:
    messagebox.showerror(title='Erro',message='Insira um valor valido')

def show_cfg():
  global box_value, color_bg, color_fg
  box_value = box_var.get()
  if box_value == 1:
    adv_options.pack()
  else:
    adv_options.pack_forget()
    scale_cfg.set(5)
    color_bg = ((255,255,255), '#ffffff')
    secundary_color_selector['bg'] = color_bg[1]
    color_fg = ((0,0,0), '#000000')
    primary_color_selector['bg'] = color_fg[1]
    
def fg_color():
  global color_fg
  if box_value == 1:
    color_fg = askcolor(title='Selecione a cor primaria')
    primary_color_selector['bg'] = color_fg[1]

def bg_color():
  global color_bg
  if box_value == 1:
    color_bg = askcolor(title='Selecione a cor secundaria')
    secundary_color_selector['bg'] = color_bg[1]

root = Tk()
root.title('FastQRgen')
root.resizable(width=False, height=False)

#Window centralize
window_width = 300
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#Widgets creation
name_frame = Frame(root)
app_name = Label(name_frame, text='FastQRgen', font='Corbel 24 bold')
instructions_text = Label(text='Insira o conteudo abaixo', font='Corbel 12 bold')
input_widget = Entry(width=30, font='Candara 10')
generate_button = Button(text='Gerar', width=10, command=generate, font='Corbel')
box_var = IntVar()
adv_checkbox = Checkbutton(text='Opções Avançadas', onvalue=1, offvalue=0, variable=box_var, command=show_cfg, font='Corbel')
adv_options = Frame()
scale_label = Label(adv_options, text='Defina o tamanho : ', height=2, anchor=SE, font='Corbel 10')
scale_cfg = Scale(adv_options, from_=1, to=10, orient=HORIZONTAL)
scale_cfg.set(5)
primary_color_text = Label(adv_options, text='Selecione a cor Primaria : ', font='Corbel 10')
primary_color_selector = Button(adv_options, command=fg_color, width=13, relief=SUNKEN)
secundary_color_text = Label(adv_options, text='Selecione a cor Secundaria : ', font='Corbel 10')
secundary_color_selector = Button(adv_options, command=bg_color, width=13, relief=SUNKEN)

#Widgets set position
name_frame.pack()
app_name.pack(pady=15, side=RIGHT)
instructions_text.pack(pady=10)
input_widget.pack()
generate_button.pack(pady=15)
adv_checkbox.pack()
scale_label.grid(row=0, column=0, sticky=E)
scale_cfg.grid(row=0, column=1)
primary_color_text.grid(row=1, column=0, sticky=E)
primary_color_selector.grid(row=1, column=1)
secundary_color_text.grid(row=2, column=0, sticky=E)
secundary_color_selector.grid(row=2, column=1)

#Window run
root.mainloop()