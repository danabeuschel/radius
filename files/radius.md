I divided the variables into two groups: string and numeric. The string category consists of alphanumeric variables 
like name, address, city, and state, as well as categorical variables like headcount, revenue, and time in business.
The numeric category consists of the three variables for which valid values are strictly numeric: zip, phone, and NAICS category.

# String
For each string variable, I found that in addition to 'null', missing values were coded as either 
' ', '0', or 'none'. These appeared in all variables, and for the string values, 
these are the values I used for non-null, non-true-valued. It's possible that there are some more invalid 
labels in name and address, but it's impossible to check each value due to the cardinality of the set. All cardinality calculations 
include the 4 invalid values.

Additionally, for the string variables, I converted the labels to lowercase before computing the cardinality. This is to ensure
that e.g. 'FIRST BAPTIST CHURCH' and 'First Baptist Church' are recognized as the same name.

## Name
The vast majority of the records include a valid name. Roughly 11% of the values are duplicates, which makes sense after looking 
into the data and seeing that many names are the type that would show up more than once, such as 'YMCA.'

### Non-null
999964

### True-valued
999910

### Cardinality
890566


## Address
Again, the vast majority of records have an address field. Again, roughly 11% are duplicates, which is a little higher than I would
have expected, but not inconceivable (there are a lot of Main Streets).
### Non-null
999957

### True-valued
999898

### Cardinality
892118

## State
The non-null and true-valued rates are again very high, similar to name and address. The number of valid responses 
is 53, which consists of all 5 states, plus three territories.

### Non-null
999952

### True-valued
999896

### Cardinality
57 

## City
Again, roughly 50 are null, with about 100 missing in total. There are 13,714 unique, valid city names, which is a lower 
bound on the actual number of cities (as the same city name can be in multiple states).
### Non-null
999952

### True-valued
999895

### Cardinality
13718

## Revenue
This variable has a lot more missing values, with roughly 5.7% not containing any information. The cardinality is low because 
responses are coded into rather broad ranges.

### Non-null
943062

### True-valued
943001

### Cardinality
15

## Headcount
About 3.8% are missing. Again, this is a categorical variable so the cardinality is rather low.
### Non-null
962332

### True-valued
962273

### Cardinality
13

## Time in business
Third of the categorical range variables. This one has the lowest response rate, with 8.4% missing in some fashion.
### Non-null
916097

### True-valued
916048

### Cardinality
9

# Numerical variables
For the numerical variables, I was able to further restrict the class of valid responses using upper and lower bounds 
on the possible valid responses. Interestingly, all of these variables, this did not result in a substantial increase in 
the number of non-true-valued, non-null responses. In fact, the non-true-valued, non-null variables are entirely blank, zero,
or 'none.' This suggests that data entry problems do not appear to be a significant problem (otherwise we might expect some 9-digit 
phone numbers, for instance).

## Zip
Since all ZIP codes are 5 digits long, and don't go lower than 000501, I was able to use this fact for determining whether 
a ZIP code was valid. Interestingly, it did not exclude many values (apart from 0, which appeared in the other variables).

The missing rate is very similar to that for other components of the address, and the cardinality is the same order of 
magnitude as that of cities, as expected.

### Non-null
999951

### True-valued
999890

### Cardinality
24539

## Category Code
In the data, all category codes were 8 digits long, with at least a 1 as the first digit, so this was used 
as the validity condition for category code.

In contrast to other variables about the business, industry code is nearly all present. There are 1189 values, suggesting 
a wide range of industries represented.

### Non-null
999961

### True-valued
999910

### Cardinality
1189


## Phone
Since telephone numbers are 10 digits long, and no area code starts with 0 or 1, again a numerical range 
is used as the validity condition.

This variable has by far the highest rate of missing, with over 40% not present.
Roughly 0.6% are duplicates, which is worth looking into, as phone number is the one column which should be unique across businesses.

### Non-null
590866

### True-valued
590798

### Cardinality
575152

# Additional Analysis

For this stage, I examined two aspects of the data: geographical distribution and industry composition.

## Geographic distribution

Below is a coordinate map of the log number of businesses per zip code across the continental US. Darker green 
indicates a higher number.

[![N|Solid](https://github.com/danabeuschel/radius/files/zip_plot.png)]

The map indicates a higher concentration of ZIP codes with _any_ businesses in the eastern half of the country and greater 
sparsity in the Rocky Mountain area. Mid-to-large cities are clearly visible as the darker shades of green. In fact, the 
geographic pattern is quite similar to that found in night-time satellite imagery, indicating a strong association with 
population density. This suggests that the data are geographically representative of the population, and do not appear to 
favor certain regions, or large metros in general.

## Industry composition
My code calculates the number of businesses per 2-digit NAICS code. Across the 24 categories, the percent of total businesses ranges from 
0.05% (Management) to over 16% (professional, technical, and scientific services). The most well-represented sectors are services (including 
construction), with manufacturing, agriculture, and heavy industry not as well represented. This coincides with the geographic distribution, as 
most services (such as dentists, or contractors) would be expected to have a strong relationship with population density, as opposed 
to industry or agriculture, where the outputs can be easily shipped anywhere.

[satellite imagery]: <http://media.gettyimages.com/photos/satellite-image-of-the-united-states-at-night-picture-idAA011470?s=170667a>

