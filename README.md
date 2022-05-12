# Surfs Up with ice cream and surf boards
## Overview
This analysis was of an exploratory nature to determine the viability of a new business based on Oahu, Hawai’i, to provide beachgoers a place to buy ice cream and rent surf boards. The analysis was to determine the best weather conditions throughout the year to see when there may be a slow down or an uptick in sales at the proposed business. Although Hawai’i is known for its beautiful views and predominantly sunny weather, it still receives plenty of rain and temperatures certainly do fluctuate, but we are curious to what degree they fluctuate. When it is 60F less people will want ice cream than when it is 90F, which of course will inform inventory sales and thus overall operating costs throughout the year. The analysis will be presented to investors or potential investors to help get the idea off the ground with solid data scientifically gathered and analyzed. 

## Methodology
We received a sqlite file containing information containing the location of the weather stations on Oahu, including their latitude, longitude, elevation; and a complementary data set detailing the measurements of those stations, including the date, temperature, and precipitation. We created an engine to connect to the sqlite file to query it, and saved the Measurement set of data and Station set of data to reference further down in our code. `engine = create_engine("sqlite:///hawaii.sqlite")` For this analysis we were primarily concerned with temperature, as many storms last for a matter of hours, not days, and thus a rainy morning could mean a busy sunny afternoon for a surf shop. We filtered the data by date and temperature observation (in code it was referred to as 'tobs') and set the dates greater than 1 June 2017, and limited the returned list to 30 items, as there are 30 days in June. `june_temps = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= june).limit(30)
` Our December analysis was identical except we limited the returned list to 31 items because there are 31 days in December. We compared the temperatures in December 2016 and the following June 2017, which of course represent the dead of winter and the middle of summer, respectively. From those lists, which we converted to dataframes, we created summary statistics of the temperatures, including maximum, minimum, and average temperatures. 

## Results
To the surprise of no one, the temperatures were warmer in June than they were in December, with a difference of 9F on average. However, the average temperature in December in Hawai’i was 70F, still well within acceptable surfing temperature. It would seem, in theory, that the surf shop should be profitable throughout the year. On the surface one would assume overall sales will slow down in December due to lower temperatures. One factor this analysis did not consider is the number of visitors to Hawai’i from the continental United States trying to find sunshine and warm weather while it’s gray and bleak at home. The owners of the surf shop might be surprised at how much business doesn’t slow down in the colder months, although that would require another analysis for another day. 
