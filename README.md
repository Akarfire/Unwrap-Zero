
# Unwrap Zero

A simple command prompt-based tool for explicit unwrapping of code templates. Code templates can be in any format, they just need to contain unwrap configuration information before the code block.

**Status: In Development**

---
### Example

*Following images are created using `Excalidraw` and do not represent the way the program LOOKS*.

![](Documentation/Images/Example%20Result.png)

The presented unwrapping is achieved through the following sequence of transformations:
![](Documentation/Images/Example%20Process.png)

---
### Requirements

* *Python* (Tested for python 3.9, 3.10, 3.11, 3.12, 3.13, 3.14).

---
### Usage

#### 1. Create a template file

```c++
@UWZ 1.0 @                          // Optional
@File `Example_1_uwz_unwrap.py` @   // Specifies output file name

// Replace operations replace every instance of the first argument (FuncName)
// with the following arguments, creating separate branches for every option

@Replace `FuncName` : `Func_1` , `Func_2` , `Func_3` @
@Replace `Index` : % range(10) % @  

// You can specify python arguments using %...%, if that argument is iterable,
// separate branches will be created for every element

// Table operation specifies parameter names (first line) and combinations, which
// those parameters will be replaced by. A new branch is created for every
// combination

@Table
`Param_1` | `Param_2` | `Param_3`
      `1` |       `2` |       `3`
      `0` |       `1` |       `2`
@

// Code template, which will have operations applies to it
@Template
def FuncName_Index():
    a = Param_4 * Param_5
    return Param_1 + Param_2 + Param_3 + a
@

@Reset@ // Optional, 
// used to reset configuration for multiple templates in the same template file
```

For more details see [Syntax Guide](Documentation/Syntax%20Guide.md).

#### 2. Run command on the template file

After *Installation* you will be able to run Unwrap Zero using the following command:
```Shell
unwrapz ./Input/File.format
```

Rich command example:
```Shell
unwrapz ./Input/Directory --output ./Output --format .uwz --recursive
```

**Arguments:**
1. *input* (mandatory) - relative or absolute to the file / directory with files that need to be unwrapped;
2. *--output* or *-o* (optional) - overrides file output directory (this argument is appended to the beginning of the path, specified in `@File ... @`);
3. *--format* or *-f* (optional) - specifies file formats that need to be processed in input directory;
4. *--recursive* or *-r* (optional) - enables recursive file scanning for directory inputs (files will be collected from all subdirectories).

---
### Installation

**Windows:**
* Run `Setup.bat`

**Manual installation (this is done automatically by `Setup.bat`):**
1. Create a `./Run` subdirectory;
2. In `./Run` create a `unwrapz.bat` with the following contents:
```batch
@echo off
python "Absolute:\Path\To\UnwrapZero.py" %*
```
3. Add `./Run` directory to user's `PATH`.

**For Developers:** [Development Install Guide](Documentation/Development%20Install%20Guide.md)

---
### Documentation

* [Philosophy](Documentation/Philosophy.md)
* [Features Testing](Documentation/Features%20Testing.md)
* [Code Documentation](Documentation/Code%20Documentation.md)
