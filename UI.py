from tkinter import*

class UI:
    def __init__(self):
        self.screen = Tk()
        self.screen.config(bg= '#375362')
        self.screen.title("Quizler")
        self.screen.config( padx=20,pady=30)
        self.screen.minsize(width=440, height=600)
        self.scorel = Label(text=f'score :{""}' ,bg='#375362' ,fg= 'white' , font= ('airal',10))
        self.scorel.grid(row=0,column=2)
        self.canva = Canvas(width=400,height=400)    
        self.questiondisplayed = self.canva.create_text(200,200,text='question',font=('Arial',20) ,fill="#375362")
        self.canva.grid(row=1,column=1,columnspan=2,pady=30)
        timg = PhotoImage(file="images/true.png")
        self.t = Button(image=timg)
        fimg = PhotoImage(file="images/false.png")
        self.f = Button(image=fimg)
        self.t.grid(row=2, column=1)
        self.f.grid(row=2,column=2)

        self.screen.mainloop()


    def addquestion(self ,tx):
        pass
        # txt = ls['question']
        # self.canva.grid(row=1,column=1,columnspan=2)