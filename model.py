from random import randint

class Model:

    def __init__(self, view):
        self.view = view
        self.grille = []
        self.width = self.view.nb_start_case
        self.height = self.width
        self.nb_case = self.width*self.height
        self.init_grille()


    def init_grille(self):
        colors = ['wight', 'black']
        self.grille = [None] * self.width
        for i in range(self.width):
            self.grille[i] = [None] * self.height
            for j in range(self.height):
                self.grille[i][j] = colors[randint(0, 1)]
        nb_uncripted_case = self.nb_case // 2
        self.cripted_tab = [-1]*self.nb_case
        for i in range(nb_uncripted_case):
            j = randint(0, self.nb_case-1)
            while(self.cripted_tab[j] != -1):
                j = randint(0, self.nb_case-1)
            x = j%self.height
            y = j//self.height
            nb_black_cells = self.count_nb_black_cells(x, y)
            self.cripted_tab[j] = nb_black_cells
            self.view.buttons_tab[x][y].config(text=str(nb_black_cells))
        for i in range(self.width):
            for j in range(self.height):
                self.grille[i][j] = 'cyan'


    def count_nb_black_cells(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(self.coord_valid(x+i, y+j) and self.grille[x+i][y+j] == 'black'):
                    count += 1
        return count

    def coord_valid(self, x, y):
        return (x>=0 and x<self.width and y>=0 and y<self.height)

    def change_a_color(self, x, y, new_color):
        self.grille[x][y] = new_color
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(self.coord_valid(x+i, y+j)):
                    nb_black_cells = self.count_nb_black_cells(x+i, y+j)
                    if(nb_black_cells == self.cripted_tab[(x+i)+(y+j)*self.width]):
                        self.view.buttons_tab[x+i][y+j].config(fg="green")
                    elif(nb_black_cells > self.cripted_tab[(x+i)+(y+j)*self.width]):
                        self.view.buttons_tab[x+i][y+j].config(fg="red")
                    else:
                        self.view.buttons_tab[x+i][y+j].config(fg="blue")

    def restart(self):
        for i in range(self.width):
            for j in range(self.height):
                self.view.buttons_tab[i][j].config(fg="blue", text="")
        self.init_grille()