import json
import pickle
import numpy as np
def get_index(arr,x):
	if x in arr:
		return arr.index(x)
	return -1

def get_price_from_model(area,bath,bhk,location,availibility,area_type):
	with open("columns.json",'r') as f:
		column=json.load(f)
	len_avai=len(column['availability_columns'])-1
	len_area=len(column['area_columns'])-1
	len_loca=len(column['location_columns'])-1
	l=3+len_avai+len_area+len_loca
	x=np.zeros(l)
	x[0]=area
	x[1]=bhk
	x[2]=bath
	pos=get_index(column['availability_columns'][:len_area],availibility)
	if pos>=0:
		x[3+pos]=1

	pos=get_index(column['area_columns'][:len_area],area_type)
	if pos>=0:
		x[3+pos+len_avai]=1

	pos=get_index(column['location_columns'][:len_loca],location)
	if pos>=0:
		x[3+pos+len_avai+len_loca]=1
	
	with open("banglore_home_prices_model.pickle",'rb') as f:
		model=pickle.load(f)

	return model.predict([x])[0]

print(get_price_from_model(area=1056.0,bhk=2,bath=2,availibility='Ready To Move',area_type='Built-up  Area',location=' Devarachikkanahalli'))