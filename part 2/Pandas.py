import numpy as np
import pandas as pd
# dict = {
#         "Name":['Gopal','Tanushree','Avik','Suvankar'],
#         "Department":['MCA','MCA','MBA','BBA'],
#         "Address":['Gangarampur','Balurghat','Falakata','Siliguri']
#         }
# # print(dict)
# df= pd.DataFrame(dict)
# print(df)
# print(df['Department'])
#
# # df.to_csv('Student.csv')
# # print(df.head(2)) #It will show the first two rows
# # print(df.tail(2)) #It will shoe the last two rows
#
# movie=pd.read_csv('Movie.csv')
# print(movie)
# print(movie['Movie Name'][1])
# movie['Genre'][2]='Horror'
# print(movie)
#
# movie.to_csv('movie.csv')

city=pd.read_csv('City.csv')
# print(city)
# temp_bombay=city[(city.CITY=='BOMBAY') & (city.MEAN_TEMP==72.2)]
# temp_bombay.to_csv('Bombay2.csv')

# temp_bombay=city[(city.CITY=='BOMBAY')].sort_values('YEAR',ascending=False)
# temp_bombay.to_csv('BombaySorted2.csv')

print(city[city.CITY.isin(['BOMBAY','CALCUTTA'])])

print(city.groupby(['CITY','YEAR']))



