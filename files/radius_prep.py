# import the converted json, read as dictionary, output as csv file
import ast

with open('data_lines.txt', 'r') as file:
    dicts = []
    i = 0
    fields = set()
    for line in file:
        d = ast.literal_eval(line)
        dicts.append(d)
        fields.update(d.keys())
        if i%100000 == 0:
            print i
            
        i += 1
        
fields = list(fields)

with open('data.csv', 'w') as file:
    file.write(','.join(fields) + '\n')
    for d in dicts:
        s = ''
        for f in fields[:-1]:
            if d[f] is not None:
            	si = str(d[f])
            	s += si.replace(',','')+','
            else:
                s += ','
        if d[fields[-1]] is not None:
        	si = str(d[fields[-1]])
        	s += si.replace(',','') + '\n'
        else:
            s += '\n'
        file.write(s)
print 'done'