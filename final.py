
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


full= pd.read_csv('C:/studies/python/csv/FullData.csv',delimiter=',')


# In[3]:


full


# In[19]:


full


# In[22]:


full.loc[0]


# In[53]:


full.loc[[0,1],['Club','Name','Rating']]


# In[51]:


p1= full.iloc[:,0:10].head()
p1


# In[62]:


full.loc[:,'Club'].value_counts().head()  # to count number of players in the list by each club


# In[63]:


full.loc[:,'Club_Position'].value_counts().head()  # to see who tops the list Right centre backs are more in the list


# In[82]:


import numpy as np
age= full.loc[:,'Age']
age1=full.loc[:,'Age'].value_counts()
age2=age.unique()
age2=np.sort(age2)  # used on my own and used numpy to sort an array
age2


# In[71]:


age1


# In[80]:


import matplotlib.pyplot as plt

plt.scatter(age2,age1,label="scat",color='k',marker='*')
plt.xlabel('age')
plt.ylabel('number of people of this age')
plt.show()




# In[86]:


a=full['Age']
a


# In[93]:


myarr=[]

            
myarr


# In[95]:


for i in range(0,len(age2)):
    count=0
    for j in range(0,len(a)):
        if age2[i]==a[j]:
            count=count+1
    myarr.append(count)


# In[96]:


myarr


# In[98]:


#Age Density of FIFA Players

import matplotlib.pyplot as plt

plt.plot(age2,myarr,label="scat",color='k',marker='*')
plt.xlabel('age')
plt.ylabel('number of people of this age')
plt.show()


# In[123]:


gr2= full.loc[:,['Club','Rating']]



gr2= gr2.groupby('Club')['Rating'].mean()
  # technique to reverse an array
gr2=gr2.sort_values()

gr2=gr2[::-1]
gr2.head()  # overall best team by ratings



# In[125]:


p2=gr2.tail() 
p2=p2[::-1]
p2 # bottom teams based on ratings


# In[299]:


import matplotlib.pyplot as plt
stamina=full.loc[:,['Stamina']]
stamina=stamina.sort_values('Stamina')
stamina=stamina[::-1]
stamina=stamina.head(100)
x=full.loc[:,['Stamina']]
y=full.loc[:,['Nationality']]
myarr=[]

stamina=stamina.as_matrix()
x=x.as_matrix()
y=y.as_matrix()
for i in range(len(stamina)):
    for j in range(len(x)):
        if stamina[i]==x[j]:
            myarr.append(y[j])


na= pd.DataFrame(myarr,columns=['Nationality']).head(100)

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
na=na.groupby('Nationality')['Nationality'].value_counts()
na=na.sort_values()
na=na[::-1]
na.plot('bar')
plt.show()







# In[ ]:





# In[302]:


africa=['Algeria','Angola','Benin','Botswana','Burkina','Burundi','Cameroon','Cape Verde','Central African Republic','Chad','Comoros','Congo','Congo Democratic Republic of','Djibouti','Egypt','Equatorial Guinea','Eritrea','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea-Bissau','Ivory Coast','Kenya','Lesotho','Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria','Rwanda','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone','Somalia','South Africa','South Sudan','Sudan','Swaziland','Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe','Burkina Faso']
asia=['Afghanistan','Bahrain','Bangladesh','Bhutan','Brunei','Burma (Myanmar)','Cambodia','China','East Timor','India','Indonesia','Iran','Iraq','Israel','Japan','Jordan','Kazakhstan','North Korea','South Korea','Kuwait','Kyrgyzstan','Laos','Lebanon','Malaysia','Maldives','Mongolia','Nepal','Oman','Pakistan','Philippines','Qatar','Russian Federation','Saudi Arabia','Singapore','Sri Lanka','Syria','Tajikistan','Thailand','Turkey','Turkmenistan','United Arab Emirates','Uzbekistan','Vietnam','Yemen','Russia']
europe=['Albania','Andorra','Armenia','Austria','Azerbaijan','Belarus','Belgium','Bosnia Herzegovina','Bulgaria','Croatia','Cyprus','Czech Republic','Denmark','Estonia','Finland','France','Georgia','Germany','Greece','Hungary','Iceland','Ireland','Italy','Latvia','Liechtenstein','Lithuania','Luxembourg','Macedonia','Malta','Moldova','Monaco','Montenegro','Netherlands','Norway','Poland','Portugal','Romania','San Marino','Serbia','Slovakia','Slovenia','Spain','Sweden','Switzerland','Ukraine','England','Vatican City','Republic of Ireland','Wales']
north_america=['Antigua and Barbuda','Bahamas','Barbados','Belize','Canada','Costa Rica','Cuba','Dominica','Dominican Republic','El Salvador','Grenada','Guatemala','Haiti','Honduras','Jamaica','Mexico','Nicaragua','Panama','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Trinidad and Tobago','United States']
oceania=['Australia','Fiji','Kiribati','Marshall Islands','Micronesia','Nauru','New Zealand','Palau','Papua New Guinea','Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu']
south_america=['Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela']



# In[303]:


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
newdat1= full.replace(europe,'Europe')
newdat2= newdat1.replace(africa,'africa')
newdat3= newdat2.replace(asia,'asia')
newdat4= newdat3.replace(north_america,'north_america')
newdat5= newdat4.replace(oceania,'oceania')
newdat6= newdat5.replace(south_america,'south_america')
newdata=newdat6
top=newdata.head(100)
top=top.loc[:,['Nationality','Rating']]
top= top.groupby('Nationality')['Rating'].mean()
top=top.sort_values()
top=top[::-1]
top.plot(kind='bar')
top
#the actual values in the graph are
#1.south_america         87.238095 
#2.Europe                86.608108 
#3.africa                85.500000
#4.north_america         85.000000
#5.Bosnia Herzegovina    85.000000
#6.Serbia                84.000000
plt.show()


# In[308]:


#best player with max points in all of the skills
bestpl=full.head(100)
bestpl= bestpl.groupby('Name')['Dribbling','Marking','Sliding_Tackle','Standing_Tackle','Aggression','Reactions','Attacking_Position',
                             'Interceptions','Vision','Composure','Crossing','Short_Pass','Long_Pass','Acceleration','Speed','Stamina',
                             'Strength','Balance','Agility','Jumping','Heading','Shot_Power','Finishing','Long_Shots','Curve',
                             'Freekick_Accuracy','Penalties','Volleys','GK_Positioning','GK_Diving','GK_Kicking','GK_Handling',
                             'GK_Reflexes'].mean()
# a player with all of skills which can we say as a complete player when comes in a team which was decided comparing 33 qualities
#top 5 best players
bestpl.head(5)




# In[309]:


# comparison between ronaldo and messi who is a complete player and who stands top in the list?
bestpl.loc[['Cristiano Ronaldo','Lionel Messi'],:]                       


# In[314]:


# which club has maximum players in top 100
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
maxplayers= full.head(100)
maxplayers=maxplayers.groupby('Club')['Club'].value_counts()
maxplayers=maxplayers.sort_values()
maxplayers=maxplayers[::-1]
maxplayers.plot('bar')

# real madrid tops the list with bayern as second


# In[354]:


import numpy as np
lis= full.loc[:,['Club_Position','Name','Rating']].head(100)
bestplayer=[]
position=[]
rate=[]
lis1=full.loc[:,['Club_Position']].head(100)
lis1.loc[0,['Club_Position']]
lis1=lis1.as_matrix()

def funct1():
    #for i in range(len(lis)):
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    c7=0
    c8=0
    c9=0
    c10=0
    c11=0
    c12=0
    
    count=0
    while(count<=12):
        for i in range(100):
            if (lis1[i]) == 'LW':
                count=count+1
                c1=c1+1
                if(c1==1):
                    bestplayer.append(lis.loc[i,['Name']])
                    position.append(lis.loc[i,['Club_Position']])
                    rate.append(lis.loc[i,['Rating']])
            elif (lis1[i]) == 'RW':
                count=count+1
                c2=c2+1
                if(c2==1):
                    bestplayer.append(lis.loc[i,['Name']])
                    position.append(lis.loc[i,['Club_Position']])
                    rate.append(lis.loc[i,['Rating']])
            elif (lis1[i]) == 'ST':
                count=count+1
                c3=c3+1
                if(c3==1):
                    bestplayer.append(lis.loc[i,['Name']])
                    position.append(lis.loc[i,['Club_Position']])
                    rate.append(lis.loc[i,['Rating']])
            elif (lis1[i]) == 'RCM':
                count=count+1
                c4=c4+1
                if(c4==1):
                    bestplayer.append(lis.loc[i,['Name']])
                    position.append(lis.loc[i,['Club_Position']])
                    rate.append(lis.loc[i,['Rating']])
            elif (lis1[i]) == 'LCM':
                count=count+1
                c5=c5+1
                if(c5==1):
                    bestplayer.append(lis.loc[i,['Name']])
                    position.append(lis.loc[i,['Club_Position']])
                    rate.append(lis.loc[i,['Rating']])
            elif (lis1[i]) == 'CAM':
                count=count+1
                c6=c6+1
                if(c6==1):
                    bestplayer.append(lis.loc[i,['Name']])
                    position.append(lis.loc[i,['Club_Position']])
                    rate.append(lis.loc[i,['Rating']])
            elif (lis1[i]) == 'RCB':
                count=count+1
                c7=c7+1
                if(c7==1):
                    bestplayer.append(lis.loc[i,['Name']])
                    position.append(lis.loc[i,['Club_Position']])
                    rate.append(lis.loc[i,['Rating']])
            elif (lis1[i]) == 'RB':
                count=count+1
                c8=c8+1
                if(c8==1):
                    bestplayer.append(lis.loc[i,['Name']])
                    position.append(lis.loc[i,['Club_Position']])
                    rate.append(lis.loc[i,['Rating']])
            elif (lis1[i]) == 'LB':
                count=count+1
                c9=c9+1
                if(c9==1):
                    bestplayer.append(lis.loc[i,['Name']])
                    position.append(lis.loc[i,['Club_Position']])
                    rate.append(lis.loc[i,['Rating']])
            elif (lis1[i]) == 'RW':
                count=count+1
                c10=c10+1
                if(c11==1):
                    bestplayer.append(lis.loc[i,['Name']])
                    position.append(lis.loc[i,['Club_Position']])
                    rate.append(lis.loc[i,['Rating']])
            elif (lis1[i]) == 'GK':
                count=count+1
                c11=c11+1
                if(c11==1):
                    bestplayer.append(lis.loc[i,['Name']])
                    position.append(lis.loc[i,['Club_Position']])
                    rate.append(lis.loc[i,['Rating']])
            elif (lis1[i]) == 'LCB':
                count=count+1
                c12=c12+1
                if(c12==1):
                    bestplayer.append(lis.loc[i,['Name']])
                    position.append(lis.loc[i,['Club_Position']])
                    rate.append(lis.loc[i,['Rating']])
            
        
funct1()     
z1=np.asarray(bestplayer)
z2=np.asarray(position)
z3=np.asarray(rate)
z11= pd.DataFrame(z1,columns=['Best Player']) 
z12= pd.DataFrame(z2,columns=['position'])
z13= pd.DataFrame(z3,columns=['Rate'])        
con= pd.concat([z11,z12,z13],axis=1)
con
    
#best player and their position in fifa18


# In[355]:


#DREAM 11 
con


# In[353]:


import matplotlib.pyplot as plt

#radar chart required 


# In[ ]:




