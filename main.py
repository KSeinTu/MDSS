import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk): # Creating a class for the app
    def __init__(self): # initialisation function
        super().__init__()
        
        self.title("AECOM Mobile Duress Suitability Software")

        self.WIDTH = 1920
        self.HEIGHT = 1080

        #----PAGE DECLARATIONS----#
        self.WelcomePage = customtkinter.CTkFrame(self, fg_color="white", width=self.WIDTH, height=self.HEIGHT)
        self.WelcomePage.pack(fill=customtkinter.BOTH)
        # Bring welcome page to the top
        #self.WelcomePage.tkraise()
        
        #self.Question2Page = customtkinter.CTkFrame(self)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}") # setting the window size

        ##----------WELCOME PAGE---------##

        #----GRID CONFIGURAIONS----
        # Adjusting the weights of the rows in the window in the case of resizing
        self.WelcomePage.grid_rowconfigure((0,1), weight=1)
        self.WelcomePage.grid_rowconfigure(6, weight=10)
        self.WelcomePage.grid_rowconfigure((3,4,5), weight=2)
        self.WelcomePage.grid_columnconfigure((1,2,3), weight=5)
        self.WelcomePage.grid_columnconfigure((0,4), weight=1)

        #----STYLING----
        customtkinter.set_default_color_theme("style/styles.json")

        #----WIDGET CONFIGURATIONS----#
        # Top bar
        self.WelcomePage.logo_frame = customtkinter.CTkFrame(self.WelcomePage, fg_color='#08343C', height=60, border_color='#08343C')
        self.WelcomePage.logo_frame.grid(row=0, column=0, columnspan=5, rowspan=1, sticky="new")
        self.company_logo = customtkinter.CTkImage(light_image=Image.open("img/AECOM_logo.png"), dark_image=Image.open("img/AECOM_logo.png"), size=(110,25))
        self.WelcomePage.company_logo_label = customtkinter.CTkLabel(self.WelcomePage.logo_frame, image=self.company_logo, text="", fg_color="#08343C", width=120)  # display image with a CTkLabel
        self.WelcomePage.company_logo_label.grid(row=0, column=0, padx=10, pady=15)

        # Create a frame for each of the buttons and blank spaces in the toolbar
        # First frame lies underneath to set the background colour
        self.WelcomePage.buttonbar_frame = customtkinter.CTkFrame(self.WelcomePage,width=self.WIDTH, height=60, fg_color='#048B6B', border_color='#048B6B')
        self.WelcomePage.buttonbar_frame.grid(row=1,column=0, columnspan=5, sticky="nesw")
        #Following grid configurations follow the same as the main page
        self.WelcomePage.buttonbar_frame.grid_columnconfigure((1,2,3), weight=5)
        self.WelcomePage.buttonbar_frame.grid_columnconfigure((0,4), weight=1)

        # Following frames separate the buttons into their own frames to align their spacing
        self.WelcomePage.buttonbar_frame0 = customtkinter.CTkFrame(self.WelcomePage.buttonbar_frame, width=200, height=60, fg_color='#048B6B', border_color='#048B6B')
        self.WelcomePage.buttonbar_frame0.grid(row=1,column=0, columnspan=1, sticky="nesw")
        self.WelcomePage.buttonbar_frame1 = customtkinter.CTkFrame(self.WelcomePage.buttonbar_frame, width=100, height=60, fg_color='#048B6B', border_color='#048B6B')
        self.WelcomePage.buttonbar_frame1.grid(row=1,column=1, columnspan=1, sticky="nsew") 
        self.WelcomePage.buttonbar_frame2 = customtkinter.CTkFrame(self.WelcomePage.buttonbar_frame, width=100, height=60, fg_color='#048B6B', border_color='#048B6B')
        self.WelcomePage.buttonbar_frame2.grid(row=1,column=2, columnspan=1, sticky="nesw") 
        self.WelcomePage.buttonbar_frame3 = customtkinter.CTkFrame(self.WelcomePage.buttonbar_frame, width=100, height=60, fg_color='#048B6B', border_color='#048B6B')
        self.WelcomePage.buttonbar_frame3.grid(row=1,column=3, columnspan=1, sticky="nesw")
        self.WelcomePage.buttonbar_frame4 = customtkinter.CTkFrame(self.WelcomePage.buttonbar_frame, width=200, height=60, fg_color='#048B6B', border_color='#048B6B')
        self.WelcomePage.buttonbar_frame4.grid(row=1,column=4, columnspan=1, sticky="nesw") 

        # Creating main content frames using grid naming convention
        # Top row of white content area
        self.WelcomePage.content_frame00 = customtkinter.CTkFrame(self.WelcomePage, width=self.WIDTH, height=100, fg_color="#ffffff", border_color="#ffffff") 
        self.WelcomePage.content_frame00.grid(row=2, column=0, columnspan=5, sticky="nesw")

        # First row of white content
        self.WelcomePage.content_frame12 = customtkinter.CTkFrame(self.WelcomePage, fg_color="#ffffff", border_color="#ffffff") # frame for welcome label
        self.WelcomePage.content_frame12.grid(row=3, column=0, columnspan=5, sticky="nsew")
        
        # Second row of white content
        self.WelcomePage.content_frame20 = customtkinter.CTkFrame(self.WelcomePage, width=300, height=100, fg_color="#ffffff", border_color="#ffffff") 
        self.WelcomePage.content_frame20.grid(row=4, column=0, columnspan=1, sticky="nesw")
        self.WelcomePage.content_frame2 = customtkinter.CTkFrame(self.WelcomePage, width=200, height=100, fg_color="#ffffff", border_color="#ffffff") # frame for guidance text
        self.WelcomePage.content_frame2.grid(row=4, column=1, columnspan=3, sticky="nesw")
        self.WelcomePage.content_frame23 = customtkinter.CTkFrame(self.WelcomePage, width=300, height=100, fg_color="#ffffff", border_color="#ffffff") 
        self.WelcomePage.content_frame23.grid(row=4, column=4, columnspan=1, sticky="nesw")

        # Third row of white content
        self.WelcomePage.content_frame30 = customtkinter.CTkFrame(self.WelcomePage, width=150, height=50, fg_color="#ffffff", border_color="#ffffff") 
        self.WelcomePage.content_frame30.grid(row=5, column=0, columnspan=1, sticky="nesw")
        self.WelcomePage.content_frame31 = customtkinter.CTkFrame(self.WelcomePage, fg_color='#ffffff', border_color="#ffffff") # frame for load button
        self.WelcomePage.content_frame31.grid(row=5,column=1, columnspan=1, sticky="nsew") 
        self.WelcomePage.content_frame32 = customtkinter.CTkFrame(self.WelcomePage, fg_color='#ffffff', border_color="#ffffff")# frame for new project button
        self.WelcomePage.content_frame32.grid(row=5, column=2, columnspan=1, sticky="nsew") 
        self.WelcomePage.content_frame33 = customtkinter.CTkFrame(self.WelcomePage, fg_color='#ffffff', border_color="#ffffff") # frame for user manual button
        self.WelcomePage.content_frame33.grid(row=5, column=3, columnspan=1, sticky="nsew")
        self.WelcomePage.content_frame34 = customtkinter.CTkFrame(self.WelcomePage, width=150, height=50, fg_color='#ffffff', border_color="#ffffff")
        self.WelcomePage.content_frame34.grid(row=5, column=4, columnspan=1, sticky="nsew") 

        # Bottom row of white content area
        self.WelcomePage.content_frame40 = customtkinter.CTkFrame(self.WelcomePage, width=self.WIDTH, fg_color="white") 
        self.WelcomePage.content_frame40.grid(row=6, column=0, columnspan=5, sticky="nesw")

        #---LABELS & BUTTONS---#
        # Welcome label
        self.WelcomePage.welcome_label = customtkinter.CTkLabel(self.WelcomePage.content_frame12,text="Welcome!", font=customtkinter.CTkFont(size=56, weight="bold"), text_color='#08343C', fg_color="transparent", anchor="center")
        self.WelcomePage.welcome_label.pack()

        # Guidance text
        self.WelcomePage.guidance_label = customtkinter.CTkLabel(self.WelcomePage.content_frame2, text="Click one of the buttons below to get started.", font=customtkinter.CTkFont(size=14), text_color='#08343C', width=600)
        self.WelcomePage.guidance_label.pack()

        # Creating buttons
        self.WelcomePage.load_button_top = customtkinter.CTkButton(self.WelcomePage.buttonbar_frame1, command=self.load_project_button_event, text='Load Project', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.WelcomePage.load_button_top.pack(padx=10, pady=10)
        self.WelcomePage.new_project_button_top = customtkinter.CTkButton(self.WelcomePage.buttonbar_frame2, command=self.change2Question1, text='New Project', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.WelcomePage.new_project_button_top.pack(padx=10, pady=10)
        self.WelcomePage.user_manual_button_top = customtkinter.CTkButton(self.WelcomePage.buttonbar_frame3, command=self.user_manual_button_event, text='User Manual', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.WelcomePage.user_manual_button_top.pack(padx=10, pady=10)

        self.WelcomePage.load_button_mid = customtkinter.CTkButton(self.WelcomePage.content_frame31, command=self.load_project_button_event, text='Load Project', fg_color="#048B6B", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.WelcomePage.load_button_mid.pack()
        self.WelcomePage.new_project_button_mid = customtkinter.CTkButton(self.WelcomePage.content_frame32, command=self.change2Question1, text='New Project', fg_color="#048B6B", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.WelcomePage.new_project_button_mid.pack()
        self.WelcomePage.user_manual_button_mid = customtkinter.CTkButton(self.WelcomePage.content_frame33, command=self.user_manual_button_event, text='User Manual', fg_color="#048B6B", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.WelcomePage.user_manual_button_mid.pack()

        #-----------------------------------------------------------------#

    def change2Question1(self): # Function to change from welcome page and question 1
        ##----------QUESTION 1 PAGE----------##
        print("change2Question1")
        self.WelcomePage.pack_forget()

        self.Question1Page = customtkinter.CTkFrame(self, fg_color="white", width=self.WIDTH, height=self.HEIGHT) # Creating frame to span the whole page
        self.Question1Page.grid_rowconfigure((0,1), weight=1)
        self.Question1Page.grid_rowconfigure((2,3,4), weight=2)
        self.Question1Page.grid_rowconfigure(5, weight=6)
        self.Question1Page.grid_columnconfigure(0, weight=2)
        self.Question1Page.grid_columnconfigure((1,2,3,4), weight=1)

        #----WIDGET CONFIGURATIONS----#
        # Top bar
        self.Question1Page.logo_frame = customtkinter.CTkFrame(self.Question1Page, fg_color='#08343C', border_color='#08343C')
        self.Question1Page.logo_frame.grid(row=0, column=0, columnspan=5, rowspan=1, sticky="new")
        self.Question1Page.company_logo_label = customtkinter.CTkLabel(self.Question1Page.logo_frame, image=self.company_logo, text="", fg_color="#08343C", width=120)  # display image with a CTkLabel
        self.Question1Page.company_logo_label.grid(row=0, column=0, padx=10, pady=15)

        # Create a frame for each of the buttons and blank spaces in the toolbar
        # First frame lies underneath to set the background colour
        self.Question1Page.buttonbar_frame = customtkinter.CTkFrame(self.Question1Page,width=self.WIDTH, height=60, fg_color='#048B6B', border_color='#08343C')
        self.Question1Page.buttonbar_frame.grid(row=1,column=0, columnspan=5, sticky="nesw")
        #Following grid configurations follow the same as the main page
        self.Question1Page.buttonbar_frame.grid_columnconfigure((1,2,3,4), weight=3)
        self.Question1Page.buttonbar_frame.grid_columnconfigure(0, weight=2)
        self.Question1Page.buttonbar_frame.grid_columnconfigure(5, weight=2)

        # Following frames separate the buttons into their own frames to align their spacing
        self.Question1Page.buttonbar_frame0 = customtkinter.CTkFrame(self.Question1Page.buttonbar_frame, width=100, height=60, fg_color='#048B6B', border_color='#048B6B')
        self.Question1Page.buttonbar_frame0.grid(row=1,column=0, columnspan=1, sticky="nesw")
        self.Question1Page.buttonbar_frame1 = customtkinter.CTkFrame(self.Question1Page.buttonbar_frame, width=40, height=60, fg_color='#048B6B', border_color='#048B6B')
        self.Question1Page.buttonbar_frame1.grid(row=1,column=1, columnspan=1, sticky="nsew") 
        self.Question1Page.buttonbar_frame2 = customtkinter.CTkFrame(self.Question1Page.buttonbar_frame, width=40, height=60, fg_color='#048B6B', border_color='#048B6B')
        self.Question1Page.buttonbar_frame2.grid(row=1,column=2, columnspan=1, sticky="nesw") 
        self.Question1Page.buttonbar_frame3 = customtkinter.CTkFrame(self.Question1Page.buttonbar_frame, width=40, height=60, fg_color='#048B6B', border_color='#048B6B')
        self.Question1Page.buttonbar_frame3.grid(row=1,column=3, columnspan=1, sticky="nesw")
        self.Question1Page.buttonbar_frame4 = customtkinter.CTkFrame(self.Question1Page.buttonbar_frame, width=40, height=60, fg_color='#048B6B', border_color='#048B6B')
        self.Question1Page.buttonbar_frame4.grid(row=1,column=4, columnspan=1, sticky="nesw")
        self.Question1Page.buttonbar_frame5 = customtkinter.CTkFrame(self.Question1Page.buttonbar_frame, width=60, height=60, fg_color='#048B6B', border_color='#048B6B')
        self.Question1Page.buttonbar_frame5.grid(row=1,column=5, columnspan=1, sticky="nesw") 

        # Creating a frame for the sidebar
        self.Question1Page.sidebar_frame = customtkinter.CTkFrame(self.Question1Page, fg_color="#048B6B", width=450)
        self.Question1Page.sidebar_frame.grid(row=2, column=0, rowspan=4, sticky="nsew")

        # Creating a frame to hold all of the content frames in the white space
        self.content_height=self.HEIGHT-self.Question1Page.buttonbar_frame.cget("height")-self.Question1Page.logo_frame.cget("height")-100
        print(self.content_height)
        self.Question1Page.content_frame = customtkinter.CTkFrame(self.Question1Page, fg_color="white", width=self.WIDTH, height=self.content_height) 
        self.Question1Page.content_frame.grid(row=2, column=1, rowspan=4, columnspan=4, sticky="nsew")

        # Creating buttons
        self.Question1Page.save_project_button = customtkinter.CTkButton(self.Question1Page.buttonbar_frame1, command=self.user_manual_button_event, text='Save Current Project', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.save_project_button.pack(padx=5, pady=10)
        self.Question1Page.load_button = customtkinter.CTkButton(self.Question1Page.buttonbar_frame2, command=self.load_project_button_event, text='Load Project', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.load_button.pack(padx=5, pady=10)
        self.Question1Page.new_project_button = customtkinter.CTkButton(self.Question1Page.buttonbar_frame3, command=self.change2Question1, text='New Project', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.new_project_button.pack(padx=5, pady=10)
        self.Question1Page.user_manual_button = customtkinter.CTkButton(self.Question1Page.buttonbar_frame4, command=self.user_manual_button_event, text='User Manual', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.user_manual_button.pack(padx=5, pady=10)

        # Creating text labels in main body

        self.Question1Page.pack(fill=customtkinter.BOTH)

    def load_project_button_event(self):
        print("test")

    def get_question_topic_text(self, question_index): # Function to operate as a lookup table for which question to get the text for, returns a tuple (question_topic, topic_desc, question_text, question type)
        match question_index: #Switch case statement to extract the necessary text for the question.
            case 1: # Each case is one of the questions in the decision tree
                question_topic = "<question_topic for Case 1>"
                topic_text = "<question_topic for Case 1>"
                question_text = "<question_text for Case 1>"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case _:
                question_topic = "<EXCEPTION REACHED>"
        return question_topic, topic_text, question_text, question_type
        
    def new_project_button_event(self):
        self.change2Question1()

    def user_manual_button_event(self):
        print("test")

if __name__ == "__main__":
    app = App()
    app.mainloop()
