import sys

# Import the OPS dictionary and other constants from architecture.py
from architecture import OPS, OP_MASK, OP_SHIFT

def disassemble_instruction(instruction):
    """Disassemble a single instruction into assembly language."""
    # Your existing implementation...

def disassemble_file(input_file, output_file):
    """Disassemble a .mx file into a .as file."""
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            line = line.strip()
            # Split the line at the colon and take the second part, which contains the instructions.
            parts = line.split(':')
            if len(parts) == 2:
                instructions = parts[1].strip().split()
                for instr in instructions:
                    if instr:
                        instruction = int(instr, 16)
                        assembly_line = disassemble_instruction(instruction)
                        fout.write(assembly_line + "\n")

def main():
    assert len(sys.argv) == 3, f"Usage: python {sys.argv[0]} input_file.mx output_file.as"
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    disassemble_file(input_file, output_file)

if __name__ == "__main__":
    main()
