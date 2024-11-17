
import os
from pyerd import draw
from tests import models


def test_pyerd():
  draw(models)
  
def test_pyerd_output():
  filename = "test.md"
  os.unlink(filename)
  draw(models, filename)
  assert os.path.exists(filename)
  