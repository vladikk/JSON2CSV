# JSON2CSV 

JSON2CSV is a Apache2 Licensed python based utility that converts json data to a csv file.

## Getting Started

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

### Prerequisites

Python 3.x

### Installing

pip install git+https://github.com/vladikk/JSON2CSV

## Running the tests

runtests.sh

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Vladik Khononov** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/vladikk/JSON2CSV/contributors) who participated in this project.

## License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details