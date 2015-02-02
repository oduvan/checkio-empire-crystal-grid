**Precondition:**

```python
1 < len(grid) <= 10
1 < len(grid[0]) ,= 10
all(len(row) == len(grid[0]) for row in grid)
all(all(ch in "XZ" for ch in line) for line in grid)
```