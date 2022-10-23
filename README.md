# PyDebugFunc

**PyDebugFunc** é um simples decorador para te ajudar a encontrar erro de exceção nas suas funções.

**PyDebugFunc** is a simple decorator to help you find exception error in your functions.

## Installing
`pip install PyDebugFunc`
## Getting Started
```python
from PyDebugFunc import debug

@debug
def my_function(a, b):
  return a / b
my_function(10, 0)
```

### Output example

`Function error 'my_function()': division by Zero`

## Authors

* **Tiago Bandeira** - creator of the *Minha Lógica* page - [github](https://github.com/minha-logica)

See also the list of [contributors](https://github.com/minha-logica/pydebugfunc/contributors) who participated in this project.
