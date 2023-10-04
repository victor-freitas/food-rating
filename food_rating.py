def solution(n, ratings):
    dish_ratings = {}
    
    for i in range(n):
        dish_id, rating = ratings[i]
        
        # check if the dish is already in the dictionary
        if dish_id in dish_ratings:
            dish_ratings[dish_id][0] += rating  # add the rating to the total
            dish_ratings[dish_id][1] += 1
        else:
            # if not in the dictionary, create a new entry
            dish_ratings[dish_id] = [rating, 1]
    
    max_average_rating = -1
    highest_rated_dish = None
    
    for dish_id, (total_rating, count) in dish_ratings.items():
        average_rating = total_rating / count  # calculate average rating
        
        # check if the current dish has a higher average rating or the same average but smaller ID
        if average_rating > max_average_rating or (average_rating == max_average_rating and \
            (not highest_rated_dish or dish_id < highest_rated_dish)):
            max_average_rating = average_rating
            highest_rated_dish = dish_id
    
    return highest_rated_dish

# sample input
n = 4
ratings = [
    (512, 2),
    (123, 3),
    (987, 4),
    (123, 5)
]
