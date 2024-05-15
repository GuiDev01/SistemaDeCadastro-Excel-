import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import openpyxl, xlrd
import pathlib
from openpyxl import Workbook


#Setando a aparecia padrão do sistema 
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.appearence()
        self.todo_sistema()


    def layout_config(self):
        self.title("Sistema de Gestão de Clientes")
        self.geometry("700x500")
        

    def appearence(self):
        self.lb_apm = ctk.CTkLabel(self, text="Tema", bg_color="transparent", text_color=['#000', '#fff']).place(x=50, y=430)

        self.opt_apm = ctk.CTkOptionMenu(self, values=["Ligth", "Dark", "System"], command=self.change_apm).place(x=50, y=460)


    def change_apm(self, nova_aparencia):
        ctk.set_appearance_mode(nova_aparencia)

    def todo_sistema(self):
        frame = ctk.CTkFrame(self, width=700, height=50, corner_radius=0, bg_color="teal", fg_color="teal").place(x=0, y=10)
        title = ctk.CTkLabel(frame, text="Sistema de Gestão de Clientes", font=("Century Gothic bold", 24),
        text_color="#fff")

        span = ctk.CTkLabel(self, text="Por favor, preencha todos os campos do formulário", font=("Century Gothic bold", 16),
        text_color=["#000", "#fff"])

        #Entrys
        name_entry = ctk.CTkEntry(self, width=350, font=("Century Gothic bold",16), fg_color="transparent") 
        contact_entry = ctk.CTkEntry(self, width=200, font=("Century Gothic bold",16), fg_color="transparent") 
        age_entry = ctk.CTkEntry(self, width=150, font=("Century Gothic bold",16), fg_color="transparent") 
        address_entry = ctk.CTkEntry(self, width=200, font=("Century Gothic bold",16), fg_color="transparent") 

        #Combobox
        gender_combobox = ctk.CTkComboBox(self, values=["Masculino", "Feminino"], font=("Century Gothic bold", 14))

        #Labels
        lb_name = ctk.CTkLabel(self, text="Por favor, preencha todos os campos do formulário", font=("Century Gothic bold", 16),
        text_color=["#000", "#fff"])
        lb_contact = ctk.CTkLabel(self, text="Por favor, preencha todos os campos do formulário", font=("Century Gothic bold", 16),
        text_color=["#000", "#fff"])
        lb_age = ctk.CTkLabel(self, text="Por favor, preencha todos os campos do formulário", font=("Century Gothic bold", 16),
        text_color=["#000", "#fff"])
        lb_gander = ctk.CTkLabel(self, text="Por favor, preencha todos os campos do formulário", font=("Century Gothic bold", 16),
        text_color=["#000", "#fff"])
        lb_address = ctk.CTkLabel(self, text="Por favor, preencha todos os campos do formulário", font=("Century Gothic bold", 16),
        text_color=["#000", "#fff"])
        lb_obs = ctk.CTkLabel(self, text="Por favor, preencha todos os campos do formulário", font=("Century Gothic bold", 16),
        text_color=["#000", "#fff"])





if __name__=="__main__":
    app = App()
    app.mainloop()