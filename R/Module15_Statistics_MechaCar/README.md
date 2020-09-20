# MechaCar

### MPG

![1](https://user-images.githubusercontent.com/65242270/91095360-16d34b00-e611-11ea-9516-7d31ea5458ee.png)
![2](https://user-images.githubusercontent.com/65242270/91095361-176be180-e611-11ea-86f2-0f78ccf6358d.png)

For a given predictor, the t-statistic evaluates whether or not there is significant association between the predictor and the outcome variable (is the beta coefficient of the predictor significantly different from zero?). If this predictor is changed, there will be significant changes to the mpg. With that, the average predicted mpg increases 6.08 for vehicle length and 3.57 for ground clearance. They are the slopes for each respective predictor. The p-value for vehicle length (7.68e-08) and ground clearance (3.26e-08) are smaller than 0.05, thus are meaningful predictors.

### Suspension Coil

![3](https://user-images.githubusercontent.com/65242270/91095362-18047800-e611-11ea-836f-82231180bbb1.png)
![4](https://user-images.githubusercontent.com/65242270/91095363-18047800-e611-11ea-9f9e-16a2754648aa.png)

The PSI variance does not exceed 100 pounds per inch for the lots in aggregate. For each lot separately, this is the same case for lot1 and lot2, however there is a variance >100 pounds for lot3.

### Suspension Coil T-Test

![5](https://user-images.githubusercontent.com/65242270/91095364-18047800-e611-11ea-884a-fde57e8f5472.png)

The p-value for all lots is above the significance level (assumption at .05 percent). Similarly, the p-value for each lot is above their respective significance level (aassumption at .05 percent). Therefore, there is no sufficient evidence to reject the null hypothesis and the two means (sample and population) are statistically similar.

### Additional Study
Fuel economy is generally a factor for consumers looking to purchase a car. Depending on the fuel economy and use for the car (i.e. commuter, ride-share, short trips, etc), these are additional recurring costs to the consumer outside of purchasing the car.
Null hypothesis: Cars with manual transmission have 10% on average better fuel economy than automatic transmission. 
Alternative hypothesis: Cars with manual transmission have less than 5% on average better fuel economy than automatic transmission.
Data for analysis: Transmission, car class, year, manufacturer, drive type, mpg
