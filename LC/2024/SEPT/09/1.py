m = 3
n = 5
head = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
print(m, n, head)

# Initialize matrix with -1
init_matrix = [[-1 for i in range(n)] for j in range(m)]
print(init_matrix)

# Define LinkedList class
class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to create linked list from array
def create_linked_list(arr):
    if not arr:
        return None
    head = LinkedList(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = LinkedList(arr[i])
        current = current.next
    return head

# Function to fill matrix in spiral order
def spiralMatrix(m, n, head):
    # Create empty matrix filled with -1
    matrix = [[-1 for i in range(n)] for j in range(m)]
    
    # Create linked list from the input array
    head = create_linked_list(head)

    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_pointer = 0

    # Start from the top-left corner of the matrix
    r, c = 0, 0

    curr = head

    while curr:
        matrix[r][c] = curr.val
        curr = curr.next

        # Compute next position
        dr, dc = directions[direction_pointer]
        next_r, next_c = r + dr, c + dc
        
        # Check if the next position is within bounds and unfilled
        if not (0 <= next_r < m and 0 <= next_c < n and matrix[next_r][next_c] == -1):
            # Change direction
            direction_pointer = (direction_pointer + 1) % 4
            dr, dc = directions[direction_pointer]
            next_r, next_c = r + dr, c + dc
        
        # Update the current position
        r, c = next_r, next_c
    
    return matrix

# Test the function
matrix_result = spiralMatrix(m, n, head)
for row in matrix_result:
    print(row)

    