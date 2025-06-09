from antlr4 import *
from grammar.pjp_grammarLexer import pjp_grammarLexer
from grammar.pjp_grammarParser import pjp_grammarParser
from visitor import Visitor
from interpreter import Interpreter
import argparse

def main():
    parser = argparse.ArgumentParser(description='ANTLR-based stack machine compiler')
    parser.add_argument('input_file', help='Input file to compile and run')
    
    args = parser.parse_args()
    
    input_stream = FileStream(args.input_file)
    lexer = pjp_grammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    grammar_parser = pjp_grammarParser(token_stream)

    tree = grammar_parser.program()
    visitor = Visitor()
    visitor.visit(tree)
    
    if visitor.errors:
        for err in visitor.errors:
            print(err)
    else:
        for instr in visitor.instructions:
            print(instr)

        print("\n--- Running interpreter ---")
        interpreter = Interpreter(visitor.instructions)
        interpreter.run()

if __name__ == "__main__":
    main()
