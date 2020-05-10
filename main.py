import requests
import bs4
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


def get_html_data(url):              # get html data of website
    data = requests.get(url)
    return data


def get_corona_detail_of_india(fine):      # extract data from html text
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="data-table table-responsive").find_all("tr" )

    kk=[]
    for block in info_div[1:34]:     # to get the value out of the html tags
        inside = block.find_all("td")
        for i in inside:
            too = i.get_text()
            kk.append(too)




    ff=[]
    for i in range(0,len(kk),5):    # to break list into list
        gg=list(kk[i:i+5])
        #gg.reverse()
        ff.append(gg)
    print(ff)


    for i in ff:                    # to remove name from list
        i.pop(1)
        i.pop(0)

    print(ff)
    qq=[]
    for i in ff:                    # for converting list to a general list to make string element to int
        for j in i:
            dd= int(j)
            qq.append(dd)
    print('qq',qq)
    oo=[]
    for i in range(0,len(qq),3):    # for converting list element from string to int
        ee=qq[i:i+3]
        oo.append(ee)
    print('oo',oo)
    aa=[]
                                    # working for ALL STATES
    for i in range(0,len(qq),3):
        all_states=qq[i]
        aa.append(all_states)


    if fine!="ALL STATES":

        dic = {"Andaman and Nicobar Islands":0, "Andhra pradesh":1, "Arunachal Pradesh":2,
                   "Assam":3, "Bihar":4, "Chandigarh":5, "Chattisgarh":6, "Dadra Nagar Haveli":7, "Delhi":8,
                   "Goa":9, "Gujarat":10, "Haryana":11, "Himachal Pradesh":12, "Jammu Kashmir":13,
                   "Jharkhand":14, "Karnataka":15, "Kerala":16, "Ladakh":17, "Madhya Pradesh":18, "Maharashtra":19,
                   "Manipaur":20, "Meghalaya":21, "Mizoram":22, "Odisha":23, "Puducherry":24, "Punjab":25, "Rajasthan":26,
                   "Tamil nadu":27, "Telangana":28, "Tripura":29, "Uttarakhand":30, "Uttar Pradesh":31, "West Bengal":32}
        print("got it",fine)
        ww=dic.get(fine)
        print(ww)

        objects = ['Active', 'Cured', 'Death']
        y_pos = np.arange(len(objects))

        plot_list = plt.bar(y_pos, oo[ww], align='center', alpha=0.5, label='Active')


        plot_list[0].set_color('#ff0000')
        plot_list[1].set_color('#1da237')
        plot_list[2].set_color('blue')


        plt.legend()

        plt.xticks(y_pos, objects)
        plt.ylabel('No.of People')
        plt.title(fine)
        plt.show()
    else:
        objects = ["AndamanNicobar","Andhra.P","Arunachal.P",
           "Assam","Bihar","Chandigarh","Chattisgarh","DadarNagarHaveli","Delhi",
           "Goa","Gujarat","Haryana","H.P.","J&K",
           "Jharkhand","Karnataka","Kerala","Ladakh","M.P.","Maharashtra",
           "Manipaur","Meghalaya","Mizoram","Odisha","Puducherry","Punjab","Rajasthan",
           "Tamil nadu","Telangana","Tripura","Uttarakhand","U.P.","West Bengal"]


        y_pos = np.arange(len(objects))

        plt.bar(y_pos, aa, align='center', alpha=0.5,color='green')
        plt.xticks(y_pos, objects,rotation=90)
        plt.ylabel('No.of People')
        plt.title('Different States')
        plt.show()



#GUI
from tkinter import *

root=tk.Tk()
root.geometry("900x800")
root.configure(background='#004d99')
title=Label(root,text=' CORONA   CASES   IN   INDIA  ',font='Calibri 10 bold',bg='#f49f1c', height=12,width=300,bd=5)
title.pack()
root.title("Corona Cases")

photoImageObj = PhotoImage(file="C:\\Users\\parth\\Desktop\\download.png")
lab = Label(root, image=photoImageObj)
lab.place(x=0,y=0)

label=Label(root,text='SELECT ANY STATE FROM INDIA', height=2,width=30)
label.place(x=50,y=215)

OPTIONS = ["SELECT STATE","Andaman and Nicobar Islands","Andhra pradesh","Arunachal Pradesh",
           "Assam","Bihar","Chandigarh","Chattisgarh","Dadar Nagar Haveli","Delhi",
           "Goa","Gujarat","Haryana","Himachal Pradesh","Jammu Kashmir",
           "Jharkhand","Karnataka","Kerala","Ladakh","Madhya Pradesh","Maharashtra",
           "Manipaur","Meghalaya","Mizoram","Odisha","Puducherry","Punjab","Rajasthan",
           "Tamil nadu","Telangana","Tripura","Uttarakhand","Uttar Pradesh","West Bengal","ALL STATES"]

variable = StringVar(root)
variable.set(OPTIONS[0])              # default value

w = OptionMenu(root, variable, *OPTIONS)
w.place(x=50,y=270,height=50,width=200)

def ok():                             #  OK button
    fine=variable.get()
    print(fine)

    get_corona_detail_of_india(fine)



button = Button(root, text="OK", command=ok)
button.place(x=50,y=345, height=40,width=75)

refresh = Button(root, text="REFRESH", command=ok)
refresh.place(x=50,y=420, height=40,width=150)


title1=Label(root,text=' ',bg='#f49f1c', height=10,width=300)
title1.place(x=0,y=700)

root.mainloop()















