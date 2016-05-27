# The Cypher Cossack
Michael Sarfati, May 2016

A web and RESTful front-end for the various ciphers.

# Installation
```bash
git clone git@github.com:msarfati/cypher-cossack.git
mkvirtualenv -p `which python3` -a . cypher-cossack
make install && make server
```

# Features
## Web GUI

## API
- generate-key(s) - POST: {'s': "your salt"}
    - api.cypher-cossack.org/generate-key
- encrypt(k, m) - POST: {'k': "your key", "m", "your m"}
    - api.cypher-cossack.org/{cipher}/encrypt
- decrypt(k, c)
    - api.cypher-cossack.org/{cipher}/decrypt
- list-ciphers() - Returns currently supported ciphers
    - api.cypher-cossack.org/list-ciphers
- get-cipher(name) - Returns metadata for a particular algorithm
    - api.cypher-cossack.org/get-cipher

# Dependencies
* [BOOTSTRA.386](https://github.com/kristopolous/BOOTSTRA.386)
* virtualenvwrapper
