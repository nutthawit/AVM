import collections


ASNode = collections.namedtuple(
    'ASTNode', ['something_1', 'something_2', 'prev_node', 'next_node'])


class AST:
    """
    The Abstract Syntax Tree use to convert user API to Set (Tree) of ASNode
    """

    pass
