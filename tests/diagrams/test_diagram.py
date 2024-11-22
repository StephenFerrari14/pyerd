
import pytest
from pyerd import get_nodes_for_classes
from pyerd.diagrams.diagram import Diagram, DiagramType
from pyerd.utils import get_classes
from tests import models


def test_mermaid_diagram():
    
    classes = get_classes(models)
    nodes = get_nodes_for_classes(classes)

    generator = Diagram(DiagramType.MERMAID)
    mermaid_diagram = generator.generate_diagram(nodes)
    assert mermaid_diagram == """
---
title: From models
---
classDiagram
BaseDonut <|-- Donut
Donut <|-- Glazed
HousePlant *-- User
BasePlant <|-- HousePlant
    
class BaseDonut{
    int id
}

class BasePlant{
    int id
str type
}

class Donut{
    str name
}

class Glazed{
    bool glazed
str sprinkles
int | str topping
}

class HousePlant{
    str house_name
User owner
}

class User{
    int id
str username
}
    """
    
def test_no_diagram_type():
  with pytest.raises(ValueError):
    generator = Diagram("Not A Diagram") # pyright: ignore reportArgumentType
    generator.generate_diagram([])