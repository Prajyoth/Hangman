import time
import curses
import threading
import queue

def pbar(window):
    start = 0
    chances = 0
    a = []
    window.clear()
    window.addstr("Welcome to Hangman.\n Press any key to begin.\n Press q to exit")
    while start==0:
        g = window.getch(0,0)
        if g:
            start = 1
    mail = queue.Queue()
    d = threading.Thread(target = timer, args = (window,mail,))
    d.setDaemon(True)
    d.start()
    window.addstr(13,10,"HANGMAN")
    window.refresh()
    window.addstr(15,10,"_ _ _ _ _ _ / _ _ _ _ _ _")
    while True:
        try:
            data = mail.get(False)
        except queue.Empty:
            data = None
        if data == "done":
            window.addstr(17,10, "YOU LOOSE! Press q to exit")
            window.refresh()
            while True:
                g = window.getch(17,10)
                if g == ord("q"): break
        c = window.getch(20,10)
        if c == ord("q"): break
        window.addstr(21,10,"You pressed " +chr(c))
        if c == ord("b"):
            a.append(chr(c))
            window.addstr(15,10,"b")
            window.addstr(15,24,"b")
        elif c == ord("a"):
            a.append(chr(c))
            window.addstr(15,12,"a")
            window.addstr(15,18,"a")
        elif c == ord("t"):
            a.append(chr(c))
            window.addstr(15,14,"t")
        elif c == ord("m"):
            a.append(chr(c))
            window.addstr(15,16,"m")
        elif c == ord("n"):
            a.append(chr(c))
            window.addstr(15,20,"n")
            window.addstr(15,32,"n")
        elif c == ord("e"):
            a.append(chr(c))
            window.addstr(15,26,"e")
        elif c == ord("g"):
            a.append(chr(c))
            window.addstr(15,28,"g")
        elif c == ord("i"):
            a.append(chr(c))
            window.addstr(15,30,"i")
        elif c == ord("s"):
            a.append(chr(c))
            window.addstr(15,34,"s")
        else :
            underline(chances,window)
            chances = chances + 1
        if chances == 7:
            window.addstr(17,10, "YOU LOOSE!")
        if len(a) == 9 :
            window.addstr(17,10,"YOU WIN!!")
        window.refresh()

def underline(chance,window):
    if chance==0:
        window.addstr(13,10,"H",curses.A_STANDOUT)
    if chance==1:
        window.addstr(13,11,"A",curses.A_STANDOUT)
    if chance==2:
        window.addstr(13,12,"N",curses.A_STANDOUT)
    if chance==3:
        window.addstr(13,13,"G",curses.A_STANDOUT)
    if chance==4:
        window.addstr(13,14,"M",curses.A_STANDOUT)
    if chance==5:
        window.addstr(13,15,"A",curses.A_STANDOUT)
    if chance==6:
        window.addstr(13,16,"N",curses.A_STANDOUT)

def timer(window,mail):
        t = 10
        curses.noecho()
        curses.curs_set(0)
        while t!=-1:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            window.addstr(12,10,timeformat)
            window.refresh()
            time.sleep(1)
            t -= 1
        window.addstr(17,10, "YOU LOOSE! Press q to exit")
        window.refresh()
        mail.put("done")

curses.wrapper(pbar)
