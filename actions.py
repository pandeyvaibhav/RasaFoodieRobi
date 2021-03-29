from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json


ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['Agra', 'Ahmedabad','Allahabad','Amritsar','Aurangabad','Bangalore','Bhopal','Bhubaneshwar', 'Chandigarh', 'Chennai', 'Coimbatore', 'Dehradun', 'Faridabad', 'Gangtok', 'Ghaziabad', 'Goa', 'Gurgaon', 'Guwahati', 'Hyderabad', 'Indore', 'Jaipur', 'Kanpur', 'Kochi', 'Kolkata', 'Lucknow', 'Ludhiana', 'Mangalore', 
'Mohali', 'Mumbai', 'Mysore', 'Nagpur', 'Nasik', 'Delhi','Noida', 'Ooty', 'Panchkula', 'Patna', 'Puducherry', 'Pune', 'Ranchi', 'Secunderabad', 'Shimla', 'Surat','Vadodara', 'Varanasi', 'Vizag']

def RestaurantSearch(City,Cuisine):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')	
		print(loc)				
		cuisine = tracker.get_slot('cuisine')
		print(cuisine)
		price = tracker.get_slot('price')
		print(price)
		if price == "300":
		    budget = 300
		elif price == "700":
		    budget = 700
		else :
		    budget=700
		print(budget)

		print("Action: action_search_restaurants")
		#print("Action: action_search_restaurants -- loc --" + loc + "-- cuisinse --" + cuisine + " -- budget --" + budget)
		results = RestaurantSearch(City=loc,Cuisine=cuisine)	
		print(results)	
		response=""
		if results.shape[0] == 0:
			print("No results found in this search!!")
			response= "No results found for the searched location"
		else:
			for restaurant in RestaurantSearch(loc,cuisine).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response = response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
			print("I got some restaurants in this search!!!")
		
		[SlotSet('location',loc)]
		dispatcher.utter_message(str(response))

		#return response

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
	    recipient = tracker.get_slot('email')

	    top10 = restaurants.head(10)
	    print("got this correct")
	    send_email(recipient, top10)
	    dispatcher.utter_message("Have a great day!")

class ActionSearchLocation(Action):
	def name(self):
		return 'action_validate_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		print("Action: action_validate_location")

		if loc.lower() in (city.lower() for city in WeOperate):
			print("found loc")
			[SlotSet('location_found',"yes")]
			return [SlotSet('location_found',"yes")]
		else:						
			print("We do not operate in that area yet, Could you please select some other location?")
			dispatcher.utter_message("We do not operate in that area yet, Could you please select some other location?")
 			
			return [SlotSet('location_found',"no")]

class ActionGetCuisineSlection(Action):
	def name(self):
		return 'action_get_cuisine'
	
	def run(self,dispatcher,tracker,domain):
		val=tracker.get_slot('num')
		cuisines=['Chinese','Mexican','Italian','American', 'South Indian','North Indian']
		print("Action: action_get_cuisine")
		return [SlotSet('cuisine',cuisines[int(val)-1])]

class ActionGetPriceSelection(Action):
	def name(self):
		return 'action_get_price'
	
	def run(self,dispatcher,tracker,domain):
		print("Action: getting budget slot value")
		val=tracker.get_slot('price')
		print("Value found -" + val)
		print("Action: action_get_price")
		print("num: - ")
		#temp_dict={'300':[0,300],'301':[300,700],'700':[700]}
		#print(temp_dict[str(val)])

		price = tracker.get_slot('price')
		print(price)
		if price == "300":
		    budget1 = 300
		elif price == "700":
		    budget1 = 699
		else :
		    budget1=700

		print(budget1)

		return [SlotSet('budget',budget1)]