import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk): # Creating a class for the app
    def __init__(self): # initialisation function
        super().__init__()
        
        self.title("AECOM Mobile Duress Suitability Software")

        WIDTH = 1920
        HEIGHT = 1080

        #----PAGE DECLARATIONS----#
        self.WelcomePage = customtkinter.CTkFrame(self, fg_color="black")
        self.WelcomePage.grid(row=0, column=0, sticky="nsew")
        # Pack all pages
        # Bring welcome page to the top
        #self.WelcomePage.tkraise()
        
        #self.Question2Page = customtkinter.CTkFrame(self)
        self.geometry(f"{WIDTH}x{HEIGHT}") # setting the window size

        ##----------WELCOME PAGE---------##

        #----GRID CONFIGURAIONS----
        # Adjusting the weights of the rows in the window in the case of resizing
        self.WelcomePage.grid_rowconfigure((0,1),weight=1)
        self.WelcomePage.grid_rowconfigure(6,weight=6)
        self.WelcomePage.grid_rowconfigure((3,4,5), weight=2)
        self.WelcomePage.grid_columnconfigure((1,2,3), weight=1)
        self.WelcomePage.grid_columnconfigure((0,2,4),weight=5)

        #----STYLING----
        customtkinter.set_default_color_theme("style/styles.json")

        #----WIDGET CONFIGURATIONS----
        # Create top frame with logo
        # self.logobar_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color='#08343C', height=10, border_color='#08343C')
        # self.logobar_frame.grid(row=0, column=1, columnspan=4, rowspan=1, sticky="nsew")
        # self.title_label = customtkinter.CTkLabel(self.logobar_frame, text="Mobile Duress Suitability Tool", font=customtkinter.CTkFont(size=20, weight="bold"), text_color='#ffffff')
        # self.title_label.grid(row=0, column=0, padx=10, pady=15)
        #image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        #self.company_logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "AECOM_logo.png")), size=(26, 26))

        # Top bar
        self.WelcomePage.logo_frame = customtkinter.CTkFrame(self.WelcomePage, fg_color='#08343C', height=10, border_color='#08343C')
        self.WelcomePage.logo_frame.grid(row=0, column=0, columnspan=5, rowspan=1, sticky="nesw")
        self.WelcomePage.company_logo = customtkinter.CTkImage(light_image=Image.open("img/AECOM_logo.png"), dark_image=Image.open("img/AECOM_logo.png"), size=(110,25))
        self.WelcomePage.company_logo_label = customtkinter.CTkLabel(self.WelcomePage.logo_frame, image=self.WelcomePage.company_logo, text="", fg_color="#08343C", width=120)  # display image with a CTkLabel
        self.WelcomePage.company_logo_label.grid(row=0, column=0, padx=10, pady=15)

        # Create a frame for each of the buttons and blank spaces in the toolbar
        self.WelcomePage.buttonbar_frame0 = customtkinter.CTkFrame(self.WelcomePage, width=200, height=40, fg_color='#048B6B', border_color='#048B6B')
        self.WelcomePage.buttonbar_frame0.grid(row=1,column=0, columnspan=1, sticky="nesw")
        self.WelcomePage.buttonbar_frame1 = customtkinter.CTkFrame(self.WelcomePage, width=100, height=40, fg_color='#048B6B', border_color='#048B6B')
        self.WelcomePage.buttonbar_frame1.grid(row=1,column=1, columnspan=1, sticky="nesw") 
        self.WelcomePage.buttonbar_frame2 = customtkinter.CTkFrame(self.WelcomePage, width=100, height=40, fg_color='#048B6B', border_color='#048B6B')
        self.WelcomePage.buttonbar_frame2.grid(row=1,column=2, columnspan=1, sticky="nesw") 
        self.WelcomePage.buttonbar_frame3 = customtkinter.CTkFrame(self.WelcomePage, width=100, height=40, fg_color='#048B6B', border_color='#048B6B')
        self.WelcomePage.buttonbar_frame3.grid(row=1,column=3, columnspan=1, sticky="nesw")
        self.WelcomePage.buttonbar_frame4 = customtkinter.CTkFrame(self.WelcomePage, width=200, height=40, fg_color='#048B6B', border_color='#048B6B')
        self.WelcomePage.buttonbar_frame4.grid(row=1,column=4, columnspan=1, sticky="nesw") 

        # Creating main content frames using grid naming convention
        # Top row of white content area
        self.WelcomePage.content_frame00 = customtkinter.CTkFrame(self.WelcomePage, width=WIDTH, height=100, fg_color="#ffffff", border_color="#ffffff") 
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
        self.WelcomePage.content_frame40 = customtkinter.CTkFrame(self.WelcomePage, width=WIDTH, fg_color="#ffffff", border_color="#ffffff") 
        self.WelcomePage.content_frame40.grid(row=6, column=0, columnspan=5, sticky="nesw")

        #---LABELS & BUTTONS---#
        # Welcome label
        self.WelcomePage.welcome_label = customtkinter.CTkLabel(self.WelcomePage.content_frame12,text="Welcome!", font=customtkinter.CTkFont(size=56, weight="bold"), text_color='#08343C', fg_color="red", anchor="center")
        #self.WelcomePage.welcome_label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        self.WelcomePage.welcome_label.pack()

        # Guidance text
        self.WelcomePage.guidance_label = customtkinter.CTkLabel(self.WelcomePage.content_frame2, text="Click one of the buttons above to get started.", font=customtkinter.CTkFont(size=14), text_color='#08343C', width=600)
        #self.WelcomePage.guidance_label.grid(row=0, column=0, padx=20, pady=10)
        self.WelcomePage.guidance_label.pack()

        # Creating buttons
        self.WelcomePage.load_button_top = customtkinter.CTkButton(self.WelcomePage.buttonbar_frame1, command=self.load_project_button_event, text='Load Project', fg_color="#08343C", border_color="#08343C")
        #self.WelcomePage.load_button_top.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        self.WelcomePage.load_button_top.pack()
        self.WelcomePage.new_project_button_top = customtkinter.CTkButton(self.WelcomePage.buttonbar_frame2, command=self.new_project_button_event, text='New Project', fg_color="#08343C", border_color="#08343C")
        #self.WelcomePage.new_project_button_top.grid(row=1, column=2, padx=30, pady=20, sticky="nsew")
        self.WelcomePage.new_project_button_top.pack()
        self.WelcomePage.user_manual_button_top = customtkinter.CTkButton(self.WelcomePage.buttonbar_frame3, command=self.user_manual_button_event, text='User Manual', fg_color="#08343C", border_color="#08343C")
        #self.WelcomePage.user_manual_button_top.grid(row=1, column=3, padx=30, pady=20, sticky="nsew")
        self.WelcomePage.user_manual_button_top.pack()

        self.WelcomePage.load_button_mid = customtkinter.CTkButton(self.WelcomePage.content_frame31, command=self.load_project_button_event, text='Load Project', fg_color="#048B6B", anchor='e')
        self.WelcomePage.load_button_mid.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")
        self.WelcomePage.new_project_button_mid = customtkinter.CTkButton(self.WelcomePage.content_frame32, command=self.new_project_button_event, text='New Project', fg_color="#048B6B")
        self.WelcomePage.new_project_button_mid.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")
        self.WelcomePage.user_manual_button_mid = customtkinter.CTkButton(self.WelcomePage.content_frame33, command=self.user_manual_button_event, text='User Manual', fg_color="#048B6B", anchor='w')
        self.WelcomePage.user_manual_button_mid.grid(row=5, column=3, padx=10, pady=10, sticky="nsew")

        #-----------------------------------------------------------------#
        

    def change2Question1(self): # Function to change from welcome page and question 1
        ##----------QUESTION 1 PAGE----------##
        self.Question1Page = customtkinter.CTkFrame(self)
        self.Question1Page.grid_rowconfigure((0,1), weight=1)
        self.Question1Page.grid_rowconfigure((2,3,4), weight=2)
        self.Question1Page.grid_rowconfigure(5, weight=6)
        self.Question1Page.grid_columnconfigure(0, weight=1)
        self.Question1Page.grid_columnconfigure((1,2), weight=3)
    def load_project_button_event(self):
        print("test")
        
    def new_project_button_event(self):
        self.change2Question1()

    def user_manual_button_event(self):
        print("test")

if __name__ == "__main__":
    app = App()
    app.mainloop()