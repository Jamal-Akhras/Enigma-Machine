Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
rotorI = ["E","K","M","F","L","G","D","Q","V","Z","N","T","O","W","Y","H","X","U","S","P","A","I","B","R","C","J"]
rotorInotch = "Q"
    
rotorII = ["A","J","D","K","S","I","R","U","X","B","L","H","W","T","M","C","Q","G","Z","N","P","Y","F","O","V","E"]    
rotorIII = ["B","D","F","H","J","L","C","P","R","T","X","V","Z","N","Y","E","I","W","G","A","K","M","U","S","Q","O"]
rotorIIInotch = "V"
    
rotorIV = ["E","S","O","V","P","Z","J","A","Y","Q","U","I","R","H","X","L","N","F","T","G","K","D","C","M","W","B"]
rotorIVnotch = "J"
    
rotorV = ["V","Z","B","R","G","I","T","Y","U","P","S","D","N","H","L","X","A","W","M","J","Q","O","F","E","C","K"]
rotorVnotch = "Z";
    
rotorVI = ['J','P','G','V','O','U','M','F','Y','Q','B','E','N','H','Z','R','D','K','A','S','X','L','I','C','T','W'] 
rotorVII = ['N','Z','J','H','G','R','C','X','M','Y','S','W','B','O','U','F','A','I','V','L','P','E','K','Q','D','T'] 
rotorVIII = ['F','K','Q','H','T','L','X','O','C','B','J','S','P','D','Z','R','A','M','E','W','N','I','U','Y','G','V']

rotorNotches = ["Z","M"]
    
rotorBeta = ["L","E","Y","J","V","C","N","I","X","W","P","B","Q","M","D","R","T","A","K","Z","G","F","U","H","O","S"]
rotorGamma = ["F","S","O","K","A","N","U","E","R","H","M","B","T","I","Y","C","W","L","Q","P","Z","X","V","G","J","D"]

reflectorA = ["E","J","M","Z","A","L","Y","X","V","B","W","F","C","R","Q","U","O","N","T","S","P","I","K","H","G","D"]
reflectorB = ["Y","R","U","H","Q","S","L","D","P","X","N","G","O","K","M","I","E","B","F","Z","C","W","V","J","A","T"]
reflectorC = ["F","V","P","J","I","A","O","Y","E","D","R","Z","X","W","G","C","T","K","U","Q","S","B","N","M","H","L"]

rotorSet = [rotorI,rotorII,rotorIII,rotorIV,rotorV,rotorVI,rotorVII,rotorVIII]



# Part 1 : Classes and functions you must implement - refer to the jupyter notebook
# You may need to write more classes, which can be done here or in separate files, you choose.

class PlugLead:
#class that replicates the functionality of using a PlugLead in an enigma machine
    def __init__(self, mapping):
    #constructor used to intialize the objects, taking a 2 letter string with each representing either the start or end of the pluglead    
        
        #mapping = mapping.casefold()
        
        self.whole = mapping
        self.start = mapping[0]
        self.end = mapping[1]
        
        if(len(mapping) > 2):
            raise ValueError("Lead cannot connect more than 2 letters together")
        if(self.start == self.end):
            raise ValueError("PlugLead cannot plug into the same letter")
          
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end
    
    def getWhole(self):
        return self.whole
    
    def encode(self,character):
    #replicates the use of the lead. Used to return the end of the lead if the start is input and vice-versa, returns the same letter if there is no lead
        if(character == self.getStart()):
            output = self.getEnd()
        elif(character == self.getEnd()):
            output = self.getStart()
        else:
            output = character
        return output
    
    def print(self):
    #function to print plugleads -- used for testing
        print("Start of Lead: " +self.start+ " End of Lead: " +self.end)
        
        

class Plugboard:
#class that replicates the functionality of a plugboard (keeping track of all leads)

    leadList = []
    
    def __init__ (self, L = "" , L1 = "", L2 = "", L3 = "", L4 = "", L5= "", L6 = "", L7 = "", L8 = "", L9 = ""):
    #defaults the 10 leads at nothing and appends a list of created leads depending if the value of the lead has been changed, this allows the suer to not use all 10 wires
    
        self.length = 0
        self.leads = []
        
        leadList= [L,L1,L2,L3,L4,L5,L6,L7,L8,L9]
        
        for x in range (0,9):
            if leadList[x] != "":
                self.leads.append(leadList[x])
                self.length += 1
    
    def encode(self, character):
        
        output = character 
        limiter = 0
        
        for x in range(0, self.length):
            if(limiter != 0):
                break
            else:
                if(character == self.leads[x].getStart() or character == self.leads[x].getEnd()):
                    output = self.leads[x].encode(character)
                    limiter = 1
        
        return output
    
    def add(self, lead):
    #add a lead to the plugboard
        
        if(self.length == 0):
            self.leads.append(lead)
            self.length += 1
        else:
            for x in range (0,self.length):
                if(lead.getStart() == self.leads[x].getStart() or lead.getStart() == self.leads[x].getEnd() or lead.getEnd() == self.leads[x].getStart() or lead.getEnd() == self.leads[x].getEnd()):
                    raise ValueError("Multiple leads cannot connect to the same letter")
            else:
                if(self.length <= 10):
                    self.leads.append(lead)
                    self.length += 1
                else:
                    raise ValueError("The maximum number of PlugLeads has been reached (10)")
                    
    def print(self):
    #function to print plugboard -- used for testing
        for x in range(0,self.length):
            self.leads[x].print()
        
class Rotor:

    rotorPos = 0
    
    def __init__(self, mappings):
        self.mapping = mappings
        self.rotorOffset = 0
        self.letters =   "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.mappings = {
                "I":    ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", ["R"], ["Q"]],
                "II":   ["AJDKSIRUXBLHWTMCQGZNPYFVOE", ["F"], ["E"]],
                "III":  ["BDFHJLCPRTXVZNYEIWGAKMUSQO", ["W"], ["V"]],
                "IV":   ["ESOVPZJAYQUIRHXLNFTGKDCMWB", ["K"], ["J"]],
                "V":    ["VZBRGITYUPSDNHLXAWMJQOFECK", ["A"], ["Z"]],
                "VI":   ["JPGVOUMFYQBENHZRDKASXLICTW", ["AN"], ["ZM"]],
                "VII":  ["NZJHGRCXMYSWBOUFAIVLPEKQDT", ["AN"], ["ZM"]],
                "VIII": ["FKQHTLXOCBJSPDZRAMEWNIUYGV", ["AN"], ["ZM"]]}
        self.turnovers = self.mappings[self.mapping][1]
        self.notch = self.mappings[self.mapping][2]
        self.order = None
        self.turnover = False
        self.reset()
     
    def reset(self):
        self.letters = "ABCDEFGHIJKLMNOPQARSTUVWXYZ"
        self.order = self.orderMappings()
        self.rotorMappings()
    
    def orderMappings(self):
        return self.mappings[self.mapping][0]
    
    def rotorMappings(self):
        for _ in range (self.rotorOffset):
            self.rotate(0)
    
    def ringMappings(self):
        for _ in range (self.rotorOffset):
            self.rotate(0)  

    def encode_right_to_left(self, character):
        for x in range (0,len(self.letters)):
            if self.letters[x] == character:
                return self.order[x]

    def encode_left_to_right(self, character):
        for x in range (0,len(self.order)):
            if self.order[x] == character:
                return self.letters[x]
    
    def rotate(self):
        self.letters = self.letters[1: ] + self.letters [ :1]
        self.order = self.order[1: ] + self.order[ :1]
        
        if(self.letters[0] in self.turnovers):
            self.turnover = True

class Reflector:
    def __init__ (self, mapping):
        self.mapping = mapping
        self.letters = "ABCDEFGHIJKLMNOPQARSTUVWXYZ"
        self.mappings = {"A":   "EJMZALYXVBWFCRQUONTSPIKHGD",
                        "B":    "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                        "C":    "FVPJIAOYEDRZXWGCTKUQSBNMHL",
                        "Gamma":"FSOKANUERHMBTIYCWLQPZXVGJD",
                        "Beta": "LEYJVCNIXWPBQMDRTAKZGFUHOS"}
        self.order = self.orderMappings()
        
    def orderMappings(self):
        return self.mappings[self.mapping]
    
    def encode(self, character):
        return self.order.character(self.letters[character])


class EnigmaMachine:
    def __init__(self):
        self.iterations = 0
        self.rotors = []
        
        

    def encode(self,text):
        # Your code here
        raise NotImplementedError()

# method which returns a Rotor object
# @param - name - name of the Rotor e.g. I or Gamma
def rotor_from_name(name):
    if(name == "Gamma" or name == "Beta"):
        return Reflector(name)
    else:
        return Rotor(name)
    

# method with returns an fully set up enigma machine object
# @param - rotors - string of the rotors used in this enigma machine e.g. "I II III"
# @param - reflector - string of the reflector used in this enigma machine e.g. "B"
# @param - ring_settings - string of the ring settings for the rotors, numbered from 01-26 e.g. "01 02 03"
# @param - initial_positions - string of the starting positions of the rotors, from A-Z e.g. "A A Z"
# @param - plugboard_pairs - list of the plugboard pairs to be used, default is an empty list
def create_enigma_machine(rotors,reflector,ring_settings,initial_positions,plugboard_pairs=[]):
    raise NotImplementedError()

# Part 2 : functions to implement to demonstrate code breaking.
# each function should return a list of all the possible answers
# code_one provides an example of how you might declare variables and the return type

def code_one():
    rotors = "Beta Gamma V"
    reflector = "B"
    ring_settings = "23 02 10"
    # initial_positions are unknown
    plugboard = ["VH", "PT", "ZG", "BJ", "EY", "FS"]

    code = "CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH"
    crib = "UNIVERSITY"

    return [code]

def code_two():
    return []

def code_three():
    return []

def code_four():
    return []

def code_five():
    return []

if __name__ == "__main__":
    # You can use this section to test your code.  However, remember that your code
    # is automarked in the jupyter notebook so make sure you have followed the
    # instructions in the notebook to make sure your code works and passes the
    # example tests.

    # NOTE - if your code does not work in the notebook when we
    # run the autograded tests you will receive a 0 mark for functionality.
    pass
