
import ast
import pprint
import dis

source_code = """
def greet(name):
    print(f"Hello, {name}!")
"""

# Parse the code into an AST
parsed_ast = ast.parse(source_code)

# Pretty-print the AST structure
pprint.pprint(ast.dump(parsed_ast, indent=4))



# Compile the source code into a code object
code_object = compile(source_code, filename="<string>", mode="exec")

# Disassemble the bytecode
dis.dis(code_object)

