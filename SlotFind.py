import requests
import time
import winsound
import tkinter as tk
  
root=tk.Tk()
 
root.geometry("600x400")

name_var=tk.StringVar()
passw_var=tk.StringVar()
 

def submit():
 
    stateid=name_var.get()
    DateForC=passw_var.get()
     
    print("Your Dist Id : " + stateid)
    print("Date You Entered : " + DateForC)
     
    name_var.set("")
    passw_var.set("")
    root.destroy()

    # From DistId.txt
    # For example 16-05-2021

    url1="https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict"

    while True:
        try:
            r=requests.get(url=url1,params={"district_id":stateid,"date":DateForC},headers={"user-agent" : "user"})
            names=r.json()
            for i in names["centers"]:
                for x in i["sessions"]:
                    if x["min_age_limit"] >17 and x["min_age_limit"]<45 and x["available_capacity_dose1"]>0:
                        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                        print(i["name"],x["min_age_limit"],x["available_capacity"],x["date"])
        except:
            print(r.status_code)

        time.sleep(5)

     
name_label = tk.Label(root, text = 'State Id', font=('calibre',10, 'bold'))
  

name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
  

passw_label = tk.Label(root, text = 'Date', font = ('calibre',10,'bold'))

passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'))

sub_btn=tk.Button(root,text = 'Submit', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
  

root.mainloop()

