from dataclasses import dataclass
import re


# Base class for all operations
class Operation:
    def __init__(self):
        pass
    
    # Override this method to add operation logic
    # Returns modifies line
    def execute(self, line : str) -> str:
        return


# OPERATIONS

# Replaces all instances of "A" with "B"
class Replace(Operation):
    def __init__(self, old_value_, new_value_):
        self.old_value = old_value_
        self.new_value = new_value_
        
    def execute(self, line : str) -> str:
        return line.replace(self.old_value, self.new_value)
        

        

# Data class that contains parameters and operations that will be applied to the code block
@dataclass
class Parameters:
    out_file : str
    operation_stack : list[Operation]

# Contains parsing context
@dataclass
class Context:
    code_block : bool = False



# Logs some kind of message
def log(message, type):
    print(type + " : ", message)
    

# Splits the line on '|', while ignoring '\|' and replacing them with normal '|'
def split_on_pipes(line : str) -> list[str]:
    
    # Split on unescaped delimiters
    pattern = r'(?<!\{}){}'.format('\\', '|')
    parts = re.split(pattern, line)
    
    # Unescape any remaining escaped delimiters in each part
    unescape_pattern = r'{}{}'.format('\\', '|')
    return [re.sub(unescape_pattern, '|', part) for part in parts]


# Analyzes a parameter line
def parse_parameter_line(line : str, parameters : Parameters, context : Context):
    
    if line.startswith("@UWZ "): return
    elif line.startswith("@File "): 
        parameters.out_file = line.replace("@File ", "").replace('\n', '').strip()
    
    elif line.startswith("@CodeStart "):
        context.code_block = True
        
    elif line.startswith("@CodeEnd "):
        context.code_block = True
    
    # Operations
    elif line.startswith("@Replace "):
        params = split_on_pipes(line.replace("@Replace ", ""))
        
        if len(params) < 2:
           log(f"Not enough parameters for @Replace, expected 2, {len(params)} provided: {params}", "Error")
           
        elif len(params) > 2:
            log(f"Too many parameters for @Replace, expected 2, {len(params)} provided: {params}", "Error")
            
        else:
            parameters.operation_stack.append(Replace(params[0], params[1]))
     
     
# Applies operations to the given line
def apply_operations(line : str, operations : list[Operation]) -> str:
    return line   


# Analyzes lines (typically coming from an input file) and executes operations on code
# Returns resulting file name and unwrapped file lines
def process(lines : list[str]) -> tuple[str, list[str]]:
    parameters = Parameters()
    context = Context()
    out_lines = []
    
    for line in lines:
        
        if context.code_block:
            out_lines.append(apply_operations(parameters.operation_stack))
        
        elif line.startswith("@"):
            parse_parameter_line(line, parameters, context)
            
    return parameters.out_file, out_lines
            


def main():
    pass


# Script entry point
if (__name__ == "__main__"):
    main()