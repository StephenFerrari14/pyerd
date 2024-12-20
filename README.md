# Pyerd
Pyre - d

Generate ERDs from Pydantic models

Supports Mermaid

## Installation

> pip install pyerd

## Usage

Create a python module that imports all the models you want to generate a diagram for.

Ex.
models.py
```
from models.common import *
from models.donuts import *
from models.plants import *
```

Import the module and call draw()
```
from pyerd import draw

# single module
from package.models import donuts
draw(donuts, "output.md")

# multiple models
from package import models

draw(models, "output.md")
```

### Generate Image
For mermaid images you can use the mermaid cli to turn the output of pyerd into an image
```
npm install -g @mermaid-js/mermaid-cli
mmdc -i output.md -o output.png -t dark -b transparent
```

## Development

```
ruff check pyerd
pyright pyerd
```

### Tests

```
poetry run pytest --cov=pyerd tests/
```
For coverage report
```
poetry run pytest --cov=pyerd --cov-report html tests/
```


## Future Features
Generate from single class
Generate from dataclass class  
Generate from SQLModel class  
Generate PlantUML diagram for supported classes  