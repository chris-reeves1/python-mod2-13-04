def count(sequence, item):
  sum = 0
  y = 9
  for n in sequence:
    if n == item:
      sum += 1
  return sum
