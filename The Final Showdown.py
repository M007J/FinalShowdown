# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 00:21:48 2020
Finished On Thu Jan 21 19:18:24 2021

@author: M7J, Shresth, Amol, Arnav
"""


from tkinter import *
from threading import Event
from random import *
A='Black'
#StartScreen
Battle=Tk()
Battle.title("The Final Showdown")
Battle.configure(bg="Black")
Battle.geometry("725x330")
SP= PhotoImage(file="StImg.png")
Battle.iconbitmap("GameIcon.ico")
global GameCnt
global GameWonCnt
GameCnt=0
GameWonCnt=0

global ScrCnt
ScrCnt=0
GamFrame=Label(Battle,height=330,width=599,bd=0,image=SP)
GamFrame.grid(row=0,column=0,rowspan=5,columnspan=1)

#ExitButton
def ExGa():
    global ScrCnt
    global GameScr
    if ScrCnt==0:
        Tk.destroy(Battle)
    else:
        Tk.destroy(GameScr)

#OptionButton    
def OptGa():
    
    OptionScr=Tk()
    OptionScr.title("The Final Showdown")
    OptionScr.iconbitmap("GameIcon.ico")
    OptionScr.geometry("200x150")
    
    #BGChange&DimensionChange
    def Bchan():
        global A
        A=Bg.get(ANCHOR)
        Battle.configure(bg=str(A))
        Tk.destroy(OptionScr)
    
    BgL=Label(OptionScr,text="Enter background colour").grid(row=0,column=0)    
    Bg=Listbox(OptionScr,selectmode=SINGLE,height=2)
    Bg.grid(row=1,column=0)
    Col=["Red","Blue","Green","Black","Brown","Pink","Turquoise","Navy","Seagreen","Cyan","Dark Cyan","MidnightBlue"]
    for i in range(len(Col)):
        Bg.insert(i,Col[i])
    
    BgChan=Button(OptionScr,height=2,width=8,text="Change",command=Bchan).grid(row=4,column=0)        
    
#StartGameButton
def OpGa():
    global ScrCnt
    global GameScr
    if ScrCnt==0:
        Tk.destroy(Battle)
    else:
        Tk.destroy(GameScr)
    
    #FightScreen
    GameScr=Tk()
    GameScr.geometry("923x480")
    global A
    GameScr.config(bg=A)
    GameScr.title("The Final Showdown")
    GameScr.iconbitmap("GameIcon.ico")

    
    ScrCnt=1
    
    PlMg=Label(GameScr,height=1,width=26,bg=A,text="Choose your player wisely !",font=("playbill",67),fg="#ff0000").grid(row=0,column=0,columnspan=4)
    
    FightScr=Canvas(GameScr,height=300,width=923,highlightthickness=0)
    Img=PhotoImage(file="CharIMG\DJ DeathF.png")
    I=FightScr.create_image(0,0,image=Img,anchor=NW)
    Img2=PhotoImage(file="CharIMG\PicLassoF.png")
    I2=FightScr.create_image(201,0,image=Img2,anchor=NW)
    Img3=PhotoImage(file="CharIMG\ZolkaF.png")
    I3=FightScr.create_image(377,0,image=Img3,anchor=NW)
    Img4=PhotoImage(file="CharIMG\BarbTheVikingF.png")
    I4=FightScr.create_image(599,0,image=Img4,anchor=NW)
    
    FightScr.grid(row=1,column=0,columnspan=4)
    
    global Char1S
    global Char2S
    global Char3S
    global Char4S

    Char1S=1
    Char2S=1
    Char3S=1
    Char4S=1
    def Clear(frame):
        for widget in frame.grid_slaves():
            widget.destroy()
    def Clear2(frame):
        for widget in frame.grid_slaves():
            if str(type(widget))=="<class 'tkinter.Button'>":
                widget.destroy()
            
    def Ch1():
        Char1B=Button(GameScr,height=1,width=8,text="DJ Death",command=Ch1,state=DISABLED).grid(row=2,column=0)
        
        global Char1S
        global Char2S
        global Char3S
        global Char4S
        Char1S=0

        
        if Char2S==0 or Char3S==0 or Char4S==0:
            
            Clear(GameScr)
            
            
            global djdeath
            global djdeathLabel
            djdeath=PhotoImage(file="CharIMG\DJ DeathF.png")
            WMsgDJ=PhotoImage(file='WLMsg\WMsgDJ.png')
            djdeathLabel=Label(GameScr,height=300,width=201,bd=0,image=djdeath)
            djdeathLabel.grid(column=1,row=0)        
            Cnt=[44,44,44,74]
            global HHealth
            global OHealth
            HHealth=100
            OHealth=100
            global OHeMe
            OHeMe=Label(GameScr,height=1,width=24,text=str(OHealth)+':Health',font=('playbill',20),bg=A,fg='red',anchor=E)
            OHeMe.grid(row=1,column=1)
            global HeMe
            HeMe=Label(GameScr,height=1,width=21,text='Health:'+str(HHealth),font=("playbill",20),bg=A,fg='green',anchor=W)
            HeMe.grid(row=1,column=0)
            
            if Char2S==0:
                LMsgPL=PhotoImage(file='WLMsg\LMsgPL.png')
                GameScr.geometry("377x420")

                piclasso=PhotoImage(file="CharIMG\PicLassoF.png")
                piclassoLabel=Label(GameScr,height=300,width=176,bd=0,image=piclasso)
                piclassoLabel.grid(column=0,row=0)
                
                PL1='AttackAnimation\PLBoomBox.gif'
                PL2='AttackAnimation\PLShockWaveGrenade.gif'
                PL3='AttackAnimation\PLDeadlyBeat.gif'
                PL4='AttackAnimation\PLMusicalEntrapment.gif'
                PLAttack=[PL1,PL2,PL3,PL4]
                
                def at1():                
                    
                    global djdeathLabel
                    global djdeath
                    attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
    
                    DJ5=[PhotoImage(file='AttackAnimation\DJBrushAttack.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        frameCnt=44
                        if ind==frameCnt:
                            djdeathLabel.configure(image=djdeath)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth) +':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=201,bd=0,image=WMsgDJ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=PLAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                PL=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)
                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:' + str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=176,bd=0,image=LMsgPL)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.configure(image=piclasso)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = PL[ind]
                                        ind+=1
                                        piclassoLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()
                        else:
                            frame = DJ5[ind]
                            ind+=1
                            djdeathLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at2():
                    global djdeathLabel
                    global djdeath
                
                    attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=59
                    DJ6=[PhotoImage(file='AttackAnimation\DJPaintBomb.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            djdeathLabel.configure(image=djdeath)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=201,bd=0,image=WMsgDJ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=PLAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                PL=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=176,bd=0,image=LMsgPL)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            piclassoLabel.configure(image=piclasso)
                                            Event().wait(0.5)
            
                                            attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = PL[ind]
                                        ind+=1
                                        piclassoLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()
                            

                        else:
                            frame = DJ6[ind]
                            ind+=1
                            djdeathLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at3():
                    global djdeathLabel
                    global djdeath
                    attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=59
                    DJ7=[PhotoImage(file='AttackAnimation\DJLassoDeath.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            djdeathLabel.configure(image=djdeath)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=201,bd=0,image=WMsgDJ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=PLAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                PL=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=176,bd=0,image=LMsgPL)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            piclassoLabel.configure(image=piclasso)
                                            Event().wait(0.5)                                    
                                            attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = PL[ind]
                                        ind+=1
                                        piclassoLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                                
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = DJ7[ind]
                            ind+=1
                            djdeathLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                def at4():
                    global djdeathLabel
                    global djdeath
                    attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                        
                    frameCnt=44
                    DJ8=[PhotoImage(file='AttackAnimation\DJSixShooter.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        
                        if ind==frameCnt:
                            djdeathLabel.configure(image=djdeath)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=201,bd=0,image=WMsgDJ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=PLAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                PL=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=176,bd=0,image=LMsgPL)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            piclassoLabel.configure(image=piclasso)
                                            Event().wait(0.5)
                                            
                                            attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = PL[ind]
                                        ind+=1
                                        piclassoLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                                        
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = DJ8[ind]
                            ind+=1
                            djdeathLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
    
                
                attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1).grid(column=0,row=2,pady=5)
                attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2).grid(column=1,row=2,pady=5)
                attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3).grid(column=0,row=3,pady=5)
                attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4).grid(column=1,row=3,pady=5)
                GameScr.mainloop()

            elif Char3S==0:
                HeMe.configure(width=26)
                LMsgZ=PhotoImage(file='WLMsg\LMsgZ.png')
                GameScr.geometry("423x420")

                zolka=PhotoImage(file="CharIMG\ZolkaF.png")
                zolkaLabel=Label(GameScr,height=300,width=222,bd=0,image=zolka)
                zolkaLabel.grid(column=0,row=0)

                Z1='AttackAnimation\ZBoomBox.gif'
                Z2='AttackAnimation\ZShockWaveGrenade.gif'
                Z3='AttackAnimation\ZDeadlyBeat.gif'
                Z4='AttackAnimation\ZMusicalEntrapment.gif'
                ZAttack=[Z1,Z2,Z3,Z4]
                
                def at1():
                    global djdeathLabel
                    global djdeath
                    attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    DJ9=[PhotoImage(file='AttackAnimation\DJVoicesFromTheVoid.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            djdeathLabel.configure(image=djdeath)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=201,bd=0,image=WMsgDJ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=ZAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                Z=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            zolkaLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=222,bd=0,image=LMsgZ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            zolkaLabel.configure(image=zolka)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = Z[ind]
                                        ind+=1
                                        zolkaLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = DJ9[ind]
                            ind+=1
                            djdeathLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at2():
                    global djdeathLabel
                    global djdeath
                    attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=89
                    DJ10=[PhotoImage(file='AttackAnimation\DJFireball.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            djdeathLabel.configure(image=djdeath)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=201,bd=0,image=WMsgDJ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=ZAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                Z=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            zolkaLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=222,bd=0,image=LMsgZ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            zolkaLabel.configure(image=zolka)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = Z[ind]
                                        ind+=1
                                        zolkaLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = DJ10[ind]
                            ind+=1
                            djdeathLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at3():
                    global djdeathLabel
                    global djdeath
                    attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    DJ11=[PhotoImage(file='AttackAnimation\DJMindDestruction.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            djdeathLabel.configure(image=djdeath)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=201,bd=0,image=WMsgDJ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=ZAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                Z=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            zolkaLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=222,bd=0,image=LMsgZ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            zolkaLabel.configure(image=zolka)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = Z[ind]
                                        ind+=1
                                        zolkaLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = DJ11[ind]
                            ind+=1
                            djdeathLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                def at4():
                    global djdeathLabel
                    global djdeath
                    attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                        
                    frameCnt=59
                    DJ12=[PhotoImage(file='AttackAnimation\DJShroudedStep.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        
                        if ind==frameCnt:
                            djdeathLabel.configure(image=djdeath)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=201,bd=0,image=WMsgDJ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=ZAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                Z=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            zolkaLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=222,bd=0,image=LMsgZ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            zolkaLabel.configure(image=zolka)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = Z[ind]
                                        ind+=1
                                        zolkaLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = DJ12[ind]
                            ind+=1
                            djdeathLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1).grid(column=0,row=2,pady=5)
                attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2).grid(column=1,row=2,pady=5)
                attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3).grid(column=0,row=3,pady=5)
                attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4).grid(column=1,row=3,pady=5)
                GameScr.mainloop()

            elif Char4S==0:
                HeMe.configure(width=37)
                LMsgBTV=PhotoImage(file='WLMsg\LMsgBTV.png')
                GameScr.geometry("525x420")

                barbtheviking=PhotoImage(file="CharIMG\BarbTheVikingF.png")
                barbthevikingLabel=Label(GameScr,height=300,width=324,bd=0,image=barbtheviking)
                barbthevikingLabel.grid(column=0,row=0)

                BTV1='AttackAnimation\BTVBoomBox.gif'
                BTV2='AttackAnimation\BTVShockwaveGrenade.gif'
                BTV3='AttackAnimation\BTVDeadlyBeat.gif'
                BTV4='AttackAnimation\BTVMusicalEntrapment.gif'
                BTVAttack=[BTV1,BTV2,BTV3,BTV4]
                
                def at1():
                    global djdeathLabel
                    global djdeath
                    attack1=Button(GameScr,text="Axe of Destruction ",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    DJ13=[PhotoImage(file='AttackAnimation\DJAxeOfDestruction.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            djdeathLabel.configure(image=djdeath)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=201,bd=0,image=WMsgDJ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=BTVAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                BTV=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            barbthevikingLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=324,bd=0,image=LMsgBTV)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            barbthevikingLabel.configure(image=barbtheviking)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Axe of Destruction ",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = BTV[ind]
                                        ind+=1
                                        barbthevikingLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = DJ13[ind]
                            ind+=1
                            djdeathLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at2():
                    global djdeathLabel
                    global djdeath
                    attack1=Button(GameScr,text="Axe of Destruction ",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    DJ14=[PhotoImage(file='AttackAnimation\DJColossalPunch.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            djdeathLabel.configure(image=djdeath)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=201,bd=0,image=WMsgDJ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=BTVAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                BTV=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            barbthevikingLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=324,bd=0,image=LMsgBTV)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            barbthevikingLabel.configure(image=barbtheviking)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Axe of Destruction ",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = BTV[ind]
                                        ind+=1
                                        barbthevikingLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = DJ14[ind]
                            ind+=1
                            djdeathLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at3():
                    global djdeathLabel
                    global djdeath
                    attack1=Button(GameScr,text="Axe of Destruction ",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    DJ15=[PhotoImage(file='AttackAnimation\DJVikingRage.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            djdeathLabel.configure(image=djdeath)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=201,bd=0,image=WMsgDJ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=BTVAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                BTV=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            barbthevikingLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=324,bd=0,image=LMsgBTV)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            barbthevikingLabel.configure(image=barbtheviking)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Axe of Destruction ",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = BTV[ind]
                                        ind+=1
                                        barbthevikingLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = DJ15[ind]
                            ind+=1
                            djdeathLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                def at4():
                    global djdeathLabel
                    global djdeath
                    attack1=Button(GameScr,text="Axe of Destruction ",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                        
                    frameCnt=44
                    DJ16=[PhotoImage(file='AttackAnimation\DJBrogueKick.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        
                        if ind==frameCnt:
                            djdeathLabel.configure(image=djdeath)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=201,bd=0,image=WMsgDJ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=BTVAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                BTV=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            barbthevikingLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=324,bd=0,image=LMsgBTV)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                            
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            barbthevikingLabel.configure(image=barbtheviking)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Axe of Destruction ",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = BTV[ind]
                                        ind+=1
                                        barbthevikingLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                           
                            frame = DJ16[ind]
                            ind+=1
                            djdeathLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()

                attack1=Button(GameScr,text="Axe Of Destruction",height=1,width=18,bg='orange',fg='white',command=at1).grid(column=0,row=2,pady=5)
                attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2).grid(column=1,row=2,pady=5)
                attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3).grid(column=0,row=3,pady=5)
                attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4).grid(column=1,row=3,pady=5)
                GameScr.mainloop()
                
        else:
            PlMg=Label(GameScr,height=1,width=26,bg=A,text="Choose your opponent!",font=("playbill",67),fg='#ff0000').grid(row=0,column=0,columnspan=4)
            
    def Ch2():
        Char2B=Button(GameScr,height=1,width=8,text="PicLasso",state=DISABLED).grid(row=2,column=1)
       
        global Char1S
        global Char2S
        global Char3S
        global Char4S
        Char2S=0
        
        if Char1S==0 or Char3S==0 or Char4S==0:
                        
            Clear(GameScr)
            
            global piclassoLabel
            global piclasso
            piclasso=PhotoImage(file="CharIMG\PicLassoF.png")
            piclassoLabel=Label(GameScr,height=300,width=176,bd=0,image=piclasso)
            piclassoLabel.grid(column=1,row=0)
            WMsgPL=PhotoImage(file='WLMsg\WMsgPL.png')
            Cnt=[44,59,59,44]
            global HHealth
            global OHealth
            HHealth=100
            OHealth=100
            global OHeMe
            OHeMe=Label(GameScr,height=1,width=21,text=str(OHealth)+':Health',font=('playbill',20),bg=A,fg='red',anchor=E)
            OHeMe.grid(row=1,column=1)
            global HeMe
            HeMe=Label(GameScr,height=1,width=21,text='Health:'+str(HHealth),font=("playbill",20),bg=A,fg='green',anchor=W)
            HeMe.grid(row=1,column=0)
            
            if Char1S==0:
                HeMe.configure(width=24)
                LMsgDJ=PhotoImage(file='WLMsg\LMsgDJ.png')
                GameScr.geometry("377x420")

                djdeath=PhotoImage(file="CharIMG\DJ DeathF.png")
                djdeathLabel=Label(GameScr,height=300,width=201,bd=0,image=djdeath)
                djdeathLabel.grid(column=0,row=0)

                DJ5='AttackAnimation\DJBrushAttack.gif'
                DJ6='AttackAnimation\DJPaintBomb.gif'
                DJ7='AttackAnimation\DJLassoDeath.gif'
                DJ8='AttackAnimation\DJSixShooter.gif'
                DJAttack=[DJ5,DJ6,DJ7,DJ8]
                
                def at1():
                    global piclassoLabel
                    global piclasso
                    attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    PL1=[PhotoImage(file='AttackAnimation\PLBoomBox.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            piclassoLabel.configure(image=piclasso)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                piclassoLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=176,bd=0,image=WMsgPL).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=DJAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                DJ=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            djdeathLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=201,bd=0,image=LMsgDJ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            djdeathLabel.configure(image=djdeath)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = DJ[ind]
                                        ind+=1
                                        djdeathLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = PL1[ind]
                            ind+=1
                            piclassoLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at2():
                    global piclassoLabel
                    global piclasso
                    attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    PL2=[PhotoImage(file='AttackAnimation\PLShockWaveGrenade.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            piclassoLabel.configure(image=piclasso)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                piclassoLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=176,bd=0,image=WMsgPL).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=DJAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                DJ=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            djdeathLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=201,bd=0,image=LMsgDJ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)                                            
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            djdeathLabel.configure(image=djdeath)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = DJ[ind]
                                        ind+=1
                                        djdeathLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = PL2[ind]
                            ind+=1
                            piclassoLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at3():
                    global piclassoLabel
                    global piclasso
                    attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    PL3=[PhotoImage(file='AttackAnimation\PLDeadlyBeat.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            piclassoLabel.configure(image=piclasso)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                djdeathLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=176,bd=0,image=WMsgPL).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=DJAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                DJ=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=201,bd=0,image=LMsgDJ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            djdeathLabel.configure(image=djdeath)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = DJ[ind]
                                        ind+=1
                                        djdeathLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = PL3[ind]
                            ind+=1
                            piclassoLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                def at4():
                    global piclassoLabel
                    global piclasso
                    attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                        
                    frameCnt=74
                    PL4=[PhotoImage(file='AttackAnimation\PLMusicalEntrapment.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        
                        if ind==frameCnt:
                            piclassoLabel.configure(image=piclasso)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                piclassoLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=176,bd=0,image=WMsgPL).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=DJAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                DJ=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            djdeathLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=201,bd=0,image=LMsgDJ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            djdeathLabel.configure(image=djdeath)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = DJ[ind]
                                        ind+=1
                                        djdeathLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                           
                            frame = PL4[ind]
                            ind+=1
                            piclassoLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()

                attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1).grid(column=0,row=2,pady=5)
                attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2).grid(column=1,row=2)
                attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3).grid(column=0,row=3,pady=5)
                attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4).grid(column=1,row=3,pady=5)
                GameScr.mainloop()
                
            elif Char3S==0:
                HeMe.configure(width=26)
                LMsgZ=PhotoImage(file='WLMsg\LMsgZ.png')
                GameScr.geometry("398x420")

                zolka=PhotoImage(file="CharIMG\ZolkaF.png")
                zolkaLabel=Label(GameScr,height=300,width=222,bd=0,image=zolka)
                zolkaLabel.grid(column=0,row=0)

                Z5='AttackAnimation\ZBrushAttack.gif'
                Z6='AttackAnimation\ZPaintBomb.gif'
                Z7='AttackAnimation\ZLassoDeath.gif'
                Z8='AttackAnimation\ZSixShooter.gif'
                ZAttack=[Z5,Z6,Z7,Z8]
                
                def at1():
                    global piclassoLabel
                    global piclasso
                    attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    PL9=[PhotoImage(file='AttackAnimation\PLVoicesFromTheVoid.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            piclassoLabel.configure(image=piclasso)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                piclassoLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=176,bd=0,image=WMsgPL).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=ZAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                Z=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            zolkaLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=222,bd=0,image=LMsgZ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            zolkaLabel.configure(image=zolka)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = Z[ind]
                                        ind+=1
                                        zolkaLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()
                        else:
                            frame = PL9[ind]
                            ind+=1
                            piclassoLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at2():
                    global piclassoLabel
                    global piclasso
                    attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=89
                    PL10=[PhotoImage(file='AttackAnimation\PLFireball.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            piclassoLabel.configure(image=piclasso)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                piclassoLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=176,bd=0,image=WMsgPL).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=ZAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                Z=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            zolkaLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=222,bd=0,image=LMsgZ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            zolkaLabel.configure(image=zolka)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = Z[ind]
                                        ind+=1
                                        zolkaLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = PL10[ind]
                            ind+=1
                            piclassoLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at3():
                    global piclassoLabel
                    global piclasso
                    attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    PL11=[PhotoImage(file='AttackAnimation\PLMindDestruction.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            piclassoLabel.configure(image=piclasso)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                piclassoLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=176,bd=0,image=WMsgPL).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=ZAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                Z=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            zolkaLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=222,bd=0,image=LMsgZ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            zolkaLabel.configure(image=zolka)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = Z[ind]
                                        ind+=1
                                        zolkaLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = PL11[ind]
                            ind+=1
                            piclassoLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                def at4():
                    global piclassoLabel
                    global piclasso
                    attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                        
                    frameCnt=59
                    PL12=[PhotoImage(file='AttackAnimation\PLShroudedStep.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        
                        if ind==frameCnt:
                            piclassoLabel.configure(image=piclasso)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                piclassoLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=176,bd=0,image=WMsgPL).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=ZAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                Z=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            zolkaLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=222,bd=0,image=LMsgZ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            zolkaLabel.configure(image=zolka)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = Z[ind]
                                        ind+=1
                                        zolkaLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                           
                            frame = PL12[ind]
                            ind+=1
                            piclassoLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()

                attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1).grid(column=0,row=2,pady=5)
                attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2).grid(column=1,row=2,pady=5)
                attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3).grid(column=0,row=3,pady=5)
                attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4).grid(column=1,row=3,pady=5)
                GameScr.mainloop()
                
            elif Char4S==0:
                HeMe.configure(width=37)
                LMsgBTV=PhotoImage(file='WLMsg\LMsgBTV.png')
                GameScr.geometry("500x420")

                barbtheviking=PhotoImage(file="CharIMG\BarbTheVikingF.png")
                barbthevikingLabel=Label(GameScr,height=300,width=324,bd=0,image=barbtheviking)
                barbthevikingLabel.grid(column=0,row=0)

                BTV5='AttackAnimation\BTVBrushAttack.gif'
                BTV6='AttackAnimation\BTVPaintBomb.gif'
                BTV7='AttackAnimation\BTVLassoDeath.gif'
                BTV8='AttackAnimation\BTVSixShooter.gif'
                BTVAttack=[BTV5,BTV6,BTV7,BTV8]
                def at1():
                    global piclassoLabel
                    global piclasso
                    attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    PL13=[PhotoImage(file='AttackAnimation\PLAxeOfDestruction.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            piclassoLabel.configure(image=piclasso)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                piclassoLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=176,bd=0,image=WMsgPL).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=BTVAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                BTV=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            barbthevikingLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=324,bd=0,image=LMsgBTV)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            barbthevikingLabel.configure(image=barbtheviking)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = BTV[ind]
                                        ind+=1
                                        barbthevikingLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()                            

                        else:
                            frame = PL13[ind]
                            ind+=1
                            piclassoLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at2():
                    global piclassoLabel
                    global piclasso
                    attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    PL14=[PhotoImage(file='AttackAnimation\PLColossalPunch.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            piclassoLabel.configure(image=piclasso)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                piclassoLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=176,bd=0,image=WMsgPL).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=BTVAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                BTV=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            barbthevikingLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=324,bd=0,image=LMsgBTV)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            barbthevikingLabel.configure(image=barbtheviking)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = BTV[ind]
                                        ind+=1
                                        barbthevikingLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = PL14[ind]
                            ind+=1
                            piclassoLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at3():
                    global piclassoLabel
                    global piclasso
                    attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    PL15=[PhotoImage(file='AttackAnimation\PLVikingRage.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            piclassoLabel.configure(image=piclasso)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                piclassoLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=176,bd=0,image=WMsgPL).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=BTVAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                BTV=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            barbthevikingLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=324,bd=0,image=LMsgBTV)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            barbthevikingLabel.configure(image=barbtheviking)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = BTV[ind]
                                        ind+=1
                                        barbthevikingLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = PL15[ind]
                            ind+=1
                            piclassoLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                def at4():
                    global piclassoLabel
                    global piclasso
                    attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                        
                    frameCnt=44
                    PL16=[PhotoImage(file='AttackAnimation\PLBrogueKick.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        
                        if ind==frameCnt:
                            piclassoLabel.configure(image=piclasso)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                piclassoLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=176,bd=0,image=WMsgPL).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=BTVAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                BTV=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            barbthevikingLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=324,bd=0,image=LMsgBTV)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            barbthevikingLabel.configure(image=barbtheviking)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = BTV[ind]
                                        ind+=1
                                        barbthevikingLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                           
                            frame = PL16[ind]
                            ind+=1
                            piclassoLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                attack1=Button(GameScr,text="Axe Of Destruction",height=1,width=18,bg='orange',fg='white',command=at1).grid(column=0,row=2,pady=5)
                attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2).grid(column=1,row=2,pady=5)
                attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3).grid(column=0,row=3,pady=5)
                attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4).grid(column=1,row=3,pady=5)
                GameScr.mainloop()
                
        else:
            PlMg=Label(GameScr,height=1,width=26,bg="Black",text="Choose your opponent!",font=("playbill",67),fg='#ff0000').grid(row=0,column=0,columnspan=4)
            
    def Ch3():
        Char3B=Button(GameScr,height=1,width=8,text="Zolka",state=DISABLED).grid(row=2,column=2)
        
        global Char1S
        global Char2S
        global Char3S
        global Char4S
        Char3S=0
        
        if Char1S==0 or Char2S==0 or Char4S==0:
                        
            Clear(GameScr)
            global zolkaLabel
            global zolka
            zolka=PhotoImage(file="CharIMG\ZolkaF.png")
            zolkaLabel=Label(GameScr,height=300,width=222,bd=0,image=zolka)
            zolkaLabel.grid(column=1,row=0)
            Cnt=[44,89,44,59]
            WMsgZ=PhotoImage(file='WLMsg\WMsgZ.png')
            global HHealth
            global OHealth
            HHealth=100
            OHealth=100
            global OHeMe
            OHeMe=Label(GameScr,height=1,width=26,text=str(OHealth)+':Health',font=('playbill',20),bg=A,fg='red',anchor=E)
            OHeMe.grid(row=1,column=1)
            global HeMe
            HeMe=Label(GameScr,height=1,width=21,text='Health:'+str(HHealth),font=("playbill",20),bg=A,fg='green',anchor=W)
            HeMe.grid(row=1,column=0)
            
            if Char1S==0:
                HeMe.configure(width=24)
                LMsgDJ=PhotoImage(file='WLMsg\LMsgDJ.png')
                GameScr.geometry("423x420")

                djdeath=PhotoImage(file="CharIMG\DJ DeathF.png")
                djdeathLabel=Label(GameScr,height=300,width=201,bd=0,image=djdeath)
                djdeathLabel.grid(column=0,row=0)
                
                DJ9='AttackAnimation\DJVoicesFromTheVoid.gif'
                DJ10='AttackAnimation\DJFireball.gif'
                DJ11='AttackAnimation\DJMindDestruction.gif'
                DJ12='AttackAnimation\DJShroudedStep.gif'
                DJAttack=[DJ9,DJ10,DJ11,DJ12]
                
                def at1():
                    global zolkaLabel
                    global zolka
                    attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    Z1=[PhotoImage(file='AttackAnimation\ZBoomBox.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            zolkaLabel.configure(image=zolka)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                zolkaLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=222,bd=0,image=WMsgZ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=DJAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                DJ=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            djdeathLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=201,bd=0,image=LMsgDJ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            djdeathLabel.configure(image=djdeath)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = DJ[ind]
                                        ind+=1
                                        djdeathLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()
                        else:
                            frame = Z1[ind]
                            ind+=1
                            zolkaLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at2():
                    global zolkaLabel
                    global zolka
                    attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    Z2=[PhotoImage(file='AttackAnimation\ZShockWaveGrenade.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            zolkaLabel.configure(image=zolka)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                zolkaLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=222,bd=0,image=WMsgZ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=DJAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                DJ=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            djdeathLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=201,bd=0,image=LMsgDJ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            djdeathLabel.configure(image=djdeath)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = DJ[ind]
                                        ind+=1
                                        djdeathLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()
                        else:
                            frame = Z2[ind]
                            ind+=1
                            zolkaLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at3():
                    global zolkaLabel
                    global zolka
                    attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    Z3=[PhotoImage(file='AttackAnimation\ZDeadlyBeat.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            zolkaLabel.configure(image=zolka)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                zolkaLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=222,bd=0,image=WMsgZ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=DJAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                DJ=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            djdeathLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=201,bd=0,image=LMsgDJ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            djdeathLabel.configure(image=djdeath)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = DJ[ind]
                                        ind+=1
                                        djdeathLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = Z3[ind]
                            ind+=1
                            zolkaLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                def at4():
                    global zolkaLabel
                    global zolka
                    attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                        
                    frameCnt=74
                    Z4=[PhotoImage(file='AttackAnimation\ZMusicalEntrapment.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        
                        if ind==frameCnt:
                            zolkaLabel.configure(image=zolka)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                zolkaLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=222,bd=0,image=WMsgZ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=DJAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                DJ=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            djdeathLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=201,bd=0,image=LMsgDJ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            djdeathLabel.configure(image=djdeath)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = DJ[ind]
                                        ind+=1
                                        djdeathLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                           
                            frame = Z4[ind]
                            ind+=1
                            zolkaLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1).grid(column=0,row=2,pady=5)
                attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2).grid(column=1,row=2,pady=5)
                attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3).grid(column=0,row=3,pady=5)
                attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4).grid(column=1,row=3,pady=5)
                GameScr.mainloop()
                
            elif Char2S==0:
                HeMe.configure(width=21)
                LMsgPL=PhotoImage(file='WLMsg\LMsgPL.png')
                GameScr.geometry("398x420")

                piclasso=PhotoImage(file="CharIMG\PicLassoF.png")
                piclassoLabel=Label(GameScr,height=300,width=176,bd=0,image=piclasso)
                piclassoLabel.grid(column=0,row=0)

                PL9='AttackAnimation\PLVoicesFromTheVoid.gif'
                PL10='AttackAnimation\PLFireball.gif'
                PL11='AttackAnimation\PLMindDestruction.gif'
                PL12='AttackAnimation\PLShroudedStep.gif'
                PLAttack=[PL9,PL10,PL11,PL12]
                
                def at1():
                    global zolkaLabel
                    global zolka
                    attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    Z5=[PhotoImage(file='AttackAnimation\ZBrushAttack.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            zolkaLabel.configure(image=zolka)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth) +':Health')
                                zolkaLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=222,bd=0,image=WMsgZ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=PLAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                PL=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)
                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:' + str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=176,bd=0,image=LMsgPL)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.configure(image=piclasso)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = PL[ind]
                                        ind+=1
                                        piclassoLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = Z5[ind]
                            ind+=1
                            zolkaLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at2():
                    global zolkaLabel
                    global zolka
                    attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=59
                    Z6=[PhotoImage(file='AttackAnimation\ZPaintBomb.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            zolkaLabel.configure(image=zolka)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth) +':Health')
                                zolkaLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=222,bd=0,image=WMsgZ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=PLAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                PL=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)
                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:' + str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=176,bd=0,image=LMsgPL)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.configure(image=piclasso)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = PL[ind]
                                        ind+=1
                                        piclassoLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = Z6[ind]
                            ind+=1
                            zolkaLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at3():
                    global zolkaLabel
                    global zolka
                    attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=59
                    Z7=[PhotoImage(file='AttackAnimation\ZLassoDeath.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            zolkaLabel.configure(image=zolka)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth) +':Health')
                                zolkaLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=222,bd=0,image=WMsgZ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=PLAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                PL=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)
                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:' + str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=176,bd=0,image=LMsgPL)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.configure(image=piclasso)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = PL[ind]
                                        ind+=1
                                        piclassoLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = Z7[ind]
                            ind+=1
                            zolkaLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                def at4():
                    global zolkaLabel
                    global zolka
                    attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                        
                    frameCnt=44
                    Z8=[PhotoImage(file='AttackAnimation\ZSixShooter.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        
                        if ind==frameCnt:
                            zolkaLabel.configure(image=zolka)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth) +':Health')
                                zolkaLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=222,bd=0,image=WMsgZ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=PLAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                PL=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)
                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:' + str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=176,bd=0,image=LMsgPL)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.configure(image=piclasso)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = PL[ind]
                                        ind+=1
                                        piclassoLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                           
                            frame = Z8[ind]
                            ind+=1
                            zolkaLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1).grid(column=0,row=2,pady=5)
                attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2).grid(column=1,row=2,pady=5)
                attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3).grid(column=0,row=3,pady=5)
                attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4).grid(column=1,row=3,pady=5)
                GameScr.mainloop()
                
            elif Char4S==0:
                HeMe.configure(width=37)
                LMsgBTV=PhotoImage(file='WLMsg\LMsgBTV.png')
                GameScr.geometry("546x420")

                barbtheviking=PhotoImage(file="CharIMG\BarbTheVikingF.png")
                barbthevikingLabel=Label(GameScr,height=300,width=324,bd=0,image=barbtheviking)
                barbthevikingLabel.grid(column=0,row=0)

                BTV9='AttackAnimation\BTVVoicesFromTheVoid.gif'
                BTV10='AttackAnimation\BTVFireball.gif'
                BTV11='AttackAnimation\BTVMindDestruction.gif'
                BTV12='AttackAnimation\BTVShroudedStep.gif'
                BTVAttack=[BTV9,BTV10,BTV11,BTV12]
                
                def at1():
                    global zolkaLabel
                    global zolka
                    attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    Z13=[PhotoImage(file='AttackAnimation\ZAxeOfDestruction.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            zolkaLabel.configure(image=zolka)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                zolkaLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=222,bd=0,image=WMsgZ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=BTVAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                BTV=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            barbthevikingLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=324,bd=0,image=LMsgBTV)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            barbthevikingLabel.configure(image=barbtheviking)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = BTV[ind]
                                        ind+=1
                                        barbthevikingLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = Z13[ind]
                            ind+=1
                            zolkaLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at2():
                    global zolkaLabel
                    global zolka
                    attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    Z14=[PhotoImage(file='AttackAnimation\ZColossalPunch.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            zolkaLabel.configure(image=zolka)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                zolkaLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=222,bd=0,image=WMsgZ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=BTVAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                BTV=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            barbthevikingLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=324,bd=0,image=LMsgBTV)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            barbthevikingLabel.configure(image=barbtheviking)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = BTV[ind]
                                        ind+=1
                                        barbthevikingLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = Z14[ind]
                            ind+=1
                            zolkaLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at3():
                    global zolkaLabel
                    global zolka
                    attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    Z15=[PhotoImage(file='AttackAnimation\ZVikingRage.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            zolkaLabel.configure(image=zolka)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                zolkaLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=222,bd=0,image=WMsgZ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=BTVAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                BTV=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            barbthevikingLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=324,bd=0,image=LMsgBTV)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            barbthevikingLabel.configure(image=barbtheviking)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = BTV[ind]
                                        ind+=1
                                        barbthevikingLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = Z15[ind]
                            ind+=1
                            zolkaLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                def at4():
                    global zolkaLabel
                    global zolka
                    attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                        
                    frameCnt=44
                    Z16=[PhotoImage(file='AttackAnimation\ZBrogueKick.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        
                        if ind==frameCnt:
                            zolkaLabel.configure(image=zolka)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                zolkaLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=222,bd=0,image=WMsgZ).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=BTVAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                BTV=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            barbthevikingLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=324,bd=0,image=LMsgBTV)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            barbthevikingLabel.configure(image=barbtheviking)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Axe of Destruction",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = BTV[ind]
                                        ind+=1
                                        barbthevikingLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                           
                            frame = Z16[ind]
                            ind+=1
                            zolkaLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                attack1=Button(GameScr,text="Axe Of Destruction",height=1,width=18,bg='orange',fg='white',command=at1).grid(column=0,row=2,pady=5)
                attack2=Button(GameScr,text="Colossal Punch",height=1,width=18,bg='orange',fg='white',command=at2).grid(column=1,row=2,pady=5)
                attack3=Button(GameScr,text="Viking Rage",height=1,width=18,bg='orange',fg='white',command=at3).grid(column=0,row=3,pady=5)
                attack4=Button(GameScr,text="Brogue Kick",height=1,width=18,bg='orange',fg='white',command=at4).grid(column=1,row=3,pady=5)
                GameScr.mainloop()
                
        else:
            PlMg=Label(GameScr,height=1,width=26,bg="Black",text="Choose your opponent!",font=("playbill",67),fg='#ff0000').grid(row=0,column=0,columnspan=4)
        
    def Ch4():
        Char4B=Button(GameScr,height=1,width=12,text="BarbTheViking",state=DISABLED).grid(row=2,column=3)
        global Char1S
        global Char2S
        global Char3S
        global Char4S
        Char4S=0

       
        if Char1S==0 or Char2S==0 or Char3S==0:

            Clear(GameScr)
            global barbthevikingLabel
            global barbtheviking
            barbtheviking=PhotoImage(file="CharIMG\BarbTheVikingF.png")
            barbthevikingLabel=Label(GameScr,height=300,width=324,bd=0,image=barbtheviking)
            barbthevikingLabel.grid(column=1,row=0)
            WMsgBTV=PhotoImage(file='WLMsg\WMsgBTV.png')
            Cnt=[44,44,44,44]
            global HHealth
            global OHealth
            HHealth=100
            OHealth=100
            global OHeMe
            OHeMe=Label(GameScr,height=1,width=37,text=str(OHealth)+':Health',font=('playbill',20),bg=A,fg='red',anchor=E)
            OHeMe.grid(row=1,column=1)
            global HeMe
            HeMe=Label(GameScr,height=1,width=21,text='Health:'+str(HHealth),font=("playbill",20),bg=A,fg='green',anchor=W)
            HeMe.grid(row=1,column=0)
            
            if Char1S==0:
                HeMe.configure(width=24)
                LMsgDJ=PhotoImage(file='WLMsg\LMsgDJ.png')
                GameScr.geometry("525x420")

                djdeath=PhotoImage(file="CharIMG\DJ DeathF.png")
                djdeathLabel= Label(GameScr,height=300,width=201,bd=0,image=djdeath)
                djdeathLabel.grid(column=0,row=0)

                DJ13='AttackAnimation\DJAxeOfDestruction.gif'
                DJ14='AttackAnimation\DJColossalPunch.gif'
                DJ15='AttackAnimation\DJVikingRage.gif'
                DJ16='AttackAnimation\DJBrogueKick.gif'
                DJAttack=[DJ13,DJ14,DJ15,DJ16]
                
                def at1():
                    global barbthevikingLabel
                    global barbtheviking
                    attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    BTV1=[PhotoImage(file='AttackAnimation\BTVBoomBox.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            barbthevikingLabel.configure(image=barbtheviking)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                barbthevikingLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=324,bd=0,image=WMsgBTV).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=DJAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                DJ=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            djdeathLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=201,bd=0,image=LMsgDJ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            djdeathLabel.configure(image=djdeath)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = DJ[ind]
                                        ind+=1
                                        djdeathLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = BTV1[ind]
                            ind+=1
                            barbthevikingLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at2():
                    global barbthevikingLabel
                    global barbtheviking
                    attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    BTV2=[PhotoImage(file='AttackAnimation\BTVShockwaveGrenade.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            barbthevikingLabel.configure(image=barbtheviking)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                barbthevikingLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=324,bd=0,image=WMsgBTV).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=DJAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                DJ=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            djdeathLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=201,bd=0,image=LMsgDJ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            djdeathLabel.configure(image=djdeath)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = DJ[ind]
                                        ind+=1
                                        djdeathLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = BTV2[ind]
                            ind+=1
                            barbthevikingLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at3():
                    global barbthevikingLabel
                    global barbtheviking
                    attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    BTV3=[PhotoImage(file='AttackAnimation\BTVDeadlyBeat.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            barbthevikingLabel.configure(image=barbtheviking)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                barbthevikingLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=324,bd=0,image=WMsgBTV).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=DJAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                DJ=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            djdeathLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=201,bd=0,image=LMsgDJ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            djdeathLabel.configure(image=djdeath)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = DJ[ind]
                                        ind+=1
                                        djdeathLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = BTV3[ind]
                            ind+=1
                            barbthevikingLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                def at4():
                    global barbthevikingLabel
                    global barbtheviking
                    attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                        
                    frameCnt=74
                    BTV4=[PhotoImage(file='AttackAnimation\BTVMusicalEntrapment.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        
                        if ind==frameCnt:
                            barbthevikingLabel.configure(image=barbtheviking)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                barbthevikingLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=324,bd=0,image=WMsgBTV).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=DJAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                DJ=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            djdeathLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=201,bd=0,image=LMsgDJ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            djdeathLabel.configure(image=djdeath)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = DJ[ind]
                                        ind+=1
                                        djdeathLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                           
                            frame = BTV4[ind]
                            ind+=1
                            barbthevikingLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                attack1=Button(GameScr,text="Boom Box",height=1,width=18,bg='orange',fg='white',command=at1).grid(column=0,row=2,pady=5)
                attack2=Button(GameScr,text="Shockwave Grenade",height=1,width=18,bg='orange',fg='white',command=at2).grid(column=1,row=2,pady=5)
                attack3=Button(GameScr,text="Deadly Beat",height=1,width=18,bg='orange',fg='white',command=at3).grid(column=0,row=3,pady=5)
                attack4=Button(GameScr,text="Musical Entrapment",height=1,width=18,bg='orange',fg='white',command=at4).grid(column=1,row=3,pady=5)
                GameScr.mainloop()
                
            elif Char2S==0:
                HeMe.configure(width=21)
                LMsgPL=PhotoImage(file='WLMsg\LMsgPL.png')
                GameScr.geometry("500x420")

                piclasso=PhotoImage(file="CharIMG\PicLassoF.png")
                piclassoLabel=Label(GameScr,height=300,width=176,bd=0,image=piclasso)
                piclassoLabel.grid(column=0,row=0)

                PL13='AttackAnimation\PLAxeOfDestruction.gif'
                PL14='AttackAnimation\PLColossalPunch.gif'
                PL15='AttackAnimation\PLVikingRage.gif'
                PL16='AttackAnimation\PLBrogueKick.gif'
                PLAttack=[PL13,PL14,PL15,PL16]
                
                def at1():
                    global barbthevikingLabel
                    global barbtheviking
                    attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Lasso of Death",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    BTV5=[PhotoImage(file='AttackAnimation\BTVBrushAttack.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            barbthevikingLabel.configure(image=barbtheviking)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth) +':Health')
                                barbthevikingLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=324,bd=0,image=WMsgBTV).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=PLAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                PL=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)
                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:' + str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=176,bd=0,image=LMsgPL)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.configure(image=piclasso)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = PL[ind]
                                        ind+=1
                                        piclassoLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = BTV5[ind]
                            ind+=1
                            barbthevikingLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at2():
                    global barbthevikingLabel
                    global barbtheviking
                    attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Lasso of Death",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=59
                    BTV6=[PhotoImage(file='AttackAnimation\BTVPaintBomb.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            barbthevikingLabel.configure(image=barbtheviking)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth) +':Health')
                                barbthevikingLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=324,bd=0,image=WMsgBTV).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=PLAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                PL=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)
                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:' + str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=176,bd=0,image=LMsgPL)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.configure(image=piclasso)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = PL[ind]
                                        ind+=1
                                        piclassoLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = BTV6[ind]
                            ind+=1
                            barbthevikingLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at3():
                    global barbthevikingLabel
                    global barbtheviking
                    attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Lasso of Death",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=59
                    BTV7=[PhotoImage(file='AttackAnimation\BTVLassoDeath.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            barbthevikingLabel.configure(image=barbtheviking)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth) +':Health')
                                barbthevikingLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=324,bd=0,image=WMsgBTV).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=PLAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                PL=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)
                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:' + str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=176,bd=0,image=LMsgPL)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.configure(image=piclasso)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = PL[ind]
                                        ind+=1
                                        piclassoLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = BTV7[ind]
                            ind+=1
                            barbthevikingLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                def at4():
                    global barbthevikingLabel
                    global barbtheviking
                    attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Lasso of Death",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                        
                    frameCnt=44
                    BTV8=[PhotoImage(file='AttackAnimation\BTVSixShooter.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        
                        if ind==frameCnt:
                            barbthevikingLabel.configure(image=barbtheviking)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth) +':Health')
                                barbthevikingLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=324,bd=0,image=WMsgBTV).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=PLAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                PL=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)
                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:' + str(HHealth))
                                            piclassoLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=176,bd=0,image=LMsgPL)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            piclassoLabel.configure(image=piclasso)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = PL[ind]
                                        ind+=1
                                        piclassoLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                           
                            frame = BTV8[ind]
                            ind+=1
                            barbthevikingLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                attack1=Button(GameScr,text="Brush Attack",height=1,width=18,bg='orange',fg='white',command=at1).grid(column=0,row=2,pady=5)
                attack2=Button(GameScr,text="Paint Bomb",height=1,width=18,bg='orange',fg='white',command=at2).grid(column=1,row=2,pady=5)
                attack3=Button(GameScr,text="Lasso Of Death",height=1,width=18,bg='orange',fg='white',command=at3).grid(column=0,row=3,pady=5)
                attack4=Button(GameScr,text="Six Shooter",height=1,width=18,bg='orange',fg='white',command=at4).grid(column=1,row=3,pady=5)
                GameScr.mainloop()
                
            elif Char3S==0:
                HeMe.configure(width=26)
                LMsgZ=PhotoImage(file='WLMsg\LMsgZ.png')
                GameScr.geometry("546x420")

                zolka=PhotoImage(file="CharIMG\ZolkaF.png")
                zolkaLabel=Label(GameScr,height=300,width=222,bd=0,image=zolka)
                zolkaLabel.grid(column=0,row=0)
                
                Z13='AttackAnimation\ZAxeOfDestruction.gif'
                Z14='AttackAnimation\ZColossalPunch.gif'
                Z15='AttackAnimation\ZVikingRage.gif'
                Z16='AttackAnimation\ZBrogueKick.gif'
                ZAttack=[Z13,Z14,Z15,Z16]
                
                def at1():
                    global barbthevikingLabel
                    global barbtheviking
                    attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    BTV9=[PhotoImage(file='AttackAnimation\BTVVoicesFromTheVoid.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            barbthevikingLabel.configure(image=barbtheviking)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                barbthevikingLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=324,bd=0,image=WMsgBTV).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=ZAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                Z=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            zolkaLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=222,bd=0,image=LMsgZ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            zolkaLabel.configure(image=zolka)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = Z[ind]
                                        ind+=1
                                        zolkaLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = BTV9[ind]
                            ind+=1
                            barbthevikingLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at2():
                    global barbthevikingLabel
                    global barbtheviking
                    attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=89
                    BTV10=[PhotoImage(file='AttackAnimation\BTVFireball.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            barbthevikingLabel.configure(image=barbtheviking)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                barbthevikingLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=324,bd=0,image=WMsgBTV).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=ZAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                Z=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            zolkaLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=222,bd=0,image=LMsgZ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            zolkaLabel.configure(image=zolka)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = Z[ind]
                                        ind+=1
                                        zolkaLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = BTV10[ind]
                            ind+=1
                            barbthevikingLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                def at3():
                    global barbthevikingLabel
                    global barbtheviking
                    attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                    frameCnt=44
                    BTV11=[PhotoImage(file='AttackAnimation\BTVMindDestruction.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        if ind==frameCnt:
                            barbthevikingLabel.configure(image=barbtheviking)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                barbthevikingLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=324,bd=0,image=WMsgBTV).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=ZAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                Z=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            zolkaLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=222,bd=0,image=LMsgZ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            zolkaLabel.configure(image=zolka)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = Z[ind]
                                        ind+=1
                                        zolkaLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                            frame = BTV11[ind]
                            ind+=1
                            barbthevikingLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                def at4():
                    global barbthevikingLabel
                    global barbtheviking
                    attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=2,pady=5)
                    attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=2,pady=5)
                    attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=0,row=3,pady=5)
                    attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',state=DISABLED).grid(column=1,row=3,pady=5)
                        
                    frameCnt=59
                    BTV12=[PhotoImage(file='AttackAnimation\BTVShroudedStep.gif',format ='gif -index %i' %(i)) for i in range(frameCnt)]
                    def update(ind):
                        
                        if ind==frameCnt:
                            barbthevikingLabel.configure(image=barbtheviking)
                            global OHeMe
                            global OHealth
                            DamageO=randint(10,30)
                            OHealth-=DamageO
                            if OHealth<=0:
                                global GameCnt
                                global GameWonCnt
                                GameCnt+=1
                                GameWonCnt+=1
                                OHealth=0
                                OHeMe.configure(text=str(OHealth)+ ':Health')
                                barbthevikingLabel.destroy()
                                WinLabel=Label(GameScr,height=300,width=324,bd=0,image=WMsgBTV).grid(column=1,row=0)
                                Event().wait(0.5)
                                Clear2(GameScr)
                                PlayAgain=Button(GameScr,height=1,width=12,text="Play Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                            else:
                                OHeMe.configure(text=str(OHealth)+':Health')
                                OAtN=randint(0,3)
                                Damage=randint(15,30)
                                At=ZAttack[OAtN]
                                frameCnt2=Cnt[OAtN]
                                Z=[PhotoImage(file=At,format ='gif -index %i' %(i)) for i in range(frameCnt2)]
                                Event().wait(0.5)

                                def update2(ind):
                                    if ind==frameCnt2:
                                        global HHealth
                                        global HeMe
                                        HHealth-=Damage
                                        if HHealth<=0:
                                            global GameCnt
                                            global GameWonCnt
                                            GameCnt+=1
                                            HHealth=0
                                            HeMe.configure(text='Health:'+ str(HHealth))
                                            zolkaLabel.destroy()
                                            LoseLabel=Label(GameScr,height=300,width=222,bd=0,image=LMsgZ)
                                            LoseLabel.grid(column=0,row=0)
                                            Event().wait(0.5)
                                            Clear2(GameScr)
                                            PlayAgain=Button(GameScr,height=1,width=12,text="Try Again!",fg='white',bg=A,command=OpGa).grid(row=2,column=0)
                                            ExitGame=Button(GameScr,height=1,width=12,text="Exit Game",fg='white',bg=A,command=ExGa).grid(row=2,column=1)
                                            GameCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Played: " + str(GameCnt)).grid(row=3,column=0,pady=5)
                                            GameWonCntLabel=Label(GameScr,height=2,width=15,bg=A,fg='white',font=('gabriola',15),text="Games Won: " + str(GameWonCnt)).grid(row=3,column=1,pady=5)
                                        else:
                                            HeMe.configure(text='Health:'+str(HHealth))
                                            zolkaLabel.configure(image=zolka)
                                            Event().wait(0.5)
                                            attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1,state=NORMAL).grid(column=0,row=2,pady=5)
                                            attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2,state=NORMAL).grid(column=1,row=2,pady=5)
                                            attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3,state=NORMAL).grid(column=0,row=3,pady=5)
                                            attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4,state=NORMAL).grid(column=1,row=3,pady=5)
                                    else:
                                        frame = Z[ind]
                                        ind+=1
                                        zolkaLabel.configure(image=frame)
                                        GameScr.after(40,update2,ind)                              
                                GameScr.after(0,update2,0)
                                GameScr.mainloop()

                        else:
                           
                            frame = BTV12[ind]
                            ind+=1
                            barbthevikingLabel.configure(image=frame)
                            GameScr.after(40,update,ind)
                    GameScr.after(0,update,0)
                    GameScr.mainloop()
                
                attack1=Button(GameScr,text="Voices From The Void",height=1,width=18,bg='orange',fg='white',command=at1).grid(column=0,row=2,pady=5)
                attack2=Button(GameScr,text="Fireball",height=1,width=18,bg='orange',fg='white',command=at2).grid(column=1,row=2,pady=5)
                attack3=Button(GameScr,text="Mind Destruction",height=1,width=18,bg='orange',fg='white',command=at3).grid(column=0,row=3,pady=5)
                attack4=Button(GameScr,text="Shrouded Step",height=1,width=18,bg='orange',fg='white',command=at4).grid(column=1,row=3,pady=5)
                GameScr.mainloop()
                
        else:
            PlMg=Label(GameScr,height=1,width=26,bg="Black",text="Choose your opponent!",font=("playbill",67),fg='#ff0000').grid(row=0,column=0,columnspan=4)
        
    Char1B=Button(GameScr,height=1,width=8,text="DJ Death",command=Ch1).grid(row=2,column=0,)
    Char2B=Button(GameScr,height=1,width=8,text="PicLasso",command=Ch2).grid(row=2,column=1)
    Char3B=Button(GameScr,height=1,width=8,text="Zolka",command=Ch3).grid(row=2,column=2)
    Char4B=Button(GameScr,height=1,width=12,text="BarbTheViking",command=Ch4).grid(row=2,column=3)

    GameScr.mainloop()

    

#StartScreenWidgets 
StGam=Button(Battle,height=1,width=15,text="Start Game",command=OpGa,bg="orange",fg="white").grid(row=0,column=1,padx=5)
OptGam=Button(Battle,height=1,width=15,text="Options",command=OptGa,bg="blue",fg="white").grid(row=1,column=1,padx=5)
ExGam=Button(Battle,height=1,width=15,text="Exit Game",command=ExGa,bg="gray",fg="white").grid(row=2,column=1,padx=5)


Battle.mainloop()
