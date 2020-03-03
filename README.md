# Meet the FAKE IT project which provide generating simple fake data

-----

## INSTALL:
- python setup.py install
- pip install fakeit
- pip install git+https://github.com/RCheese/fakeit

## USAGE:
Generating fake data for python types

### Bytes
```python
    >>> from fakeit import bytes
    >>> bytes.fake_bytes(min_length=2, max_length=5)
    ... b'/\xf5Q\x9a\xcd'
    
    >>> bytes.fake_b64(min_length=2, max_length=5)
    ... b'QpwJug=='
```

### Hashes
```python
    >>> from fakeit import hashes
    >>> hashes.fake_md5()
    ... '37c6c63ee4dd8516d3d8ee4319b3e7b8'
    >>> hashes.fake_sha256()
    ... 'bc6c64d150e869cf10e3d9c0cf582fa78fe46282de75911b464c46a023a08038'
```

### Numerics
```python
    >>> from fakeit import numerics
    >>> numerics.fake_complex(1,2,3,4)
    ... (1.2157335093960198+3.17909803327301j)
    >>> numerics.fake_complex(1,2,3,4, round=True)
    ... (2+4j)
    >>> numerics.fake_int(1 ,20)
    ... 11
    >>> numerics.fake_float(1, 20)
    ... 3.448023122876366
```

### Strings
```python
    >>> from fakeit import strings
    >>> strings.fake_string(min_length=5, max_length=5)
    ... 'CPOcO'
    
    >>> fake_string(min_length=5, max_length=5, unique=True)
    ... 'qEiwW'
    
    >>> fake_string(min_length=5, max_length=5, alphabet="ABCdE")
    ... 'EdBdB'
    
    >>> fake_strings(5)
    ... <generator object fake_strings at 0x7f67579e4660>
    
    >>> for i in fake_strings(5):
    >>>     print(i)
    >>>
    ... 1r3OxTKis20KF
    ... 
    ... 3YN28kOPLuc
    ... DaLQ
    ... j7J9MMJcF2
    
    >>> for i in all_combinations_with_replacement_fake_string(min_length=3, max_length=3, alphabet="abc"):
    >>>     print(i)
    ... aaa
    ... aab
    ... aac
    ... abb
    ... abc
    ... acc
    ... bbb
    ... bbc
    ... bcc
    ... ccc
```

### Personal
``
```python
    >>> from fakeit import personal
    >>> personal.names.fake_fullname()
    ... 'Justin Hall'
    >>> personal.names.fake_name()
    ... 'Johnny'
    >>> personal.names.fake_surname()
    ... 'Gill'
    
    >>> personal.phones.fake_international()
    ... '+67-910-8211582'
    >>> personal.phones.fake_international(mediator="")
    ... '+974665503991'
    >>> fake_international(country_code=7, area_code=923)
    ... '+7-923-4915850'
    
    >>> personal.emails.fake_email()
    ... '0mfJz0QD@VqujvpRDiuMfuyB.VRQfn'
    >>> personal.emails.fake_enough_email()
    ... 'Henry.Hill@google.cn'
    
    >>> personal.fake_person()
    ... <Person Stephen Robertson> (FirstName=Stephen, LastName=Robertson, Email=Stephen.Robertson@whatsapp.net, Phone=+1-990-5674435)
```

## TODO:

- Geo
    - Position
    - Named (Country, City, and etc.)
    - Address
- Text data
- Tables
    - ?
- Unit tests
- SQLAlchemy type casting
- Django type casting
- Sphinx docs
- CI
- Compilation request

<a href="https://www.buymeacoffee.com/RussianCheese" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/arial-violet.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>
