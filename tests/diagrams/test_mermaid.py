
from pyerd.diagrams.mermaid import nodes_to_mermaid
from pyerd.model_node import ModelNode


def test_nodes_to_mermaid_no_field():
  nodes = [ModelNode(name="Test", fields={"null_field": None}, parents=[])]
  assert nodes_to_mermaid(nodes) == """
---
title: From models
---
classDiagram

    
class Test{
    
}
    """