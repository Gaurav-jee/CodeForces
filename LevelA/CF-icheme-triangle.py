
def is_valid_triangle(x, y, z):
  """Checks if the triangle inequality holds for the given sides."""
  return (x + y > z) and (y + z > x) and (x + z > y)

def solve_triangle(a, b, c, d):
  """Finds valid side lengths for a triangle within the given ranges."""
  x, y, z = b, c, d
  while not is_valid_triangle(x, y, z):
    z -= 1  # Decrement the longest side if triangle inequality fails
  return x, y, z

t = int(input())
for _ in range(t):
  a, b, c, d = map(int, input().split())
  x, y, z = solve_triangle(a, b, c, d)
  print(x, y, z)
