#2NDASSIGNMENT
The two algorithms I've created have to sort the numbers of a taken list in order.
I created the QuickSort algorithm that takes a random quantity of numbers in a list,then that algorithm will take a pivot(a defined number) and then the algorithm takes a number of those in the list i've chosen and it puts the number on the left of the pivot if the number is smaller, or on the right if the number is bigger than the pivot. After this passage, the algorithm will swap between the elements until it reaches the right order.

The mergesort algorithm basically will do the same passages of the quicksort algorithm but it will not use the pivot element so the algorithm will divide every time until it arrives with a single number and then it will check every single number in the list and sort it with the next element of that list

After I made those two algorithms , I used timeit that is a function that measures the time the two algorithms will take to sort all the elements in the list.I obtain the result of that function : quicksort is generally faster than mergesort and it stores less memory but it doesn't mean that it's better because in the worst case of quicksort, the algorithm mergesort will function better due to its capability to deal with big data. I chose also a random list because I want to check if this statement is true through all the possibilities.
Once I have had the results, I take those results and put them in a plot I've created to get a precise overview of the rate of the two algorithms, I checked also that the trend that reflects the quicksort is faster as I said before.

