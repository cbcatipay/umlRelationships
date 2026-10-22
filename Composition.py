class CPU:
  def _init_(self, model: str):
    self.model = model

class Computer:
  def _init_(self):
    self.cpu = CPU

my_pc = Computer()
print(f"Computer running with: {my_pc.cpu.model}")
