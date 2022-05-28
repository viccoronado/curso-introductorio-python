#La conjetura del Dr. Lothar

def lothar(n):
  # Solucion
    if n == 0:
        return 0
    counter = 0
    while n != 1:
        n = (n / 2) if n % 2 == 0 else (3 * n + 1)
        counter += 1
    return counter
        
        
n = int(input())
print( lothar(n) )