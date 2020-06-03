from tkinter import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#chrome version error fixing : https://stackoverflow.com/questions/60296873/sessionnotcreatedexception-message-session-not-created-this-version-of-chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
win=Tk()
win.title("Transaction Search Monitor")
win.geometry="720x720"

def show_page():
	arg=entry.get()
	argtwo=entrytwo.get()
		
	if arg=="bitcoin":
		url='https://www.blockchain.com/btc/address/'+argtwo
		driver.get(url)
		base_window=driver.window_handles[0]
	elif arg=="bitcoincash":
		url='https://www.blockchain.com/bch/address/'+argtwo
		driver.get(url)
		base_window=driver.window_handles[0]
	elif arg=="etherium":
		url='https://www.blockchain.com/eth/address/'+argtwo
		driver.get(url)
		base_window=driver.window_handles[0]
	else:
		print("Dear user,please write bitcoin,bitcoincash or etherium.We do not accept abbrevations as input and system is sensetive against capital-minor letters!")
		
label=Label(win,text="Type your crypto currency type(bitcoin,etherium or bitcoincash accepted)?")
label.grid(row=0,column=0)
						
entry=Entry(win)
entry.grid(row=1,column=0)
						
labeltwo=Label(win,text="Type cryptocurrency address which you want to search.")
labeltwo.grid(row=2,column=0)
						
entrytwo=Entry(win)
entrytwo.grid(row=3,column=0)
button=Button(win,text="search",command=show_page)
button.grid(row=4,column=0)
win.mainloop()

