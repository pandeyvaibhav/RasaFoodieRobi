## Story Delhi_Chinese
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "less than 300"}
    - slot{"budget": "1"}
    - action_search_restaurants
* restaurant_search{"budget": "between 300 to 700"}
    - slot{"budget": "2"}
    - action_search_restaurants
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "3"}
    - action_search_restaurants
* affirm{"email": "noresponse@vp.com"}
    - slot{"email": "noresponse@vp.com"}
    - action_send_mail
    - export

## Story Jabalpur_Chinese
* greet
    - utter_greet
* restaurant_search{"location": "Jabalpur"}
    - slot{"location": "Jabalpur"}
    - action_validate_location
    - utter_not_operational


