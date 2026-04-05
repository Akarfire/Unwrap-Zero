
# Input

```c++
@UWZ 1.0 @
@File `ExampleUnwrap.py` @

@Replace `FuncName` : `Func` , `cnuF` @

@Table
`ID` | `A` | `B`
`1`  | `1` | `3`
`2`  |`"unwrap"` | `"example"`
@

@Template
def FuncName_ID():
    return A + B
@
```

# Output

```python
def Func_1():
    return 1 + 3

def Func_2():
    return "unwrap" + "example"

def cnuF_1():
    return 1 + 3
    
def cnuF_2():
    return "unwrap" + "example"
```

