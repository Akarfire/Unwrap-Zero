# Feature List

### Unwrap Zero Script

- [x] Can unwrap a template with NO operations
- [x] Can unwrap a template with ONE operation:
	- [x] Replace operation:
		- [x] No arguments -> error
		- [x] No replacement values -> error
		- [x] One string replacements
		- [x] One `iterable` replacement
		- [x] Multiple replacements
	- [x] Table operation:
		- [x] No arguments -> error
		- [x] No combinations -> error
		- [x] Invalid row length -> error
		- [x]  String arguments
		- [x] `Iterable` arguments
- [x] Can unwrap a template with multiple operations
- [x] Can unwrap multiple templates in one file

---
### Command Usage

* [x] Setup script works on Windows
* [ ] #Missing Setup script works on Linux
* [x] Can call using a simple name on Windows
* [ ] #Missing Can call using a simple name on Linux
* [x] Can specify a file as an input
* [x] Can specify a directory as an input
* [x] Recursive scan input directory option
* [x] Can specify custom output directory
* [x] Can specify file format for directory inputs