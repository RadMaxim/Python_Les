import cv2
import tkinter as tk
# root=tk.Tk()
# root1=tk.Tk()
# root.title("My Window")
# root1.title("My Window1")
# root.geometry("1000x100")
# root1.geometry("100x1000")
# root.mainloop()
# root1.mainloop()
# for id,i in enumerate(range(10),1):
#     root=tk.Tk()
#     root.title("My Window")
#     root.geometry(f"{str(100*id)}x{str(100*id)}")
#     root.mainloop()
#     cv2.waitKey(1000)

import cv2
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("OCV Tkinter")
#Сначала мы создаем фрейм в окне с определенными размерами (как окно в окне)
imageFrame = tk.Frame(window, width=600, height=500)

# Затем мы создаем сетку нашего окна с координатами (это как отступы у ворд)
imageFrame.grid(row=0, column=0, padx=10, pady=2)
# Создаем метку лейбл, которая будет играть роль транслируемого изображения, а также создаем для нее сетку, где именно будет находиться наше изображение
label = tk.Label(imageFrame)
label.grid(row=0, column=0)
# Считываем значение из камеры и переводим в понятный формат с помощью метода fromarray()
cap = cv2.VideoCapture(0)
# Вся функция вызывается раз и запускается окно с нашим изображением
def show_frame():
   global frame
   _, frame = cap.read()
   frame= cv2.flip(frame, 1)
   img = Image.fromarray(frame)
   # Теперь мы можем занести в наш лейбл считаемые изображения.
   # Наше изображение будет отображаться как фоновое изображение метки,
   # выставив это с помощью configure(image=imgtk)
   imgtk = ImageTk.PhotoImage(image=img)
   label.image = imgtk
   label.configure(image=imgtk)
   # Метод after позволяет нам с таймаутом в мс перезапускать нашу функцию снова.
   label.after(10, show_frame)
def saveimg():
   cv2.imwrite("myphoto.png", frame)
   print("Successful")

button = tk.Button(imageFrame, text="Hello",command=saveimg)
button.grid(row=1, column=0)
show_frame()
window.mainloop()


