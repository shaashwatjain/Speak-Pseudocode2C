import spacy
from replacements import repl_dict_while

"""
Actions : 
Input
Output
If
While
For
Assign
Declare
Start
End

Used in declare
Type checking:
Number, Int -> Integer
Letter, Char -> Character
Decimal, Double -> Float

Declare: 
    If using syntax : 
        declare type variable_names
        type has to be either integer, character or float. Nothing else allowed. No synonyms.

Add in rules : exit ends everything

Can add a functionality in printf- print without newline to get output in one line. useful
for printing patterns.

"""

class NLP:
    def __init__(self) -> str:
        self.nlp = spacy.load("en_core_web_sm")
        self.dict_map = {
            ('start', 'begin', 'initiate', 'commence'): self.start_nlp,
            ('end', 'finish', 'conclude', 'close', 'terminate'): self.end_nlp,
            ('input', 'read', 'load', 'store', 'scan', 'get', 'enter'): self.input_nlp,
            ('output', 'print', 'display', 'show', 'write'): self.print_nlp,
            ('assign', 'set', 'initialize', 'initialise', 'give', 'allocate'): self.assign_nlp,
            ('declare', 'make'): self.declare_nlp,
            ('if', 'else', 'while'): self.do_then_nlp,
            ('for',): self.for_nlp

        }
        self.type_map = {
            ('integer', 'int', 'number', 'numeral'): 'integer',
            ('char', 'character', 'letter'): 'character',
            ('float', 'double', 'decimal'): 'float'
        }
        

    def find_action_in_dict(self, action, curr_dict):
        for key in curr_dict:
            for actions in key:
                if actions == action:
                    return curr_dict[key]
        return None

    def process_nlp(self, line: str) -> str:
        try:
            ind = line.index(' ')
        except ValueError:
            ind = len(line)
        action = line[:ind]
        action = self.find_action_in_dict(action, self.dict_map)
        if action:
            line = action(line, ind)
        return line
    
    def start_nlp(self, line: str, ind: int) -> str:
        return "start"
    
    def end_nlp(self, line: str, ind: int) -> str:
        return "end"
    
    def input_nlp(self, line: str, ind: int) -> str:
        return "input" + line[ind:]
    
    def print_nlp(self, line: str, ind: int) -> str:
        return "print" + line[ind:]
    
    def assign_nlp(self, line: str, ind: int) -> str:
        line = line.replace(" is "," = ")
        line = line.replace(" to "," = ")
        return "assign" + line[ind:]
    
    def declare_nlp(self, line: str, ind: int) -> str:
        doc = self.nlp(line)
        content = []
        doc_len = len(doc)
        i = 0
        type_flag1 = False
        while i < doc_len:
            if(i == 0):
                content.append("declare")
                i += 1
                continue
            if(i == 1 and (doc[i].lemma_ == "integer" or doc[i].lemma_ == "character" or doc[i].lemma_ == "float")):
                i += 1
                type_flag1 = True
                continue
            if(doc[i].pos_ == "CCONJ" or doc[i].pos_ == "PUNCT"):
                i += 1
                if(i < doc_len):
                    content.append(doc[i].lemma_)
                    i += 1
                continue
            if(i == doc_len - 1 and doc_len != 2 and not type_flag1):
                temp_conv = self.find_action_in_dict(doc[i].lemma_, self.type_map)
                if temp_conv:
                    content.append(temp_conv)
                    i += 1
                    continue
            if(i < doc_len):
                content.append(doc[i].lemma_)
                i += 1
        if(type_flag1):
            content.append(doc[1].lemma_)
        return " ".join(content)
    
    def do_then_nlp(self,line: str, ind: int) -> str:
        line = line.split(" ")
        if line[-1]=='do' or line[-1]=='then':
            line.pop(-1)
        return " ".join(line)

    def for_nlp(self, line: str, ind: int) -> str:
        for key in repl_dict_while.keys():
            line = line.replace(" "+key+" ", " " + repl_dict_while[key] + " ")
        print(line)
        return line
