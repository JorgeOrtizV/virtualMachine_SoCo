import sys

# Import the OPS dictionary and other constants from architecture.py
sys.path.append('../vm')
from architecture import OPS, OP_MASK, OP_SHIFT

def disassemble_instruction(instruction):
    """Disassemble a single instruction into assembly language."""
    op = instruction & OP_MASK
    instruction >>= OP_SHIFT
    arg0 = instruction & OP_MASK
    instruction >>= OP_SHIFT
    arg1 = instruction & OP_MASK

    for mnem, op_info in OPS.items():
        if op_info["code"] == op:
            format_str = op_info["fmt"]
            if format_str == "--":
                return f"{mnem}"
            elif format_str == "rv":
                return f"{mnem} R{arg0} {arg1}"
            elif format_str == "rr":
                return f"{mnem} R{arg0} R{arg1}"
            elif format_str == "r-":
                return f"{mnem} R{arg0}"
    return "UNKNOWN"

def disassemble_file(input_file, output_file):
    """Disassemble a .mx file into a .as file."""
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            line = line.strip()
            if line:
                instruction = int(line, 16)
                assembly_line = disassemble_instruction(instruction)
                fout.write(assembly_line + "\n")
def main():
    assert len(sys.argv) == 3, f"Usage: python {sys.argv[0]} input_file.mx output_file.as"
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    disassemble_file(input_file, output_file)

if __name__ == "__main__":
    main()
