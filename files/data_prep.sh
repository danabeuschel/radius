# since the JSON took forever to load, I converted it to text and then csv. this is the first step,
# converting it to a python-friendly txt file by adding line breaks, converting null to None, and 
# removing braces
head data_analysis.json > data.txt
sed 's/\[{/{/g;s/}\]/}/g;s/}, /}\
/g;s/ null,/ None,/g;s/ null}/ None}/g;s/"null"/None/g' data.txt > data_lines.txt
python radius_prep.py