import pandas
from random import randrange
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

colors = ['green','blue','orange','purple','brown','pink','gray','olive','cyan','red']
df = pandas.read_csv('database.csv')

while True:
    print("Welcome to CountryComparator! Select which type of data you'd like to compare: ")
    type =input("1. Population\n2. Area\n3. GDP per capita.\n4. Birthrate\n5. Deathrate.\n6. Exit\n")
    if(type=='1'):
        type='Population';
        measure='';
    elif(type=='2'):
        type='Area';
        measure='square kilometres';
    elif(type=='3'):
        type='GDP';
        measure='U$ per capita';
    elif(type=='4'):
        type='Birthrate';
        measure='per thousand population';
    elif(type=='5'):
        type='Deathrate';
        measure='per thousand population';
    elif(type=='6'):
        print("Thank you for using CountryComparator!")
        print("\n----------\n")
        break;    
    else:
        print("Invalid option.")
        print("\n----------\n")
        continue;
    print("\n----------\n")
    print("You selected ",type,". Now select how you'd like to compare your data: ")
    print("\n----------\n")
    print("1. Select some countries and compare their ", type,".\n2. Select one country and compare it's", type," with the ",type," of a random country.\n3. Compare the ",type," of two randomly selected countries.\n4. Exit\n")
    mode =input()
    print("\n----------\n")
    
    if(mode=='1'):
        data=[]
        countries =[]
        flag=True
        try:
            quant=int(input("\nHow many countries would you like to compare? Choose at least 2: \n"))
        except ValueError:
            print("You need to choose a number.")
            print("\n----------\n")
            flag=False;
            break;
        if(quant<2):
            print("You need to choose at least 2.")
            print("\n----------\n")
            continue;
        
        for i in range(quant):
                
                print("Type the name of the country # ",i+1)
                country = input()
                if(country in countries):
                    print("You have already selected ", country,".")
                    flag=False;
                    break;                
                try:
                    data.append(df[df['Country']==country][type].values[0])
                    countries.append(country)                    
                except IndexError:
                    print("There's no such country as ",country,".")
                    print("\n----------\n")
                    flag=False;
                    break;
        if(flag==True):        
            for i in range(quant):
                print("As of 2020, the ",type," of ",countries[i]," is ",data[i],measure,".")
                           
            if(type=='Population'):
                ylabel=type;
            elif(type=='GDP'):
                ylabel=type+' ('+measure+')';
            else:
                ylabel=type+' - '+measure;
            title=type+' comparison of countries';
        
            x = np.arange(len(countries))
            plt.bar(x,data,color=colors)
            plt.xticks(x,countries)
            plt.ylabel(ylabel)
            plt.title(title)

            plt.show()
            print("\n----------\n")
            continue;
        else:
            continue;
    elif(mode=='2'):
        country=input("Type the name of the country: ")
        try:
            data= df[df['Country']==country][type].values[0]
        except IndexError:
            print("There's no such country as ",country,".")
            continue;
        index = (df[df['Country']==country].index.values)+1

        df2 = pandas.read_csv('database.csv',skiprows=[index])

        rand = randrange(2,236)

        country2 = df2.loc[rand, 'Country']
        data2 =  df2.loc[rand, type]

        print("As of 2020, the ",type," of ",country," is ", data, measure,", and the ",type," of ",country2," is ",data2,measure,".", country,"'s ",type," is at least ", "{:.2f}".format(int(data)/int(data2)) ,"times the ",type," of", country2,"!")
        print("\n----------\n")

        labels = [country,country2]
        data = [data,data2]
        if(type=='Population'):
            ylabel=type;
        elif(type=='GDP'):
            ylabel=type+' ('+measure+')';
        else:
            ylabel=type+' - '+measure;
        title=type+' comparison of countries';
       
        x = np.arange(len(labels))
        plt.bar(x,data,color=colors)
        plt.xticks(x,labels)
        plt.ylabel(ylabel)
        plt.title(title)

        plt.show()
        
        continue;

    elif(mode=='3'):

        rand = randrange(2,236)
        country = df.loc[rand, 'Country']
        data=  df.loc[rand, type]

        index = (df[df['Country']==country].index.values)+1
        df2 = pandas.read_csv('database.csv',skiprows=[index])
        
        rand2 = randrange(2,236)
        
        if(rand2==rand):
            while(rand2==rand):
                rand2 = randrange(2,236)
                            
        country2 = df2.loc[rand2, 'Country']
        data2 =  df2.loc[rand2, type]

        print("As of 2020, the ",type," of ",country," is ", data, measure, ", and the ",type," of ",country2," is ",data2, measure,".", country,"'s ",type," is at least ", "{:.2f}".format(int(data)/int(data2)) ,"times the ",type," of", country2,"!")
        print("\n----------\n")

        labels = [country,country2]
        data = [data,data2]
        if(type=='Population'):
            ylabel=type;
        elif(type=='GDP'):
            ylabel=type+' ('+measure+')';
        else:
            ylabel=type+' - '+measure+'';
        title=type+' comparison of countries';
         
        x = np.arange(len(labels))
        plt.bar(x,data,color=colors)
        plt.xticks(x,labels)
        plt.ylabel(ylabel)
        plt.title(title)

        plt.show()
        continue;

    elif(mode=='4'):
        print("Thank you for using CountryComparator!")
        print("\n----------\n")
        break;

    else:
        print("Invalid option.")
        print("\n----------\n")
        continue;
