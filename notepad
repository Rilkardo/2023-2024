import tkinter as tk        # Importē tkinter bibliotēku un piešķir tai aizstājvārdu "tk"               
from tkinter import filedialog     # Importē failu dialoga moduli no tkinter   

class Notepad:       # Definē klasi ar nosaukumu "Notepad"    
    def __init__(self, root):      # Konstruktora metode, inicializē Notepad gadījumu ar saknes logu
        self.root = root           # Piešķir saknes logu instances mainīgajam "self.root"
        self.root.title("Notepad")          # Iestata saknes loga nosaukumu      
        self.root.geometry("600x400")       # Iestata saknes loga sākotnējo izmērus

        self.text_area = tk.Text(self.root, wrap="word", undo=True)     # Izveido teksta logrīku teksta apgabalam ar vārdu aplaušanu un atsaukšanas funkcionalitāti
        self.text_area.pack(expand="yes", fill="both")           # Iesaiņo teksta logrīku, lai aizpildītu pieejamo vietu

        self.menu_bar = tk.Menu(self.root)              # Izveido izvēlnes logrīku izvēļņu joslai
        self.root.config(menu=self.menu_bar)              # Konfigurē saknes logu, lai izmantotu šo izvēlni

      
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)              # Izvēļņu joslā izveido apakšizvēlni Fails
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)    # Pievieno komandas (Jauns, Atvērt, Saglabāt, Iziet) apakšizvēlnē Fails ar atbilstošām metodēm
        self.file_menu.add_command(label="Open", command=self.open_file)  # Pievieno komandu atvērt apakšizvēlnē Fails ar atbilstošām metodēm
        self.file_menu.add_command(label="Save", command=self.save_file)  # Pievieno komandu saglabāt apakšizvēlnē Fails ar atbilstošām metodēm
        self.file_menu.add_separator()                                           # Pievieno separator
        self.file_menu.add_command(label="Exit", command=self.root.destroy) # Pievieno komandu iziet 

    def new_file(self):      # Teksta apgabala notīrīšanas metode
        self.text_area.delete(1.0, tk.END)

    def open_file(self):    # Metode, lai atvērtu failu un ielādētu tā saturu teksta apgabalā
        file_path = filedialog.askopenfilename(defaultextension=".txt",  # pievieno parastas teksta linijas 
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])  
        if file_path:
            with open(file_path, "r") as file: 
                content = file.read()
                self.text_area.delete(1.0, tk.END)  # Pievieno komandu dzēst 
                self.text_area.insert(tk.END, content)  # Atļauj ievdīt datus

    def save_file(self):    # Metode teksta apgabala satura saglabāšanai failā
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

if __name__ == "__main__":
    root = tk.Tk()         # Izveido Tkinter saknes logu
    notepad = Notepad(root)  # Izveido Notepad klases gadījumu ar saknes logu
    root.mainloop()   # Sāk Tkinter notikumu cilpu
