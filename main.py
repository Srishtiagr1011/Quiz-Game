from tkinter import *

questions = [
    "Which infinity stone would you choose?",
    "Who is your favourite actor?",
    "What's your best personality traits?",
    "Which height is best suited to you?",
    "Which favourite food would you prefer?",
    "What's your strength?",
    "Which weapon would you select?",
    "What is your best feature?",
    "What is your weaknesses?",
    "What is your biggest flaw?",
    "What you do in your free time?",
    "How is your relation with your friends?"
]

firstoption = ["The Reality Stone", "Chris Hemsworth","Unpredictable","6'6''","Junk food","Your Royal status","Hammer","Worthy","Your relationship","Determination",
               "Reading","Have great \nfriendships"
]

secondoption = ["The Mind Stone", "Tony Stark","Strong","6'3''","Burgers","Your mind and body","Repulsor","Mind","Easily can get hurt","Arrogant","Work",
                "Enjoy's everyone \ncompany"
]

thirdoption = ["The Space Stone", "Chris Evans","Honest","6'1''","Apple pie","Your courage","Sheild","Protective","Petty side","Akward around people",
               "WIth friends or family","Have a number of\n great friends"
]

fourthoption = ["The Ego Stone", "Mark Raffalo","Angry","7'6''","Beans","Your reality","Axe","Strength","Your ego","Inconsistency","Alone time",
                "Dosen't have \nmany friends"
]
#score=["Thor","Iron Man,"Captain America","The Hulk"]
score = [0, 0, 0, 0]
#start quiz
def start():
    logoLabel.destroy()
    startButton.destroy()
    startquiz()
#quiz ui page
def startquiz():
    topFrame = Frame(root, bg='black')
    topFrame.grid(row=0, column=0)

    bottomFrame = Frame(root, bg='black')
    bottomFrame.grid(row=1, column=0)

    global layLabel, layoutLabel, labelA, labelB, labelC, labelD
    layLabel = Label(topFrame, image=layImage, bg='black', width=1500, height=500, bd=0)
    layLabel.grid(row=0, column=0)

    layoutLabel = Label(bottomFrame, image=layoutImage, bg='black', width=750, height=300, bd=0)
    layoutLabel.grid(row=1, column=0)

    labelA=Label(bottomFrame,text='A:', font=('arial', 13, 'bold'), bg='black', fg='white', bd=0)
    labelA.place(x=140, y=135)
    labelB = Label(bottomFrame, text='B:', font=('arial', 13, 'bold'), bg='black', fg='white', bd=0)
    labelB.place(x=140, y=220)
    labelC = Label(bottomFrame, text='C:', font=('arial', 13, 'bold'), bg='black', fg='white', bd=0)
    labelC.place(x=420, y=135)
    labelD = Label(bottomFrame, text='D:', font=('arial', 13, 'bold'), bg='black', fg='white', bd=0)
    labelD.place(x=420, y=220)
    global questionArea, optionButton1, optionButton2, optionButton3, optionButton4
    questionArea = Text(bottomFrame, font=('arial', 18, 'bold'), width=34, height=2, wrap='word', bg='black',
                        fg='white', bd=0)
    questionArea.place(x=155, y=35)
    questionArea.insert(END, questions[0])

    optionButton1=Button(bottomFrame, text=firstoption[0], font=('arial', 13, 'bold'), bg='black', fg='white', bd=0,
                         activebackground='black',activeforeground='white', cursor='hand2')
    optionButton1.place(x=160,y=132)
    optionButton2 = Button(bottomFrame, text=secondoption[0], font=('arial', 13, 'bold'), bg='black', fg='white', bd=0,
                           activebackground='black',activeforeground='white',cursor='hand2')
    optionButton2.place(x=160, y=218)
    optionButton3 = Button(bottomFrame, text=thirdoption[0], font=('arial', 13, 'bold'), bg='black', fg='white', bd=0,
                           activebackground='black',activeforeground='white',cursor='hand2')
    optionButton3.place(x=440, y=132)
    optionButton4 = Button(bottomFrame, text=fourthoption[0], font=('arial', 13, 'bold'), bg='black', fg='white', bd=0,
                           activebackground='black',activeforeground='white',cursor='hand2')
    optionButton4.place(x=440, y=218)

    optionButton1.bind('<Button-1>', select)
    optionButton2.bind('<Button-1>', select)
    optionButton3.bind('<Button-1>', select)
    optionButton4.bind('<Button-1>', select)
#option button is clicked(change of questions)
def select(event):
    global questionArea, optionButton1, optionButton2, optionButton3, optionButton4
    b = event.widget
    value = b['text']
    for i in range(12):
        if value == firstoption[i]:
            if i == 11:
                result()
                break
            score[0] = score[0] + 1
            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i+1])
            optionButton1.config(text=firstoption[i+1])
            optionButton2.config(text=secondoption[i+1])
            optionButton3.config(text=thirdoption[i+1])
            optionButton4.config(text=fourthoption[i+1])

        elif value == secondoption[i]:
            if i == 11:
                result()
                break
            score[1] = score[1] + 1
            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])
            optionButton1.config(text=firstoption[i + 1])
            optionButton2.config(text=secondoption[i + 1])
            optionButton3.config(text=thirdoption[i + 1])
            optionButton4.config(text=fourthoption[i + 1])

        elif value == thirdoption[i]:
            if i == 11:
                result()
                break
            score[2] = score[2] + 1
            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])
            optionButton1.config(text=firstoption[i + 1])
            optionButton2.config(text=secondoption[i + 1])
            optionButton3.config(text=thirdoption[i + 1])
            optionButton4.config(text=fourthoption[i + 1])

        elif value == fourthoption[i]:
            if i == 11:
                result()
                break
            score[3] = score[3] + 1
            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])
            optionButton1.config(text=firstoption[i + 1])
            optionButton2.config(text=secondoption[i + 1])
            optionButton3.config(text=thirdoption[i + 1])
            optionButton4.config(text=fourthoption[i + 1])
#print(score)
#calculation of results
def result():
    layLabel.destroy()
    layoutLabel.destroy()
    questionArea.destroy()
    optionButton1.destroy(), optionButton2.destroy(), optionButton3.destroy(), optionButton4.destroy()
    labelA.destroy(), labelB.destroy(), labelC.destroy(), labelD.destroy()
    #print(score)
    maxscore = max(score)

    imLabel = Label(root, image=imImage, bd=0, width=250, height=250, bg='black')
    imLabel.place(x=200, y=100)
    imA = Label(root, text='Iron Man', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0)
    imA.place(x=250, y=60)
    thorLabel = Label(root, image=thorImage, bd=0, width=250, height=250, bg='black')
    thorLabel.place(x=500, y=100)
    thor= Label(root, text='Thor', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0)
    thor.place(x=580, y=60)
    hulkLabel = Label(root, image=hulkImage, bd=0, width=250, height=250, bg='black')
    hulkLabel.place(x=800, y=100)
    hulk = Label(root, text='Hulk', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0)
    hulk.place(x=880, y=60)
    capamericaLabel = Label(root, image=capamericaImage, bd=0, width=250, height=250, bg='black')
    capamericaLabel.place(x=1100, y=100)
    capamerica = Label(root, text='Captain America', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0)
    capamerica.place(x=1140, y=60)

    if(maxscore == score[0]):
        resulti=Label(root, text='Congratulations!! You are Thor.', font=('arial', 25, 'bold'), bg='black', fg='white', bd=0)
        resulti.place(x=600, y=400)
        thorim = Label(root, image=thorImage, bd=0, width=250, height=250, bg='black')
        thorim.place(x=300, y=500)
        resultii = Label(root, text='You are constantly growing and changing as a person.\nYou and your friends know you are multi-dimensional.' , font=('arial', 25, 'bold'), bg='black',
                        fg='white', bd=0)
        resultii.place(x=580, y=550)
    elif (maxscore == score[1]):
        resulti = Label(root, text='Congratulations!! You are Iron Man.', font=('arial', 25, 'bold'), bg='black',
                            fg='white', bd=0)
        resulti.place(x=600, y=400)
        imim = Label(root, image=imImage, bd=0, width=250, height=250, bg='black')
        imim.place(x=300, y=500)
        resultii = Label(root, text='Just Like Iron Man you are brash but brilliant character.\n You are there for your friends no matter what.', font=('arial', 25, 'bold'), bg='black',
                         fg='white', bd=0)
        resultii.place(x=580, y=550)
    elif (maxscore == score[2]):
        resulti = Label(root, text='Congratulations!! You are Captain America.', font=('arial', 25, 'bold'), bg='black',
                        fg='white', bd=0)
        resulti.place(x=600, y=400)
        capim = Label(root, image=capamericaImage, bd=0, width=250, height=250, bg='black')
        capim.place(x=300, y=500)
        resultii = Label(root, text='A natural born leader who stands out from the crowd.\n You are never afraid to talk your own mind.', font=('arial', 25, 'bold'), bg='black',
                         fg='white', bd=0)
        resultii.place(x=580, y=550)
    elif (maxscore == score[3]):
        resulti = Label(root, text='Congratulations!! You are Hulk.', font=('arial', 25, 'bold'), bg='black',
                        fg='white', bd=0)
        resulti.place(x=600, y=400)
        hulkim = Label(root, image=hulkImage, bd=0, width=250, height=250, bg='black')
        hulkim.place(x=300, y=500)
        resultii = Label(root, text='Fiercely protective of friends and family you are always \nthere to help out in a time of need.'
                                    '\n You always have the best intention at heart.', font=('arial', 25, 'bold'), bg='black',
                         fg='white', bd=0)
        resultii.place(x=580, y=550)

root=Tk()

root.geometry('1530x1300+0+0')
root.title('Which Avenger Are You?')
root.config(bg='black')
root.resizable(0,0)

topImage = PhotoImage(file='background.png')
logoLabel = Label(root, image=topImage, bd=0, width=1500, height=800, bg='black')
logoLabel.grid(row=0, column=0)

startImage = PhotoImage(file='start.png')
startButton = Button(root, image=startImage, bd=0, bg='black', relief=FLAT, cursor='hand2', activebackground='black', width=300,
                       height=60, command=start)
startButton.place(x=600, y=320)
layImage = PhotoImage(file='top.png')
layoutImage = PhotoImage(file='lay.png')
imImage = PhotoImage(file='ironman.png')
thorImage = PhotoImage(file='thor.png')
hulkImage = PhotoImage(file='hulk.png')
capamericaImage = PhotoImage(file='capamerica.png')


root.mainloop()