# The Cypher Cossack
Michael Sarfati, 2016

A web and RESTful front-end for the various ciphers.

# Features
## Web GUI

## RESTful API
- generate-key(s) - POST: {'s': "your salt"}
    - api.cutlass.org/generate-key
- encipher(k, m) - POST: {'k': "your key", "m", "your m"} 
    - api.cutlass.org/{cipher}/encipher
- decipher(k, c)
    - api.cutlass.org/{cipher}/decipher
- list-ciphers() - Displays currently supported ciphers
    - api.cutlass.org/list-ciphers
- get-cipher(id) - Displays pseudocode for generation of a particular algorithm
    - api.cutlass.org/get-cipher

# Dependencies
* [BOOTSTRA.386](https://github.com/kristopolous/BOOTSTRA.386)
* 