# config

## add key to config

- add_any
    - key any : value any
- add_string
    - key string : value string
- add_int
    - key int : value int
- add_float
    - key float : value float
- add_bool
    - key bool : value bool
- add_default
  - default value,if key not exist,add key and value
    dict: ``` {
    key1 : value1
    key2 : value2 ...
    }``` 

- add_const
  - default value,if key not exist or value is not equal to default value,add key and value
    dict: ``` {
    key1 : value1
    key2 : value2 ...
    }```  

## save config
- object.save
  - save config to file
  - 
## load config
- object.load
  - load config from file