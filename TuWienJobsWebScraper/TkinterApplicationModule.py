import tkinter as tk
import webbrowser
import DataLoggerModule as logger



class ApplicationWindow:
    def __init__(self):
        self.root = tk.Tk() #Create main window
        self.root.title("Clickable Table")
        self.root.geometry("450x450")

        self.table_frame = tk.Frame(self.root) #creates container that can hold certain other widgets tkinter provides (is attatched to root)
        self.table_frame.pack(padx=10, pady=10)

        self.explainer_frame = tk.Frame(self.root)
        self.explainer_frame.pack(padx=10, pady=10)

        self.date_frame = tk.Frame(self.root)
        self.date_frame.pack(padx=10, pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=10)

        #label is a text displaying widget. the first argument [table_frame] is the parent widget.
        #so essentially we are attatching our lables to table_frame so we can easier organize things later.
        tk.Label(self.table_frame, text="Title", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5) 
        tk.Label(self.table_frame, text="Location", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=5, pady=5)
        #   root (main window)
        #   └── table_frame (container for table)
        #       ├── Label "Title" (row=0, col=0)
        #       └── Label "Location" (row=0, col=1)

        tk.Label(self.explainer_frame, text="black = NEW", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5) 
        tk.Label(self.explainer_frame, text="grey = OLD JOB", font=("Arial", 10)).grid(row=0, column=1, padx=5, pady=5) 
        tk.Label(self.explainer_frame, text="green = CHOSEN INSTITUTE", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=5) 

        tk.Label(self.date_frame, text= "Last Update: " + logger.getLastUpdateTime(), font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5) 

        tk.Button(self.button_frame, text="Reset Log Data", command=logger.resetLogger).pack()

    def open_link(self, url):
        webbrowser.open(url)


    def updateData(self, jobData):
        # Populate the table
        for i, job in enumerate(jobData, start=1):
            # Clickable Title
            title_label = tk.Label(self.table_frame, text=job['Title'], fg="blue", cursor="hand2", font=("Arial", 11, "underline"))
            title_label.grid(row=i, column=0, sticky="w", padx=5, pady=5)
            title_label.bind("<Button-1>", lambda e, url=job['Link']: self.open_link(url))

            # Location
            location_label = tk.Label(self.table_frame, text=job['Location'], fg=job["Color"], font=("Arial", 11))
            location_label.grid(row=i, column=1, sticky="w", padx=5, pady=5)

    #start mainloop (only needs to be done once!)
    def run(self):
       self.root.geometry("")         # Resize window to fit widgets
       self.root.mainloop()

    