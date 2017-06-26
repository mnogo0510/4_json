# Prettify JSON

pprint_json.py allows to output content of json file to a console in "pretty" form

# Quickstart

You can import quadratic_eqation module into your script by:
```#!bash
import pprint_json.py
```

pprint_json.py contains two functions:
load_data(filepath) - for loading text file with json content, deserialize file to Python-object, returns Python-object
pretty_print_json(data) - for "pretty" print content into console

For "pretty" printing a content of file with json content you should invoke at first: load_data(filepath), then invoke pretty_print_json(data) where the data is a result of invokation of function load_data(filepath)

Example of using::

```#!bash
pObj = load_data(json.txt)
pretty_print_json(pObj)
```

Help:
```#!bash
pprint_json.py -h
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
