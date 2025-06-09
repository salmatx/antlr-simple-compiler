from grammar.pjp_grammarVisitor import pjp_grammarVisitor
from grammar.pjp_grammarParser import pjp_grammarParser

class Visitor(pjp_grammarVisitor):
    def __init__(self):
        super().__init__()
        self.instructions = []
        self.variables = set()
        self.var_types = {}
        self.label_counter = 0
        self.errors = []
        
    def error(self, message, ctx):
        line = ctx.start.line
        self.errors.append(f"[Line {line}] Semantic error: {message}")

    def get_next_label(self):
        label = self.label_counter
        self.label_counter += 1
        return label

    def visitProgram(self, ctx: pjp_grammarParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitEmptyStmt(self, ctx: pjp_grammarParser.EmptyStmtContext):
        return None

    def visitVarDecl(self, ctx: pjp_grammarParser.VarDeclContext):
        type_name = ctx.TYPE().getText()
        var_list = [var.getText() for var in ctx.VAR()]

        for var in var_list:
            if var in self.variables:
                self.error(f"Variable '{var}' already declared", ctx)
                return None
            self.variables.add(var)
            self.var_types[var] = type_name

            if type_name == 'int':
                self.instructions.append('push I 0')
            elif type_name == 'float':
                self.instructions.append('push F 0.0')
            elif type_name == 'bool':
                self.instructions.append('push B false')
            elif type_name == 'string':
                self.instructions.append('push S ""')

            self.instructions.append(f'save {var}')
        return None

    def visitExprStmt(self, ctx: pjp_grammarParser.ExprStmtContext):
        result = self.visit(ctx.expression())
        if result is not None:
            self.instructions.append('pop')
        return None

    def visitReadStmt(self, ctx: pjp_grammarParser.ReadStmtContext):
        var_names = [var.getText() for var in ctx.VAR()]
        
        for var in var_names:
            if var not in self.var_types:
                self.error(f"Cannot read into undeclared variable '{var}'", ctx)
                continue
                
            typ = self.var_types.get(var, 'int')
            read_instr = {
                'int': 'read I',
                'float': 'read F',
                'bool': 'read B',
                'string': 'read S'
            }.get(typ, 'read I')
            self.instructions.append(read_instr)
            self.instructions.append(f'save {var}')
        return None

    def visitWriteStmt(self, ctx: pjp_grammarParser.WriteStmtContext):
        exprs = ctx.expression()
        valid_exprs = 0
        
        for expr in exprs:
            result = self.visit(expr)
            if result is not None:
                valid_exprs += 1
        
        if valid_exprs > 0:
            self.instructions.append(f'print {valid_exprs}')
        return None

    def visitAssignExpr(self, ctx: pjp_grammarParser.AssignExprContext):
        var_name = ctx.VAR().getText()
        
        var_type = self.var_types.get(var_name)
        if var_type is None:
            self.error(f"Assignment to undeclared variable '{var_name}'", ctx)
            return None
        
        expr_type = self.visit(ctx.expression())
        if expr_type is None:
            return None
        
        if var_type == 'int' and expr_type == 'float':
            self.error(f"Cannot assign float to int variable '{var_name}'", ctx)
            return None
        
        if var_type == 'float' and expr_type == 'int':
            self.instructions.append('itof')
        
        self.instructions.append(f'save {var_name}')
        self.instructions.append(f'load {var_name}')
        return var_type

    def _visitAndPromote(self, leftCtx, rightCtx):
        left_type = self.visit(leftCtx)
        right_type = self.visit(rightCtx)

        if left_type == 'int' and right_type == 'float':
            self.instructions.insert(-1, 'itof')
            return 'float'
        elif left_type == 'float' and right_type == 'int':
            self.instructions.append('itof')
            return 'float'
        elif left_type == right_type:
            return left_type
        return 'int'

    def visitOrExpr(self, ctx: pjp_grammarParser.OrExprContext):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        self.instructions.append('or')
        return 'bool'

    def visitAndExpr(self, ctx: pjp_grammarParser.AndExprContext):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        self.instructions.append('and')
        return 'bool'

    def visitEqExpr(self, ctx: pjp_grammarParser.EqExprContext):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        
        if left_type is None or right_type is None:
            return 'bool'  # Return bool even on error to continue execution
        
        # Handle type promotion for comparisons
        if left_type == 'int' and right_type == 'float':
            # Need to convert the left operand (second on stack)
            self.instructions.insert(-1, 'itof')
            result_type = 'F'
        elif left_type == 'float' and right_type == 'int':
            # Convert the right operand (top of stack)
            self.instructions.append('itof')
            result_type = 'F'
        elif left_type == right_type:
            if left_type == 'float':
                result_type = 'F'
            elif left_type == 'string':
                result_type = 'S'
            else:
                result_type = 'I'
        else:
            result_type = 'I'
        
        op = ctx.op.text
        if op == '==':
            self.instructions.append(f'eq {result_type}')
        else:  # !=
            self.instructions.append(f'eq {result_type}')
            self.instructions.append('not')
        return 'bool'

    def visitRelExpr(self, ctx: pjp_grammarParser.RelExprContext):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        
        if left_type is None or right_type is None:
            return 'bool'  # Return bool even on error to continue execution
        
        # Handle type promotion for relational comparisons
        if left_type == 'int' and right_type == 'float':
            self.instructions.insert(-1, 'itof')
            result_type = 'F'
        elif left_type == 'float' and right_type == 'int':
            self.instructions.append('itof')
            result_type = 'F'
        elif left_type == 'float':
            result_type = 'F'
        else:
            result_type = 'I'
    
        op = ctx.op.text
        self.instructions.append(f'lt {result_type}' if op == '<' else f'gt {result_type}')
        return 'bool'

    def visitAddExpr(self, ctx: pjp_grammarParser.AddExprContext):
        op = ctx.op.text
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        
        if left_type is None or right_type is None:
            return None
        
        if left_type == 'string' or right_type == 'string':
            self.error("Addition operator (+/-) cannot be used with strings", ctx)
            return None
        
        if left_type == 'int' and right_type == 'float':
            self.instructions.insert(-1, 'itof')
            result_type = 'float'
        elif left_type == 'float' and right_type == 'int':
            self.instructions.append('itof')
            result_type = 'float'
        elif left_type == right_type:
            result_type = left_type
        else:
            result_type = 'int'
    
        self.instructions.append(f'add {"F" if result_type == "float" else "I"}' if op == '+' else f'sub {"F" if result_type == "float" else "I"}')
        return result_type

    def visitMulExpr(self, ctx: pjp_grammarParser.MulExprContext):
        op = ctx.op.text
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        
        if left_type is None or right_type is None:
            return None
        
        # For division, handle integer division vs float division
        if op == '/':
            if left_type == 'int' and right_type == 'int':
                # Integer division - result is int
                self.instructions.append('div I')
                return 'int'
            else:
                # At least one operand is float - promote and return float
                if left_type == 'int':
                    self.instructions.insert(-1, 'itof')
                elif right_type == 'int':
                    self.instructions.append('itof')
                self.instructions.append('div F')
                return 'float'
        else:  # Multiplication
            if left_type == 'int' and right_type == 'float':
                self.instructions.insert(-1, 'itof')
                result_type = 'float'
            elif left_type == 'float' and right_type == 'int':
                self.instructions.append('itof')
                result_type = 'float'
            elif left_type == right_type:
                result_type = left_type
            else:
                result_type = 'int'
            
            self.instructions.append(f'mul {"F" if result_type == "float" else "I"}')
            return result_type

    def visitNotExpr(self, ctx: pjp_grammarParser.NotExprContext):
        expr_type = self.visit(ctx.expression())
        if expr_type is None:
            return 'bool'  # Return bool even on error
        self.instructions.append('not')
        return 'bool'

    def visitNegExpr(self, ctx: pjp_grammarParser.NegExprContext):
        typ = self.visit(ctx.expression())
        if typ is None:
            return 'int'
        self.instructions.append(f'uminus {"F" if typ == "float" else "I"}')
        return typ

    def visitParensExpr(self, ctx: pjp_grammarParser.ParensExprContext):
        return self.visit(ctx.expression())

    def visitLiteralExpr(self, ctx: pjp_grammarParser.LiteralExprContext):
        lit = ctx.literal()
        if lit.INT():
            self.instructions.append(f'push I {lit.INT().getText()}')
            return 'int'
        elif lit.FLOAT():
            self.instructions.append(f'push F {lit.FLOAT().getText()}')
            return 'float'
        elif lit.BOOL():
            self.instructions.append(f'push B {lit.BOOL().getText()}')
            return 'bool'
        elif lit.STRING():
            value = lit.STRING().getText()[1:-1]
            self.instructions.append(f'push S "{value}"')
            return 'string'

    def visitVarExpr(self, ctx: pjp_grammarParser.VarExprContext):
        var_name = ctx.VAR().getText()
        if var_name not in self.var_types:
            self.error(f"Use of undeclared variable '{var_name}'", ctx)
            return None
        self.instructions.append(f'load {var_name}')
        return self.var_types.get(var_name)

    def visitBlockStmt(self, ctx: pjp_grammarParser.BlockStmtContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitIfStmt(self, ctx: pjp_grammarParser.IfStmtContext):
        self.visit(ctx.condition())  # Evaluate condition
        
        else_label = self.get_next_label()
        end_label = self.get_next_label()
        
        self.instructions.append(f'fjmp {else_label}')  # Jump to else if condition is false
        
        # Then branch
        self.visit(ctx.statement(0))
        
        if ctx.statement(1):  # Has else branch
            self.instructions.append(f'jmp {end_label}')  # Jump to end after then branch
            self.instructions.append(f'label {else_label}')
            self.visit(ctx.statement(1))  # Else branch
            self.instructions.append(f'label {end_label}')
        else:
            # Even without else, we need the jump and labels for proper control flow
            self.instructions.append(f'jmp {end_label}')
            self.instructions.append(f'label {else_label}')
            self.instructions.append(f'label {end_label}')
        
        return None

    def visitWhileStmt(self, ctx: pjp_grammarParser.WhileStmtContext):
        loop_start = self.get_next_label()
        loop_end = self.get_next_label()
        
        self.instructions.append(f'label {loop_start}')
        self.visit(ctx.condition())  # Evaluate condition
        self.instructions.append(f'fjmp {loop_end}')  # Jump to end if condition is false
        
        self.visit(ctx.statement())  # Loop body
        
        self.instructions.append(f'jmp {loop_start}')  # Jump back to condition
        self.instructions.append(f'label {loop_end}')
        
        return None
    
    def visitMuduloExpr(self, ctx: pjp_grammarParser.MuduloExprContext):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        
        if left_type is None or right_type is None:
            return None
        
        if left_type == 'float' or right_type == 'float':
            self.error("Modulo operator (%) cannot be used with floats", ctx)
            return None
        
        if left_type == 'int' and right_type == 'int':
            self.instructions.append('mod')
            return 'int'
        else:
            self.error("Modulo operator (%) can be used with only with int", ctx)
            return None
    
    def visitConcatExpr(self, ctx: pjp_grammarParser.ConcatExprContext):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        
        if left_type is None or right_type is None:
            return None
    
        if left_type != 'string' or right_type != 'string':
            self.error("Concatenation operator (.) requires both operands to be strings", ctx)
            return None
        
        self.instructions.append('concat')
        return 'string'
        
    def visitTernaryExpr(self, ctx: pjp_grammarParser.TernaryExprContext):
        # condition ? true_expr : false_expr
        cond_type = self.visit(ctx.expression(0))  # condition
        if cond_type is None:
            return 'int'  # Default fallback
        
        else_label = self.get_next_label()
        end_label = self.get_next_label()
        
        self.instructions.append(f'fjmp {else_label}')  # Jump to false expr if condition is false
        
        # True expression
        true_type = self.visit(ctx.expression(1))
        if true_type is None:
            true_type = 'int'  # Default fallback
        self.instructions.append(f'jmp {end_label}')
        
        # False expression
        self.instructions.append(f'label {else_label}')
        false_type = self.visit(ctx.expression(2))
        if false_type is None:
            false_type = 'int'  # Default fallback
        
        self.instructions.append(f'label {end_label}')
        
        # Return type should be the promoted type of both branches
        if true_type == false_type:
            return true_type
        elif (true_type == 'int' and false_type == 'float') or (true_type == 'float' and false_type == 'int'):
            return 'float'
        else:
            return 'int'  # Default fallback
    
    def visitBoolCondition(self, ctx: pjp_grammarParser.BoolConditionContext):
        return self.visit(ctx.expression())
    
    def visitDoWhileStmt(self, ctx: pjp_grammarParser.DoWhileStmtContext):
        loop_start = self.get_next_label()
        loop_end = self.get_next_label()
        
        self.instructions.append(f'label {loop_start}')
        
        self.visit(ctx.statement())  # Loop body
        
        self.visit(ctx.condition())  # Evaluate condition
        self.instructions.append(f'fjmp {loop_end}')  # Jump to end if condition is false
        self.instructions.append(f'jmp {loop_start}')  # Jump back to start
        
        self.instructions.append(f'label {loop_end}')
        
        return None
    
    def visitForStmt(self, ctx: pjp_grammarParser.ForStmtContext):
        loop_start = self.get_next_label()
        loop_end = self.get_next_label()
        
        # Initialization
        self.visit(ctx.expression(0))
        self.instructions.append('pop')  # Discard result
        
        self.instructions.append(f'label {loop_start}')
        
        # Condition
        self.visit(ctx.condition())
        self.instructions.append(f'fjmp {loop_end}')
        
        # Loop body
        self.visit(ctx.statement())
        
        # Update expression
        self.visit(ctx.expression(1))
        self.instructions.append('pop')  # Discard result
        
        self.instructions.append(f'jmp {loop_start}')
        self.instructions.append(f'label {loop_end}')
        
        return None
