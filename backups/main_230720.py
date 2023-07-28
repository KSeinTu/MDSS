import tkinter
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

        #----GRID CONFIGURAIONS----

        self.geometry(f"{WIDTH}x{HEIGHT}") # setting the window size
        # Adjusting the weights of the rows in the window in the case of resizing
        self.grid_rowconfigure((0,1),weight=1)
        self.grid_rowconfigure((2,6),weight=6)
        self.grid_rowconfigure((3,4,5), weight=2)
        self.grid_columnconfigure((1,2,3), weight=1)
        self.grid_columnconfigure((0,4),weight=5)

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

        #### NOT YET WORKING
        self.logo_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color='#08343C', height=10, border_color='#08343C')
        self.logo_frame.grid(row=0, column=0, columnspan=5, rowspan=1, sticky="nesw")
        self.company_logo = customtkinter.CTkImage(light_image=Image.open("img/AECOM_logo.png"), dark_image=Image.open("img/AECOM_logo.png"), size=(110,25))
        self.company_logo_label = customtkinter.CTkLabel(self.logo_frame, image=self.company_logo, text="", fg_color="#08343C", width=120)  # display image with a CTkLabel
        self.company_logo_label.grid(row=0, column=0, padx=10, pady=15)

        # Create a frame for each of the buttons and blank spaces in the toolbar
        self.buttonbar_frame0 = customtkinter.CTkFrame(self, width=200, height=20, corner_radius=0, fg_color='#048B6B', border_color='#048B6B')
        self.buttonbar_frame0.grid(row=1,column=0, columnspan=1, sticky="nesw")
        self.buttonbar_frame1 = customtkinter.CTkFrame(self, width=100, height=20, corner_radius=0, fg_color='#048B6B', border_color='#048B6B')
        self.buttonbar_frame1.grid(row=1,column=1, columnspan=1, sticky="nesw") 
        self.buttonbar_frame2 = customtkinter.CTkFrame(self, width=100, height=20, corner_radius=0, fg_color='#048B6B', border_color='#048B6B')
        self.buttonbar_frame2.grid(row=1,column=2, columnspan=1, sticky="nesw") 
        self.buttonbar_frame3 = customtkinter.CTkFrame(self, width=100, height=20, corner_radius=0, fg_color='#048B6B', border_color='#048B6B')
        self.buttonbar_frame3.grid(row=1,column=3, columnspan=1, sticky="nesw")
        self.buttonbar_frame4 = customtkinter.CTkFrame(self, width=200, height=20, corner_radius=0, fg_color='#048B6B', border_color='#048B6B')
        self.buttonbar_frame4.grid(row=1,column=4, columnspan=1, sticky="nesw") 

        # Creating main content frames using grid naming convention
        # Top row of white content area
        self.content_frame10 = customtkinter.CTkFrame(self, width=WIDTH, height=30, corner_radius=0, fg_color="#ffffff", border_color="#ffffff") 
        self.content_frame10.grid(row=2, column=0, columnspan=5, sticky="nesw")

        # Second row of white content
        self.content_frame20 = customtkinter.CTkFrame(self, width=300, height=10, corner_radius=0, fg_color="#ffffff", border_color="#ffffff") 
        self.content_frame20.grid(row=3, column=0, columnspan=1, sticky="nesw")
        self.content_frame2 = customtkinter.CTkFrame(self, width=200, height=10, corner_radius=0, fg_color="#ffffff", border_color="#ffffff") # frame for welcome label
        self.content_frame2.grid(row=3, column=1, columnspan=3, sticky="nesw")
        self.content_frame23 = customtkinter.CTkFrame(self, width=300, height=10, corner_radius=0, fg_color="#ffffff", border_color="#ffffff") 
        self.content_frame23.grid(row=3, column=4, columnspan=1, sticky="nesw")

        # Third row of white content
        self.content_frame30 = customtkinter.CTkFrame(self, width=150, height=50, corner_radius=0, fg_color="#ffffff", border_color="#ffffff") 
        self.content_frame30.grid(row=5, column=0, columnspan=1, sticky="nesw")
        self.content_frame31 = customtkinter.CTkFrame(self, width=200, height=50, corner_radius=0, fg_color='#ffffff', border_color="#ffffff") # frame for load button
        self.content_frame31.grid(row=5,column=1, columnspan=1, sticky="nesw") 
        self.content_frame32 = customtkinter.CTkFrame(self, width=200, height=50, corner_radius=0, fg_color='#ffffff', border_color="#ffffff")# frame for new project button
        self.content_frame32.grid(row=5, column=2, columnspan=1, sticky="nesw") 
        self.content_frame33 = customtkinter.CTkFrame(self, width=200, height=50, corner_radius=0, fg_color='#ffffff', border_color="#ffffff") # frame for user manual button
        self.content_frame33.grid(row=5, column=3, columnspan=1, sticky="nesw")
        self.content_frame34 = customtkinter.CTkFrame(self, width=150, height=50, corner_radius=0, fg_color='#ffffff', border_color="#ffffff")
        self.content_frame34.grid(row=5, column=4, columnspan=1, sticky="nesw") 

        # Fourth row of white content
        self.content_frame40 = customtkinter.CTkFrame(self, width=300, height=100, corner_radius=0, fg_color="#ffffff", border_color="#ffffff") 
        self.content_frame40.grid(row=4, column=0, columnspan=1, sticky="nesw")
        self.content_frame4 = customtkinter.CTkFrame(self, width=200, height=100, corner_radius=0, fg_color="#ffffff", border_color="#ffffff") # frame for welcome label
        self.content_frame4.grid(row=4, column=1, columnspan=3, sticky="nesw")
        self.content_frame43 = customtkinter.CTkFrame(self, width=300, height=100, corner_radius=0, fg_color="#ffffff", border_color="#ffffff") 
        self.content_frame43.grid(row=4, column=4, columnspan=1, sticky="nesw")

        # Bottom row of white content area
        self.content_frame10 = customtkinter.CTkFrame(self, width=WIDTH, height=100, corner_radius=0, fg_color="#ffffff", border_color="#ffffff") 
        self.content_frame10.grid(row=6, column=0, columnspan=5, sticky="nesw")

        # Welcome label
        self.welcome_label = customtkinter.CTkLabel(self.content_frame2,text="Welcome!", font=customtkinter.CTkFont(size=56, weight="bold"), text_color='#08343C', width=600)
        self.welcome_label.grid(row=0, column=0, padx=20, pady=10)

        # Guidance text
        self.guidance_label = customtkinter.CTkLabel(self.content_frame4, text="Click one of the buttons above to get started.", font=customtkinter.CTkFont(size=14), text_color='#08343C', width=600)
        self.guidance_label.grid(row=0, column=0, padx=20, pady=10)

        # Creating buttons
        self.load_button_top = customtkinter.CTkButton(self.buttonbar_frame1, command=self.load_project_button_event, text='Load Project', fg_color="#08343C", border_color="#08343C")
        self.load_button_top.grid(row=1,column=1, padx=20, pady=20, sticky="ns")
        self.new_project_button_top = customtkinter.CTkButton(self.buttonbar_frame2, command=self.new_project_button_event, text='New Project', fg_color="#08343C", border_color="#08343C")
        self.new_project_button_top.grid(row=1,column=2, padx=30, pady=20, sticky="ns")
        self.user_manual_button_top = customtkinter.CTkButton(self.buttonbar_frame3, command=self.user_manual_button_event, text='User Manual', fg_color="#08343C", border_color="#08343C")
        self.user_manual_button_top.grid(row=1,column=3, padx=30, pady=20, sticky="ns")

        self.load_button_mid = customtkinter.CTkButton(self.content_frame31, command=self.load_project_button_event, text='Load Project', fg_color="#048B6B")
        self.load_button_mid.grid(row=5, column=1, padx=30, pady=10, sticky="nsew")
        self.new_project_button_mid = customtkinter.CTkButton(self.content_frame32, command=self.new_project_button_event, text='New Project', fg_color="#048B6B")
        self.new_project_button_mid.grid(row=5, column=2, padx=30, pady=10, sticky="nsew")
        self.user_manual_button_mid = customtkinter.CTkButton(self.content_frame33, command=self.user_manual_button_event, text='User Manual', fg_color="#048B6B")
        self.user_manual_button_mid.grid(row=5, column=3, padx=30, pady=10, sticky="nsew")


    def load_project_button_event(self):
        print("test")
        
    def new_project_button_event(self):
        print("test")

    def user_manual_button_event(self):
        print("test")

if __name__ == "__main__":
    app = App()
    app.mainloop()