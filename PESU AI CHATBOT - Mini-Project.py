from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3 as tts
import webbrowser
from tkinter import*
from PIL import ImageTk,Image


chatbot = ChatBot('My Bot:1.0')

trainer = ListTrainer(chatbot)
trainer.train([
    "introduction of bot",
    '''Hi,I'm a PES University chatbot.How may I help you?'''
    "Located_where?",
    '''PES University,located in the Silicon City of India,Bengaluru,has two campuses.The main campus
is situated in Ring Road,Banashankari and the other one is situated in Electronic City''',
    "placements in pes",
    "PESU has amazing placements with more than 11 lakh average package",
    "What is the attendance criteria?",
    "PESU has strict attendance criterion of 85%",
    "Courses",
    '''PESU offers wide range of courses which includes Engineering, Medical, Law, Business Management, Pharmacy, etc.
    Please visit PES official website for further details.''',
    "Fees",
    '''PESU has varying fee structure for various courses,depending upon the means of acquiring the seat.
Please refer PES official website for fee structure''',
    "Clubs",
    '''PESU constitutes many clubs which includes clubs centered around scientific innovation,motorsports
and cultural activites.We also encourage sports events''',
    "Fest",
    '''PESU hosts two fests every year. The fest at the Ring Road campus is called Aatmatrisha and
the fest at Electronic City is called Maaya''',
    "Syllabus",
    '''PES is a completely autonomous university and follows it's own syllabus which
is curated based on the current requirements of the industry''',
    "Scholarships granted",
    '''PES offers lucrative scholarships to its students that perform exceptionally well in their academics and co-curricular activities.
Please visit the official website for more details''',
    "PESSAT",
    '''PESSAT is an all India online entrance exam for admission to PES University.Test centres are provided all over the country.
    Please visit the official PESSAT website or contact us for further information''',
    "Contact",
    "You can contact us through the numbers '+91 80 23721983' or '+91 80 26722108' ",
    "Hostel",
    '''PESU offers state of the art and modern hostels to any students who wish to avail the facilities.
Please contact us for further details.'''

])

engine=tts.init()



window=Tk()
window.geometry("450x600")
window.title("PESU CHAT_BOT")
window.configure(bg="tan1")



img=Image.open("bp.png")
resize=img.resize((340,250),Image.ANTIALIAS)
new_image=ImageTk.PhotoImage(resize)
l1=Label(window,image=new_image)
l1.pack()

frame=Frame(window)
frame.pack()
scy=Scrollbar(frame)
scy.pack(side=RIGHT,fill=Y)

chatbox=Listbox(frame,width=200,height=13,font=("Aerial",12))
chatbox.pack(side=LEFT,fill=BOTH)
chatbox.config(yscrollcommand=scy.set)
scy.config(command=chatbox.yview)



def ask_bot():
          query=user_input.get()
     
          if ("located" in query) or ("location" in query):
             bot_input=chatbot.get_response("Located_where?")
        
          elif "attendance" in query:
             bot_input=chatbot.get_response("What is the attendance criteria?")
        
          elif("placement" in query) or ("placements" in query):
             bot_input=chatbot.get_response("placements in pes")
        
          elif("course" in query) or ("courses" in query):
             bot_input=chatbot.get_response("Courses")
       
          elif("fee" in query) or ("fees" in query):
             bot_input=chatbot.get_response("Fees")
        
          elif("club" in query) or ("clubs" in query):
             bot_input=chatbot.get_response("Clubs")
        
          elif("fest" in query) or ("fests" in query):
             bot_input=chatbot.get_response("Fest")
        
          elif("syllabus" in query):
             bot_input=chatbot.get_response("Syllabus")
        
          elif("scholarship" in query) or ("scholarships" in query):
             bot_input=chatbot.get_response("Scholarships granted")
        
          elif("pessat" in query) or ("entrance exam" in query) or ("entrance examination" in query) or ("entrance exams" in query) or ("entrance examinations" in query):
            bot_input=chatbot.get_response("PESSAT")
       
          elif("contact" in query):
             bot_input=chatbot.get_response("Contact")
        
          elif("hostel" in query) or ("hostels" in query) or ("living arrangements" in query):
             bot_input=chatbot.get_response("Hostel")
        
     
          if("courses" in query or "fee" in query or "fees" in query or "Scholarships" in query or "scholarhips" in query or "Scholarship" in query or "scholarship" in query):
             webbrowser.open("https://pes.edu")
          elif("PESSAT" in query or "pessat" in query or "Entrance exam" in query or "Entrance examination" in query or "Entrance Exam" in query or "Entrance Examination" in query or  "entrance exam" in query or "entrance examination" in query or "entrance exams" in query or "entrance examinations" in query):
             webbrowser.open("https://www.pessat.com")
          chatbox.insert(END,"YOU: "+str(query))
          
          chatbox.insert(END,"From Bot: "+str(bot_input))
          
          engine.say(bot_input)
          user_input.delete(0,END)
          chatbox.yview()
          engine.runAndWait()


user_input=Entry(window,font=('Aerial',18))
user_input.pack(fill=BOTH)

intro=chatbot.get_response("introduction of bot")
chatbox.insert(END,"From Bot: "+str(intro))



b1=Button(window,text="Ask Bot",font=('Aerial',13),bg="cornflower blue",fg="white",command=ask_bot)
b1.pack(pady=13)



window.mainloop()
    
