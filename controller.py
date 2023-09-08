class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.height_button =self.view.nb_start_case
        self.width_button =self.view.nb_start_case
        self.actual_clicked_button = [-1, -1]
        for i in range(self.width_button):
            for j in range(self.height_button):
                self.view.buttons_tab[i][j].config(command=lambda i=i, j=j: self.click_on_button(i, j))
        self.view.restart_button.config(command=self.model.restart)
        self.view.window.bind("<KeyPress-a>", lambda event: self.change_color(event, "white"))
        self.view.window.bind("<KeyPress-z>", lambda event: self.change_color(event, "black"))
        self.view.window.bind("<KeyPress-e>", lambda event: self.change_color(event, "cyan"))


    def click_on_button(self, i, j):
        if(self.actual_clicked_button[0] != -1):
            self.view.buttons_tab[self.actual_clicked_button[0]][self.actual_clicked_button[1]].config(relief="raised")
        self.actual_clicked_button[0] = i
        self.actual_clicked_button[1] = j
        self.view.buttons_tab[i][j].config(relief="ridge")


    def change_color(self, event, color):
        i = self.actual_clicked_button[0]
        j = self.actual_clicked_button[1]
        if(i != -1):
            self.view.buttons_tab[i][j].config(background=color)
            self.model.change_a_color(i, j, color)