import sys
import re
from architecture import VMState
from vm_step import VirtualMachineStep


class VirtualMachineExtend(VirtualMachineStep):
    # [init]
    def __init__(self, reader=input, writer=sys.stdout):
        super().__init__(reader, writer)
        self.handlers = {
            "d": self._do_disassemble,
            "dis": self._do_disassemble,
            "i": self._do_ip,
            "ip": self._do_ip,
            "m": self._do_memory,
            "memory": self._do_memory,
            "q": self._do_quit,
            "quit": self._do_quit,
            "r": self._do_run,
            "run": self._do_run,
            "s": self._do_step,
            "step": self._do_step,
        }
    # [/init]

    # [interact]
    def interact(self, addr):
        prompt = "".join(sorted({key[0] for key in self.handlers}))
        interacting = True
        addresses=[]
        while interacting:
            try:
                command = self.read(f"{addr:06x} [{prompt}]> ")
                if re.match(re.compile('[a-z]+ [0-9]+'), command) or re.match(re.compile('[a-z]+ [0-9]+ [0-9]+'),command):
                    command_list = command.split()
                    command = command_list[0]
                    addresses = list(map(int, command_list[1:]))
                if not command:
                    continue
                elif command not in self.handlers:
                    self.write(f"Unknown command {command}")
                else:
                    print(command)
                    if command == 'm' or command == 'memory':
                        interacting = self.handlers[command](self.ip, addresses)
                    elif command == 'b' or command == 'break' or command=='clear' or command=='c':
                        interacting = self.handlers[command](self.ip, addresses)
                    else:
                        interacting = self.handlers[command](self.ip)
                addresses=[]
            except EOFError:
                self.state = VMState.FINISHED
                interacting = False
    # [/interact]

    def _do_disassemble(self, addr):
        self.write(self.disassemble(addr, self.ram[addr]))
        return True

    def _do_ip(self, addr):
        self.write(f"{self.ip:06x}")
        return True

    # [memory]
    def _do_memory(self, addr, addresses=[]):
        if len(addresses) == 0:
            self.show()
        elif len(addresses) == 1:
            self.show_addr(addresses[0])
        elif len(addresses) == 2:
            self.show_addrs(addresses)
        return True
    # [/memory]

    def _do_quit(self, addr):
        self.state = VMState.FINISHED
        return False

    def _do_run(self, addr):
        self.state = VMState.RUNNING
        return False

    # [step]
    def _do_step(self, addr):
        self.state = VMState.STEPPING
        return False
    # [/step]


if __name__ == "__main__":
    VirtualMachineExtend.main()
