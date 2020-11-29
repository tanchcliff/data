# Plots


## Lap Times Heat Map

![sg_laptimes_heatmap](https://raw.githubusercontent.com/tanchcliff/data/main/f1_2019/charts/2019_15_Singapore_F1_Lap_Times_Heatmap.png)

above is a heatmap of lap times (seconds) of each driver across the laps of the race in Singapore.

very interesting to see the overall race progression in a single chart, e.g.:

- how carlos sainz had issues early in the race, george russell as well
- how major changes begun at around lap 36 onwards for all drivers, and again on laps 44 and 50, corresponding to when safety car were deployed
- how driver lap times mostly fell drastically after they race restarts
- how daniel riccardo's lap times were relatively more evenly spread compared to the rest of the field

## Lap Times Distribution

![sg_laptimes_distribution_plot_kde](https://raw.githubusercontent.com/tanchcliff/data/main/f1_2019/charts/2019_15_Singapore_F1_Lap_Times_Dist_Plot_KDE.png)

quick and simple plot using seaborn 0.9.0's distplot() function, generating a histogram and fitting a kernal density estimate, using the default bandwidth value.

we see that it is a multimodal distribution, with majority of values below approximately 120 seconds.

this helped when we develop box plots for the lap times of each driver below. 

![sg_laptimes_box_plot_all](https://raw.githubusercontent.com/tanchcliff/data/main/f1_2019/charts/2019_15_Singapore_F1_Lap_Times_Box_Plot_1.png)

first box plot is for all lap times of all drivers.

![sg_laptimes_box_plot_filtered](https://raw.githubusercontent.com/tanchcliff/data/main/f1_2019/charts/2019_15_Singapore_F1_Lap_Times_Box_Plot_2.png)

the second is for lap times under 120 seconds, allowing for a better appreciation of the distribution of the fast laps around the circuit.

it still amazes me how the lap times are closely matched.

the difference in the median lap times of leclerc and vettel is just 0.1 second - the time for our eyes to blink!
