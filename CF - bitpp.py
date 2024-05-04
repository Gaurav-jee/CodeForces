

def execute_bitpp_program(program):
  x = 0
  for statement in program:
    if "+" in statement:
      x += 1
    else:
      x -= 1
  return x

if __name__ == "__main__":
  n = int(input())
  program = [input() for _ in range(n)]
  final_value = execute_bitpp_program(program)
  print(final_value)