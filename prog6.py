import matplotlib.pyplot as plt;
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
langs=['c','c++','java','android','python']
students=[23,17,45,62,10]
ax.bar(langs,students)
plt.show()
