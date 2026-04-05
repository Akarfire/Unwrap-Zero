#@UWZ 1.0 @
#@File `./Example_1_py_unwrap.py` @

#@Replace `FuncName` : `Func_1` , `Func_2` , `Func_3` @
#@Replace `Index` : % range(10) % @

#@Table
#`Param_1` | `Param_2` | `Param_3`
#      `1` |       `2` |       `3`
#      `0` |       `1` |       `2`
#@

#@Template
def FuncName_Index():
    a = 3 * 4
    return Param_1 + Param_2 + Param_3 + a
#@