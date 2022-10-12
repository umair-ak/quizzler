from tkinter import*
from data import Data
import time

class QuizLogicAndInterface:
    def __init__(self,tx:Data):
        self.i = 0
        self.score = 0
        self.screen = Tk()
        self.Q = tx.getQuestions()
        self.screen.config(bg= '#375362')
        self.screen.title("Quizler")
        self.screen.config( padx=20,pady=30)
        self.screen.minsize(width=440, height=600)
        self.scorel = Label(text=f'score :{""}' ,bg='#375362' ,fg= 'white' , font= ('airal',10))
        self.scorel.grid(row=0,column=2)
        self.canva = Canvas(width=400,height=400)    
        self.questiondisplayed = self.canva.create_text(200,200,text='question',font=('Arial',20) ,fill="#375362" , width=370)
        self.canva.grid(row=1,column=1,columnspan=2,pady=30)
        timg = PhotoImage(file="images/true.png")
        self.t = Button(image=timg , command=self.checkiftrue)
        fimg = PhotoImage(file="images/false.png")
        self.f = Button(image=fimg , command=self.checkiffalse)
        self.t.grid(row=2, column=1)
        self.f.grid(row=2,column=2)
        self.addquestion(self.Q)
        

        self.screen.mainloop()

    def quizover(self):
        self.canva.itemconfig(self.questiondisplayed,text=f"The Quiz is over !!\nyour score is {self.score}")

    def checkiftrue(self):
        try:
            corr = self.Q[self.i]['correct_answer']

        except IndexError:
            self.quizover()
            
        else:
            self.i += 1
            if corr == 'True':
                self.score +=1
                self.changecolor('green')
                
            else:
                self.changecolor('red')

    def checkiffalse(self):
        try :
            corr = self.Q[self.i]['correct_answer']
        except IndexError:
            self.quizover()
            
        else:
            self.i += 1
            if corr == "False":
                self.score +=1
                self.changecolor('green')
            else:
                self.changecolor('red')
        
    def changecolor(self,COLOR):
        self.canva.config(bg=COLOR)
        self.screen.after(700,self.addquestion , self.Q)


    def addquestion(self ,tx):
        self.canva.config(bg="white")
        try:
            texT = f"Q{self.i+1} {tx[self.i]['question']}"
        except IndexError:
            self.quizover()
            
        else:
            self.canva.itemconfig(self.questiondisplayed,text=texT)
        finally:
            self.scorel.config(text=f"Score :{self.score}")
        