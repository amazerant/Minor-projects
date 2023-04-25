#Class methods written by Pogorzelski Krystian https://github.com/KrystianPog
#Tests written by Mazerant Adam https://github.com/amazerant

from sympy import simplify
import ast
import pytest
from hypothesis import given, settings, strategies as st
import Binary_Tree

class ExpressionTree(Binary_Tree.BinaryTree):

    def __init__(self, token: str, left=None, right=None):
        super().__init__()
        if not isinstance(token, str):
            raise TypeError('token must be string')
        self._add_root(token)
        if left is not None:
            if token not in '+-*/^':
                raise ValueError('token must be valid operator')
            self._attach(self.root_index(), left, right)

    def __repr__(self):
        return super().__str__()

    def __str__(self):
        pieces = []
        self._parenthesize_recur(self.root_index(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p: int, result: list):
        if self.is_leaf(p):
            result.append(str(self.element(p)))
        else:
            result.append('(')
            self._parenthesize_recur(self.get_left_child_pos(p), result)
            result.append(self.element(p))
            self._parenthesize_recur(self.get_right_child_pos(p), result)
            result.append(')')

    def evaluate(self):
        return self._evaluate_recur(self.root_index())

    def _evaluate_recur(self, p: int):
        if self.is_leaf(p):
            return float(self.element(p))
        else:
            op = self.element(p)
            left_val = self._evaluate_recur(self.get_left_child_pos(p))
            right_val = self._evaluate_recur(self.get_right_child_pos(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            elif op == '^':
                return left_val ** right_val
            else:
                return left_val * right_val

def recurse(node: ast.Module):
    raw = ''
    if isinstance(node, ast.BinOp):
        raw += '('
        raw += recurse(node.left)
        raw += recurse(node.op)
        raw += recurse(node.right)
        raw += ')'
    elif isinstance(node, ast.Add):
        raw += '+'
    elif isinstance(node, ast.Sub):
        raw += '-'
    elif isinstance(node, ast.Mult):
        raw += '*'
    elif isinstance(node, ast.Div):
        raw += '/'
    elif isinstance(node, ast.Pow):
        raw += '^'
    elif isinstance(node, ast.Num):
        raw += str(node.n)
    elif isinstance(node, ast.Name):
        raw += node.id
    elif isinstance(node, ast.Call):
        raw += node.func.id + '(' + recurse(node.args[0]) + ')'
    else:
        for child in ast.iter_child_nodes(node):
            raw += recurse(child)
    return raw

def tokenize(raw: str):
    raw = raw.replace('^', '**')
    raw = raw.replace('-','+(0-1)*')
    raw = ast.parse(raw)
    raw = recurse(raw)
    SYMBOLS = set('+-*/()^ ')
    mark = 0
    tokens = []
    n = len(raw)
    for j in range(n):
        if raw[j] in SYMBOLS:
            if mark != j:
                tokens.append(raw[mark:j])
            if raw[j] != ' ':
                tokens.append(raw[j])
            mark = j+1
    if mark != n:
        tokens.append(raw[mark:n])

    FUNCTIONS = ['sin', 'cos', 'tan', 'cot', 'sec', 'csc',
                 'arcsin', 'arccos', 'arctan', 'arccot', 'arcsec', 'arccsc',
                 'sinh', 'cosh', 'tanh', 'coth', 'sech', 'csch',
                 'arcsinh', 'arccosh', 'arctanh', 'arccoth', 'arcsech', 'arccsch',
                 'log', 'abs']
    for index,val in enumerate(tokens):
        if val in FUNCTIONS:
            tokens[index] += tokens[index+1]
            tokens.pop(index+1)
            stack = 1
            while stack:
                if tokens[index+1] == '(':
                    stack += 1
                if tokens[index+1] == ')':
                    stack -= 1
                tokens[index] += tokens[index+1]
                tokens.pop(index+1)
    return tokens

def build_expression_tree(tokens: list):
    S = []
    for t in tokens:
        if t in '+-*/^':
            S.append(t)
        elif t not in '()':
            S.append(ExpressionTree(t))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
    return S.pop()

def derivative(func: str, symbol: str):
    if symbol in func:
        if symbol == func:
            return 1
        elif func.startswith('sinh'):
            inside = func[5:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) * cosh({inside})')
        elif func.startswith('cosh'):
            inside = func[5:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) * sinh({inside})')
        elif func.startswith('tanh'):
            inside = func[5:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) * (sech({inside}))**2')
        elif func.startswith('coth'):
            inside = func[5:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'-({tree_derivative(inside_tree, symbol)}) * (csch({inside}))**2')
        elif func.startswith('sech'):
            inside = func[5:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'-({tree_derivative(inside_tree, symbol)}) * sech({inside}) * tanh({inside})')
        elif func.startswith('csch'):
            inside = func[5:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'-({tree_derivative(inside_tree, symbol)}) * csch({inside}) * coth({inside})')
        elif func.startswith('arcsinh'):
            inside = func[8:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) / ((({inside})**2 + 1)**(1/2))')
        elif func.startswith('arccosh'):
            inside = func[8:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) / ((({inside})**2 - 1)**(1/2))')
        elif func.startswith('arctanh'):
            inside = func[8:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) / (1 - ({inside})**2)')
        elif func.startswith('arccoth'):
            inside = func[8:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) / (1 - ({inside})**2)')
        elif func.startswith('arcsech'):
            inside = func[8:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'-({tree_derivative(inside_tree, symbol)}) / (({inside}) * (1 - ({inside})**2)**(1/2))')
        elif func.startswith('arccsch'):
            inside = func[8:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) / (abs({inside}) * (({inside})**2 + 1)**(1/2))')
        elif func.startswith('sin'):
            inside = func[4:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) * cos({inside})')
        elif func.startswith('cos'):
            inside = func[4:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'-({tree_derivative(inside_tree, symbol)}) * sin({inside})')
        elif func.startswith('tan'):
            inside = func[4:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) * (sec({inside}))**2')
        elif func.startswith('cot'):
            inside = func[4:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'-({tree_derivative(inside_tree, symbol)}) * (csc({inside}))**2')
        elif func.startswith('sec'):
            inside = func[4:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) * sec({inside}) * tan({inside})')
        elif func.startswith('csc'):
            inside = func[4:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'-({tree_derivative(inside_tree, symbol)}) * csc({inside}) * cot({inside})')
        elif func.startswith('arcsin'):
            inside = func[7:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) / (1 - ({inside})**2)**(1/2)')
        elif func.startswith('arccos'):
            inside = func[7:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'-({tree_derivative(inside_tree, symbol)}) / (1 - ({inside})**2)**(1/2)')
        elif func.startswith('arctan'):
            inside = func[7:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) / (1 + ({inside})**2)')
        elif func.startswith('arccot'):
            inside = func[7:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'-({tree_derivative(inside_tree, symbol)}) / (1 + ({inside})**2)')
        elif func.startswith('arcsec'):
            inside = func[7:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) / (abs({inside}) * (({inside})**2 - 1)**(1/2))')
        elif func.startswith('arccsc'):
            inside = func[7:-1]
            inside_tree = build_expression_tree(tokenize(inside))
            return simplify(f'-({tree_derivative(inside_tree, symbol)}) / (abs({inside}) * (({inside})**2 - 1)**(1/2))')
        elif func.startswith('abs'):
            inside = func[4:-1]
            inside_tree = build_expression_tree(tokenize(func[4:-1]))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) * ({inside} / abs({inside}))')
        elif func.startswith('log'):
            inside = func[4:-1]
            inside_tree = build_expression_tree(tokenize(func[4:-1]))
            return simplify(f'({tree_derivative(inside_tree, symbol)}) / ({inside})')
    else:
        return 0

def tree_derivative(tree: ExpressionTree, symbol: str, p = 0):
    element = tree.element(p)
    if tree.is_leaf(p):
        return derivative(element, symbol)
    else:
        deriv_left = tree_derivative(tree, symbol, tree.get_left_child_pos(p))
        deriv_right = tree_derivative(tree, symbol, tree.get_right_child_pos(p))

        if element == '+':
            expression = simplify(f'{deriv_left}+{deriv_right}')
            return expression
        if element == '-':
            expression = simplify(f'{deriv_left}-({deriv_right})')
            return expression

        left_pieces = []
        tree._parenthesize_recur(tree.get_left_child_pos(p), left_pieces)
        left = ''.join(left_pieces)
        right_pieces = []
        tree._parenthesize_recur(tree.get_right_child_pos(p), right_pieces)
        right = ''.join(right_pieces)

        if element == '*':
            expression = simplify(f'({deriv_left})*({right}) + ({left})*({deriv_right})')
            return expression
        if element == '/':
            expression = simplify(f'(({deriv_left})*({right}) - ({left})*({deriv_right}))/(({right})**2)')
            return expression
        if element == '^':
            expression = simplify(f'({left})^({right}) * ((({right})*({deriv_left}))/{left} + ({deriv_right})*log({left}))')
            return expression

@settings(deadline=None)
@given(st.integers(),st.integers(min_value=0,max_value=26))
def test_scalar(a,b):
    functions = ['1','sinh(x)','cosh(x)','tanh(x)','coth(x)','sech(x)','csch(x)','arcsinh(x)','arccosh(x)','arctanh(x)','arccoth(x)','arcsech(x)',
                'arccsch(x)','sin(x)','cos(x)','tan(x)','cot(x)','sec(x)','csc(x)','arcsin(x)','arccos(x)','arctan(x)','arccot(x)','arcsec(x)',
                'arccsc(x)','abs(x)','log(x)']

    assert str(tree_derivative(build_expression_tree(tokenize(f"{a}*{functions[b]}")),'x')) ==\
        str(simplify(f"{a}*{derivative(functions[b],'x')}"))

@settings(deadline=None)
@given(st.integers(min_value=0,max_value=26),st.integers(min_value=0,max_value=26))
def test_addition(a,b):
    functions = ['1','sinh(x)','cosh(x)','tanh(x)','coth(x)','sech(x)','csch(x)','arcsinh(x)','arccosh(x)','arctanh(x)','arccoth(x)','arcsech(x)',
                'arccsch(x)','sin(x)','cos(x)','tan(x)','cot(x)','sec(x)','csc(x)','arcsin(x)','arccos(x)','arctan(x)','arccot(x)','arcsec(x)',
                'arccsc(x)','abs(x)','log(x)']
    assert str(tree_derivative(build_expression_tree(tokenize(f"{functions[a]}+{functions[b]}")),'x')) ==\
    str(simplify(f"{derivative(functions[a],'x')} + {derivative(functions[b],'x')}"))

@settings(deadline=None)
@given(st.integers(min_value=0,max_value=26),st.integers(min_value=0,max_value=26))
def test_substraction(a,b):
    functions = ['1','sinh(x)','cosh(x)','tanh(x)','coth(x)','sech(x)','csch(x)','arcsinh(x)','arccosh(x)','arctanh(x)','arccoth(x)','arcsech(x)',
                'arccsch(x)','sin(x)','cos(x)','tan(x)','cot(x)','sec(x)','csc(x)','arcsin(x)','arccos(x)','arctan(x)','arccot(x)','arcsec(x)',
                'arccsc(x)','abs(x)','log(x)']
    assert str(tree_derivative(build_expression_tree(tokenize(f"{functions[a]}-{functions[b]}")),'x')) ==\
    str(simplify(f"{derivative(functions[a],'x')} - {derivative(functions[b],'x')}"))

@settings(deadline=None)
@given(st.integers(min_value=0,max_value=26),st.integers(min_value=0,max_value=26))
def test_multiplication(a,b):
    functions = ['1','sinh(x)','cosh(x)','tanh(x)','coth(x)','sech(x)','csch(x)','arcsinh(x)','arccosh(x)','arctanh(x)','arccoth(x)','arcsech(x)',
                'arccsch(x)','sin(x)','cos(x)','tan(x)','cot(x)','sec(x)','csc(x)','arcsin(x)','arccos(x)','arctan(x)','arccot(x)','arcsec(x)',
                'arccsc(x)','abs(x)','log(x)']
    assert str(tree_derivative(build_expression_tree(tokenize(f"{functions[a]}*{functions[b]}")),'x')) ==\
    str(simplify(f"{derivative(functions[a],'x')}*{functions[b]} + {derivative(functions[b],'x')}*{functions[a]}"))

@settings(deadline=None)
@given(st.integers(min_value=0,max_value=26),st.integers(min_value=0,max_value=26))
def test_division(a,b):
    functions = ['1','sinh(x)','cosh(x)','tanh(x)','coth(x)','sech(x)','csch(x)','arcsinh(x)','arccosh(x)','arctanh(x)','arccoth(x)','arcsech(x)',
                'arccsch(x)','sin(x)','cos(x)','tan(x)','cot(x)','sec(x)','csc(x)','arcsin(x)','arccos(x)','arctan(x)','arccot(x)','arcsec(x)',
                'arccsc(x)','abs(x)','log(x)']
    assert str(tree_derivative(build_expression_tree(tokenize(f"{functions[a]}/{functions[b]}")),'x')) ==\
    str(simplify(f"({derivative(functions[a],'x')}*{functions[b]} - {derivative(functions[b],'x')}*{functions[a]})/({functions[b]})^2"))



if __name__ == '__main__':
    pass