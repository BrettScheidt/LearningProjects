import tkinter as tk
import random

global playerTotal
global dealerTotal
global Win
global Loss
win = 0
loss = 0
playerTotal = 0
dealerTotal = 0


Bui = tk.Tk()
Bui.title("BlackJack")
Bui.geometry("400x300")

def hit_click():
    print("Hit button clicked")
    #listbox.insert(tk.END, "Hit button clicked") #end is at the bottom
    deal("Player")

def stand_click():
    print("Stand button clicked")
    #listbox.insert(0, "Stand button clicked") Zero is top
    checkWin()

hit = tk.Button(Bui, text="Hit", command= hit_click, width= 7, height=2) #, padx=17, pady=10
hit.place(x=300, y=50)
stand = tk.Button(Bui, text="Stand", command = stand_click, width= 7, height=2)
stand.place(x=300, y=100)
listbox = tk.Listbox(Bui, width=40, height=5)
listbox.place(x=10, y=50)
listboxD = tk.Listbox(Bui, width=40, height=5)
listboxD.place(x=10, y=180)
winloss = tk.Label(Bui, text="Wins: 0 Losses: 0")
winloss.place(x=285, y=10)
DTotal = tk.Label(Bui, text="Dealer Total: 0")
DTotal.place(x=285, y=180)
PTotal = tk.Label(Bui, text="Player Total: 0")
PTotal.place(x=285, y=150)
PList = tk.Label(Bui, text="Player Cards:")
PList.place(x=10, y=10)
Dlist = tk.Label(Bui, text="Dealer Cards:")
Dlist.place(x=10, y=150)
Gamelog = tk.Listbox(Bui, width=16, height=3)
Gamelog.place(x=280, y=230)
LogTitle = tk.Label(Bui, text="Game Log:")
LogTitle.place(x=285, y=210)


def deal(User):
    global playerTotal
    global dealerTotal
    card = random.randint(1, 13)

    if (User == "Player" and playerTotal < 21):
        if card > 10:
            card = 10
        elif card == 1:
            if playerTotal + 11 > 21:
                card = 1
            else:
                card = 11
        playerTotal += card
        listbox.insert(0, card)
        print("Player was dealt a " + str(card) + ". Player total is now " + str(playerTotal))
        PTotal.config(text ="Player Total: " + str(playerTotal))
        if 21 <= playerTotal :
            checkWin()
    elif (User == "Player" and 21 <= playerTotal):
         checkWin() 
    elif User == "Dealer":
        if card > 10:
            card = 10
        elif card == 1:
            if dealerTotal + 11 > 21:
                card = 1
            else:
                card = 11
        dealerTotal += card
        listboxD.insert(0, card)
        DTotal.config(text ="Dealer Total: " + str(dealerTotal))
        print("Dealer was dealt a ",card,". Dealer total is now ",dealerTotal) # have to use commas when not using just strings

def checkWin():
    global playerTotal
    global dealerTotal
    global win
    global loss
    while dealerTotal < 17 and playerTotal <= 21:
        deal("Dealer")
    if playerTotal <= 21:
        deal("Dealer")
        if dealerTotal > 21 or playerTotal > dealerTotal:
            print("Player wins!")
            win += 1
            Gamelog.insert(0, str(playerTotal) + " to " + str(dealerTotal) + "Player Wins")
        elif dealerTotal > playerTotal:
            print("Dealer wins!")
            loss += 1
            Gamelog.insert(0, str(playerTotal) + " to " + str(dealerTotal) + "Dealer Wins")
        elif dealerTotal == playerTotal:
            print("Dealer Wins on a tie!")
            loss += 1
            Gamelog.insert(0, str(playerTotal) + " to " + str(dealerTotal) + "Dealer Wins")
    elif playerTotal > 21:
        print("Player busts! Dealer wins!")
        loss += 1
        Gamelog.insert(0, str(playerTotal) + " to " + str(dealerTotal) + "Dealer Wins")
    winloss.config(text="Wins: " + str(win) + " Losses: " + str(loss))
    reset()

def DealerDraw():
    global dealerTotal
    while (dealerTotal < 17):
        deal("Dealer")

def reset():
    global playerTotal
    global dealerTotal
    playerTotal = 0
    dealerTotal = 0
    PTotal.config(text ="Player Total: " + str(playerTotal))
    DTotal.config(text ="Dealer Total: " + str(dealerTotal))
    listbox.delete(0, tk.END)
    listboxD.delete(0, tk.END)
    run()


def run():
    deal("Player")
    deal("Player")
    deal("Dealer")
         
run()
Bui.mainloop()