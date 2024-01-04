# TAMS - Auction App (Group 8 for Web Programming Module)
An auction application similar to eBay which allows users to create an account, upload items they'd like to sell along with a description, price, image, and more. Also allows users to search through these items, place a bid, view their inventory, comment on items such as to ask questions, and receive an email once the bid has expired if they are the highest bidder. 

## Group Members
- Aysha Uddin
- Tazmena Hussain
- Syeda Sadia Taznim
- Sadia Muna Abedin

## Tasks Completed
Each team member completed all tasks assigned to them. <br>
- **Aysha Anita Uddin** <br>
Database, Profile Page, Comments, Place Bids
- **Tazmena Hussain** <br>
Sign Up/Login User Authentication Framework, Item Display, Email Winner, Sessions
- **Syeda Sadia Taznim** <br>
Routing/Navbar, View Bids, Search Bar
- **Sadia Muna Abedin** <br>
Add Bids, Logout, Inventory

## Deployment URL
App has not been deployed to OpenShift.

## Installation Instructions
**To run the app, complete the following steps:** 
 - Open a terminal window and CD into the Django project folder named 'tams'
 - Run pip install -r requirements.txt
 - Run python manage.py runserver
 - Open another terminal window and CD into the Vue/Vite project folder named 'frontend'
 - Run npm install 
 - Run npm run dev
 - **Navigate to 'localhost:8000/auctionapp/' to login, (NOT '127.0.0.1:8000/')**


## Admin Details
**Username:** admin@tams.com
<br>
**Password:** admin

## 7 Test User Details
### *User 1*
**Username:** aysha@tams.com
<br>
**Password:** admin
<br>
### *User 2*
**Username:** tazmena@tams.com
<br>
**Password:** admin
<br>
### *User 3*
**Username:** paulogroup8@gmail.com
<br>
**Password:** admin2022
### *User 4*
**Username:** sadia@tams.com
<br>
**Password:** admin
<br>
### *User 5*
**Username:** muna@tams.com
<br>
**Password:** admin
### *User 6*
**Username:** admin@tams.com
<br>
**Password:** admin
### *User 7*
**Username:** tams2022group8@gmail.com
<br>
**Password:** admin2022

## Testing Advice
- Signup and Login: Sign up with the correct details and login with those details, a session will be created.
- Profile page: Should display default image with user's current details. Allow's user to change image, email, date of birth etc.
- Inventory page: Allows users to view items they've posted, add new items and delete their items.
- Auctions page: Users can search based off a given keyword, and return a list of items with that keyword.
- Items page: After searching on auctions page, click on View Item to see more information and place bids, a user can only place one bid, before the end date/time. Users can ask questions to the owner about the item, and the owner can send responses.
- Email Winner: At the end of an auction's time, the user who placed the highest bid will receive an email. In order to test this, place the highest bid with the given gmails so you can view the emails that are sent. Due to our program, you must be in the item's page and refresh when time becomes 0, only then will the email be send, item deleted and redirected back to search page.
- Eg. Log in with multiple accounts (eg. aysha@tams.com, password is admin) (tazmena@tams.com, password is admin) and place a bid on a specific item. Then, login with the paulogroup8@gmail.com (password is admin2022), and place the highest bid on that item. Then, wait for time to expire, navigate away from the item page and then back onto it, and the email should be sent to paulogroup8@gmail.com. The item should then be deleted, and the user should be redirected to the search page. Log into gmail with the same login details to see if the email was sent.
- To make testing easier, add an item in inventory with a short time (eg 5 minutes from now), bid that item on multiple accounts but have the highest bidder be paulogroup8@gmail.com, then wait for time to run out, navigate back into that item's page, such as searching for it and viewing that item. You should receive the email and be redirected to search.
