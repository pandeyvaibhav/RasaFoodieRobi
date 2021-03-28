from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

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
		budget = tracker.get_slot('budget')
		print(budget)

		print("Action: action_search_restaurants")
		#print("Action: action_search_restaurants -- loc --" + loc + "-- cuisinse --" + cuisine + " -- budget --" + budget)
		results = RestaurantSearch(City=loc,Cuisine=cuisine)	
		print(results)	
		response=""
		if results.shape[0] == 0:
			print("No results found in this search!!")
			response= "no results"
		else:
			for restaurant in RestaurantSearch(loc,cuisine).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
				
		print("I got some restaurants")
		return [SlotSet('location',loc)]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('mail_id')
		print("Action: action_send_mail")

		sendmail(MailID,response)
		return [SlotSet('mail_id',MailID)]


class ActionSearchLocation(Action):
	def name(self):
		return 'action_validate_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		print("Action: action_validate_location")

		if loc.lower() in (city.lower() for city in WeOperate):
			print("got loc")
			[SlotSet('loc',loc)]
			return [SlotSet('location_found',"yes")]
		else:						
			print("We do not operate in that area yet, Could you please select some other location?") 	
			return [SlotSet('location_found',"no")]

class ActionGetCuisineSlection(Action):
	def name(self):
		return 'action_get_cuisine'
	
	def run(self,dispatcher,tracker,domain):
		val=tracker.get_slot('num')
		cuisines=['Chinese','Mexican','Italian','American','Thai', 'South Indian','North Indian']
		print("Action: action_get_cuisine")
		return [SlotSet('cuisine',cuisines[int(val)-1])]

class ActionGetPriceSelection(Action):
	def name(self):
		return 'action_get_price'
	
	def run(self,dispatcher,tracker,domain):
		val=tracker.get_slot('budget')
		print("Action: action_get_price")
		print("num: - ")
		temp_dict={'1':[0,300],'2':[300,700],'3':[700]}
		print(temp_dict[str(val)])
		return [SlotSet('price',temp_dict[str(val)])]