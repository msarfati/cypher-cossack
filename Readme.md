# The Cypher Cossack
Michael Sarfati, 2016

A web and RESTful front-end for the various ciphers.

# Features
## Web GUI

## RESTful API
- generate-key(s) - POST: {'s': "your salt"}
    - api.cypher-cossack.org/generate-key
- encipher(k, m) - POST: {'k': "your key", "m", "your m"}
    - api.cypher-cossack.org/{cipher}/encrypt
- decipher(k, c)
    - api.cypher-cossack.org/{cipher}/decrypt
- list-ciphers() - Returns currently supported ciphers
    - api.cypher-cossack.org/list-ciphers
- get-cipher(id) - Returns metadata for a particular algorithm
    - api.cypher-cossack.org/get-cipher

# Dependencies
* [BOOTSTRA.386](https://github.com/kristopolous/BOOTSTRA.386)
* 