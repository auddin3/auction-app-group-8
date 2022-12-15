# TAMS - Group 8 Auction App

## Group Members
- Aysha Anita Uddin
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

**To run the app, complete the following steps:** 
 - Open a terminal window and CD into the Django project folder named 'tams'
 - Run pip install -r requirements.txt
 - Run python manage.py runserver
 - Open another terminal window and CD into the Vue/Vite project folder named 'frontend'
 - Run npm install 
 - Run npm run dev
 - **Navigate to 'localhost:8000/auctionapp/' to login**


## Admin Details
**Username:** admin@tams.com
<br>
**Password:** admin

## 5 Test User Details
### *User 1*
**Username:** aysha@tams.com
<br>
**Password:** admin
<br>
### User 2
**Username:** tazmena@tams.com
<br>
**Password:** admin
<br>
### User 3
**Username:** sadia@tams.com
<br>
**Password:** admin
<br>
### User 4
**Username:** muna@tams.com
<br>
**Password:** admin
### User 5
**Username:** admin@tams.com
<br>
**Password:** admin

Testing Advice
- Signup and Login: Sign up with the correct details and login with those details, a session will be created.
- Profile page: Should display default image with user's current details. Allow's user to change image, email, date of birth etc.
- Inventory page: Allows users to view items they've posted, and add new items.
- Auctions page: Users can search based off a given keyword, and return a list of items with that keyword.
- Items page: After searching on auctions page, click on an item to see more information and place bids, a user can only place one bid, before the end date/time. Users can ask questions to the owner about the item, and the owner can send responses.
- Email Winner: At the end of an auction's time, the user who placed the highest bid will receive an email. In order to test this, place the highest bid with the given gmails so you can view the emails that are sent. Due to our program, you must be in the item's page and refresh when time becomes 0, only then will the email be send, item deleted and redirected back to search page.
- Eg. Log in with multiple accounts (eg. aysha@tams.com, password is admin) (tazmena@tams.com, password is admin) and place a bid on a specific item. Then, login with the paulogroup8@gmail.com (password is admin2022), and place the highest bid on that item. Then, wait for time to expire, and go on the item page/refresh the item page if already there, and the email should be sent to paulogroup8@gmail.com. The item should then be deleted, and the user should be redirected to search page. Log into gmail with the same login details to see if the email was sent.
