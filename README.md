Food ratings 

A restaurant has launched an app for their food delivery. 'n' reviews about various of their menu items have been submitted. Users have submitted a rating out of 5 (1 being worst and 5 being best). The manager wants to know the most loved dish in the restaurant.

Find out the dish with the highest average rating.

Note: If two dishes are rated the same, return the dish with the smallest ID.

Function description:

COmple the function solution() provided in the editor. The function takes the following 2 paramerters and returns the solution:
 
n: Represents the number of reviews(this parameter is for internal purpores, don't remove it from the function)
ratings: Represents the reviews of each dish

The input format is custom testing
Note: Use this input format if you are testing against custom input or writing code in language where we do'nt provide boilerplate code
thee first line contains n denoting the number of reviews.
NExt, the n line contains two integers each, the ID and rating of ther iTH review.

Output format

Print a single integer, representing the ID of the hightest-rated dish.

Contraints

1 <= n <=10 elevado ao 5
1 <= rating[í][0] <= 10 elevado a 9
1 <= ratings[i][1] <= 5



sample input 

4 
512 2
123 3
987 4
123 5

sample output 123
