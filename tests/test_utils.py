
from pyerd.utils import get_classes


def test_get_classes():
  from tests.models import common
  
  classes = get_classes(common)
  assert len(classes) == 1