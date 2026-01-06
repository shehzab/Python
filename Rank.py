def swap_rows(m, i, j):
  m[i],m[j] = m[j], m[i]

def matrix_rank(m):
    rows = len(m)
    cols =len(m[0])
    rank = 0

    for col in range(cols):
      pivot_row = None

      for r in range(rank, rows):
        if m[r][col] != 0:
          pivot_row = r
          break

      if pivot_row is not None:
        swap_rows(m, rank, pivot_row)

        pivot = m[rank][col]
        for r in range(rank + 1, rows):
          factor = m[r][col] / pivot
          for c in range(col, cols):
            m[r][c] -= factor * m[rank][c]
        
        rank += 1

    return rank


matrix = [
  [1,2,4],
  [9,4,6],
  [2,4,6]
]

print("rank of matrix:", matrix_rank(matrix))