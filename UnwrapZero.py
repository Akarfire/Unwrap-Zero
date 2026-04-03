# UTILITY
from dataclasses import dataclass

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


# Contains a code template and all operations that need to be applied to it
@dataclass
class UnwrapTemplate:
    out_file : str
    template_code : str
    operations : list[Operation]
    

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
        super.__init__(arguments_)
        
    def execute(self, code : str) -> list[str]:
        
        if (len(self.arguments) < 2):
            log("Not enough arguments for a replace operation!", "ERROR")
        
        out_branches : list[str] = []
        
        find = self.arguments[0]
        for rep in range(1, len(self.arguments)):
            replacement = self.arguments[rep]
            
            if (is_iterable(replacement)):
                for i in replacement:
                    out_branches.append(code.replace(find, i))
                    
            else:
                out_branches.append(code.replace(find, replacement))
    

# PARSING

# Parses provided code to determine required operations and template
def Parse(code : str) -> list[UnwrapTemplate]:
    
    # Current sate
    # ...
    
    # Current token
    current_token : str = ""
       

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
        output[temp.out_file] = unwrapped[i]
        
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