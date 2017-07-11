import tkinter
from PIL import ImageDraw, Image, ImageTk
import sys
import xlwt


args=1
book = xlwt.Workbook()
ws = book.add_sheet('First Sheet',cell_overwrite_ok=True) 

window = tkinter.Tk(className="bla")

image = Image.open(sys.argv[1] if len(sys.argv) >=2 else "600.png")
image = image.resize((1000, 800), Image.ANTIALIAS)
canvas = tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)

canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)
click=1

def callback(event,click):
   
    
    print ("clicked at: ", event.x, event.y , click)
    if(click==1):
        ws.write(0,0 , event.x)
        ws.write(1,0 , event.y)
        #book.save('C:/Users/ASHUTOSH2408/Desktop/Excelfileq' + '.xls')
        
        
    else:
        ws.write(0,1 , event.x)
        ws.write(1,1 , event.y)
        book.save('C:/Users/ASHUTOSH2408/Desktop/Excelfileq' + '.xls')
        click=1

    
print("h")    
args=0
canvas.bind("<Button-1>",lambda event, args=args: callback(event ,args=args+1))

tkinter.mainloop()