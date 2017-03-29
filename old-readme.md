JSON2CSV v1.0
=============

JSON2CSV is a Apache2 Licensed python based utility that converts json data to a csv file.

Usage
-----

```
python json2csv.py "input_file.json" "output_file.csv"
```

If you pass in the following json file:
``` json
[
    {
        "id": 1,
        "name": {
            "first": "john",
            "last": "johnson"
        },
        "age": 27,
        "languages": [ "c#", "vb", "python" ]
     },
     {
        "id": 2,
        "name": {
            "first": "scott",
            "middle": "scottster",
            "last": "scottson"
        },
        "age": 29,
        "languages": [ "objective-c", "c++" ]
     }
]
```

You'll get the following csv file:
```
age ,id ,languages_0    ,languages_1        ,languages_2        ,name_first ,name_last  ,name_middle
27  ,1  ,c#             ,vb                 ,python             ,john       ,johnson    ,
29  ,2  ,objective-c    ,c++                ,                   ,scott      ,scottson   ,scottster
```