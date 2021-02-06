import matplotlib.pyplot as plt

years = [1950,1955,1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2015,2020]

peeps = [1.650,
         2.525, 2.758, 3.010, 3.322, 3.682, 4.061, 4.440, 4.853, 5.310, 5.735, 6.127, 6.520, 6.930, 7.349]

deaths = [
    1.2, 1.7, 1.8, 2.2, 2.5, 2.7, 2.9, 3, 3.1, 3.3, 3.5, 3.8, 4.0, 4.3, 4.5
]
plt.plot(years, peeps, '--', color=(255/255, 100/255, 100/255))
plt.plot(years, deaths, color=(.1, .4, .6))
plt.ylabel("population in billions")
plt.xlabel('population growth by year')


plt.title(" our population between 1950 - 2020")
plt.show()