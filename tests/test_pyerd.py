
import os
from pyerd import draw


def test_pyerd_draw():
  from tests import models
  draw(models)
  
def test_pyerd_draw_output():
  from tests import models
  filename = "test.md"
  draw(models, filename)
  assert os.path.exists(filename)
  os.unlink(filename)
  
def test_pyerd_union():
  from tests.models import union
  diagram = draw(union)
  assert diagram == """
---
title: From models
---
classDiagram

    
class Jack{
    str | int colors
dict | list states
bool raised
}
    """


def test_pyerd_field():
  from tests.models import field
  diagram = draw(field)
  assert diagram == """
---
title: From models
---
classDiagram

    
class Roast{
    str name
int price
}
    """
  