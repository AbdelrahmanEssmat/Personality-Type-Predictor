import tkinter
from tkinter import *
from tkinter import ttk
import array as arr
import numpy as np

root = Tk()
root.title('Personality Predictor Project')
root.geometry('1020x700')


# Create A Main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create Frame for X Scrollbar
sec = Frame(main_frame)
sec.pack(fill=X, side=BOTTOM)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbars to Canvas
y_scrollbar = ttk.Scrollbar(
    main_frame, orient=VERTICAL, command=my_canvas.yview)
y_scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas
my_canvas.configure(yscrollcommand=y_scrollbar.set)
my_canvas.bind("<Configure>", lambda e: my_canvas.config(
    scrollregion=my_canvas.bbox(ALL)))

# Create Another Frame INSIDE the Canvas
second_frame = Frame(my_canvas)
second_frame.configure(bg='#80b3ff')


# Add that New Frame a Window In The Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

input_list = [[]]
input_array = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def rad_q1_call():
    rad_q1_sal = rad_q1_Var.get()
    if rad_q1_sal == 1:
        input_array[0] = 1
    elif rad_q1_sal == 2:
        input_array[0] = 0
    print(input_array)


def rad_q2_call():
    rad_q2_sal = rad_q2_Var.get()
    if rad_q2_sal == 1:
        input_array[1] = 1
    elif rad_q2_sal == 2:
        input_array[1] = 0
    print(input_array)


def rad_q3_call():
    rad_q3_sal = rad_q3_Var.get()
    if rad_q3_sal == 1:
        input_array[2] = 1
    elif rad_q3_sal == 2:
        input_array[2] = 0
    print(input_array)


def rad_q4_call():
    rad_q4_sal = rad_q4_Var.get()
    if rad_q4_sal == 1:
        input_array[3] = 1
    elif rad_q4_sal == 2:
        input_array[3] = 0
    print(input_array)


def rad_q5_call():
    rad_q5_sal = rad_q5_Var.get()
    if rad_q5_sal == 1:
        input_array[4] = 1
    elif rad_q5_sal == 2:
        input_array[4] = 0
    print(input_array)


def rad_q6_call():
    rad_q6_sal = rad_q6_Var.get()
    if rad_q6_sal == 1:
        input_array[5] = 1
    elif rad_q6_sal == 2:
        input_array[5] = 0
    print(input_array)


def rad_q7_call():
    rad_q7_sal = rad_q7_Var.get()
    if rad_q7_sal == 1:
        input_array[6] = 1
    elif rad_q7_sal == 2:
        input_array[6] = 0
    print(input_array)


def rad_q8_call():
    rad_q8_sal = rad_q8_Var.get()
    if rad_q8_sal == 1:
        input_array[7] = 1
    elif rad_q8_sal == 2:
        input_array[7] = 0
    print(input_array)


def rad_q9_call():
    rad_q9_sal = rad_q9_Var.get()
    if rad_q9_sal == 1:
        input_array[8] = 1
    elif rad_q9_sal == 2:
        input_array[8] = 0
    print(input_array)


def rad_q10_call():
    rad_q10_sal = rad_q10_Var.get()
    if rad_q10_sal == 1:
        input_array[9] = 1
    elif rad_q10_sal == 2:
        input_array[9] = 0
    print(input_array)


def rad_q11_call():
    rad_q11_sal = rad_q11_Var.get()
    if rad_q11_sal == 1:
        input_array[10] = 1
    elif rad_q11_sal == 2:
        input_array[10] = 0
    print(input_array)


def rad_q12_call():
    rad_q12_sal = rad_q12_Var.get()
    if rad_q12_sal == 1:
        input_array[11] = 1
    elif rad_q12_sal == 2:
        input_array[11] = 0
    print(input_array)


def rad_q13_call():
    rad_q13_sal = rad_q13_Var.get()
    if rad_q13_sal == 1:
        input_array[12] = 1
    elif rad_q13_sal == 2:
        input_array[12] = 0
    print(input_array)


def rad_q14_call():
    rad_q14_sal = rad_q14_Var.get()
    if rad_q14_sal == 1:
        input_array[13] = 1
    elif rad_q14_sal == 2:
        input_array[13] = 0
    print(input_array)


def rad_q15_call():
    rad_q15_sal = rad_q15_Var.get()
    if rad_q15_sal == 1:
        input_array[14] = 1
    elif rad_q15_sal == 2:
        input_array[14] = 0
    print(input_array)


def rad_q16_call():
    rad_q16_sal = rad_q16_Var.get()
    if rad_q16_sal == 1:
        input_array[15] = 1
    elif rad_q16_sal == 2:
        input_array[15] = 0
    print(input_array)


def button():
    ff = []
    for i in range(16):
        ff.append(input_array[i])
    test = [ff]
    if Classifier.predict(test) == 0:
        Label1 = Label(second_frame, text='You Are An Extrovert', font=(
            'Arial 22'), fg='red', bg='#80b3ff').grid(row=51, column=0, padx=20, pady=20)
    if Classifier.predict(test) == 1:
        Label2 = Label(second_frame, text='You Are An Introvert', font=(
            'Arial 22'), fg='red', bg='#80b3ff').grid(row=51, column=0, padx=20, pady=20)


rad_q1_Var = tkinter.IntVar()
rad_q2_Var = tkinter.IntVar()
rad_q3_Var = tkinter.IntVar()
rad_q4_Var = tkinter.IntVar()
rad_q5_Var = tkinter.IntVar()
rad_q6_Var = tkinter.IntVar()
rad_q7_Var = tkinter.IntVar()
rad_q8_Var = tkinter.IntVar()
rad_q9_Var = tkinter.IntVar()
rad_q10_Var = tkinter.IntVar()
rad_q11_Var = tkinter.IntVar()
rad_q12_Var = tkinter.IntVar()
rad_q13_Var = tkinter.IntVar()
rad_q14_Var = tkinter.IntVar()
rad_q15_Var = tkinter.IntVar()
rad_q16_Var = tkinter.IntVar()


title = Label(second_frame, text='Personality Test', font=(
    'Arial 32'), fg='#e60000', bg='#80b3ff').grid(row=1, column=0, padx=10, pady=10)
subtitle = Label(second_frame, text='Kindly Answer These Questions :', font=(
    'Arial 16 underline'), fg='#0000b3', bg='#80b3ff').grid(row=2, column=0, padx=20, pady=20)

q1 = Label(second_frame, text='1. Do you often hangout with friends ?', font=(
    'Arial 14'), fg='black', bg='#80b3ff').grid(row=3, column=0, padx=20, pady=20)
rad1_q1 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                              variable=rad_q1_Var, value=1, command=rad_q1_call).grid(row=4, column=0)
rad2_q1 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                              variable=rad_q1_Var, value=2, command=rad_q1_call).grid(row=5, column=0)

q2 = Label(second_frame, text='2. Do you feel comfortable just walking up to someone you find interesting and striking up a conversation ?',
           font=('Arial 14'), fg='black', bg='#80b3ff').grid(row=6, column=0, padx=20, pady=20)
rad1_q2 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                              variable=rad_q2_Var, value=1, command=rad_q2_call).grid(row=7, column=0)
rad2_q2 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                              variable=rad_q2_Var, value=2, command=rad_q2_call).grid(row=8, column=0)

q3 = Label(second_frame, text='3. You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.',
           font=('Arial 14'), fg='black', bg='#80b3ff').grid(row=9, column=0, padx=20, pady=20)
rad1_q3 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                              variable=rad_q3_Var, value=1, command=rad_q3_call).grid(row=10, column=0)
rad2_q3 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                              variable=rad_q3_Var, value=2, command=rad_q3_call).grid(row=11, column=0)

q4 = Label(second_frame, text='4. After a long and exhausting week, a lively social event is just what you need.',
           font=('Arial 14'), fg='black', bg='#80b3ff').grid(row=12, column=0, padx=20, pady=20)
rad1_q4 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                              variable=rad_q4_Var, value=1, command=rad_q4_call).grid(row=13, column=0)
rad2_q4 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                              variable=rad_q4_Var, value=2, command=rad_q4_call).grid(row=14, column=0)

q5 = Label(second_frame, text='5. You tend to avoid drawing attention to yourself.', font=(
    'Arial 14'), fg='black', bg='#80b3ff').grid(row=15, column=0, padx=20, pady=20)
rad1_q5 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                              variable=rad_q5_Var, value=1, command=rad_q5_call).grid(row=16, column=0)
rad2_q5 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                              variable=rad_q5_Var, value=2, command=rad_q5_call).grid(row=17, column=0)

q6 = Label(second_frame, text='6. You usually prefer to be around others rather than on your own.',
           font=('Arial 14'), fg='black', bg='#80b3ff').grid(row=18, column=0, padx=20, pady=20)
rad1_q6 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                              variable=rad_q6_Var, value=1, command=rad_q6_call).grid(row=19, column=0)
rad2_q6 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                              variable=rad_q16_Var, value=2, command=rad_q6_call).grid(row=20, column=0)

q7 = Label(second_frame, text='7. You enjoy going to art museums.', font=(
    'Arial 14'), fg='black', bg='#80b3ff').grid(row=21, column=0, padx=20, pady=20)
rad1_q7 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                              variable=rad_q7_Var, value=1, command=rad_q7_call).grid(row=22, column=0)
rad2_q7 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                              variable=rad_q7_Var, value=2, command=rad_q7_call).grid(row=23, column=0)

q8 = Label(second_frame, text='8. In your social circle, you are often the one who contacts your friends and initiates activities.',
           font=('Arial 14'), fg='black', bg='#80b3ff').grid(row=24, column=0, padx=20, pady=20)
rad1_q8 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                              variable=rad_q8_Var, value=1, command=rad_q8_call).grid(row=25, column=0)
rad2_q8 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                              variable=rad_q8_Var, value=2, command=rad_q8_call).grid(row=26, column=0)

q9 = Label(second_frame, text='9. At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know.',
           font=('Arial 14'), fg='black', bg='#80b3ff').grid(row=27, column=0, padx=20, pady=20)
rad1_q9 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                              variable=rad_q9_Var, value=1, command=rad_q9_call).grid(row=28, column=0)
rad2_q9 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                              variable=rad_q9_Var, value=2, command=rad_q9_call).grid(row=29, column=0)

q10 = Label(second_frame, text='10. You enjoy participating in group activities.', font=(
    'Arial 14'), fg='black', bg='#80b3ff').grid(row=30, column=0, padx=20, pady=20)
rad1_q10 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                               variable=rad_q10_Var, value=1, command=rad_q10_call).grid(row=31, column=0)
rad2_q10 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                               variable=rad_q10_Var, value=2, command=rad_q10_call).grid(row=32, column=0)

q11 = Label(second_frame, text='11. You avoid leadership roles in group settings.', font=(
    'Arial 14'), fg='black', bg='#80b3ff').grid(row=33, column=0, padx=20, pady=20)
rad1_q11 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                               variable=rad_q11_Var, value=1, command=rad_q11_call).grid(row=34, column=0)
rad2_q11 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                               variable=rad_q11_Var, value=2, command=rad_q11_call).grid(row=35, column=0)

q12 = Label(second_frame, text='12.You enjoy watching people argue.', font=(
    'Arial 14'), fg='black', bg='#80b3ff').grid(row=36, column=0, padx=20, pady=20)
rad1_q12 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                               variable=rad_q12_Var, value=1, command=rad_q12_call).grid(row=37, column=0)
rad2_q12 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                               variable=rad_q12_Var, value=2, command=rad_q12_call).grid(row=38, column=0)

q13 = Label(second_frame, text='13. You avoid making phone calls.', font=(
    'Arial 14'), fg='black', bg='#80b3ff').grid(row=39, column=0, padx=20, pady=20)
rad1_q13 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                               variable=rad_q13_Var, value=1, command=rad_q13_call).grid(row=40, column=0)
rad2_q13 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                               variable=rad_q13_Var, value=2, command=rad_q13_call).grid(row=41, column=0)

q14 = Label(second_frame, text='14. You rarely feel insecure.', font=(
    'Arial 14'), fg='black', bg='#80b3ff').grid(row=42, column=0, padx=20, pady=20)
rad1_q14 = tkinter.Radiobutton(second_frame, text="Yes", bg='#80b3ff',
                               variable=rad_q14_Var, value=1, command=rad_q14_call).grid(row=43, column=0)
rad2_q14 = tkinter.Radiobutton(second_frame, text="No", bg='#80b3ff',
                               variable=rad_q14_Var, value=2, command=rad_q14_call).grid(row=44, column=0)

q15 = Label(second_frame, text='15. What is your gender?', font=(
    'Arial 14'), fg='black', bg='#80b3ff').grid(row=45, column=0, padx=20, pady=20)
rad1_q15 = tkinter.Radiobutton(second_frame, text="Male", bg='#80b3ff',
                               variable=rad_q15_Var, value=1, command=rad_q15_call).grid(row=46, column=0)
rad2_q15 = tkinter.Radiobutton(second_frame, text="Female", bg='#80b3ff',
                               variable=rad_q15_Var, value=2, command=rad_q15_call).grid(row=47, column=0)

q16 = Label(second_frame, text='16. How old are you ?', font=(
    'Arial 14'), fg='black', bg='#80b3ff').grid(row=48, column=0, padx=20, pady=20)
rad1_q16 = tkinter.Radiobutton(second_frame, text="More than 21", bg='#80b3ff',
                               variable=rad_q16_Var, value=1, command=rad_q16_call).grid(row=49, column=0)
rad2_q16 = tkinter.Radiobutton(second_frame, text="Less than 21", bg='#80b3ff',
                               variable=rad_q16_Var, value=2, command=rad_q16_call).grid(row=50, column=0)

submit = Button(second_frame, text='Submit', command=button).grid(
    row=51, column=0, pady=20)


root.mainloop()
