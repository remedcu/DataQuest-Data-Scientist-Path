## 1. Lists ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

## 2. Indexing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
ratings_1 = row_1[3]
ratings_2 = row_2[3]
ratings_3 = row_3[3]
ratings_4 = row_4[3]
ratings_5 = row_5[3]
total = ratings_1 + ratings_2 + ratings_3 + ratings_4 + ratings_5
average = total/5

## 3. Negative Indexing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
rating_1 = row_1[-1]
rating_2 = row_2[-1]
rating_3 = row_3[-1]
rating_4 = row_4[-1]
rating_5 = row_5[-1]
total_rating = rating_1 + rating_2 + rating_3 + rating_4 + rating_5
average_rating = total_rating / 5

## 4. Retrieving Multiple List Elements ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
fb_rating_data = [row_1[0], row_1[3], row_1[4]]
insta_rating_data = [row_2[0], row_2[3], row_2[4]]
pandora_rating_data = [row_5[0], row_5[3], row_5[4]]
cc_pricing_data = [row_3[0], row_3[1], row_3[2]]
tr_pricing_data = [row_4[0], row_4[1], row_4[2]]
avg_rating = (fb_rating_data[-1] + insta_rating_data[-1] + pandora_rating_data[-1]) / 3
avg_pricing = (cc_pricing_data[1] + tr_pricing_data[1]) / 2

## 5. List Slicing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
first_4_fb = row_1[:4]
last_3_fb = row_1[-3:]
insta_2_4 = row_2[1:4]
pandora_3_4 = row_5[2:4]
last_2_insta = row_2[-2:]
avg_rating = (last_3_fb[-1] + last_2_insta[-1]) / 2
avg_price = (first_4_fb[1] + insta_2_4[0]) / 2

## 6. List of Lists ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
app_data_set = [row_1, row_2, row_3, row_4, row_5]
avg_rating = (app_data_set[0][-1] + app_data_set[1][-1] + app_data_set[2][-1] + app_data_set[3][-1] + app_data_set[4][-1]) /5

## 7. Opening a File ##

from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

print(len(apps_data))
print(apps_data[0])
print(apps_data[1:3])
col_names = apps_data[0]
apps_data = apps_data[1:]
print(col_names)
print(apps_data[0:3])
print(len(apps_data))

## 8. Repetitive Processes ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

for row in app_data_set:
    print(row)
    print('----------------')
    
list_a = [10, 20, 30, 40]
for a in list_a:
    print(a)
    
list_of_lists = [[1,2], [11,12], [21,22]]
for a in list_of_lists:
    print(a[0])

for a in list_of_lists:
    print(a[-1])

for a in list_of_lists:
    print(a)

a_sum = 0
list_b = [1, 3, 5]
print(a_sum)

for value in list_b:
    a_sum += value
    print(a_sum)

## 9. For Loops ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

rating_sum = 0
for a in app_data_set:
    rating = a[-1]
    rating_sum += rating
    
avg_rating = rating_sum / len(app_data_set)

## 10. The Average App Rating ##

from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)
rating_sum = 0
for i in apps_data[1:]:
    rating = i[7]
    rating_sum += float(rating)

avg_rating = rating_sum / len(apps_data[1:])

## 11. Alternative Way to Compute an Average ##

from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)
all_ratings = []
for i in apps_data[1:]:
    all_ratings.append(float(i[7]))

avg_rating = sum(all_ratings) / len(all_ratings)