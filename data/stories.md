## Story Delhi_Chinese
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 3003 to 700"}
    - action_search_restaurants
    - export

## Story Bokaro_Chinese
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bokaro Steel City"}
    - slot{"location": "Bokaro Steel City"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}
    - slot{"budget": "between 300 to 700"}
    - action_search_restaurants
* affirm
    - utter_goodbye
* goodbye
    - export

## Story -Delhi_Mexican
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## Story -Chennai_SouthIndian
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget

* restaurant_search{"budget": "between 300 to 700"}
    - slot{"budget": "between 300 to 700"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## Story Bangalore_NorthIndian
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* affirm{"email": "vaibhavapk@gmail.com"}
    - slot{"email": "vaibhavapk@gmail.com"}
    - action_send_mail
* goodbye
    - export

## Story Bangalore_Chinese
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}
    - slot{"budget": "between 300 to 700"}
    - action_search_restaurants
* affirm
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* affirm{"email": "vaibhavapk@gmail.com"}
    - slot{"email": "vaibhavapk@gmail.com"}
    - action_send_mail
* affirm
* goodbye
    - utter_goodbye
    - export

## Story -Pune_Chinese
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}
    - slot{"budget": "between 300 to 700"}
    - action_search_restaurants
* affirm
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* affirm{"email": "vaibhavapk@gmail.com"}
    - slot{"email": "vaibhavapk@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - export

## Story Mumbai_Max
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}
    - slot{"budget": "between 300 to 700"}
    - action_search_restaurants
* affirm
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* affirm{"email": "vaibhavapk@gmail.com"}
    - slot{"email": "vaibhavapk@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - export

## Story -Kolkata_Chinese
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}
    - slot{"budget": "between 300 to 700"}
    - action_search_restaurants
* affirm
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* affirm{"email": "vaibhavapk@gmail.com"}
    - slot{"email": "vaibhavapk@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye
    - export

## Story -Chennai_American
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
* affirm
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
    - export

## Story -Mumbai_Italian
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
* affirm
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* affirm{"email": "vaibhavapk@gmail.com"}
    - slot{"email": "vaibhavapk@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - export

## Story -Bokaro_Budget
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bokaro Steel City"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bokaro Steel City"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_budget
* restaurant_search{"budget": "between 300 to 700"}
    - slot{"budget": "between 300 to 700"}
    - action_search_restaurants
* affirm
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* affirm{"email": "vaibhavapk@gmail.com"}
    - slot{"email": "vaibhavapk@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - export

## Story -Bokaro_Chinese
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bokaro Steel City"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bokaro Steel City"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "lesser than 300"}
    - slot{"budget": "lesser than 300"}
    - action_search_restaurants
* affirm
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* affirm{"email": "vaibhavapk@gmail.com"}
    - slot{"email": "vaibhavapk@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - export

## Story -Bokaro_SouthIndian
* greet
    - utter_greet
* restaurant_search{"location": "Bokaro Steel City"}
    - slot{"location": "Bokaro Steel City"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_search_restaurants
* goodbye
    - utter_goodbye
    - export

