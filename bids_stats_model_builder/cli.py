"""
CLI tool to build bids-stats-models.

Parses stats model schema and recursively descends its structure to generate user prompts to populate a model
"""
    
import json
import pkg_resources

import jsonschema
from prompt_toolkit import PromptSession, prompt
from prompt_toolkit.shortcuts import confirm

schema_file = pkg_resources.resource_filename(__name__, "schema.json")
with open(schema_file) as fp:
    schema = json.load(fp)

validator = jsonschema.Draft7Validator(schema=schema)

prompt_list = [u"boolean", u"integer", u"number", u"string"]

# for testing set to false and the key value will be used instead of user input
PROMPT = False

def basic_prompt(key, value, store):
    if PROMPT:
        store[key] = prompt(f"{key} > ")
    else:
        store[key] = key

def array_prompt(key, value, store):
    """
    Add as many elements to array as user wants.
    Arrays items property can be an object, most often containing a straightforward type, or an anyOf/oneOf object.
    or they can be an array of acceptable types. 
    """
    store[key] = []
    while confirm(f"do you want to add a {key}?"):
        if type(value.get("items")) is dict:
            store[key].append(schema_prompt(key, value["items"], {}))
        elif type(value.get("items")) is array:
            store[key].append(schema_prompt(key, value["items"][0], {}))
    return store

def dict_prompt(key, value, store):
    """
    Try and figure out how to prompt for an object in the schema based on available keys.
    Currently only promting for first type listed in 'anyOf' or 'oneOf' entries.
    """
    print(f"key: {key}")
    if value.get("type") == "object" and value.get("properties"):
        store[key] = {}
        for sub_key in value["properties"]:
            store[key].update(schema_prompt(sub_key, value["properties"][sub_key], {}))
    elif value.get("type") in prompt_list:
        basic_prompt(key, value, store)
    elif value.get("type") == "array":
        array_prompt(key, value, store)
    elif type(value) is dict and "$ref" in value.keys():
        de_ref = validator.resolver.resolve(value["$ref"])
        schema_prompt(key, de_ref[1], store)
    elif type(value) is dict and "anyOf" in value.keys():
        schema_prompt(key, value["anyOf"][0], store)   
    elif type(value) is dict and "oneOf" in value.keys():
        schema_prompt(key, value["oneOf"][0], store)   
    else:
        print(f"uncaught key/value {key}  -   {value}")
    return store

def schema_prompt(key, value, store):
    """
    Maps pythonic type values of what we see in the schema to approprate handler.
    """
    if (type(value) is dict):
        dict_prompt(key, value, store)
    elif (type(value) is str):
        basic_prompt(key, value, store)
    elif (type(value) is list):
        array_prompt(key, value, store)
    return store

def main():
    store = {}
    schema_prompt("root", schema, store)
    print(store)

if __name__ == '__main__':
    main()
