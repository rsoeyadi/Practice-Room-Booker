### Usage

This script automates the process of opening up the practice room portal (ASIMUT) at midnight every night to book practice rooms. It is currently set to run at **23:59** every night, with the actual booking occuring at **00:00**. 

All you need to do is save this script to your computer and:

1. Enter your credentials in **lines 23 and 24** of **rooms.py**

2. Open up **roomsInput.py**

   1. Choose up to three rooms you'd like to book and enter in the information carefully in the format provided in the commented code (up to three rooms; you can add more if needed)

   ```python
   #I.e.
   roomYouWant = "421" 
   timeYouWant = "10:30 am - 12:30 pm" 
   ```

3. After you complete steps 1 and 2, you are set! I recommend setting up a crontab to run this script in the background every day.

