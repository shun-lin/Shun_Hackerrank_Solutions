def height(n, height_bank):
  if n in height_bank:
    return height_bank[n]
  if n == 1:
    return 0
  if n % 2 == 0:
    ans = 1 + height(n / 2)
    height_bank[n] = ans
  else:
    ans = 1 + height(n * 3 + 1)
    height_bank[n] = ans
  return ans

def findHighest(n):
  height_bank = dict()
  max_height = 0
  max_hell = 1
  for i in range(1, n):
    temp_height = height(i, height_bank)
    if (temp_height > max_height):
      max_height = temp_height
      max_hell = i
  return max_hell

print(findHighest(1000000));
