from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json

import smtplib
from email.message import EmailMessage

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City,Cuisine):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

def sendmail(MailID,response):
	smtp_connect = smtplib.SMTP("smtp.gmail.com", 587)
	smtp_connect.starttls()
	smtp_connect.login("mlc20foodie@gmail.com","Random@123")
	msg = EmailMessage()
	msg['Subject'] = "Results of your search on Foodie"
	msg['From'] = "mlc20foodie@gmail.com"

	msg.set_content(response)
	msg['To'] = MailID

	smtp_connect.send_message(msg)
	smtp_connect.quit()
	return []

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		print(cuisine)
		price = tracker.get_slot('price')
		print(price)
		if price == "300":
		    budget_min = 0
		    budget_max = 300
		elif price == "700":
		    budget_min = 300
		    budget_max = 700
		else :
		    budget_min=700
		    budget_max=50000

		print(budget_max)

		print("Action: action_search_restaurants")
		#print("Action: action_search_restaurants -- loc --" + loc + "-- cuisinse --" + cuisine + " -- budget --" + budget)
		results = RestaurantSearch(City=loc,Cuisine=cuisine)	
		print(results)	
		response=""
		if results.shape[0] == 0:
			print("No results found in this search!!")
			response= "We do not operate in that area yet, Could you please select some other location?"
		else:
			for restaurant in RestaurantSearch(loc,cuisine).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Aggregate Rating']} with avg cost {restaurant['Average Cost for two']} \n\n"
			print("I got some restaurants in this search!!!")
		
		[SlotSet('location',loc)]
		dispatcher.utter_message(str(response))

		#return response

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('mail_id')
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		results = RestaurantSearch(City=loc,Cuisine=cuisine)
		
		response = "Hi there! "
		if results.shape[0] == 0:
			response = response + F"No results found for your query."
		else:
			for restaurant in RestaurantSearch(loc,cuisine).iloc[:10].iterrows():
				restaurant = restaurant[1]
				response=response + F"Here are the results of your query.\n" + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
		sendmail(MailID,response)
		dispatcher.utter_message("Email sent as per request!")
		dispatcher.utter_message("Have a great day!")
		return [SlotSet('mail_id',MailID)]

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

		price = tracker.get_slot('price')
		print(price)
		if price == "300":
		    budget_min = 0
		    budget_max = 300
		elif price == "700":
		    budget_min = 300
		    budget_max = 700
		else :
		    budget_min=700
		    budget_max=50000

		print(budget_max)

		return [SlotSet('budget',budget_max)]