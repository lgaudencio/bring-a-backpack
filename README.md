# Bring a Backpack

Bring a Backpack is a site for reviewing travel destinations and photography sharing. Users from around the world can sign up and add their travel reviews to the website and share their photography skills with other travel enthusiasts and helpfully help other users decide on their next journey. The site provides users with a simple and easy system to write their reviews, upload pictures and customise their profile. The live link to the site can be found here: Live Site - Bring a Backpack

## User Experience Design

### The Strategy Plane

#### Site Goals

The site is aimed at all travel enthusiasts who are planning their next adventure and would like a source of inspiration from other fellow travellers. Site users can sign up, login, create a destination review and the published reviews can be easily edited or even deleted. Users can also share their photography skills but creating posts with 10 images, just like the destination reviews, these posts can be edited and deleted when needed. Additionally, users have their own profiles, it will show other users their recent reviews/posts. The profile can also be edited, such as info and the display picture. 

#### Agile Planning 

This project was developed using agile methodologies, delivering small features at a time. All projects were assigned to epics, prioritised under labels - Must have, Should have and Could have. The core project requirements were given the ‘Must have’ label to ensure they were prioritised and completed before moving onto the requirements that had the other two labels. 

The Kanban board was created using Github projects and can be seen here and can be viewed to see more information on the project cards. Most stories will have acceptance criteria to define its function, once the function has been met, it is then marked off as completed. 

##### Epics

The project had 8 main Epics (milestones):

**EPIC 1 – Base Setup**
 
The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible, therefore it was the first epic to be delivered as all other features will depend on the completion of the base setup. 
 
**EPIC 2 – Authentication**
 
The authentication epic is for all stories that are related to the sign up, login and authorisation of views. Authorisation provides crucial and critical functionality, as without it, users would not be able to make a destination review and/or a photography post securely without the threat of other site users being able to edit or delete their review and/or photos.
 
**EPIC 3 – Destinations**
 
The destinations epic is for all stories that relate to creating, viewing, editing and deleting a destination review. This allows site visitors to view all destination reviews and it allows registered users to manage their own reviews by using a simple to use user interface.

**EPIC 4 - Profiles**

The profiles epic is for all stories relating to creating and editing a profile. This allows all signed up users to be able to create their own profiles and edit them as they wish. Users can add such things as, a name, display picture, nationality, type of traveller and a bio. 

**EPIC 5 - Photography** 

The destinations epic is for all stories that relate to creating, viewing, editing and deleting a photography post. This allows site visitors to view all photography posts and it allows registered users to manage their own posts by using a simple to use user interface.

**EPIC 6 - Stand alone pages**

The stand alone pages epic is for small pages that did not have enough stories to warrant their own full epics. Therefore, these small deliverables were added under this one epic. 

**EPIC 7 - Deployment**

This epic is relating to the deployment of the app to heroku so that the site can be made live for all users.

**EPIC 8 - Documentation**

This epic is relating to all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explains all stages of development and necessary information on running, deploying and using the application. 

##### User Stories

**EPIC 1 - Base Setup**

As a developer, I need to set up the project so that it is ready to implement the core features

As a developer, I need to create a logo and navbar so that the user can navigate around the site across any given device

As a developer, I need to create a footer with social media links so that the user can keep up with new destination reviews across various social media platforms

As a developer, I need to create static resources so that images, CSS and JavaScript work on the website 

As a developer I need to create a base.html page and structure so that all other pages across the site can reused the layout 

**EPIC 2 - Authentication**

As a developer I need to implement allauth so that users can sign up and have access to the sites features 

As a site owner I would like the allauth pages to be customised so that they fit into the rest of the site design 

**EPIC 3 - Destinations** 

As a user I want to see all travel destination reviews so that I can decide whether to travel to that specific city/country 

As a user I want to be able to create new travel reviews so that I can share my travel experiences 

As a user I want to be able to edit travel review entries so that I can add any new information 

As a user I want to be able to delete a destination review entry 

As a user I want to be able to search for a specific destination so that I can save time by not needing to scroll down on recent destinations

**EPIC 4 - Profiles**

As a user I want to create a profile so that when I sign up, users can navigate to my profile and see the reviews I wrote
 
As a user I want to edit my profile so that I can make changes when needed 

As a user I want to view another users profile so that I can see all their posted destination reviews 

**EPIC 5 - Photography** 

As a user I want to see photography posts by other users so that I can see how they have captured their visited destination 

As a user I want to be able to create photography posts so that I can share it with my community 

As a user I want to be able to edit my photography post so that I can add or delete any pictures 

As a user I want to be able to delete a photography post

**EPIC 6 - Stand alone pages**

As a site owner I would like a homepage so that site users are greeted with a welcoming landing page explaining the site and has key links 

As a developer I need to implement a 403 error page for unauthorised users to be redirected so that I can secure my views 

As a developer I need to implement a 404 error page so that users are alerted when they have landed on a page that does not exist 

As a developer I need to implement a 500 error page so that users are alerted when an internal server error occurs

**EPIC 7 - Deployment** 

As a developer I need to deploy the project to heroku so that it is live for users 

**EPIC 8 - Documentation**

Task: 

Complete the readme documentation 

### The Scope Plane

* The site must have responsive design, it should be fully functional on all devices from 320px and above.

* Hamburger menu must be displays on mobile devices.

* Ability to perform CRUD functionality on the Destination Reviews and the Photography Posts.

* Restricted roles based on features.

* Home must contain information about the site and quick links to some pages.

### The Surface Plane

#### Design 

#### Colour Scheme

The main colour schemes for the website are as follows:

* White (#FFFFFF) – This colour was used for the background of the website and for text inside all buttons.

* Black (#000000) – This colour was used for all text used in the website and all button background colours.

* Blue (#007EA7) – This colour was used in two places. First, it was used for the active class, this way the user will know on what page they are on. Secondly, it is used for when the user hovers over the social media icons.

#### Typography 

Three fonts were used throughout the website, these were:

* Playfair Display – Used for all heading levels across the website

* Dosis – Used for all other text across the website

* Nunito – Used only for the text on the navbar

#### Imagery 

The website logo was designed using Canva and matches the colour scheme of the website.

All images used across the website are my photographs taken from my own travels around Europe.

### Technologies

* HTML
    * The structure of the website was developed using HTML as the main language.

* CSS
    * The website was styled using custom CSS in an external file.

* JavaScript
    * JavaScript was used to create the modal where the users can update/edit their profile. 
 
* Python
    * Python was the main programming language used for the application using the Django framework.

* Visual Studio Code
    * The website was developed using Visual Studio Code IDE.

* GitHub
    * Source code is hosted on GitHub.

* Git
    * Used to commit and push code during the development of the website.

* Font Awesome
    * This was used for the social media icons that can be seen on the footer of the website.

* Canva
    * This was used to create thew website logo which can be seen on the header of the website and it was used to create the design of the favicon.

* Favicon.io
    * Favicon files were created at [favicon.io](https://favicon.io/)

### Deployment 

#### Version Control 

The site was created using Visual Studio Code editor and pushed to GitHub.

The following git commands were used throughout development to push the code to the remote repo:

* *git add* - This command was used to add file(s) to the staging area before they are committed.

* *git commit -m “commit message”* – This command was used to commit changes to the local repository queue ready for the final step.

* *git push* – This command was used to push all committed code to the remote repository on GitHub.
