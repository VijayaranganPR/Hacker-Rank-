n = int(input())
l = [int(input()) for i in range(n)]
for element in l:
    sum_of_squares =(element*(element+1)*(2*element+1))/6
    square_of_sums = (element*(element+1)/2)**2
    print(int(abs(sum_of_squares-square_of_sums)))
