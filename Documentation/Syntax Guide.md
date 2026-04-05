# Syntax Guide

### General

All `uwz` commands are specified in `@`-brackets: `@Command ... @`. Commands almost always have arguments, that are specified inside of backtick brackets and separated by any of the separator symbols:

```c++
@Command `Argument` `Argument` | `Argument`, `Argument` @
```

Separators are used completely interchangeably and include the following symbols:
*Space* , `:`, `;`, `,`, `|`, `-` `/`, `\n`.

#### `@UWZ version@`
This command is entirely optional, and is purely for marking purposes

#### `@File 'FileName.format' @`
This command specifies the name of an output file, that will contain unwrapped code. This name can be a relative path, but must not be an absolute path. For absolute paths use `--output` command argument. If multiple `@File ...@` commands are used, only the last one takes effect.

Example:
```cpp
@File `OutputFileName.txt` @
```

---

### Iterable Python Arguments

You can specify python-evaluated arguments using `% ... %` (instead of backtick brackets). If the specified argument is *Iterable*, this command will be applied with every element from that iterable in-place of this argument. Every element of the iterable is converted to a string. Nested iterables are not supported (inner iterables will be converted to strings). If an argument specified in `% ... %` is not iterable, it will be simple converted to a string.

Example:
```c++
@Replace `Index` : % range(10) % @
```

---

### Operations

#### `@Replace 'FindName' : 'Replace_1', 'Replace_2', ...` `
This command replaces all instances of "A" with every version of "B". 
* First argument - what needs to be replaced
* Further arguments (Second, Third, ...) - replacement options
For every replacement option a separate version of code is branched out.

Example:
```c++
@Replace `FindMe` : `ReplaceWithMe_1`, `ReplaceWithMe_1`@
```
*Note: Argument separators do not have to exactly match the ones in example.*

#### `@Table ...@`
This command unwraps a code template, branching for every parameter combination, that is specified in the table. Argument rows are separated by a new line symbol.
* First row specifies parameters, that will be replaced;
* Further rows - parameter value combinations.

Example:
```c++
@Table
`Param_1` | `Param_2` | `Param_3`
      `1` |       `2` |       `3`
      `0` |       `1` |       `2`
@
```

---

### Multiple Templates in One File

You can, just as well, specify multiple code templates in one file. 

```c++
@UWZ 1.0 @
@File `Unwrap.py` @

@Replace `FuncName` : `Func_1` , `Func_2` , `Func_3` @
@Replace `Index` : % range(10) % @

// Template one
@Template
def Temp_1_FuncName_Index():
    a = Param_4 * Param_5
    return Param_1 + Param_2 + Param_3 + a
@

// Template_2
@Template
def Temp_2_FuncName_Index():
    a = Param_4 * Param_5
    return Param_1 + Param_2 + Param_3 + a
@
```

This way both templates will have the same stack of operations applied to them.

You can add additional operations before the second template and override it's the output file.

```c++
@UWZ 1.0 @
@File `Unwrap.py` @

@Replace `FuncName` : `Func_1` , `Func_2` , `Func_3` @
@Replace `Index` : % range(10) % @

// Template one
@Template
def Temp_1_FuncName_Index():
    a = Param_4 * Param_5
    return Param_1 + Param_2 + Param_3 + a
@

@File `AnotherUnwrap.py`@ // <----
@Replace `a` : `b` , `c` @ // <---

// Template_2
@Template
def Temp_2_FuncName_Index():
    a = Param_4 * Param_5
    return Param_1 + Param_2 + Param_3 + a
@
```

This way, the first template will have 2 operations applied to it and will be written into `Unwrap.py`, while the second template will have all 3 operations applied and will be written into `AnotherUnwrap.py`.

If you want to apply different sets of operations to templates, you just need to add a `@Reset@` command in between them. Note that this will also reset the file name.

```c++
@UWZ 1.0 @
@File `Unwrap.py` @

@Replace `FuncName` : `Func_1` , `Func_2` , `Func_3` @
@Replace `Index` : % range(10) % @

// Template one
@Template
def Temp_1_FuncName_Index():
    a = Param_4 * Param_5
    return Param_1 + Param_2 + Param_3 + a
@

@Reset@ // <-----

@File `AnotherUnwrap.py`@
@Replace `a` : `b` , `c` @

// Template_2
@Template
def Temp_2_FuncName_Index():
    a = Param_4 * Param_5
    return Param_1 + Param_2 + Param_3 + a
@
```

This way, the first template will have 2 operations applied to it and will be written into `Unwrap.py`, while the second template will have only 1 operation applied and will be written into `AnotherUnwrap.py`.