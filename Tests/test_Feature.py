import UnwrapZero
import pytest

def test_no_operations_template():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file.py" : '''
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
def test_error_no_file_command():
    
    input = '''
    @UWZ 1.0 @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    with pytest.raises(Exception):
        UnwrapZero.Process(input)
        
    
def test_error_empty_file_command():
    
    input = '''
    @UWZ 1.0 @
    @File@
    @File @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    with pytest.raises(Exception):
        UnwrapZero.Process(input)
        
def test_error_two_arguments_in_file_command():
    
    input = '''
    @UWZ 1.0 @
    @File `File.py`, `File_2.py`@
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''

    with pytest.raises(Exception):
        UnwrapZero.Process(input)
    
    
def test_replace_error_no_arguments():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Replace@
    @Replace @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    with pytest.raises(Exception):
        UnwrapZero.Process(input)
        
        
def test_replace_error_no_replacements():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Replace `FindMe`@
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    with pytest.raises(Exception):
        UnwrapZero.Process(input)
    
    
def test_replace_one_string_argument():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Replace : `FuncName` : `Func_1` @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file.py" : '''
    def Func_1_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
def test_replace_one_iterable_argument():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Replace : `Index` : % range(2) % @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file.py" : '''
    def FuncName_0():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def FuncName_1():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
def test_replace_multiple_arguments():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Replace : `Index` : % range(2) %, `NotIndex`, `MaybeIndex` @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file.py" : '''
    def FuncName_0():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def FuncName_1():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def FuncName_NotIndex():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def FuncName_MaybeIndex():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
def test_multiple_replace_operations():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Replace : `FuncName` : `Func_1`, `Func_2` @
    @Replace : `Index` : % range(2) % @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file.py" : '''
    def Func_1_0():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def Func_1_1():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def Func_2_0():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def Func_2_1():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
def test_table_error_no_arguments():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Table @
    @Table@
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    with pytest.raises(Exception):
        UnwrapZero.Process(input)
        
        
def test_table_error_no_combinations():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Table `Param_1`, `Param_2`@
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    with pytest.raises(Exception):
        UnwrapZero.Process(input)
        
def test_table_error_incomplete_combination():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Table 
    `Param_1`, `Param_2`
    `Option_1`, `Options_2`,
    `Option_3`
    @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    with pytest.raises(Exception):
        UnwrapZero.Process(input)
        
    
def test_table_string_arguments():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Table
    `Param_1` | `Param_2` | `Param_3`
          `1` |       `2` |       `3`
          `0` |       `1` |       `2`
    @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file.py" : '''
    def FuncName_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    
    def FuncName_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
def test_table_string_and_one_iterable_arguments():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Table 
    `Param_1` | `Param_2` | `Param_3`
    `1` |       `2` |  %["cool", "iterable"]%
    `0` |       `1` |       `2`
    @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file.py" : '''
    def FuncName_Index():
        a = Param_4 * Param_5
        return 1 + 2 + cool + a
    
    def FuncName_Index():
        a = Param_4 * Param_5
        return 1 + 2 + iterable + a
    
    def FuncName_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
def test_table_string_and_two_iterable_arguments():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Table
    `Param_1` | `Param_2` | `Param_3`
          `1` |  %[8, 6]% | %["cool", "iterable"]%
          `0` |       `1` |       `2`
    @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file.py" : '''
    def FuncName_Index():
        a = Param_4 * Param_5
        return 1 + 8 + cool + a
    
    def FuncName_Index():
        a = Param_4 * Param_5
        return 1 + 6 + cool + a
    
    def FuncName_Index():
        a = Param_4 * Param_5
        return 1 + 8 + iterable + a
    
    def FuncName_Index():
        a = Param_4 * Param_5
        return 1 + 6 + iterable + a
    
    def FuncName_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    

def test_replace_and_table_arguments():
    
    input = '''
    @UWZ 1.0 @
    @File `file.py`@
    @Replace : `FuncName` : `Func_1`, `Func_2` @
    @Table
    `Param_1` | `Param_2` | `Param_3`
          `1` |       `2` |       `3`
          `0` |       `1` |       `2`
    @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file.py" : '''
    def Func_1_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    
    def Func_1_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    
    def Func_2_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    
    def Func_2_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
     
def test_uwz_syntax_in_python_comments():
    
    input = '''
    #@UWZ 1.0 @
    #@File `file.py`@
    #@Replace : `FuncName` : `Func_1`, `Func_2` @
    #@Table
    #`Param_1` | `Param_2` | `Param_3`
    #      `1` |       `2` |       `3`
    #      `0` |       `1` |       `2`
    #@
    #@Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    #@
    '''
    
    expected = {"file.py" : '''
    def Func_1_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    #
    def Func_1_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    #
    def Func_2_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    #
    def Func_2_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    #'''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
    
def test_symbols_outside_of_commands():
    
    input = '''
    @UWZ 1.0 @ // Optional
    @File `file.py`@ // Specifies output file name
    
    // Replace commands replace every instance of the first argument (FuncName)
    // with the following arguments, creating separate branches for every option
    @Replace : `FuncName` : `Func_1`, `Func_2` @
    // %...%, if that argument is iterable, separate branches will be created for 
    // every element
    
    
    // Table command specifies parameter names (first line) and combinations, which
    // those parameters will be replaced by. A new branch is created for every
    // combination
    @Table
    `Param_1` | `Param_2` | `Param_3`
          `1` |       `2` |       `3`
          `0` |       `1` |       `2`
    @
    
    // Code template, which will have commands applies to it
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file.py" : '''
    def Func_1_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    
    def Func_1_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    
    def Func_2_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    
    def Func_2_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
    
def test_multiple_templates_operation_reset():
    
    input = '''
    @UWZ 1.0 @
    @File `file_1.py`@
    @Replace : `FuncName` : `Func_1`, `Func_2` @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    
    @Reset@
    
    @File `file_2.py`@
    @Table
    `Param_1` | `Param_2` | `Param_3`
          `1` |       `2` |       `3`
          `0` |       `1` |       `2`
    @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file_1.py" : '''
    def Func_1_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def Func_2_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    ''',
    "file_2.py" : '''
    def FuncName_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    
    def FuncName_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
def test_multiple_templates_operation_reset_to_one_file():
    
    input = '''
    @UWZ 1.0 @
    @File `file_1.py`@
    @Replace : `FuncName` : `Func_1`, `Func_2` @
    @Template
    def Temp_1_FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    
    @Reset@
    @File `file_1.py`@
    
    @Table
    `Param_1` | `Param_2` | `Param_3`
          `1` |       `2` |       `3`
          `0` |       `1` |       `2`
    @
    @Template
    def Temp_2_FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file_1.py" : '''
    def Temp_1_Func_1_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def Temp_1_Func_2_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def Temp_2_FuncName_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    
    def Temp_2_FuncName_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
def test_multiple_templates_operation_expansion():
    
    input = '''
    @UWZ 1.0 @
    @File `file_1.py`@
    @Replace : `FuncName` : `Func_1`, `Func_2` @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    
    @File `file_2.py`@
    @Table
    `Param_1` | `Param_2` | `Param_3`
          `1` |       `2` |       `3`
          `0` |       `1` |       `2`
    @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file_1.py" : '''
    def Func_1_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def Func_2_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    ''',
    "file_2.py" : '''
    def Func_1_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    
    def Func_1_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    
    def Func_2_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    
    def Func_2_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct
    
    
def test_multiple_templates_operation_expansion_to_one_file():
    
    input = '''
    @UWZ 1.0 @
    @File `file_1.py`@
    @Replace : `FuncName` : `Func_1`, `Func_2` @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    
    @Table
    `Param_1` | `Param_2` | `Param_3`
          `1` |       `2` |       `3`
          `0` |       `1` |       `2`
    @
    @Template
    def FuncName_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    @
    '''
    
    expected = {"file_1.py" : '''
    def Func_1_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def Func_2_Index():
        a = Param_4 * Param_5
        return Param_1 + Param_2 + Param_3 + a
    
    def Func_1_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    
    def Func_1_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    
    def Func_2_Index():
        a = Param_4 * Param_5
        return 1 + 2 + 3 + a
    
    def Func_2_Index():
        a = Param_4 * Param_5
        return 0 + 1 + 2 + a
    '''}
    
    result = UnwrapZero.Process(input)
    
    correct = result == expected
    
    if not correct:
        print("Result: ")
        print(result)
        print("Expected: ")
        print(expected)
        
    assert correct