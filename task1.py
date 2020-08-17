#!/usr/bin/python3

f = open('names', 'rt')
lst = f.read().replace('"', '').replace('\ufeff','').replace('\n','').split(',')

#print(lst)
spisok_sorted = sorted(lst)

res=0
for num, element in enumerate(spisok_sorted, 1):
    summ=0
    for letter in element:
        summ += ord(letter)-64
    mult = num*summ
    res += mult
    print('{} {}: {} ; {}'.format(num, element, summ, mult))

print(res)