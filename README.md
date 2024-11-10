## Snake Game With PyGame ##

Source: [www.edureka.co](https://www.edureka.co/blog/snake-game-with-pygame/#createthesnake)

A quick tutorial on how to build a Snake game using the **PyGame** library.

This will be broken down into *7x steps*, where in each step I will walk through how to create aspects of the game - from building the screen, moving the Snake to displaying the score.
- **Step 1:** Create the screen
- **Step 2:** Create the Snake
- **Step 3:** Moving the Snake
- **Step 4:** Game over when the Snake hits the boundaries
- **Step 5:** Adding the food
- **Step 6:** Increasing the length of the Snake
- **Step 7:** Displaying the score
#### Creating Your Virtual Environment ####
 You will need to create a virtual environment in your machine to  install the packages needed to run the game 
 ```
Python -m venv Your_Virtual_Environment
 ```
 #### Run Your Virtual Environment
 We will need to run our virtual environment in order to install our libraries/packages
#### Installing PyGame ####
To be able to use the PyGame library we have to install it on your machine.
```
Your_Virtual_Environment\Script\activate        # on Windows
source Your_Virtual_Environment/bin/activate    # on MacOS/Linus

deactivate                                      # Close virtual environment
pip install pygame

pip install -r requirements.txt                 # You can also install from the requirements.txt file

```
#### PyGame Functions ####
These will be the PyGame functions that we will be using along with the descriptions of what they do.
```
init()
```
This will initialise all of the imported PyGame modules.  It returns a tuple telling the developer success/failure of initialisations.
```
display.set_mode()
```
Takes a tuple or a list as it's parameter to create a surface (a tuple is preferred).
```
update()
```
Updates the screen being used.
```
quit()
```
Used to uninitialise everything.
```
set_caption()
```
Will set the saption text at the top of the display screen.
```
event.get()
```
Returns a list of all events.
```
Surface.fill()
```
Will fill the surface with a solid colour.
```
time.Clock()
```
Helps track the time.
```
font.SysFont()
```
Will create a PyGame font from the System font resources.
***Once you have installed PyGame and read through the functions, you are ready to code!***