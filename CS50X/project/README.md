# BI for SME

#### Video Demo: https://youtu.be/faO_b0GJ3Hw

#### Description:

BI for SME is a web app for CS50X final project and also for use by V-Cred, my startup. The idea for BI for SME arose when a potential customer, Mas, told us that he found a Power BI report we made for him very useful and that he would pay for it. We then needed a way to share the report with him given that he did not have a Microsoft Power BI user account. So the BI for SME website allowed us to host the Power BI reports for him and other customers while allowing us to control the user authorisation.

The website has a landing page with a demo report, FAQ and About Us section. Visitors to the site can also express their interest in our service via the Sign Up section.

Once users sign up, the web admin can create an account for them and assign them a Power BI report and drive storage. The Google Drive storage allows users to upload data required to make the Power BI report. Users can interact with the live Power BI report similar to if it were hosted on the Power BI web service.

Users may also update their own account details and add notes to their dashboard.

Design:
The web app was built using Flask and styled with Bootstrap. (credits to the Tech with Tim Youtube channel for their Flask tutorial which helped me build the initial base)

The auth apis were written in auth.py. Initially users could immediately sign up and receive an account. But in order to control access onto the platform and because I would need to obtain user requirements prior to onboarding them onto the platform, I switched the sign up functionality so that only the admin can sign up users and the sign up page was changed to a Google Form which helps with the requirement gathering.

Different users have different acceess, but the admin has access to view all reports and to change other people's access authority. I set it so that once the web app is launched, the first user account created is by default an admin account.

Sqlite database was used for the authorisation, notes and managing which users were from which companies and had access to which reports. The db model can be referred to in models.py.

Creating the admin panel and setting up the relationships between the various db tables was challenging. It was hard to make sure that I could restrict and control access only from an admin account and that the Power BI URL would be assigned to specific companies and that users were then assigned to these companies. Using Postman to test my apis and using the PHPmyadmin graphical interface made this process a lot easier.

The Power BI reports are manually created by me and uploaded into my PowerBI account. I then publish it on the MS Power BI web service and make access public. I then take the public link and display it on the BI for SME web app using HTML iframes. I set it so that the iframe displays the PBI URL either based on the user's company or a drop-down selector if the user is an Admin account.

Storage was via Google Drive's api because it's free. The sign up form uses Google forms also displayed on our platform via an iframe.
