import matplotlib.pyplot as plt
plt.plot([7.688200000000034e-05,0.0009726660000000109,0.013967699,0.20680972599999997],label='Quicksort')
plt.plot([0.00014516200000000423,0.0020301590000000036,0.031863664999999985,0.418527621],label='Mergesort')
plt.annotate('Mergesort',xy=(2.1,0.14),xytext=(1.8,0.2), arrowprops=dict(facecolor='blue',shrink=0.05))
plt.annotate('Quicksort',xy=(2.5,0.08),xytext=(3,0.02),arrowprops=dict(facecolor='black',shrink=0.05))
plt.ylabel('t')
plt.title('Quicksort vs Mergesort')
plt.show()
