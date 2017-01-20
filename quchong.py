# -*-coding:utf-8 -*-

city_name = 'hotels_tianjin'

f = open('input/' + city_name + '.txt','r')

d = f.readlines()

f.close()


out_f = open('output/' + city_name + '.txt','w')

hotel_dict = {}

count = 1

for data in d:
    new_data = data.split()
    if len(new_data) == 1:
        new_data.append('0')
    # print new_data[0]
    #
    # print count
    #
    # count +=1


    key = new_data[0]
    value1 = new_data[1]

    hotel_dict[key] = value1

for key in hotel_dict:
    out_f.write(key + ' ' + hotel_dict[key] + '\n')


out_f.close()



print len(hotel_dict)

print city_name + " all has been done!!!"





