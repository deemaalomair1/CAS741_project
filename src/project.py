from tkinter import * #tkinter is built-in package for GUI.
from tkinter import ttk #some tkinter object need to be imported explicitly. we will use it to create combobox.
from tkinter import messagebox #some tkinter object need to be imported explicitly.
from atomicMass import * #atomicMass is a library that contains all the elements with their atomic mass value.

my_list=["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si",
         "P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni",
         "Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo",
         "Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba",
         "La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb",
         "Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po",
         "At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf",
         "Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"]
# my_list is a list contains all chemical elements to be used later.



class App: #class that contains all needed functions.

    def is_number(self, P): #function to check if the entered value is number or not.
        if str.isdigit(P)  or P == "" or P == ".": #if p is a digit return true
            return True
        else: #if not it will show an error massage to the user
            messagebox.showerror("Error", "Atom and mass values should be a number ! ")
            return False
    #we will use above function to check if the atoms value entered by the user is a number.
    # otherwise error massage will appear.


    def __init__(self, root):#function used for all GUI related code.
        # root is the main window.. all the widgets will be inside it.
        # GUI will be divided into two frames one fo the equation entry and other for calculation
        self.topFrame = Frame(root) #this command will create the top frame in the root.
        self.bottomFrame = Frame(root) #this command will create the bottom frame in the root.
        self.topFrame.grid(row=2) #this command will place the top frame in the root. in the second row of the window
        self.bottomFrame.grid(row=14) #this command will place the bottom frame in the root.

        vcmd = (self.topFrame.register(self.is_number))
        # vcmd will use the function self.is_number each time it's called.


        #introduction label
        self.intro = Label(root , text="This chemical equation balancer can help you to balance an "
                                       "unbalanced equation. This balancer can also help you check whether the equation"
                                     " is balanced or not ")
        # placing the label in row 1 of root windo.
        self.intro.grid(row=1, sticky=W)
        #staring reactant 1 related widgets.
        self.react1Label = Label(self.topFrame, text="reactant1:")
        #this command will create a label inside top frame.
        # the label widget text parameter is the text that will be shown to the user.
        self.react1Label.grid(row=2, column=0, sticky=W)
        # placing the label in row 2 and first column , sticky=W means to the end west of the location.
        self.elem1Label = Label(self.topFrame, text="element1:", bg="yellow")
        #this command will create a label inside top frame. bg is the background color of the label
        self.elem1Label.grid(row=3, column=2, sticky=W)
        # placing the label in row 3 and  column 2.
        self.combo1 = ttk.Combobox(self.topFrame, values=my_list, width=6, state="readonly")
        #this will create a comobobox that consists of all chemical elements to choose from.
        # user will use this combo to choose the element in the equation (both for reactant and product
        # first combo is self.combo1 which is for the first element in reactant 1.
        # state = "readonly" means user can not enter into comobobox new value , he just can choose from the list.
        #combobox need to use ttk (imported before)
        self.combo1.grid(row=3, column=3, sticky=W)
        # placing self.combo1  in row 3 and  column 3.
        self.atoms1Label = Label(self.topFrame, text="atom1:")
        # this command will create a label inside top frame.
        self.atoms1Label.grid(row=3, column=4, sticky=W)
        # placing the label in row 3 and  column 4.
        self.atoms1Entry = Entry(self.topFrame, width=6 , validate = "key", validatecommand=(vcmd, '%P'))
        # Entry widget  to enter the atom amount in top frame.
        # validate option determines the type of event that triggers the validation
        #validatecommand will use the vcmd and the entry from the user to make sure it is a number.
        # self.atoms1Entry is for the first atom ( atom for element 1 in reactant 1)
        self.atoms1Entry.grid(row=3, column=5, sticky=W)
        # placing the entry in row 3 and  column 5.
        self.atoms1Entry.insert(END, 0)
        # the default value is 0 if the user did not choose an element.
        #if the user choose an element he needs to change the 0 to valid atom number.
        self.elem2Label = Label(self.topFrame, text="element2:", bg="yellow")
        # this command will create a label inside top frame.
        self.elem2Label.grid(row=3, column=8, sticky=W)
        # placing the label in row 3 and  column 8.
        self.combo2 = ttk.Combobox(self.topFrame, values=my_list, width=6, state="readonly")
        # second combo is self.combo2 which is for the second element in reactant 1.
        self.combo2.grid(row=3, column=9, sticky=W)
        # placing the combo in row 3 and  column 9.
        self.atoms2Label = Label(self.topFrame, text="atom2:")
        # this command will create a label inside top frame.
        self.atoms2Label.grid(row=3, column=10, sticky=W)
        # placing the label in row 3 and  column 10.
        self.atoms2Entry = Entry(self.topFrame, width=6 , validate = "key", validatecommand=(vcmd, '%P'))
        # self.atoms2Entry is for the second atom ( atom for element 2 in reactant 1)
        self.atoms2Entry.insert(END, 0)
        # the default value is 0 if the user did not choose an element.
        # if the user choose an element he needs to change the 0 to valid atom number.
        self.atoms2Entry.grid(row=3, column=11, sticky=W)
        # placing the entry in row 3 and  column 11.
        #done from reactant 1 widgets.
        # -------------------------
        #starting reactant2 related widgets
        #same as reactant1 but with different variables name.
        self.plusLabel = Label(self.topFrame, text="+")
        # this command will create a label inside top frame.
        self.plusLabel.grid(row=4, column=0, sticky=W)
        # placing the label in row 4 and  column 0.
        self.react2Label = Label(self.topFrame, text="reactant2:")
        # this command will create a label inside top frame.
        self.react2Label.grid(row=5, column=0, sticky=W)
        # placing the label in row 5 and  column 0.
        self.elem3Label = Label(self.topFrame, text="element1:", bg="yellow")
        # this command will create a label inside top frame.
        self.elem3Label.grid(row=6, column=2, sticky=W)
        # placing the label in row 6 and  column 2.
        self.combo3 = ttk.Combobox(self.topFrame, values=my_list, width=6, state="readonly")
        # third combo is self.combo3 which is for the first element in reactant 2.
        self.combo3.grid(row=6, column=3, sticky=W)
        # placing the combo in row 6 and  column 3.
        self.atoms3Label = Label(self.topFrame, text="atom1")
        # this command will create a label inside top frame.
        self.atoms3Label.grid(row=6, column=4, sticky=W)
        # placing the label in row 6 and  column 4.
        self.atoms3Entry = Entry(self.topFrame, width=6 , validate = "key", validatecommand=(vcmd, '%P'))
        # self.atoms3Entry is for atom of element 1 in reactant 2
        self.atoms3Entry.grid(row=6, column=5, sticky=W)
        # placing the entry in row 6 and  column 5.
        self.atoms3Entry.insert(END, 0)
        # the default value is 0 if the user did not choose an element.
        # if the user choose an element he needs to change the 0 to valid atom number.
        self.elem4Label = Label(self.topFrame, text="element2:", bg="yellow")
        # this command will create a label inside top frame.
        self.elem4Label.grid(row=6, column=8, sticky=W)
        # placing the label in row 6 and  column 8.
        self.combo4 = ttk.Combobox(self.topFrame, values=my_list, width=6, state="readonly")
        # fourth combo is self.combo4 which is for the second element in reactant 2.
        self.combo4.grid(row=6, column=9, sticky=W)
        # placing the combo in row 6 and  column 9.
        self.atoms4Label = Label(self.topFrame, text="atom2:")
        # this command will create a label inside top frame.
        self.atoms4Label.grid(row=6, column=10, sticky=W)
        # placing the label in row 6 and  column 10.
        self.atoms4Entry = Entry(self.topFrame, width=6 , validate = "key", validatecommand=(vcmd, '%P'))
        # self.atoms4Entry is for atom of element 2 in reactant 2
        self.atoms4Entry.grid(row=6, column=11, sticky=W)
        # placing the entry in row 6 and  column 11.
        self.atoms4Entry.insert(END, 0)
        # the default value is 0 if the user did not choose an element.
        # if the user choose an element he needs to change the 0 to valid atom number.
        #end of reactant 2 related widgets.
        # -----------------------------------
        #starting product 1 related widgets
        self.equalLabel = Label(self.topFrame, text="=>")
        # this command will create a label inside top frame.
        self.equalLabel.grid(row=7, column=0, sticky=W)
        # placing the label in row 7 and  column 0.
        self.product1Label = Label(self.topFrame, text="product1:")
        # this command will create a label inside top frame.
        self.product1Label.grid(row=8, column=0, sticky=W)
        # placing the label in row 8 and  column 0.
        self.elem11Label = Label(self.topFrame, text="element1:", bg="yellow")
        # this command will create a label inside top frame
        self.elem11Label.grid(row=9, column=2, sticky=W)
        # placing the label in row 9 and  column 2.
        self.combo11 = ttk.Combobox(self.topFrame, values=my_list, width=6, state="readonly")
        # fifth combo is self.combo11 which is for the first element in product 1.
        self.combo11.grid(row=9, column=3, sticky=W)
        # placing the combo in row 9 and  column 3.
        self.atoms11Label = Label(self.topFrame, text="atom1")
        # this command will create a label inside top frame
        self.atoms11Label.grid(row=9, column=4, sticky=W)
        # placing the label in row 9 and  column 4.
        self.atoms11Entry = Entry(self.topFrame, width=6 , validate = "key", validatecommand=(vcmd, '%P'))
        # self.atoms11Entry is for atom of element 1 in product 1.
        self.atoms11Entry.grid(row=9, column=5, sticky=W)
        # placing the entry in row 9 and  column 5.
        self.atoms11Entry.insert(END, 0)
        # the default value is 0 if the user did not choose an element.
        # if the user choose an element he needs to change the 0 to valid atom number.
        self.elem22Label = Label(self.topFrame, text="element2:", bg="yellow")
        # this command will create a label inside top frame
        self.elem22Label.grid(row=9, column=8, sticky=W)
        # placing the label in row 9 and  column 8.
        self.combo22 = ttk.Combobox(self.topFrame, values=my_list, width=6, state="readonly")
        # sixth combo is self.combo22 which is for the second element in product 1.
        self.combo22.grid(row=9, column=9, sticky=W)
        # placing the combo in row 9 and  column 9.
        self.atoms22Label = Label(self.topFrame, text="atom2:")
        # this command will create a label inside top frame
        self.atoms22Label.grid(row=9, column=10, sticky=W)
        # placing the label in row 9 and  column 10.
        self.atoms22Entry = Entry(self.topFrame, width=6 , validate = "key", validatecommand=(vcmd, '%P'))
        # self.atoms22Entry is for atom of element 2 in product 1.
        self.atoms22Entry.grid(row=9, column=11, sticky=W)
        # placing the entry in row 9 and  column 11.
        self.atoms22Entry.insert(END, 0)
        # the default value is 0 if the user did not choose an element.
        # if the user choose an element he needs to change the 0 to valid atom number.
        #end of product 1 related widgets.
        # ---------------------------------------
        #starting product 2 related widgets.
        self.plus2Label = Label(self.topFrame, text="+")
        # this command will create a label inside top frame
        self.plus2Label.grid(row=10, column=0, sticky=W)
        # placing the label in row 10 and  column 0.
        self.product2Label = Label(self.topFrame, text="product2:")
        # this command will create a label inside top frame
        self.product2Label.grid(row=11, column=0, sticky=W)
        # placing the label in row 11 and  column 0.
        self.elem33Label = Label(self.topFrame, text="element1:", bg="yellow")
        # this command will create a label inside top frame
        self.elem33Label.grid(row=12, column=2, sticky=W)
        # placing the label in row 12 and  column 2.
        self.combo33 = ttk.Combobox(self.topFrame, values=my_list, width=6, state="readonly")
        # seventh combo is self.combo33 which is for the first element in product 2.
        self.combo33.grid(row=12, column=3, sticky=W)
        # placing the combo in row 12 and  column 3.
        self.atoms33Label = Label(self.topFrame, text="atom1")
        # this command will create a label inside top frame
        self.atoms33Label.grid(row=12, column=4, sticky=W)
        # placing the label in row 12 and  column 4.
        self.atoms33Entry = Entry(self.topFrame, width=6 ,validate = "key", validatecommand=(vcmd, '%P'))
        # self.atoms33Entry is for atom of element 1 in product 2.
        self.atoms33Entry.grid(row=12, column=5, sticky=W)
        # placing the entry in row 12 and  column 5.
        self.atoms33Entry.insert(END, 0)
        # the default value is 0 if the user did not choose an element.
        # if the user choose an element he needs to change the 0 to valid atom number.
        self.elem44Label = Label(self.topFrame, text="element2:", bg="yellow")
        # this command will create a label inside top frame
        self.elem44Label.grid(row=12, column=8, sticky=W)
        # placing the label in row 12 and  column 8.
        self.combo44 = ttk.Combobox(self.topFrame, values=my_list, width=6, state="readonly")
        # eighth combo is self.combo44 which is for the second element in product 2.
        self.combo44.grid(row=12, column=9, sticky=W)
        # placing the combo in row 12 and  column 9.
        self.atoms44Label = Label(self.topFrame, text="atom2:")
        # this command will create a label inside top frame
        self.atoms44Label.grid(row=12, column=10, sticky=W)
        # placing the label in row 12 and  column 10.
        self.atoms44Entry = Entry(self.topFrame, width=6 , validate = "key", validatecommand=(vcmd, '%P'))
        # self.atoms44Entry is for atom of element 2 in product 2.
        self.atoms44Entry.grid(row=12, column=11, sticky=W)
        # placing the entry in row 12 and  column 11.
        self.atoms44Entry.insert(END, 0)
        # the default value is 0 if the user did not choose an element.
        # if the user choose an element he needs to change the 0 to valid atom number.
        #end of product two related widgets.
        #all chemical equation related widgets has been done.
        # -----------------------------------
        #starting the bottom frame widgets.
        self.button1 = Button(self.bottomFrame, text="enter to check if the equation is balance", fg="blue",
                              command=lambda: self.IsBalance())
        # create a button in the bottom frame.
        # text is what will appear in the button for the user.
        # fg = "blue is the font color of the text.
        #  command=lambda: self.IsBalance() means when the user click the button self.IsBalance() function will be called.
        # this button will call the function to check if the chemical equation entered is valid or not.
        self.button1.grid(row=14)
        # place the button in the window.
        self.balancelabel = Label(self.bottomFrame)
        # this command will create a label inside bottom frame
        # no text in this label , so it will be hidden
        # we will fill this text as needed in self.IsBalance() function
        #this label to show the user if the entered equation is balance or not.
        self.balancelabel.grid(column=1, row=14)
        # placing the label in row 14 and  column 1.
        #------------------------------------
        self.MassLabel2 = Label(self.bottomFrame,
                                text="choose the number of reactant with known mass then enter mass value:",
                                bg="yellow")
        # this command will create a label inside bottom frame
        # this label will ask the user to choose which reactant is mass known and ask him to enter the mass.
        self.MassLabel2.grid(row=16)
        # place the label in the window.
        self.combomass = ttk.Combobox(self.bottomFrame, values=['1','2'], width=6, state="readonly")
        # create a combobox to make the user choose which reactant is mass known 1 or 2.
        # he can not enter a value he just can choose from the list.
        self.combomass.grid(row=16, column=1)
        # place the combo in the window.
        self.MassEntry = Entry(self.bottomFrame, width=6, validate="key",validatecommand=(vcmd, '%P'))
        # entry widget to enter the mass amount of known reactant.
        # only digits are allowed to be entered.
        self.MassEntry.grid(row=16, column=2)
        # place the entry in the window.
        self.MassEntry.insert(END, 1)
        #default value is 1 . user will change is as needed.
        self.button3 = Button(self.bottomFrame, text="enter to calculate mass", fg="blue",
                              command=lambda: self.MoleToMass())
        # create a button in the bottom frame.
        #this button for calculating the mass value of the other reactant.
        # when clicked self.MoleToMass() function will be called.
        self.button3.grid(row=17)
        # place the button in the window.
        self.Resultlabel = Label(self.bottomFrame)
        # this label is to display the mass result to the user
        self.Resultlabel.grid( row=18)
        #place the label in the window.

        # the end of the GUI widgets code.
        #-----------------------------------



#-------------------------------
#starting IsBalance(self) function to check if the entered rection is blance or not.
# if not balanced it will balance the reaction and print the balance one to the user.
    def IsBalance(self):

        self.elem1 = self.combo1.get()
        # self.elem1 will get the value chosen from self.combo1 (element 1 of reactant 1)
        self.elem2 = self.combo2.get()
        # self.elem2 will get the value chosen from self.combo2 (element 2 of reactant 1)
        self.elem3 = self.combo3.get()
        # self.elem3 will get the value chosen from self.combo3 (element 1 of reactant 2)
        self.elem4 = self.combo4.get()
        # self.elem4 will get the value chosen from self.combo4 (element 2 of reactant 2)
        self.elem11 = self.combo11.get()
        # self.elem11 will get the value chosen from self.combo11 (element 1 of product 1)
        self.elem22 = self.combo22.get()
        # self.elem22 will get the value chosen from self.combo22 (element 2 of product 1)
        self.elem33 = self.combo33.get()
        # self.elem33 will get the value chosen from self.combo33 (element 1 of product 2)
        self.elem44 = self.combo44.get()
        # self.elem44 will get the value chosen from self.combo44 (element 2 of product 2)
        self.atom1 = int(self.atoms1Entry.get())
        # self.atom1 will get the value entered in self.atoms1Entry (first element's atom of reactant 1)
        self.atom2 = int(self.atoms2Entry.get())
        # self.atom2 will get the value entered in self.atoms2Entry (second element's atom of reactant 1)
        self.atom3 = int(self.atoms3Entry.get())
        # self.atom3 will get the value entered in self.atoms3Entry (first element's atom of reactant 2)
        self.atom4 = int(self.atoms4Entry.get())
        # self.atom4 will get the value entered in self.atoms4Entry (second element's atom of reactant 2)
        self.atom11 = int(self.atoms11Entry.get())
        # self.atom11 will get the value entered in self.atoms11Entry (first element's atom of product 1)
        self.atom22 = int(self.atoms22Entry.get())
        # self.atom22 will get the value entered in self.atoms22Entry (second element's atom of product 1)
        self.atom33 = int(self.atoms33Entry.get())
        # self.atom33 will get the value entered in self.atoms33Entry (first element's atom of product 2)
        self.atom44 = int(self.atoms44Entry.get())
        # self.atom44 will get the value entered in self.atoms44Entry (second element's atom of product 2)


        if self.elem1 !="" and self.atom1 <= 0 or self.elem2 !="" and self.atom2 <= 0 or self.elem3 !="" and \
            self.atom3 <= 0 or self.elem4 !="" and self.atom4 <= 0 or self.elem11 !="" and self.atom11 <= 0 or\
            self.elem22 !="" and self.atom22 <= 0 or self.elem33 !="" and self.atom33 <= 0 or self.elem44 !="" and \
                self.atom44 <= 0:
             messagebox.showerror("Error", "if you choose an element then atom value should be greater than 0")
        # if the user selected an item then entered atom value in any atom's entries is less than 0
        # it will show an error massage to the user.
        if self.elem1 == "" or self.elem3 == "" or self.elem11 == "":
            messagebox.showerror("Error", "you should have at least two reactants and one product ")
            self.balancelabel['text'] = ""
            return
        # if the user did not entered two reactants and one product error massage will be shown
        # each chemical reaction need to have at least two reactants and one product
        # if the if statement is true it will go out from the function.



        reactant = [
            {self.elem1: self.atom1, self.elem2: self.atom2},
            {self.elem3: self.atom3, self.elem4: self.atom4}]
        # creating a reactant dictionary to save all reactants information
        product = [
            {self.elem11: self.atom11, self.elem22: self.atom22},
            {self.elem33: self.atom33, self.elem44: self.atom44}]
        # creating a product dictionary to save all reactants information
        merged = {}
        # creating an empty dictionary to save all reactants elements with the number of their atoms
        for d in reactant:
            for k, v in d.items():
                if k not in merged: merged[k] = []
                merged[k].append(v)
        # loop through reactant dictionary and add each element as a key in merged dictionary.
        # add the number of atoms of this element as it's values.
        # for example [H:[2,1]] if it appear as H2 in reactant 1 and H in reactant 2.
        Result = {key: sum(values) for key, values in merged.items()}
        # Result dictionary will sum the atoms value of each element and add it as a value for reactants side.
        # this will give us the total number of atoms used for each element in the reactant side
        # for example: [H : 3]
        merged2 = {}
        # creating an empty dictionary to save all product elements with the number of their atoms
        for d in product:
            for k, v in d.items():
                if k not in merged2: merged2[k] = []
                merged2[k].append(v)
        # loop through product dictionary and add each element as a key in merged2 dictionary.
        # add the number of atoms of this element as it's values.
        # for example [H:[2,1]] if it appear as H2 in product 1 and H in product 2.
        Result1 = {key: sum(values) for key, values in merged2.items()}
        # Result1 dictionary will sum the atoms value of each element and add it as a value for products side.
        # this will give us the total number of atoms used for each element in the product side
        # for example: [H : 3]
        # we will use these dictionaries as basices to do the balancing.
        # -----------------------------

        # first let's checks if the entered reaction is balanced or not!
        '''the if statement will use the result and result1 dictionaries to do the comparision. 
                it will compare two things:
                first: if the element used in one side but not in the other 
                second: if the total number of atoms for each element used in the reactant
                 side do not equal the total number
                of atoms in the product sides '''
        if Result != Result1:
            self.balancelabel['text'] = "not balance"
        # if not equal it will print not balance in the label that was created as empty before.
        # then we need to divide the reaction more
        # r1 will save only the elements of the first reactant
        # where element name is the key and number of atoms is the value
        # example : r1 = [ H:2 , O:2]
        # the loop will go through the first reactant elements in r1
        # then the if statement will check if element 2 is empty
        # if the first reactant consists of only one element then it will remove the empty one.
        # this will reduce r1 size and will get rid of the 0 in the atom entry.
        # for example if reactant 1 is only : Na
        # remember that element 1 of the first reactant must be filled.
            r1 = reactant[0]
            for key in r1.copy():
                if key == "":
                    r1.pop(key)
        # r2 will save only the elements of the second reactant
        # where element name is the key and number of atoms is the value
        # we will repeat the same thing for reactant 2
        # save it in r2 then remove the empty element !
        # remember that element 1 of the second reactant must be filled.
            r2 = reactant[1]
            for key in r2.copy():
                if key == "":
                    r2.pop(key)
        # p1 will save only the elements of the first product
        # where element name is the key and number of atoms is the value
        # we will repeat the same thing for product 1
        # save it in p1 then remove the empty element !
        # remember that element 1 of the first product must be filled.
            p1 = product[0]
            for key in p1.copy():
                if key == "":
                    p1.pop(key)
        # p2 will save only the elements of the second product
        # where element name is the key and number of atoms is the value
        # we will repeat the same thing for product 2
        # save it in p2 then remove the empty element !
        # remember that product 2 may it be all empty.
            p2 = product[1]
            for key in p2.copy():
                if key == "":
                    p2.pop(key)
        # remove the empty element from Result!
            for key in Result.copy():
                if Result[key] == 0:
                    Result.pop(key)
        # remove the empty element from Result1!
            for key in Result1.copy():
                if Result1[key] == 0:
                    Result1.pop(key)
            #print dictionaries before balancing
            print("Reactant dictionary: ", Result)
            print("Product dictionary: ", Result1)
        #------------------------------------
        #lets check if the user enter an element in one side only which is considred as wrong entry
        # the element entered the reaction should go out from the reaction and vise versa.
            '''loop through r1 and r2 using the the key and if this key is not found 
            in both products then below 
            text will be shown to the user in the label. and then it will go out from the function'''
            for key in r1 or key in r2:
                if key not in p1 and key not in p2:
                    self.balancelabel['text'] = "wrong entry! element should be in the products side as well"
                    return
            '''loop through p1 and p2 using the the key and if this key is not found in both reactants then below 
                        text will be shown to the user in the label. and then it will go out from the function'''
            for key in p1 or key in p2:
                if key not in r1 and key not in r2:
                    self.balancelabel['text'] = "wrong entry! element should be in the reactants side as well"
                    return
        # if the Result == result1 then it means the reaction is balanced.
        # balanced will be printed in the label.
        else:
            self.balancelabel['text'] = "balance"
        # until here we checked if the reaction is balanced or not and if all entries are right.
        # we are done from the first part of the function
        # if the reaction is not balanced then we need to balance it
        # starting the process of balancing the reaction next:

        while Result != Result1:  # as long as it's not balanced yet !
            for key in Result: # for each element in the reactants side do the followings:

                if key in Result1 and Result[key] != Result1[key]:

                    '''if you find this key in the product side and the total atoms value is not the same
                        that means this element is not balanced '''
                    ''' we will assess this element through multiple cases:
                     we have four potential cases: 
                     1- its total atom value  of an element is 1 in the reactants side.
                     2- its total atom value of an element is 1 in the product side.
                     3- the reminder of the division between  total atoms of one side over the other is 0.
                     4-  the reminder of the division between  total atoms of one side over the other is not 0.
                    each element will go over one of these options'''
                    # first case total atom value  of an element is 1 in the reactants side:
                    if Result[key] == 1:  # if the total atoms value in reactant side is one
                        coff = Result1[key]  # the coefficient will be the number of atoms in the product side.
                        '''for example : if we have H in reactant side and 2H in product side ,
                         coefficient will be 2.
                        multiplying H  in the reactant side by 2 this will equal 2H = 2H '''
                        # we need to know if this element in reactant 1 or 2
                        # because the total number of atom of this element is 1
                        # so it will be either in reactant 1 or 2:
                        if key in r1:  # if this element is in reactant1
                            r1.update((k, coff * r1[k]) for k in r1)
                            '''update the total atom value of this element in reactant1 by multiply the number 
                                    of atom of this element which is 1 with the coefficient'''
                            Result.update((k, r1[k]) for k in r1)
                            # we will update the total number of atoms for this element in the Result as well.
                            # we need to update Result to check if result == Result1 after the new coefficient
                        elif key in r2:

                            # if this element is in reactant2 we will do the same thing but we will update r2

                            r2.update((k, coff * r2[k]) for k in r2)

                            # we will update the total number of atoms for this element in the Result as well.
                            # we need to update Result to check if result == Result1 after the new coefficient
                            Result.update((k, r2[k]) for k in r2)


                    # second case total atom value  of an element is 1 in the product side:
                    elif Result1[key] == 1:
                        '''if the total number of atoms is 1 in the product side we will do the same but in opposite way
                        we will multiply the element in the product side by the number of atoms in the reactant side.'''
                        coff = Result[key]
                        # coefficient value equal to total number of atom of this element in the reactant side
                        # because the total number of atom of this element is 1 so it will be either in product 1 or 2:
                        if key in p1: # if this element in product1
                                    p1.update((k, coff * p1[k]) for k in p1) #update p1 with the new value
                                    '''update the total atom value of this element in product1 by multiply the number 
                                                    of atom of this element which is 1 with the coefficient'''
                                    Result1.update((k, p1[k]) for k in p1) #update Result1 with the new value
                        elif key in p2:  # if this element in product2
                                    p2.update((k, coff * p2[k]) for k in p2)
                                    # update p2 with the new value
                                    '''update the total atom value of this element in product2 by multiply the number 
                                                    of atom of this element which is 1 with the coefficient'''
                                    Result1.update((k, p2[k]) for k in p2) #update Result1 with the new value

            # if the total atom value of an element is greater than 1 then:
            #third case: the reminder of the division between  total atoms of one side over the other is 0.
                    # checks if the total atom value in each side can be divided by each other
                    elif Result[key] % Result1[key] == 0 or Result1[key] % Result[key] == 0:
                        # if the reminder is 0
                        m = min(Result[key], Result1[key])
             # we will check which side of the same element has smaller total of atoms and save it in m
                        g = max(Result[key], Result1[key])
            # we will check which side of the same element has greater total of atoms and save it in g
                        coff = int(g / m)
                        ''' dividing the m by g will give us the coefficient and we will multiply it 
                        by the element in the smaller side 
                        for example 2H = 4H (not balanced) -> 4/2 = 2 -> 2*2 H = 4H -> 4H=4H (balanced)'''
                        if Result[key] < Result1[key]: # if reactant side is the smaller then


                            if key in r1:  # check if element in reactant 1?
                                    r1.update((k, coff * r1[k]) for k in r1)
                                    '''update the total atom value of this element in reactant1 by multiply the number 
                                                of atom of this element with the coefficient'''
                                    Result.update((k, r1[k]) for k in r1)  # update Result1 with the new value
                            elif key in r2:  # check if element in reactant 2?
                                    r2.update((k, coff * r2[k]) for k in r2)
                                    '''update the total atom value of this element in reactant1 by multiply the number 
                                                of atom of this element with the coefficient'''
                                    Result.update((k, r2[k]) for k in r2)  # update Result1 with the new value



                        elif Result[key] > Result1[key]:
     # if product side is the smaller then we will repeat the same thing but in the product side instead.


                            if key in p1: # check if element in product 1?
                                    p1.update((k, coff * p1[k]) for k in p1)
                                    '''update the total atom value of this element in product1 by multiply the number 
                                                    of atom of this element with the coefficient'''
                                    Result1.update((k, p1[k]) for k in p1)  # update Result1 with the new value

                            elif key in p2: # check if element in product 2?
                                    p2.update((k, coff * p2[k]) for k in p2)
                                    '''update the total atom value of this element in product1 by multiply the number 
                                                    of atom of this element with the coefficient'''
                                    Result1.update((k, p2[k]) for k in p2)  # update Result1 with the new value





    # fourth case: the reminder of the division between  total atoms of one side over the other is not 0.
    # if they are not dividable by each other
    # we need to multiply each side by the total amount of atoms in the other side
                    elif Result[key] % Result1[key] != 0 or Result1[key] % Result[key] != 0:
                        coff1 = Result[key]
                        # let make coefficient1 == to total number of atoms of an element in reactant side
                        coff2 = Result1[key]
                        # let make coefficient2 == to total number of atoms of an element in product side
                        if key in r1: # check if element in reactant 1?
                                r1.update((k, coff2 * r1[k]) for k in r1)
                                '''then we need to multiply it by the total number of atoms of product side which is 
                                     coefficient2 '''
                                Result.update((k, r1[k]) for k in r1)  # update Result1 with the new value
                        elif key in r2:  # check if element in reactant 2?
                                r2.update((k, coff2 * r2[k]) for k in r2)
                                '''then we need to multiply it by the total number of atoms of product side which is 
                                    coefficient2 '''
                                Result.update((k, r2[k]) for k in r2)  # update Result1 with the new value


                        if key in p1:  # check if element in product 1?
                                p1.update((k, coff1 * p1[k]) for k in p1)
                                '''then we need to multiply it by the total number of atoms of product side which is 
                                    coefficient1 '''
                                Result1.update((k, p1[k]) for k in p1) # update Result1 with the new value
                        elif key in p2:  # check if element in product 2?
                                p2.update((k, coff1 * p2[k]) for k in p2)
                                '''then we need to multiply it by the total number of atoms of product side which is 
                                    coefficient1 '''
                                Result1.update((k, p2[k]) for k in p2)  # update Result1 with the new value
                    for key in Result:
                        if key in r1 and key in r2:
                            # if element in both reactant 1 and 2 sum the value and add it to result
                            Result[key] = r1[key] + r2[key]  # update Result1 with the new value
                    for key in Result1:
                        if key in p1 and key in p2:
                            # if element in both products 1 and 2 sum the value and add it to result1
                            Result1[key] = p1[key] + p2[key]  # update Result1 with the new value

        #print the dictionaries after balancing
        print("Reactant1 dictionary: " , Result)
        print("Product1 dictionary: " , Result1)

        if Result == Result1: # check if they are equal now
            # if total atom number for each element is equal in both side so it finally balance!
            # this section is to print the answer to end user

            for key in r1: # for each element in reactant 1
                if key != "": # if element is not empty
                    self.total1 = r1[key] # save the total atom value in variable total and exist the loop
                    break   # we need just the first element


            for key in r2: # for each element in reactant 2
                if key != "": # if element is not empty
                    self.total2 = r2[key] # save the total atom value in variable total and exist the loop
                    break # we need just the first element


            for key in p1:
                if key != "": # for each element in product 1
                    self.total3 = p1[key] # if element is not empty
                    # save the total atom value in variable total and exist the loop
                    break # we need just the first element

                # because product2 is allowed to be empty but reactant 1 , 2 product1 must at leas have one element
            if p2 == {}: #if the whole product is empty make the total 0
                self.total4 = 0
            else:
                for key in p2: #if there is element
                    self.total4 = p2[key]  # save the total atom value in variable total and exist the loop
                    break

                # coefficient1 to display:
                '''coefficient1 will be before reactant 1 coefficient1 is equal to the total number of atoms of the 
                first element of the reactant 1 after balancing / total number of atoms of the element before balancing'''
            self.coefficient1 = int(self.total1 / self.atom1)
            '''coefficient2 will be before reactant 2 coefficient2 is equal to the total number of atoms of the 
                first element of the reactant 2 after balancing / total number of atoms of the element before balancing'''
            self.coefficient2 = int(self.total2 / self.atom3)
            '''coefficient3 will be before product 1 coefficient3 is equal to the total number of atoms of the 
                first element of the product 1 after balancing / total number of atoms of the element before balancing'''
            self.coefficient3 = int(self.total3 / self.atom11)
            # if the total is 0 or total atoms is 0 that mean product 2 is empty and no need for coefficient
            if self.total4 == 0 or self.atom33 == 0:
                self.coefficient4 = 0
            else: #otherwise calculate the coefficient
                self.coefficient4 = int(self.total4 / self.atom33)
                '''coefficient4 will be before product 2 coefficient4 is equal to the total number of atoms of the 
                first element of the product 2 after balancing / total number of atoms of the element before balancing'''
            print("coefficient1: " + str(self.coefficient1))
            print("coefficient2: " + str(self.coefficient2))
            print("coefficient3: " + str(self.coefficient3))
            print("coefficient4: " + str(self.coefficient4))
            plus1= " + "
            new = ",+" #to use it in display
            self.answer = "the balance form is: " + str(self.coefficient1)+self.elem1+str(self.atom1)+self.elem2+\
                str(self.atom2) + plus1 + str(self.coefficient2)+self.elem3+str(self.atom3)+self.elem4+str(self.atom4)+"=" \
                +str(self.coefficient3)+self.elem11+str(self.atom11)+self.elem22+str(self.atom22)+new \
                +str(self.coefficient4)+self.elem33+str(self.atom33)+self.elem44+str(self.atom44)
            '''self.answer will print out the new chemical reaction after balancing with the new
                    coefficient placed before each reactant and product as needed'''

            if str(self.coefficient4) == '0' :
                # if coefficient4 = 0 that means there is no product 2 so we need to remove the second + sign
                self.answer= self.answer.replace(new,'') # replace + with empty space.

            self.answer= self.answer.replace("0",'')
                #  if  atom = 0  that means empty element no need to display it.
            self.answer = self.answer.replace("1", '')
                # if the atom or coefficient equal 1 no need to display 1 it's understood.

            self.AfterBalancelabel = Label(self.bottomFrame, text=  self.answer)  # print final answer to the label.
            self.AfterBalancelabel.grid(row=15)  # place the label

    #second function is to calculate MolecularWeight 1 ( for the first reactant)
    def MolecularWeight1(self):
        element1AtomicMass = 0  # assign 0 to reactant1AtomicMass as initial value.
        element2AtomicMass = 0
        for self.element , self.AtomicMass in MM_of_Elements.items():
            '''MM_of_Elements is a dictionary consist of all chemical elements as a key and their atomic values as a 
             a value , for example {He : 4.002602, 'Sc': 44.955912, 'Ti': 47.867,}
             self.element will return  element name and self.AtomicMass will return the atomic mass value
             so, we will loop through  MM_of_Elements'''
            if self.element == self.elem1:
                '''if we found element in MM_of_Elements == to element 1 or element 2 in  reactant1 we will
                add it to variable reactant1AtomicMass'''
                element1AtomicMass += self.AtomicMass
                print("element name: " , self.elem1, "atomic mass: ", self.AtomicMass)
            if self.element == self.elem2:
                element2AtomicMass += self.AtomicMass
                print("element name: ", self.elem2, "atomic mass: ", self.AtomicMass)
                '''after we get the atomic mass for reactant 1 we need to multiply it with the total 
                atoms values of this reactant to get  Molecular_Weight for reactant1'''
        self.Molecular_Weight1 = (self.atom1 * element1AtomicMass) +(self.atom2 * element2AtomicMass)
        # saving the result in variable self.Molecular_Weight1
        reactant = self.elem1 + str(self.atom1) + self.elem2 + str(self.atom2)
        print("reactant name:", reactant,  "Molecular Weigh: ", self.Molecular_Weight1)
        return self.Molecular_Weight1

        #return this variable to be used in other functions as needed.

    # THIRD function is to calculate MolecularWeight 2 ( for the SECOND reactant)
    def MolecularWeight2(self):
        element1AtomicMass = 0  # assign 0 to reactant1AtomicMass as initial value.
        element2AtomicMass = 0
        for self.element, self.AtomicMass in MM_of_Elements.items():
            '''MM_of_Elements is a dictionary consist of all chemical 
            elements as a key and their atomic values as a a value , 
            for example {He : 4.002602, 'Sc': 44.955912, 'Ti': 47.867,}
            self.element will return  element name and self.AtomicMass will return the atomic mass value
            so, we will loop through  MM_of_Elements'''
            if self.element == self.elem3:
                '''if we found element in MM_of_Elements == to element 1 or element 2 in  reactant2 we will
                                add it to variable reactant1AtomicMass'''
                element1AtomicMass += self.AtomicMass
            if self.element == self.elem4:
                element2AtomicMass += self.AtomicMass
                '''after we get the atomic mass for reactant 2 we need to multiply it with the total 
                            atoms values of this reactant to get  Molecular_Weight for reactant2'''
        self.Molecular_Weight2 = (self.atom3 * element1AtomicMass) + (self.atom4 * element2AtomicMass)
        # saving the result in variable self.Molecular_Weight1
        reactant = self.elem3 + str(self.atom3) + self.elem4 + str(self.atom4)
        print("reactant name:", reactant, "Molecular Weigh: ", self.Molecular_Weight2)
        return self.Molecular_Weight2

        # return this variable to be used in other functions as needed.

    # FOURTH function is to calculate Mole 1 (mole for reactant with known mass)
    def Mole1(self):

            '''to calculate the mole for the first reactant we need
            to divide the entered mass by MolecularWeight
         we will get the mass from self.MassEntry , MolecularWeight
         was calculated before so we will just call
         the function , if the known mass for reactant 1 we will call
         MolecularWeight1 and if the known mass
         for reactant 2 we will call MolecularWeight2'''
            Mass1 = int(self.MassEntry.get())

            if Mass1 <= 0: #to assert that entered mass is greater than 0
                messagebox.showerror("Error", "Mass value should be greater than 0 ! ")
            if self.elem1 == "" or self.elem3 == "" or self.elem11 == "":
    #if the user did not enter correct reactaion format it will not alculate the mass and error massage will show up.
                messagebox.showerror("Error", "you should have at least two reactants and one product ")
                return
            self.choosen = self.combomass.get()  # get for which reactant the known mass is
            if self.choosen == '1':  # if the mass for reactant 1
                mw1 = self.MolecularWeight1()  # call MolecularWeight1 function and save the result in variable mw1.
                self.Mole_1 = Mass1 / mw1   # self.Mole_1 will be equal to division result.
                print("Mole1: " , self.Mole_1)
                return self.Mole_1  # return the result.

            elif self.choosen == '2':  # if the mass for reactant 2
                mw2 = self.MolecularWeight2() # call MolecularWeight2 function and save the result in variable mw2.
                self.Mole_1 = Mass1 / mw2  # self.Mole_1 will be equal to division result.
                print("Mole1: " , self.Mole_1)
                return self.Mole_1  # return the result.
            else:  # if user did not chhose a reactant with knawn mass it will arise an error massage.
                messagebox.showerror("Error", "you should choose the reactant number first ")

    # FIFTH function is to calculate Mole ratio between two reactants.
    def Moleratio (self):
        ''' if the entered reaction is already balanced then the ratio between
        coefficient1 and  coefficient2
        is already 1 because all of them eqaul 1'''
        c = self.combomass.get()
        if self.balancelabel.cget("text") == "balance":  # check if the entered reaction is already balance
            if c == '1' or c == '2':
                self.ratio = 1
        else:
            ''' if the entered reaction is not balanced then we need to
             calculate mole ratio between reactants
                mole ratio =  coefficient of reactant with unknown mass 
                / coefficient of reactant with unknown mass  '''
            if c == '1':
                ''' if the user choose c==1 that means the entered mass was 
                for reactant 1 then the known coefficient
            will be for reactant 1 which is equal to  coefficient 1 and unknown 
            coefficient will equal coefficient 2'''
                self.ratio = self.coefficient2 / self.coefficient1
            elif c == '2':
                ''' if the user choose c==2 that means the entered mass was for 
                reactant 2 then the known coefficient
          will be for reactant 2 which is equal to  coefficient 2 and unknown 
          coefficient will equal coefficient 2'''
                self.ratio = self.coefficient1  / self.coefficient2
        print("ratio" , self.ratio)

        return self.ratio  # return the result.

    # SIXTH function is to calculate Mole for the reactant with unknown mas.
    def MoleRatioToMole(self):
            ''' to calculate the mole of the reactant with unknown mass
             we need to divide the mole of known mass
        by the mole ratio '''
            Mole_r1 = self.Mole1()  # get the mole of reactant with known mass from self.Mole1() function.
            Ratio = self.Moleratio()  # get the mole ratio from self.Moleratio() function.
            Mole2 = Mole_r1/Ratio  # calculate the mole of reactant with unkown mass
            print("mol2: ", Mole2)
            return Mole2  # return the result.

    # LAST function is to calculate mass for the reactant.
    def MoleToMass(self):
        ''' to calculate the mass of the reactant with unknown mass we need to
         multyply the mole of that reactant
         by its MolecularWeight , if the known mass for reactant 1 we
          will call MolecularWeight2 and if the known mass
         for reactant 2 we will call MolecularWeight1'''
        self.choosen = self.combomass.get()  # get for which reactant the known mass is
        Mole_r2 = self.MoleRatioToMole()  # get the mole value of the reactant

        if self.choosen == '1':  # if the known mass for reactant 1
            # we need the MolecularWeight for reactant with unknown mass so we will need reactant 2 MolecularWeight
            mw2 = self.MolecularWeight2()  # call MolecularWeight2 function and save the result in variable mw2.
            self.FinalMass = Mole_r2 * mw2  # final mass is result of multiplication between mole and MolecularWeight
            reactant = self.elem3 + str(self.atom3) + self.elem4 + str(self.atom4)  # print reactant name to user
            reactant = reactant.replace("0", '')  # do not show any 0 in display (if second element does not exist)
            reactant = reactant.replace("1", '')  # do not show any 0 in display (if number of atoms is 1)
            self.Resultlabel['text'] = "The mass value for the reactant" , reactant , "=" , self.FinalMass ,"g"
            # print final mass value in self.Resultlabel
        elif self.choosen == '2' : # if the known mass for reactant 2
            # we need the MolecularWeight for reactant with unknown mass so we will need reactant 1 MolecularWeight
            mw1 = self.MolecularWeight1()  # call MolecularWeight1 function and save the result in variable mw1.
            self.FinalMass = Mole_r2 * mw1  # final mass is result of multiplication between mole and MolecularWeight
            reactant = self.elem1 + str(self.atom1) + self.elem2 + str(self.atom2)  # print reactant name to user
            reactant = reactant.replace("0", '') # do not show any 0 in display (if second element does not exist)
            reactant = reactant.replace("1", '') # do not show any 0 in display (if number of atoms is 1)
            self.Resultlabel['text'] = "The mass value for the reactant" , reactant + "=" , self.FinalMass ,"g"
        print("Final Mass: ", self.FinalMass)
            # print final mass value in self.Resultlabel


root = Tk()  # this command will create blank window "object" from class Tk(), the name of this window is root.
app = App(root) #call the class
app.IsBalance() # call the function
root.mainloop()  # makes the window display until the user close it.







