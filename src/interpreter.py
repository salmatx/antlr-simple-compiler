class Interpreter:
    def __init__(self, instructions):
        self.stack = []
        self.variables = {}
        self.labels = {}
        self.instructions = instructions
        self.instruction_pointer = 0

        # Preprocess labels
        for i, instr in enumerate(instructions):
            if instr.startswith("label"):
                _, label = instr.split()
                self.labels[int(label)] = i

    def run(self):
        while self.instruction_pointer < len(self.instructions):
            instr = self.instructions[self.instruction_pointer]
            self.execute(instr)
            self.instruction_pointer += 1

    def execute(self, instr):
        parts = instr.split()
        op = parts[0]

        if op == "push":
            typ, val = parts[1], " ".join(parts[2:])
            if typ == "I":
                self.stack.append(int(val))
            elif typ == "F":
                self.stack.append(float(val))
            elif typ == "B":
                self.stack.append(val == "true")
            elif typ == "S":
                self.stack.append(val.strip('"'))
        elif op == "pop":
            self.stack.pop()
        elif op == "load":
            var = parts[1]
            self.stack.append(self.variables[var])
        elif op == "save":
            var = parts[1]
            self.variables[var] = self.stack.pop()
        elif op == "add":
            self._binary_op(parts[1], lambda x, y: x + y)
        elif op == "sub":
            self._binary_op(parts[1], lambda x, y: x - y)
        elif op == "mul":
            self._binary_op(parts[1], lambda x, y: x * y)
        elif op == "div":
            typ = parts[1]
            if typ == "I":
                self._binary_op(typ, lambda x, y: x // y)  # Integer division
            else:
                self._binary_op(typ, lambda x, y: x / y)   # Float division
        elif op == "mod":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a % b)
        elif op == "uminus":
            _ = parts[1]
            a = self.stack.pop()
            self.stack.append(-a)
        elif op == "concat":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a + b)
        elif op == "and":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a and b)
        elif op == "or":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a or b)
        elif op == "not":
            a = self.stack.pop()
            self.stack.append(not a)
        elif op == "gt":
            self._binary_op(parts[1], lambda x, y: x > y)
        elif op == "lt":
            self._binary_op(parts[1], lambda x, y: x < y)
        elif op == "eq":
            self._binary_op(parts[1], lambda x, y: x == y)
        elif op == "itof":
            val = self.stack.pop()
            self.stack.append(float(val))
        elif op == "print":
            n = int(parts[1])
            values = [self.stack.pop() for _ in range(n)][::-1]
            print(" ".join(str(v) for v in values))
        elif op == "read":
            typ = parts[1]
            raw = input().strip()
            val = {
                "I": int,
                "F": float,
                "S": str,
                "B": lambda x: x.lower() == "true"
            }[typ](raw)
            self.stack.append(val)
        elif op == "jmp":
            label = int(parts[1])
            self.instruction_pointer = self.labels[label] - 1
        elif op == "fjmp":
            label = int(parts[1])
            condition = self.stack.pop()
            if not condition:
                self.instruction_pointer = self.labels[label] - 1
        elif op == "label":
            pass

    def _binary_op(self, typ, func):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(func(a, b))
