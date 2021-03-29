from flask import Flask
from random import randint

app = Flask(__name__)



@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    """Takes in 2 strings and displays a funny (but work-appropriate) story using them!"""
    return f"My friend had a {adjective} {noun}"

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Takes in 2 numbers, multiplies them, and displays the results"""
    try:
        number1 = int(number1)
        number2 = int(number2)
        return f"{number1} times {number2} is {int(number1) * int(number2)}"
    except Exception:
        return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<times>')
def sayntimes(word, times):
    if times.isdigit():
        s = ""
        for _ in range(int(times)):
            s += word + " "
        return f"{s}"
    else:
        return "Invalid input. Please try again by entering a word and a number!"

@app.route('/dicegame')
def dicegame():
    n = randint(1,6)
    if n == 6:
        return f"You rolled a {n}. You won!"
    else:
        return f"You rolled a {n}. You lost!"

if __name__ == '__main__':
    app.run(debug=True)



# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
