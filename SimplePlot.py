import matplotlib.pyplot as plt
x=["JAVA","PYTHON","RUBY","PHP"]
y=[200,400,300,500]
plt.bar(x,y)
plt.xlabel("courses")
plt.ylabel("students controlled")
plt.title("students controlled for different course 2022")
# plt.plot(x,y,color='green', linewidth=3, linestyle='dashed')
# plt.plot(x, y, color='red', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
plt.show()


# –	solid line style
# —	dashed line style
# -.	dash-dot line style
# :	dotted line style

# .	point
# o	circle
# v	triangle down
# ^	triangle up
# s	square
# p	pentagon
# *	star
# +	plus
# x	cross
# D	diamond