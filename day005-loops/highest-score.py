scores = [10,2,3,55,3,6,74,23,43, 89]

max_score = 0

for score in scores:
    if score > max_score:
        max_score = score

print(f"Max score: {max_score}")