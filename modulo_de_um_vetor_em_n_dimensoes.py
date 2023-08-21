dimensions = int(input('Type a number: '))
components = []
square_sum = 0
for i in range(1, dimensions + 1):
    components.append(float(input(f'Enter the components for dimension {i} do vetor:')))
for e in components:
    square_sum += e**2
print(f'The module is equal to {square_sum**0.5:.2f}')
