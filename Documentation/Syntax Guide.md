# Syntax Guide

### General

All `uwz` commands are specified in `@`-brackets: `@Command ... @`. Commands almost always have arguments, that are separated by any of the separator symbols and specified in the following manner:

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
@File `Example_1_uwz_1_unwrap.py` @

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