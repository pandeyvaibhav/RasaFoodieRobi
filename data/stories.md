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
* affirm{"mail_id": "noresponse@vp.com"}
    - slot{"mail_id": "noresponse@vp.com"}
    - action_send_mail
    - export

## Story Jabalpur_Chinese
* greet
    - utter_greet
* restaurant_search{"location": "Jabalpur"}
    - slot{"location": "Jabalpur"}
    - action_validate_location
    - slot{"location_found": "no"}
    - utter_not_operational



* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_found": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"price": "300"}
    - slot{"price": "300"}
    - action_search_restaurants


## test story 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* location{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_validate_location
    - slot{"location_found": true}
    - utter_ask_budget
* budget{"price": "300"}
    - slot{"price": "300"}
    - action_search_restaurants
    - utter_ask_ifmail
* affirm
    - utter_ask_mailid
* email{"mail_id": "nihit.sh@gmail.com"}
    - slot{"mail_id": "nihit.sh@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "nihit.sh@gmail.com"}
* affirm
    - utter_goodbye

## test story 2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* location{"location": "madrid"}
    - slot{"location": "madrid"}
    - action_validate_location
    - slot{"location_found": false}
    - utter_not_operational
* budget{"price": "300"}
    - slot{"price": "300"}
    - action_search_restaurants
    - utter_ask_ifmail
* affirm
    - utter_ask_mailid
* email{"mail_id": "nihit.sh@gmail.com"}
    - slot{"mail_id": "nihit.sh@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "nihit.sh@gmail.com"}
* affirm
    - utter_goodbye

## test story 3
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - slot{"location_found": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"price": "700"}
    - slot{"price": "700"}
    - action_search_restaurants
    - utter_ask_ifmail
* affirm
    - utter_ask_mailid
* email{"mail_id": "nihit.sh@gmail.com"}
    - slot{"mail_id": "nihit.sh@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "nihit.sh@gmail.com"}

## test story 4
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"location": "chandigarh"}
    - slot{"location_found": true}
    - utter_ask_budget
* budget{"price": "300"}
    - slot{"price": "300"}
    - action_search_restaurants
    - utter_ask_ifmail
* affirm
    - utter_ask_mailid
* email{"mail_id": "nihit.sh@gmail.com"}
    - slot{"mail_id": "nihit.sh@gmail.com"}
    - action_send_mail
    - slot{"mail_id": "nihit.sh@gmail.com"}

## test story 5
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"location": "chandigarh"}
    - slot{"location_found": true}
    - utter_ask_budget
* budget{"price": "300"}
    - slot{"price": "300"}
    - action_search_restaurants
    - utter_ask_ifmail
* deny
    - utter_goodbye