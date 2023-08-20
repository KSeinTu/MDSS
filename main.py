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
        self.WelcomePage.new_project_button_top = customtkinter.CTkButton(self.WelcomePage.buttonbar_frame2, command=self.changeToQuestion1, text='New Project', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.WelcomePage.new_project_button_top.pack(padx=10, pady=10)
        self.WelcomePage.user_manual_button_top = customtkinter.CTkButton(self.WelcomePage.buttonbar_frame3, command=self.user_manual_button_event, text='User Manual', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.WelcomePage.user_manual_button_top.pack(padx=10, pady=10)

        self.WelcomePage.load_button_mid = customtkinter.CTkButton(self.WelcomePage.content_frame31, command=self.load_project_button_event, text='Load Project', fg_color="#048B6B", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.WelcomePage.load_button_mid.pack()
        self.WelcomePage.new_project_button_mid = customtkinter.CTkButton(self.WelcomePage.content_frame32, command=self.changeToQuestion1, text='New Project', fg_color="#048B6B", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.WelcomePage.new_project_button_mid.pack()
        self.WelcomePage.user_manual_button_mid = customtkinter.CTkButton(self.WelcomePage.content_frame33, command=self.user_manual_button_event, text='User Manual', fg_color="#048B6B", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.WelcomePage.user_manual_button_mid.pack()

        #-----------------------------------------------------------------#

    def changeToQuestion1(self): # Function to change from welcome page and question 1
        ##----------QUESTION 1 PAGE----------##
        print("changeToQuestion1")
        self.WelcomePage.pack_forget()
        

        self.Question1Page = customtkinter.CTkFrame(self, fg_color="white", width=self.WIDTH, height=self.HEIGHT) # Creating frame to span the whole page
        self.Question1Page.grid_rowconfigure((0,1), weight=1)
        self.Question1Page.grid_rowconfigure((2,3,4), weight=5)
        self.Question1Page.grid_rowconfigure(5, weight=6)
        self.Question1Page.grid_columnconfigure(0, weight=1)
        self.Question1Page.grid_columnconfigure((1,2,3,4), weight=8)

        #----WIDGET CONFIGURATIONS----#
        # Top bar
        self.Question1Page.logo_frame = customtkinter.CTkFrame(self.Question1Page, fg_color='#08343C', border_color='#08343C')
        self.Question1Page.logo_frame.grid(row=0, column=0, columnspan=5, rowspan=1, sticky="new")
        self.Question1Page.company_logo_label = customtkinter.CTkLabel(self.Question1Page.logo_frame, image=self.company_logo, text="", fg_color="#08343C", width=120)  # display image with a CTkLabel
        self.Question1Page.company_logo_label.grid(row=0, column=0, padx=10, pady=15)

        # Create a frame for each of the buttons and blank spaces in the toolbar
        # First frame lies underneath to set the background colour
        self.Question1Page.buttonbar_frame = customtkinter.CTkFrame(self.Question1Page,width=self.WIDTH-200, height=60, fg_color='#048B6B')
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
        self.Question1Page.sidebar_frame = customtkinter.CTkFrame(self.Question1Page, fg_color="#048B6B", width=50)
        self.Question1Page.sidebar_frame.grid(row=2, column=0, rowspan=4, sticky="nsew")
        self.Question1Page.sidebar_frame.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)
        self.Question1Page.sidebar_frame.grid_columnconfigure(0, weight=1)

        # Title on the sidebar
        self.Question1Page.sidebar_title = customtkinter.CTkLabel(self.Question1Page.sidebar_frame, text="Chapter Select", text_color="#08343C", font=customtkinter.CTkFont(size=20, weight="bold", underline=True))
        self.Question1Page.sidebar_title.grid(row=0, column=0, sticky="nesw")

        # Buttons on the Sidebar
        self.Question1Page.chapter1_button = customtkinter.CTkButton(self.Question1Page.sidebar_frame, state="disabled", text='Accuracy Req.', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.chapter1_button.grid(row=1, column=0, sticky="ew", padx=30, pady=30)
        self.Question1Page.chapter2_button = customtkinter.CTkButton(self.Question1Page.sidebar_frame, state="enabled", text='Existing WLAN', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.chapter2_button.grid(row=2, column=0, sticky="ew", padx=30, pady=30)
        self.Question1Page.chapter3_button = customtkinter.CTkButton(self.Question1Page.sidebar_frame, state="enabled", text='Budget', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.chapter3_button.grid(row=3, column=0, sticky="ew", padx=30, pady=30) # This button is only enabled for the existing facility option
        self.Question1Page.chapter4_button = customtkinter.CTkButton(self.Question1Page.sidebar_frame, state="enabled", text='Existing Cabling', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.chapter4_button.grid(row=4, column=0, sticky="ew", padx=30, pady=30)
        self.Question1Page.chapter5_button = customtkinter.CTkButton(self.Question1Page.sidebar_frame, state="enabled", text='Handsets', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.chapter5_button.grid(row=5, column=0, sticky="ew", padx=30, pady=30)
        self.Question1Page.chapter6_button = customtkinter.CTkButton(self.Question1Page.sidebar_frame, state="enabled", text='Materials', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.chapter6_button.grid(row=6, column=0, sticky="ew", padx=30, pady=30)
        

        # Creating a frame to hold all of the content frames in the white space
        self.content_height=self.HEIGHT-self.Question1Page.buttonbar_frame.cget("height")-self.Question1Page.logo_frame.cget("height")-100
        print(self.content_height)
        self.Question1Page.content_frame = customtkinter.CTkFrame(self.Question1Page, fg_color="white", width=self.WIDTH, height=self.content_height) 
        self.Question1Page.content_frame.grid(row=2, column=1, rowspan=4, columnspan=4, sticky="nsew", padx=20, pady=10)
        self.Question1Page.content_frame.grid_rowconfigure(0, weight=2)
        self.Question1Page.content_frame.grid_rowconfigure((1,2), weight=1)
        self.Question1Page.content_frame.grid_rowconfigure(3, weight=6)
        self.Question1Page.content_frame.grid_columnconfigure(0, weight=2)

        # Creating buttons
        self.Question1Page.save_project_button = customtkinter.CTkButton(self.Question1Page.buttonbar_frame1, command=self.user_manual_button_event, text='Save Current Project', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.save_project_button.pack(padx=5, pady=10)
        self.Question1Page.load_button = customtkinter.CTkButton(self.Question1Page.buttonbar_frame2, command=self.load_project_button_event, text='Load Project', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.load_button.pack(padx=5, pady=10)
        self.Question1Page.new_project_button = customtkinter.CTkButton(self.Question1Page.buttonbar_frame3, command=self.changeToQuestion1, text='New Project', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.new_project_button.pack(padx=5, pady=10)
        self.Question1Page.user_manual_button = customtkinter.CTkButton(self.Question1Page.buttonbar_frame4, command=self.user_manual_button_event, text='User Manual', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.user_manual_button.pack(padx=5, pady=10)

        # Creating text labels in main body
        self.Question1Page.question_title = customtkinter.CTkLabel(self.Question1Page.content_frame, text=self.get_question_text(1)[0], font=customtkinter.CTkFont(size=24, weight="bold"), text_color="#08343C", anchor="w")
        self.Question1Page.question_title.grid(row=0, column=0, columnspan=1, sticky="nsew", padx=20, pady=20)
        self.Question1Page.question_desc = customtkinter.CTkLabel(self.Question1Page.content_frame, text=self.get_question_text(1)[1], font=customtkinter.CTkFont(size=16, weight="bold"), text_color="#08343C", anchor="w")
        self.Question1Page.question_desc.grid(row=1, column=0, columnspan=1, sticky="nsew", padx=20, pady=20)
        self.Question1Page.question_text = customtkinter.CTkLabel(self.Question1Page.content_frame, text=self.get_question_text(1)[2], font=customtkinter.CTkFont(size=16, weight="bold"), text_color="#08343C", anchor="w")
        self.Question1Page.question_text.grid(row=2, column=0, columnspan=1, sticky="nsew", padx=20, pady=20)
        self.Question1Page.option_frame = customtkinter.CTkFrame(self.Question1Page.content_frame, width=100, height=200)
        self.Question1Page.option_frame.grid(row=3, column=0, columnspan=1, sticky="nsew", padx=20, pady=20)
        self.Question1Page.prevnext_frame = customtkinter.CTkFrame(self.Question1Page.content_frame)
        self.Question1Page.prevnext_frame.grid(row=4, column=0, columnspan=1, sticky="nsew", padx=20, pady=20)
        self.Question1Page.prevnext_frame.grid_columnconfigure(0,weight=15)
        self.Question1Page.prevnext_frame.grid_columnconfigure((1,2),weight=1)
        self.Question1Page.prevnext_frame.grid_rowconfigure(0,weight=1)
        
        # Creating radio buttons
        self.Question1Page.radio_option = customtkinter.IntVar(value=0) # Create a variable for storing the value of the radio button
        self.Question1Page.option1_frame = customtkinter.CTkFrame(self.Question1Page.option_frame, fg_color="#08343C", border_color="#08343C", height=80, corner_radius=8)
        #self.Question1Page.option1_frame.grid(row=0, column=0, padx=10, sticky="ew")
        self.Question1Page.option1_frame.pack(pady=10, padx=30, anchor="w")
        self.Question1Page.option1_radio = customtkinter.CTkRadioButton(master=self.Question1Page.option1_frame, variable=self.Question1Page.radio_option, value=1, font=customtkinter.CTkFont(size=16), text=self.get_question_options(1)[0], text_color="white", corner_radius=6)
        self.Question1Page.option1_radio.grid(row=0, column=0, pady=10, padx=30, sticky="nsew")

        self.Question1Page.option2_frame = customtkinter.CTkFrame(self.Question1Page.option_frame, fg_color="#08343C", border_color="#08343C", height=80, corner_radius=8)
        #self.Question1Page.option2_frame.grid(row=1, column=0, padx=10, sticky="ew")
        self.Question1Page.option2_frame.pack(pady=10, padx=30, anchor="w")
        self.Question1Page.option2_radio = customtkinter.CTkRadioButton(master=self.Question1Page.option2_frame, variable=self.Question1Page.radio_option, value=2, font=customtkinter.CTkFont(size=16), text=self.get_question_options(1)[1], text_color="white", corner_radius=6)
        self.Question1Page.option2_radio.grid(row=0, column=0, pady=10, padx=30, sticky="nsew")

        # Creating Previous and next buttons at the bottom of the page
        self.Question1Page.prev_button = customtkinter.CTkButton(self.Question1Page.prevnext_frame, state="disabled", text='Previous', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.prev_button.grid(row=0, column=1)
        self.Question1Page.next_button = customtkinter.CTkButton(self.Question1Page.prevnext_frame, command=self.changeQuestion, text='Next', fg_color="#08343C", border_color="#08343C", font=customtkinter.CTkFont(size=14, weight="bold"), height=40)
        self.Question1Page.next_button.grid(row=0, column=2)

        self.Question1Page.pack(fill=customtkinter.BOTH)

    def load_project_button_event(self):
        print("test")

    def get_question_text(self, question_index): # Function to operate as a lookup table for which question to get the text for, returns a tuple (question_topic, topic_desc, question_text, question type)
        match question_index: #Switch case statement to extract the necessary text for the question.
            case "1": # Each case is one of the questions in the decision tree
                question_text = "What level of accuracy is required for this facility?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Accuracy Requirements"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "2": # Each case is one of the questions in the decision tree
                question_text = "Is this a new or existing facility?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "New/Existing Facility"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "3a": # Each case is one of the questions in the decision tree
                question_text = "Is there an existing WLAN (Wi-Fi) Network?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Existing WLAN"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "3b": # Each case is one of the questions in the decision tree
                question_text = "What grade is the existing WLAN?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Existing WLAN"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "4": # Each case is one of the questions in the decision tree
                question_text = "What level of budget is allocated to the Mobile Duress System?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Budget"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "5a": # Each case is one of the questions in the decision tree
                question_text = "What level of budget is allocated to the Mobile Duress System?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Budget"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "5b": # Each case is one of the questions in the decision tree
                question_text = "What level of budget is allocated to the Mobile Duress System?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Budget"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "6": # Each case is one of the questions in the decision tree
                question_text = "Is there a lot of existing cabling in the area of works?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Existing Cabling"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "7": # Each case is one of the questions in the decision tree
                question_text = "What type of handsets are intending to be deployed?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Handsets"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "8": # Each case is one of the questions in the decision tree
                question_text = "What type of handsets are intending to be deployed?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Handsets"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "9a": # Each case is one of the questions in the decision tree
                question_text = "What type of walls primarily make up the facility (between rooms where RTLS is desired)"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Building Materials"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "9b": # Each case is one of the questions in the decision tree
                question_text = "Is the building primarily made of brick/concrete internal walls?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Building Materials"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "9c": # Each case is one of the questions in the decision tree
                question_text = "Are there many glass panels in internal areas?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Building Materials"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "9d": # Each case is one of the questions in the decision tree
                question_text = "Are there bright outdoor locations that require RTLS coverage?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Building Materials"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case "9e": # Each case is one of the questions in the decision tree
                question_text = "Is RTLS coverage required in plant rooms?"
                topic_text = "<question_topic for Case 1>"
                question_topic = "Building Materials"
                question_type = "<question_type for Case 1>" # Might not be necessary if there is only one question type in the program.
            case _:
                question_topic = "<EXCEPTION REACHED>"
        return question_topic, topic_text, question_text, question_type
        
    def get_question_options(self, question_index): # Function to operate as a lookup table for options to provide to the user (option1, option2, ...)
        match question_index: #Switch case statement to get the text for each of the options within the question
            case "1": # Each case is one of the questions in the decision tree
                question_option1 = "Within 3m"
                question_option2 = "Between 3m and 5m"
                question_option3 = "Greater than 5m"
                num_options = 3
            case "2": # Each case is one of the questions in the decision tree
                question_option1 = "New Facility"
                question_option2 = "Existing Facility"
                num_options = 2            
            case "3a": # Each case is one of the questions in the decision tree
                question_option1 = "Yes"
                question_option2 = "No"
                num_options = 2         
            case "3b": # Each case is one of the questions in the decision tree
                question_option1 = "Voice-grade or Data-grade"
                question_option2 = "RTLS-grade"
                num_options = 2         
            case "4": # Each case is one of the questions in the decision tree
                question_option1 = "Low-medium"
                question_option2 = "High"
                num_options = 2         
            case "5a": # Each case is one of the questions in the decision tree
                question_option1 = "Low-medium"
                question_option2 = "High"
                num_options = 2  
            case "5b": # Each case is one of the questions in the decision tree
                question_option1 = "Low-medium"
                question_option2 = "High"
                num_options = 2  
            case "6": # Each case is one of the questions in the decision tree
                question_option1 = "Yes"
                question_option2 = "No"
                num_options = 2        
            case "7": # Each case is one of the questions in the decision tree
                question_option1 = "Smartphone, Wi-Fi and bluetooth capable"
                question_option2 = "Smartphone, Wi-Fi capable only"
                question_option3 = "DECT Handset"
                question_option4 = "RF Handset"
                num_options = 4        
            case "8": # Each case is one of the questions in the decision tree
                question_option1 = "Yes"
                question_option2 = "No"
                num_options = 2   
            case "9a": # Each case is one of the questions in the decision tree
                question_option1 = "Thick walls"
                question_option2 = "Thin walls or medium walls or not sure"
                num_options = 2   
            case "9b": # Each case is one of the questions in the decision tree
                question_option1 = "Yes"
                question_option2 = "No"
                num_options = 2   
            case "9c": # Each case is one of the questions in the decision tree
                question_option1 = "Yes"
                question_option2 = "No"
                num_options = 2   
            case "9d": # Each case is one of the questions in the decision tree
                question_option1 = "Yes"
                question_option2 = "No"
                num_options = 2   
            case "9e": # Each case is one of the questions in the decision tree
                question_option1 = "Yes"
                question_option2 = "No"
                num_options = 2   
            case _:
                question_option1 = "<EXCEPTION REACHED>"
                question_option2 = "<EXCEPTION REACHED>"
                num_options=2

        match num_options: # Return the options based on whether or not they exist.
            case 2: # If the question has 2 selectable options
                return num_options, question_option1, question_option2
            case 3: # If the question has 3 selectable options
                return num_options, question_option1, question_option2, question_option3
            case 4: # If the question has 4 selectable options
                return num_options, question_option1, question_option2, question_option3, question_option4
            case _: # exception case
                print("<EXCEPTION REACHED>")

    def new_project_button_event(self):
        self.changeToQuestion1()

    def user_manual_button_event(self):
        print("test")

    def changeQuestion(self, question_index):
        # Changes to the text associated with the question
        print("changeQuestion")
        self.question_arr = self.get_question_text(question_index) # gets the text associated with each of the questions
        self.Question1Page.question_title.configure(text=self.question_arr[0])
        self.Question1Page.question_desc.configure(text=self.question_arr[1])
        self.Question1Page.question_text.configure(text=self.question_arr[2])
        # Changes the options associated with the question
    
    #def questionLogic(self) # Method takes the value of the current question and the value of the radio button to know which question should come next
        

if __name__ == "__main__":
    app = App()
    app.mainloop()