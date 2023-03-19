from all_blocks import block

import ast

@block("int_literal", {}, (1, 0, 0))
def int_literal(inp: dict):
    return ast.Constant(int(inp["field1"]))
