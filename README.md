# Requestz

*HTTP library for humans, just like Requests but better!*

Requestz is a simple HTTP library that provides an improved API over the popular Requests library.

## Installation

```
pip install requestz
```

## Usage

```python
import requestz

# Make a GET request
response = requestz.get('https://api.github.com')

# Print the response content
print(response.text)

# Make a POST request
response = requestz.post('https://httpbin.org/post', data={'key': 'value'})

# Print the JSON response
print(response.json())
```

## Features

- Simple and intuitive API
- Automatic JSON encoding and decoding
- Sessions with cookie persistence
- Advanced connection pooling
- SSL verification
- Elegant key/value cookies

## License

MIT 
