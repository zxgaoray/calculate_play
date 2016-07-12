from calculator import Centroid

user_input = raw_input()

centroid = Centroid.Centroid()
centroid.polygonRing(user_input)
user_input = centroid.calculate()

print user_input