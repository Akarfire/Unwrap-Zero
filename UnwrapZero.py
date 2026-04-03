# UTILITY
from dataclasses import dataclass, field

# Whter obj is iterable or not
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
    

# Logs some kind of message
def log(message, type):
    print(type + " : ", message)
    
    if type == "ERROR":
        raise Exception(message)


# Contains a code template and all operations that need to be applied to it
@dataclass
class UnwrapTemplate:
    out_file : str = ""
    template_code : str = ""
    operations : list[Operation] = field(default_factory=list)
    

# OPERATIONS

# Describes an operation that needs to be applied to a code template
class Operation:
    def __init__(self, arguments_ : list[any]):
        self.arguments = arguments_
    
    # Override this method to add operation logic
    def execute(self, code : str) -> list[str]:
        return []

# OPERATION : REPLACE

# Replaces all instances of "A" with every version of "B"
class Replace(Operation):
    def __init__(self, arguments_):
        super().__init__(arguments_)
        
    def execute(self, code : str) -> list[str]:
        
        if (len(self.arguments) < 2):
            log("Not enough arguments for a replace operation!", "ERROR")
        
        out_branches : list[str] = []
        
        find = self.arguments[0]
        for rep in range(1, len(self.arguments)):
            replacement = self.arguments[rep]

            if (type(replacement) != str and is_iterable(replacement)):
                for i in replacement:
                    out_branches.append(code.replace(find, str(i)))
                    
            else:
                out_branches.append(code.replace(find, replacement))
                
        return out_branches
    

# PARSING

# If c is a separator sybmol
def is_separator(c : str) -> bool:
    return c in " :;,|-/\n"
    

# Parses provided code to determine required operations and template
def Parse(code : str) -> list[UnwrapTemplate]:
    
    result : list[UnwrapTemplate] = []
    
    currentTepmplate = UnwrapTemplate()
    
    # Current sate
    is_command : bool = False
    is_command_name : bool = False
    is_literal : bool = False
    is_pyargument : bool = False
    is_template : bool = False
    is_special : bool = False
    
    command_name = ""
    current_arguments = []
    # ...
    
    # Current token
    current_token : str = ""
    
    # Parsing loop
    for c in code:
        
        if c == '\\': is_special = True
        
        if c == '@' and not is_special and not is_literal and not is_pyargument: 
            
            is_command = not is_command
            if (is_command):
                is_command_name = True
                
            elif is_template:
                # print(command_name)
                # print(current_token)
                currentTepmplate.template_code = current_token
                is_template = False
                
                # Appending result
                result.append(currentTepmplate)
                
                current_token = ""
                
            else:
                current_token = ""
                # Command words resolving
                
                if command_name == "UWZ": current_arguments = [] 
                
                elif command_name == "File":
                    currentTepmplate.out_file = current_arguments[0]
                    current_arguments = []
                    
                elif command_name == "Reset":
                    currentTepmplate = UnwrapTemplate()
                    current_arguments = []
                    
                # OPERATION CREATION
                # @Replace ... @ opertion
                elif command_name == "Replace":
                    currentTepmplate.operations.append(Replace(current_arguments))
                    current_arguments = []
                    
                else:
                    current_arguments = []
                                    
                
        elif c == '`' and not is_special and not is_pyargument:
            is_literal = not is_literal
            if not is_literal:
                current_arguments.append(current_token)
                current_token = ""
                
        elif c == '%' and not is_special and not is_literal:
            is_pyargument = not is_pyargument
            if not is_pyargument:
                pyarg = eval(current_token)
                current_arguments.append(pyarg)
                current_token = ""
        
        elif is_separator(c) and not (is_literal or is_pyargument or is_template) and not is_special:
            if is_command_name:
                is_command_name = False
                command_name = current_token
                current_token = ""
                
                if command_name == "Template":
                    is_template = True
                    current_token += c
        
        else:
            current_token += c
            is_special = False
        
    return result
       

# UNWRAPPING
            
# Sequentially branches code and applies operations, described in templates 
def Unwrap(templates : list[UnwrapTemplate]) -> list[list[str]]:
    results : list[list[str]] = []
    
    for temp in templates:
        cache : list[list[str]] = []
        cache.append([temp.template_code])
        
        for op in temp.operations:
            cache.append([])
            for code in cache[-2]:
                for branch in op.execute(code):
                    cache[-1].append(branch)
                    
        results.append(cache[-1])
        
    return results


# PACKING

# Takes unwrapped templates and packs them into a strings, that will later be written to files
def Pack(unwrapped : list[list[str]], templates : list[UnwrapTemplate]) -> dict[str : str]:
    output : dict[str : str] = {}
    
    for i, temp in enumerate(templates):
        compilation = ""
        for s in unwrapped[i]:
            compilation += s
        
        output[temp.out_file] = compilation
        
    return output


# PROCESSING

# Processes concatenated code and unwraps templates based on instructions found in it 
def Process(code : str) -> dict[str : str]:
    templates : list[UnwrapTemplate] = Parse(code)
    unwrapped : list[list[str]] = Unwrap(templates)
    return Pack(unwrapped, templates)
    


# Run script
def main():
    pass

# Script entry point
if (__name__ == "__main__"):
    main()