import sys

from architecture import NUM_REG, OP_MASK, OP_SHIFT, OPS, RAM_LEN, VMState

COLUMNS = 4
DIGITS = 8


class VirtualMachineBase:
    @classmethod
    def main(cls):
        """Run a program and show the result."""
        assert len(sys.argv) == 2, f"Usage: {sys.argv[0]} program"
        with open(sys.argv[1], "r") as reader:
            lines = [ln.strip() for ln in reader.readlines()]
        program = [int(ln, 16) for ln in lines if ln]
        vm = cls()
        vm.initialize(program)
        vm.run()
        vm.show()

    # [init]
    def __init__(self, writer=sys.stdout):
        """Set up memory."""
        self.writer = writer
        self.initialize([])
        self.watching=[]
    # [/init]

    def initialize(self, program):
        """Copy the program into memory and clear everything else."""
        assert len(program) <= RAM_LEN, "Program is too long for memory"
        self.ram = [program[i] if (i < len(program)) else 0 for i in range(RAM_LEN)]
        self.ip = 0
        self.reg = [0] * NUM_REG

    # [run]
    def run(self):
        """Execute instructions one by one until the program ends."""
        self.state = VMState.RUNNING
        while self.state != VMState.FINISHED:
            addr, op, arg0, arg1 = self.fetch()
            self.execute(op, arg0, arg1)
    # [/run]

    def fetch(self):
        """Get the next instruction."""
        assert (
            0 <= self.ip < len(self.ram)
        ), f"Program counter {self.ip:06x} out of range 0..{len(self.ram):06x}"
        old_ip = self.ip
        instruction = self.ram[self.ip]
        self.ip += 1
        return (old_ip, *self.decode(instruction))

    def decode(self, instruction):
        """Decode an instruction to get an op code and its operands."""
        op = instruction & OP_MASK
        instruction >>= OP_SHIFT
        arg0 = instruction & OP_MASK
        instruction >>= OP_SHIFT
        arg1 = instruction & OP_MASK
        return op, arg0, arg1

    def execute(self, op, arg0, arg1):
        """Execute a single instruction."""
        if op == OPS["hlt"]["code"]:
            self.state = VMState.FINISHED

        elif op == OPS["ldc"]["code"]:
            self.assert_is_register(arg0)
            self.reg[arg0] = arg1

        elif op == OPS["ldr"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_register(arg1)
            self.reg[arg0] = self.ram[self.reg[arg1]]

        elif op == OPS["cpy"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_register(arg1)
            self.reg[arg0] = self.reg[arg1]

        elif op == OPS["str"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_register(arg1)
            self.assert_is_address(self.reg[arg1])
            self.ram[self.reg[arg1]] = self.reg[arg0]
            if int(self.reg[arg1]) in self.watching:
                self.write('Halting due to value change in memory address {}'.format(int(self.reg[arg1])))
                self.state = VMState.STEPPING

        elif op == OPS["add"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_register(arg1)
            self.reg[arg0] += self.reg[arg1]

        elif op == OPS["sub"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_register(arg1)
            self.reg[arg0] -= self.reg[arg1]

        elif op == OPS["beq"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_address(arg1)
            if self.reg[arg0] == 0:
                self.ip = arg1

        elif op == OPS["bne"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_address(arg1)
            if self.reg[arg0] != 0:
                self.ip = arg1

        # [prr]
        elif op == OPS["prr"]["code"]:
            self.assert_is_register(arg0)
            self.write(f"{self.reg[arg0]:06x}")
        # [/prr]

        elif op == OPS["prm"]["code"]:
            self.assert_is_register(arg0)
            self.assert_is_address(self.reg[arg0])
            self.write(f"{self.ram[self.reg[arg0]]:06x}")

        elif op == OPS["inc"]["code"]:
                self.reg[arg0] += 1
        elif op == OPS["dec"]["code"]:
            self.reg[arg0] -= 1
        elif op == OPS["swp"]["code"]:
            self.ram[self.reg[arg0]], self.ram[self.reg[arg1]] = self.ram[self.reg[arg1]], self.ram[self.reg[arg0]]

        else:
            assert False, f"Unknown op {op:06x}"

    def show(self, addresses=[]):
        """Show the IP, registers, and memory."""
        # Show IP and registers
        self.write(f"IP{' ' * 6}= {self.ip:06x}")
        for (i, r) in enumerate(self.reg):
            self.write(f"R{i:06x} = {r:06x}")

        # How much memory to show
        top = max(i for (i, m) in enumerate(self.ram) if m != 0)

        # Show memory
        base = 0
        while base <= top:
            output = f"{base:06x}: "
            for i in range(COLUMNS):
                output += f"  {self.ram[base + i]:06x}"
            self.write(output)
            base += COLUMNS

    def show_addr(self, address):
        output = f"{address:06x}: "
        output += f"  {self.ram[address]:06x}"
        self.write(output)

    def show_addrs(self, addresses):
        start = addresses[0]
        end = addresses[1]
        printed = 1
        mems = []
        for i in range(start, end+1):
            mems.append(f"{self.ram[i]:06x}")
            printed+=1
            if printed%5 == 0:
                output = f"{i-3:06x}: "
                output += '  '.join(mems)
                self.write(output)
                printed=1
                mems = []
        # print any remaining mems
        if len(mems) > 0:
            output = f"{end-len(mems)+1:06x}: "
            output += '  '.join(mems)
            self.write(output)


    def assert_is_register(self, reg):
        assert 0 <= reg < len(self.reg), f"Invalid register {reg:06x}"

    def assert_is_address(self, addr):
        assert 0 <= addr < len(self.ram), f"Invalid register {addr:06x}"

    # [write]
    def write(self, *args):
        msg = "".join(args) + "\n"
        self.writer.write(msg)
    # [/write]

if __name__ == "__main__":
    VirtualMachineBase.main()
