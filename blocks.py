variable_dict = {}

class bloque():
    def __init__(self):
        self.i_flow = False
        self.o_flow = self.i_flow

'''Bloques de flujo'''
class On_Start():
    def __init__(self):
        self.i_flow = True
        self.o_flow = self.i_flow
    
class On_Update():
    def __init__(self):
        self.o_flow = True
        
class cycle():
    def __init__(self):
        self.i_flow = True
        self.o_flow = self.i_flow

'''Bloques de Asigancion''' 

class set_var(bloque):
    def execute(self):
        while self.i_flow == False:
            pass
        
        variable_dict[self.i_name] = self.i_value
        self.o_variable_created = self.i_value
        
    def __init__(self):

        self.i_name = ""
        self.i_value = None
        self.o_variable_created = None

class set_arr(bloque):
    def execute(self):
        while self.i_flow == False:
            pass
        
        variable_dict[self.i_name] = [x for x in self.i_value if x!= ',']
        self.o_variable_created = self.i_value
        
    def __init__(self):
        self.i_name = ""
        self.i_value = ""
        self.o_variable_created = None

class call_var(bloque):
    def execute(self):
        while self.i_flow == False:
            pass
        
        self.o_value = variable_dict.get(self.i_name, None)

        
    def __init__(self):
        self.i_name = ""
        self.o_value = None

'''Bloques de Ejecución''' 

class log(bloque):   
    def execute(self):
        while self.i_flow == False:
            pass
        print(self.i_value)

    def __init__(self):
        self.i_value = None
        
class branch():
    def execute(self):
        while self.i_flow == False:
            pass
        if self.i_condition == True:
            self.o_true_flow == True
            self.o_false_flow == False
        else:
            self.o_true_flow == False
            self.o_false_flow == True
            
    def __init__(self):
        self.i_flow = False
        self.o_true_flow = False
        self.o_false_flow = False
        self.i_condition = None
        
class compare(bloque):   
    def execute(self):
        while self.i_flow == False:
            pass
        if self.i_A_value < self.i_B_value :
            self.o_menorque = True
        if self.i_A_value > self.i_B_value :
            self.o_mayorque = True
        if self.i_A_value == self.i_B_value :
            self.o_igual = True
        if self.i_A_value != self.i_B_value :
            self.o_desigual = True

    def __init__(self):
        
        self.i_A_value = None
        self.i_B_value = None
        self.o_menorque = False
        self.o_mayorque = False
        self.o_igual = False
        self.o_desigual = False
                  
class greater_equal(bloque):   
    def execute(self):
        while self.i_flow == False:
            pass
        if self.i_A_value >= self.i_B_value :
            self.o_mayor_igual = True

    def __init__(self):
        
        self.i_A_value = None
        self.i_B_value = None
        self.o_mayor_igual = False

class less_equal(bloque):   
    def execute(self):
        while self.i_flow == False:
            pass
        if self.i_A_value <= self.i_B_value :
            self.o_menor_igual = True

    def __init__(self):
        
        self.i_A_value = None
        self.i_B_value = None
        self.o_menor_igual = False

class for_iter(bloque):   
    def execute(self):
        while self.i_flow == False:
            pass
        print(self.i_value)

    def __init__(self):
        self.i_flow = False
        self.i_value = None     
    
'''Bloques operacionales'''

class add(bloque):   
    def execute(self):
        while self.i_flow == False:
            pass
        self.o_result = self.i_A_value + self.i_B_value

    def __init__(self):
        self.i_A_value = 0 
        self.i_B_value = 0 
        self.o_result= 0

class sub(bloque):   
    def execute(self):
        while self.i_flow == False:
            pass
        self.o_result = self.i_A_value - self.i_B_value

    def __init__(self):
        self.i_A_value = 0 
        self.i_B_value = 0 
        self.o_result= 0


class mult(bloque):   
    def execute(self):
        while self.i_flow == False:
            pass
        self.o_result = self.i_A_value * self.i_B_value

    def __init__(self):
        self.i_A_value = 0 
        self.i_B_value = 0 
        self.o_result= 0 

class div(bloque):   
    def execute(self):
        while self.i_flow == False:
            pass
        self.o_result = self.i_A_value / self.i_B_value

    def __init__(self):
        self.i_A_value = 0 
        self.i_B_value = 0 
        self.o_result= 0 

class div_int(bloque):   
    def execute(self):
        while self.i_flow == False:
            pass
        self.o_result = self.i_A_value // self.i_B_value

    def __init__(self):
        self.i_A_value = 0 
        self.i_B_value = 0 
        self.o_result= 0 

class mod(bloque):   
    def execute(self):
        while self.i_flow == False:
            pass
        self.o_result = self.i_A_value % self.i_B_value

    def __init__(self):
        self.i_A_value = 0 
        self.i_B_value = 0 
        self.o_result= 0 


class append_arr(bloque):   
    def execute(self):
        while self.i_flow == False:
            pass
        
        self.o_value = variable_dict.get(self.i_name, None)

        
    def __init__(self):
        self.i_flow = False
        self.i_name = ""
        self.o_value = None 