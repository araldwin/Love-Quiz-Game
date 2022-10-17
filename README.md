# Developer: Aldwin Arriola

![Image](docs/pqg-quizgame-main.png)

[Live website](https://love-quiz-game.herokuapp.com/)

## Table of content
1. [Purpose of the project](#purpose-of-the-project)
2. [User stories](#user-stories)
3. [Features](#features)
4. [Color scheme](#color-scheme)
5. [Flowchart](#flowchart)
6. [Technology](#technology)
7. [Testing](#testing)
   - 7.1 Code Validation
   - 7.2 Fixed bugs
   - 7.3 Test cases
8. [Deployment](#deployment)
9. [Credits](#credits)

## Purpose of the project
The purpose of this project is for Project #3(Python), this is part of me achieving the Diploma in Full Stack Software Development at [Code Institute](https://codeinstitute.net/). Besides it is another General Knowledge, Fun Trivia question quiz game project, it can provide additional knowledge for the User.

## User stories
As a user:
  - there must be a main menu with a graphic welcome message.
  - there must be a username input.
  - there should be a choice whether I'm ready to play or not.
  - I should have a choice to answer each question.
  - question number must be displayed.
  - the score of correct answer should be displayed.
  - if my answer is wrong, I should see the correct answer to the question.
  - every correct answer should increase my score.
  - after I answer all the questions I should see the total of my final score.
  - at the end of the game I should have a options whether to play the game again or not.

## Features
- ### A Simple, Easy to Remember URL:[https://love-quiz-game.herokuapp.com/](https://love-quiz-game.herokuapp.com/)
-----
### Main Menu
 - <details>
       <summary> Display Welcome Message </summary>
       <img src="docs/pqg-mainwelcome.png">
       </details>

       - It has a graphic welcome message.

### User name input
- <details>
       <summary> Ask User for Username input </summary>
       <img src="docs/pqg-usernameinputvalidation.png">
       </details>

       - User are not allowed to use Special Characters.
       - User are not allowed to have a more than 15 Characters.


### Play game options
- <details>
       <summary> start option screen shot </summary>
       <img src="docs/pqg-startoption.png">
       </details>

       -  User may type input "start,Start,sTaRt, ..." only.
       -  when user input is valid it will display a message to proceed into the main game.

- <details>
       <summary> exit screen shot </summary>
       <img src="docs/pqg-exitoption.png">
       </details>

       -  User may type input "exit,EXIT,exit, ..." only.
       -  when user input is valid it will display a message quote and exit the game. 

### Main Game
- <details>
       <summary> Display Question no., Question, and Option screen shot</summary>
       <img src="docs/pqg-displayqo.png">
       </details>

- <details>
       <summary> User answer input validation screen shot</summary>
       <img src="docs/pqg-answerinputval.png">
       </details>

       - User must only select numbers from 1 - 4 or else it will be invalid and return to input an answer.
       - after choosing a valid answer it will proceed to the next question.

- <details>
       <summary> check user answer screen shot</summary>
       <img src="docs/pqg-checkuseranswer.png">
       </details>

       - when User answer is wrong, it will display a message "Incorrect", 
         after that it will display the correct answer, and then display the User's current score.
       - if the User answer is correct, it will display a message "Correct", 
         and add +1 score to User's current score.

### End game options
- <details>
       <summary> display final score screen shot </summary>
       <img src="docs/pqg-displayfs.png">
       </details>

       - when User are finish answering all the question, it will display a message "Congratulations...
         Calculating total of score..." 
       - it will display Final Score of the User's all correct answers out of total lenght of questions.

- <details>
       <summary> play again screen shot </summary>
       <img src="docs/pqg-playagainoption.png">
       </details>

       - User may tpye "yes,YES,yEs, ..." to play again.

- <details>
       <summary> exit game screen shot </summary>
       <img src="docs/pqg-playagainquit.png">
       </details>

       - User may tpye anything to exit the game except "yes,YES,yEs, 'space'Yes ..."
       - it will display a quote message and "exiting the game..."


-----

 - ### Future features
    - Add more questions 
    - Make questions random
    - Highest scores
 -----     
## Color scheme
- [termcolor](https://pypi.org/project/termcolor/) - Module used to achieve text color in Terminal.
  - How to install termcolor in Python [(Click the link)](https://blog.finxter.com/how-to-install-termcolor-in-python/).
  - How to import and use termcolor in python [(Click the link)](https://pypi.org/project/termcolor/).
    
- <details>
       <summary> Color Scheme screen shot</summary>
       <img src="docs/pqg-colorscheme.png" width="40%">
       
     - I used these colors to make the quiz app text look good and enhance user experience.
       - Red - For Incorrect and Invalid text.
       - Blue - For correct answer text.
       - Green - Mostly message text before entering answer to input.
       - Yellow - Welcome message, current score, final score text.
       - White - Is normal or default text color from the terminal.
       </details>

-----
## Flowchart

- [Quiz Game flowchart](https://lucid.app/lucidchart/682080d9-52a3-4cfb-97e4-d4db0ea5a972/edit?viewport_loc=-374%2C-119%2C2994%2C1481%2C0_0&invitationId=inv_187ec8c7-02cc-423c-b08d-85ee8d078fe9#)

- <details>
       <summary> Flowchart Screenshot</summary>
       <img src="docs/pqg-flowchart.png" width="100%">
       </details>


-----
## Technology
### Languages used
- [Python](https://www.python.org/)

### Python Module/Package

- [time](https://realpython.com/python-time-module/#:~:text=Python's%20time%20module%20provides%20a,the%20epoch%20called%20localtime()%20.&text=Notice%20that%20tm_isdst%3D0%20.,applicable%20for%20the%20given%20time.)
- [sys](https://www.geeksforgeeks.org/python-sys-module/#:~:text=The%20sys%20module%20in%20Python,interact%20strongly%20with%20the%20interpreter.)
- [termcolor](https://pypi.org/project/termcolor/)
- [pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) - ASCII art figlet_format used for Main menu banner Quiz Game.

### Others
- [Git](http://gitscm.com) - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [Gitpod](https://gitpod.io) - IDE used to code the project.
- [GitHub](https://github.com) - GitHub is used to store the project's code after being pushed from Git.
- [Lucidchart](https://www.lucidchart.com/) - Tools used to build a flowchart.
- [Pep8](http://pep8online.com/) - Use to validate code. 
- [Pylint.org](https://pypi.org/project/pylint/) - Used to improve and correct my code.
- [Termcolor](https://pypi.org/project/termcolor/) - Module used to achieve text color in Terminal.
- Visual Studio Code for Windows - IDE used to code the project.
- Windows Snipping Tool - Used to save the screen shot.

-----

## Testing

### 7.1 Code Validation
- <details>
       <summary>PEP8 Python Validation screen shot</summary>
       <img src="docs/pep8validation.png">
       
     - **No Errors or Warnings found**.
       </details>
       - <details>
              <summary>Pylint Validation screen shot</summary>
              <img src="docs/pylintvalidation.png">
              
       - **No Errors or Warnings found**.
              </details>
------

### 7.2 fixed bugs
Bugs

- When typing username, it has no validation, anything can be input like special characters and there is no limit on how many charcters can be entered. and when nothing is written it can also continue in the game.
   - <details>
       <summary>To fix</summary>
       - I put a conditional statement.

      ------

       <img src="docs/username_bugfixed.png" width="50%">
       </details>

- Score and question_index do not increment after each correct answer and question.
   - <details>
       <summary>To fix</summary>
       - To solve the error, I mark the variable as ***global***.

      ------

       <img src="docs/score_bugfixed.png">

      ------

       <img src="docs/questionindex_bugfixed.png">
       </details>


- If User choose playing again , the incrementing of the question number and score continues where it should the score and question number back into zero.
   - <details>
       <summary>To fix</summary>
       - To solve the error, I mark the variable as ***global***.

      ------

        <img src="docs/repeatgame_bugfixed.png">
       </details>

- Creating global variables and global key gives me problem when checking it into pylint.<br>When it comes to pylint, pylint wants to avoid using global variable.<br>Avoid to use constant and modify the value that was declared outside of any function that are in all caps is the naming convention. since the constant should not change its value
    - <details>
       <summary>pylint error screen shot</summary>
       <img src="docs/pylintglobalfixed.png">
       </details>
    - <details>
        <summary>To fix</summary>
        <img src="docs/pylinterrorfixed.png">
        </details>

        1. remove global variable QUESTION_INDEX and PLAYER_SCORE and reposition this inside main function as local variable.
        2. reposition incrementing player_score, question_index and conditional statement inside main function.
        3. add parameters player_score and total_of_question to check_and_display_final_score function.

### 7.3 Test Cases
| Test<br>Case<br>ID | Test Case<br>Description | Test Steps | Test Data | Expected<br>Result | Actual<br>Result| Pass/Fail |
| :---: | :---: | --- | --- |--- | :---: | :---: |
| TC01 | Username input<br>Valid. | 1. Go to site [https://love-quiz-game.herokuapp.com/](https://love-quiz-game.herokuapp.com/).<br>2. Type a username input.<br>3. Press Enter. | Username =<br>Aldwin | User should<br>proceed to start/exit option. | As Expected | Pass<br><details> <summary>Test case 01 screen shot</summary> <img src="docs/tc01.png"> </details> |
| TC02 | Username input<br>Invalid. | 1. Go to site [https://love-quiz-game.herokuapp.com/](https://love-quiz-game.herokuapp.com/).<br>2. Type a username input.<br>3. Press Enter. | Username =<br>aldwin@codeinstitute | 1. User should not<br>proceed to start/exit option.<br>2. User will be ask <br>to Enter username again. | As Expected | Pass<br><details> <summary>Test case 02 screen shot</summary> <img src="docs/tc02.png"> </details> |
| TC03 |  User main menu option<br>(starting the game). | 1. Go to site [https://love-quiz-game.herokuapp.com/](https://love-quiz-game.herokuapp.com/).<br>2. Type a correct username input.<br>3. Press Enter.<br>4. Type Start.<br>5. Press Enter. | Type  = start | User should <br>proceed to<br>the Quiz first question. | As Expected |Pass<br><details> <summary>Test case 03 screen shot</summary> <img src="docs/tc03.png"> </details> |
| TC04 |  User main menu option<br>(Exiting the game). | 1. Go to site [https://love-quiz-game.herokuapp.com/](https://love-quiz-game.herokuapp.com/).<br>2. Type a correct username input.<br>3. Press Enter.<br>4. Type Exit.<br>5. Press Enter. | Type = exit | User should <br>exit the game. | As Expected | Pass<br><details> <summary>Test case 04 screen shot</summary> <img src="docs/tc04.png"> </details> |
| TC05 |  Check User Correct answer. | 1. Continuing procedure from TC03<br>(Question number 1).<br>2. Type the correct answer.<br>3. Press Enter. | Type = 2<br>(is the correct answer<br>in Question number 1). | 1. Display Message Correct.<br>2. Display user current score.<br>3. User should proceed to<br>the next question. | As Expected | Pass<br><details> <summary>Test case 05 screen shot</summary> <img src="docs/tc05.png"> </details> |
| TC06 |  Check User Incorrect answer. | 1. Continuing procedure from TC05<br>(Question number 2).<br>2. Type the Incorrect answer.<br>3. Press Enter. | Type = 3<br>(is the incorrect answer<br>in Question number 2). | 1. Display message<br>answer is Incorrect.<br>2. Display the Correct asnwer.<br>3. Display user current score.<br>4. User should proceed to<br>the next question. | As Expected | Pass<br><details> <summary>Test case 06 screen shot</summary> <img src="docs/tc06.png"> </details> |
| TC07 |  Check User valid answer. | 1. Continuing procedure from TC06<br>(Question number 3).<br>2. Type Alphabet answer.<br>3. Press Enter.<br> | Type = cat and 5. | 1. Display message<br>invalid input.<br>2. Display choose asnwer<br>between 1 - 4.<br>3. User will be ask <br>to Enter answer again. | As Expected | Pass<br><details> <summary>Test case 07 screen shot</summary> <img src="docs/tc07.png"> </details> |
| TC08 |  Check Total of user score. | 1. Continuing procedure from TC07<br>(Question number 4).<br>2. Answer all the<br>given questions.<br>3. By the end of the questions. | Answer all questions | 1. Display message<br>Congratulations.<br>2. Display message calculating<br>total of scores.<br>3. Display the <br> final score.<br>4. User will proceed to end<br>game options | As Expected | Pass<br><details> <summary>Test case 08 screen shot</summary> <img src="docs/tc08.png"> </details> |
| TC09 |  Play again. | 1. Continuing procedure from TC08<br>(end game options).<br>2. Type yes.<br>3. Press enter. | Type = yes | 1. User will repeat<br>the game, starting<br>to Question number 1. | As Expected | Pass<br><details> <summary>Test case 09 screen shot</summary> <img src="docs/tc09.png"> </details> |
| TC10 | End game | 1. Continuing procedure from TC08<br>(end game options).<br>2. Press enter. | Press enter | 1. Display message quote<br>2. Display message exiting the game. | As Expected | Pass<br><details> <summary>Test case 10 screen shot</summary> <img src="docs/tc10.png"> </details> |

   
-----
## Deployment
- via gitpod
   - go to and log in to [github](https://github.com/).
   - after login. on the top right side of the page next to the bell icon click on the "+" and select "New repository".
   - now i can create a new repository. put repository template, repository name, its description and other options, after that just go to the bottom and press "Create repository" and then it take me to gitpod.

- via Heroku
     - go and log in to [Heroku]((https://id.heroku.com/login))
     - from the Heroku dashboard "Create new app".
     - name app adjust it to something unique, select region and clicked   "Create   app".
     - after creating, proceed to the Settings and click "Config Var", in field Type the key is PORT and the value is 8000, and then click "Add".
     - next step is Scroll down and "Add buildpack". Add "python" buildpack first and then save changes, then add "nodejs" and click save again. build pack should be in order. python on top   and nodejs  at the bottom.
     - go to Deploy section. In deployment method select "GitHub", and confirm to "connect to GitHub".
     - search for Github repository name and clicked "connect".
     - scroll down and choose if "Automatic deploys" or "Manual deploy", then click "Deploy branch".
     - after clicking "Deploy branch" the app is being built, App will successfully deploy after couple of minutes and click "view".
     - the link will proceed and open our mock terminal.

## Credits
   - [bobbyhadz.com](https://bobbyhadz.com/) - learning guide.
   - [finxter](https://blog.finxter.com/how-to-install-termcolor-in-python/) - guide on how to install termcolor in Python.
   - [freecodecamp.org](https://www.freecodecamp.org/) - learning guide.
   - [geeksforgeeks.org](https://www.geeksforgeeks.org/) - learning guide.
   - [peps.python.org](https://peps.python.org/pep-0008/) – style guide for Python code.
   - [programiz.com](https://www.programiz.com/) - learning guide.
   - [pypi.org](https://pypi.org/project/termcolor/) - guide on how to use termcolor module.
   - [quiztriviagames.com](https://www.quiztriviagames.com/multiple-choice-trivia-questions/) - get my questions and answers.
   - [realpython.com](https://realpython.com/python-pep8/) - guide for Python Code.
   - [stackoverflow.com](https://stackoverflow.com/) - learning guide.
   - [W3C School](https://www.w3schools.com/) - for more knowledge that I learned.
   - [Youtube.com](https://www.youtube.com/) - for Python tutorials.
## Acknowledgements
   - @Mr. Rohit to my mentor
   - @Jay Rodriguez
   - @Zack Owen
   - @Warwick Hart
   - @Student Support
   - @Slack community
   - @Code institute

## Disclaimer
   - love-quiz-game was created for educational purpose only.