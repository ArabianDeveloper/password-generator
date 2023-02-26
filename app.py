from tkinter import *
import random
def generate():
    passlen = int(spn.get())
    passent.delete(0,passlen)
    chars = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890!@#$%^&*?_'
    passw = ''
    for i in range(passlen):
        passw += random.choice(chars)

    passent.insert(INSERT, passw)

root = Tk()
root.geometry('220x125')
root.resizable(False, False)
btnco = Button(root, text='نسخ', font=("Tajawal", 9))
btnco.place(x = 15, y = 30, width = 40, height = 30)

passent = Entry(root, font=('Tajawal', 14))
passent.place(x = 60, y = 30, width = 140)

spn = Spinbox(root, from_=0, to=50, font=("Tajawal", 9))
spn.place(x = 160, y = 65, width = 40, height = 30)

btncr = Button(root, text='انشاء', command=generate, font=("Tajawal", 9))
btncr.place(x = 15, y = 65, width = 140, height = 30)

rilab = Label(root, text='جميع الحقوق محفوظة ©', font=("Tajawal", 8))
rilab.place(x = 45, y = 100)
root.mainloop()