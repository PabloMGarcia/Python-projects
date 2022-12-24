#IMPORTING ALL REQUIRED TO CONNECT TO OSIsoft PI
import sys
import clr

sys.path.append(r'C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0')  
clr.AddReference('OSIsoft.AFSDK')

from OSIsoft.AF.PI import *
from OSIsoft.AF.Search import *
from OSIsoft.AF.Asset import *
from OSIsoft.AF.Data import *
from OSIsoft.AF.Time import *


#IMPORTING ALL REQUIRED TO CREATE GUI ELEMENTS WITH TKINTER LIBRARY
from tkinter import *
from datetime import date
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkcalendar import Calendar
from pandas import *
from datetime import datetime
import matplotlib.pyplot as plt
import os

#Defining functions for the different elements in GUI
def RetreiveValues():
   # PI Data Archive
   piServers = PIServers()  
   piServer = piServers[piserver_names.get()]
   pt = PIPoint.FindPIPoint(piServer, "sinusoid")
   starttime = StartTime_entry.get()
   endtime = EndTime_entry.get()
   time_range = AFTimeRange(starttime , endtime)
   #time_range = AFTimeRange("01.12.2022 17:00:00" , "10.12.2022 10:00:00")
   #time_now = AFTime("*")
   #time_range = AFTimeRange ("1-nov-2022 01:00:00" , "15-nov-2022 00:00:00")
   #result = 'Tag: {0}. Current Value: {1}'.format(pt.Name, pt.CurrentValue())
   #result = pt.RecordedValue(time_now)
   global Return_RecordedValues
   global Dates
   global Values
   Dates = []
   Values = []
   Return_RecordedValues = pt.RecordedValues(time_range , AFBoundaryType.Inside, "", True)
   for element in Return_RecordedValues:
      if element.IsGood == True:
         #print('Value: {0}   and Timestamp:{1}'.format(element.Value, element.Timestamp))
         result = 'Value: ' + str(element.Value) + ' timestamp: ' + str(element.Timestamp) + '\n'
         datetime_format = datetime.strptime(str(element.Timestamp), '%d.%m.%Y %H:%M:%S')
         Dates.append(datetime_format)
         Values.append(element.Value)
         #print(type(element.Timestamp))
         text_area.insert("1.0" , result)
   plt.plot(Dates,Values)
   plt.show()
   messagebox.showinfo("Information", "Values loaded")

def ExportValues():
   f = open('test.txt', 'w')
   f.write(text_area.get("1.0", END))
   f.close()
   messagebox.showinfo("Information", "Values exported in " + os.path.abspath(f.name))


def SendValue():
   if Checkbox_status.get() == 1:
      Tagname = Tag_entry.get()
      Timestamp = Timestamp_entry.get()
      Value = Value_entry.get()
      #work in progress in this function!!!!
      result = 'Tag: ' + Tagname + ' timestamp: ' + Timestamp + ' Value: ' + Value +'\n'
      text_area.delete('1.0', END)
      text_area.insert(INSERT, result)
      #print('Tag', Tagname, 'timestamp',Timestamp, 'Value', Value)
   else:
      messagebox.showwarning("Be careful", "Please, check the Confirmation button to send the value")


def select_file():
    filetypes = (('text files', '*.txt'), ('All files', '*.*')  )
    filename = askopenfilename(title='Open a file', initialdir='/',    filetypes=filetypes)
    file_open = open(filename)
    text_area.delete('1.0', END)
    text_area.insert(INSERT, file_open.read())
    file_open.close()


def Confirmation_CheckBox():
   if Checkbox_status.get() == 1:
      messagebox.showinfo("Information", "You agree and understand the impact of this action")


def TestConnection():
   try:
      piServers = PIServers()
      server_name = piserver_names.get()
      #piServer = piServers.DefaultPIServer
      piServer = piServers[server_name]
      piServer.Connect()
      #print (piServer.Description)
      messagebox.showinfo("Information", "Connection successful!")
      piServer.Disconnect()
      
   except:
      #print("Oops!  That was no valid number.  Try again...")
      messagebox.showwarning("Error", "Oops!  Something went wrong.  Try again...")


root = Tk()
root.geometry("900x450")
root.resizable(True, True)
root.title("GUI APP")

TitleLabel=Label(root, text="Welcome to the PIthon app!", font=("Arial", 25))
TitleLabel
TitleLabel.place(x=200, y=5)

Tag_label=Label(root, text="Tag")
Tag_label.place(x=5, y=40, height=20, width=30)
Tag_entry = Entry(root)
Tag_entry.place(x=5, y=60, height=20, width=100)

Timestamp_label=Label(root, text="Timestamp in format DD.MM.YYYY HH:mm:ss")
Timestamp_label.place(x=120, y=40, height=20, width=250)
Timestamp_entry = Entry(root)
Timestamp_entry.place(x=120, y=60, height=20, width=250)

Value_label=Label(root, text="Value")
Value_label.place(x=400, y=40, height=20, width=30)
Value_entry = Entry(root)
Value_entry.place(x=400, y=60, height=20, width=100)

Checkbox_status = IntVar()
Confirmation_Checkbox = Checkbutton(root, text='Confirmation', variable=Checkbox_status, onvalue=1, offvalue=0, command=Confirmation_CheckBox)
Confirmation_Checkbox.place(x=500, y=60)

Button_SendValue = Button(root, text="Send Value", command=SendValue)
Button_SendValue.place(x=625, y=60)                                                

SelectPIServer_label=Label(root, text="Select PI Server")
SelectPIServer_label.place(x=10, y=105)
OPTIONS = ["OPTION1","OPTION2","OPTION3"] #etc
piserver_names = StringVar(root)
piserver_names.set("Select PI Server") # default value
Dropdown_menu = OptionMenu(root, piserver_names, *OPTIONS)
Dropdown_menu.place(x=100, y=100)

button_RetreiveValues = Button(root, text="Retreive Values", command=RetreiveValues)
button_RetreiveValues.place(x=500, y=175)                                                
#button.pack()

button_ExportValues = Button(root, text="Export Values", command=ExportValues)
button_ExportValues.place(x=600, y=175) 

# create the text widget
text_area = ScrolledText(root, width=50, height=15, wrap='word')
text_area.place(x=10, y=150)

openfile_button = Button(root, text='Open a File', command=select_file)
openfile_button.place(x=400, y=100)

TestConnection_button = Button(root, text='Test Connection', command=TestConnection)
TestConnection_button.place(x=250, y=105)

WriteTagName_label=Label(root, text="Write tag name")
WriteTagName_label.place(x=500, y=220)
WriteTagName_entry = Entry(root)
WriteTagName_entry.place(x=500, y=240, height=20, width=250)

StartTime_label=Label(root, text="Start Time (format DD.MM.YYYY HH:mm:ss)")
StartTime_label.place(x=500, y=280, height=20, width=250)
StartTime_entry = Entry(root)
StartTime_entry.place(x=500, y=300, height=20, width=250)

EndtTime_label=Label(root, text="End Time (format DD.MM.YYYY HH:mm:ss)")
EndtTime_label.place(x=500, y=350, height=20, width=250)
EndTime_entry = Entry(root)
EndTime_entry.place(x=500, y=370, height=20, width=250)

root.mainloop()

