def getHitProbability(R, C, G):
    total_cells = R * C
    battleship_cells = sum(sum(row) for row in G)
    return battleship_cells / total_cells

# Sample test cases
print(getHitProbability(2, 3, [[0, 0, 1], [1, 0, 1]]))  # Expected output: 0.50000000
print(getHitProbability(2, 2, [[1, 1], [1, 1]]))  # Expected output: 1.00000000