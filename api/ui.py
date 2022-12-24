import customtkinter

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue") 

class UIComponents(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    self.__configure_window()
    self.__create_side_bar_label()
    self.__create_appearance_mode()
    self.__create_scaling_mode()
    self.__create_main_frame()
    self.__configure_screen_brightness()
    self.__configure_default_values()
  
  def __configure_default_values(self):
    self.appearance_mode_optionemenu.set("Dark")
    self.scaling_optionemenu.set("100%")
    
  def __configure_window(self):
    self.title("Controladora de brilho")
    self.geometry(f"{400}x{580}")
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure((2, 3), weight=0)
    self.grid_rowconfigure((0, 1, 2), weight=1)
    
  def __create_side_bar_label(self):
    self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
    self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
    self.sidebar_frame.grid_rowconfigure(5, weight=1)
    
    self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    
  def __create_appearance_mode(self):
    self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
    self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=(10, 0))
    self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
    self.appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(10, 10))
    
  def __create_scaling_mode(self):
    self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
    self.scaling_label.grid(row=3, column=0, padx=20, pady=(10, 0))
    self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
    self.scaling_optionemenu.grid(row=4, column=0, padx=20, pady=(10, 10))
    
  def change_scaling_event(self, value: str):
    new_scaling_float = int(value.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)
    
  def __create_main_frame(self):
    self.main_frame = customtkinter.CTkFrame(self, fg_color="transparent")
    self.main_frame.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
    self.main_frame.grid_columnconfigure(0, weight=1)
    self.main_frame.grid_rowconfigure(4, weight=1)
    
  def __configure_screen_brightness(self):
    self.screen_brightness = customtkinter.CTkOptionMenu(
      self.main_frame, 
      values=["Monitor 1", "Monitor 2"],
      command=self.change_appearance_mode_event
    )
    
    self.screen_brightness.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
    self.slider = customtkinter.CTkSlider(self.main_frame, orientation="vertical")
    self.slider.grid(row=1, column=0, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
    
  def change_appearance_mode_event(self, value: str):
    customtkinter.set_appearance_mode(value)
    
  def run(self):
    self.mainloop()

class UI():
  def __init__(self, components = UIComponents()):
    self.__components = components
    
  def change_brigthness_event(self, value):
    pass
    
  def run(self):
    self.__components.run()

if __name__ == "__main__":
  ui = UI()
  ui.run()