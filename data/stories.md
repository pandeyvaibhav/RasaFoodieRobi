## Story Delhi_Chinese
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Less than 300"}
    - slot{"budget": "1"}
    - action_search_restaurants
* restaurant_search{"budget": "between 300 to 700"}
    - slot{"budget": "2"}
    - action_search_restaurants
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "3"}
    - action_search_restaurants
    - export

