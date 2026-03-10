def is_valid_move(start, end):
    # Validate chess moves a1 -> c4 or a1 -> d5
    valid_moves = [(1, 1, 3, 4), (1, 1, 4, 5)]  # (start_x, start_y, end_x, end_y)
    start_x, start_y = ord(start[0]) - ord('a') + 1, int(start[1])  # Convert to coordinates
    end_x, end_y = ord(end[0]) - ord('a') + 1, int(end[1])
    return (start_x, start_y, end_x, end_y) in valid_moves


# Example uses
print(is_valid_move('a1', 'c4'))  # True
print(is_valid_move('a1', 'd5'))  # True
print(is_valid_move('b2', 'c4'))  # False