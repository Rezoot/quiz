from tkinter import Button,Text,Tk
from random import shuffle
tabelka1=[]
tabelka2=[]
f='pytania.txt'
ktore=0
def nowa():
    global ktore
    ktore=-1
    shuffle(tabelka2)
    nast()
def sprawdz(but):
    if but.cget('text')==tabelka2[ktore][5][3:]:
        but.config(bg="green")
    else:
        but.config(bg="red")
def nast():
    global ktore,tabelka2
    ktore+=1
    tek.delete("1.0","end")
    if ktore<len(tabelka1)/6:
        tek.insert("end",tabelka2[ktore][0])
        odp=tabelka2[ktore][1:5]
        shuffle(odp)
        shuffle(odp) 
        a.config(text=odp[0][3:],bg="grey")
        b.config(text=odp[1][3:],bg="grey")
        c.config(text=odp[2][3:],bg="grey")
        d.config(text=odp[3][3:],bg="grey")
    else:
        tek.insert("end","koniec")
        a.config(text="",command="")
        b.config(text="",command="")
        c.config(text="",command="")
        d.config(text="",command="")
with open(f,encoding="UTF-8") as fil:
    for i in fil:
        tabelka1.append(i)   
for i in range(0,len(tabelka1),6):
    tabelka2.append(tabelka1[i:i+6])
shuffle(tabelka2) 
shuffle(tabelka2) 
quiz=Tk()
tek=Text(quiz,height=8,font=("a",20))
a=Button(quiz,text='',command=lambda: sprawdz(a),bg="grey")
b=Button(quiz,text='',command=lambda: sprawdz(b),bg="grey")
c=Button(quiz,text='',command=lambda: sprawdz(c),bg="grey")
d=Button(quiz,text='',command=lambda: sprawdz(d),bg="grey")
nastepne=Button(quiz,text="nastepne",command=nast,width=100,height=4,bg="pink").grid(row=10,column=0,columnspan=10)
odnowa=Button(quiz,text="od nowa",command=nowa,width=100,height=4,bg="pink").grid(row=11,column=0,columnspan=10)
tek.insert("end",tabelka2[ktore][0])
odp=tabelka2[ktore][1:5]
shuffle(odp)
shuffle(odp) 
a.config(text=odp[0][3:])
b.config(text=odp[1][3:])
c.config(text=odp[2][3:])
d.config(text=odp[3][3:])
tek.grid(row=0,column=0,columnspan=4)
a.grid(row=2,column=0,columnspan=2,rowspan=2)
b.grid(row=2,column=2,columnspan=2,rowspan=2)
c.grid(row=4,column=0,columnspan=2)
d.grid(row=4,column=2,columnspan=2,rowspan=2)
quiz.mainloop()