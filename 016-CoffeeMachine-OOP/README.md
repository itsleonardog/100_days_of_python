# Coffee Machine Simulator (OOP)

Welcome to the Coffee Machine Simulator! This object-oriented Python program allows you to interact with a virtual coffee machine, offering three delightful drinks: espresso, latte, and cappuccino.

## Table of Contents

1. [Description](#description)
2. [File Structure](#file-structure)
3. [Usage](#usage)
4. [Reports](#reports)
5. [Turning Off the Machine](#turning-off-the-machine)

## Description

The Coffee Machine Simulator is an object-oriented console-based application that mimics the functionality of a coffee vending machine. It manages resources, processes orders, accepts payments, and provides delicious beverages. The program is divided into different modules, each serving a specific purpose, providing a clean and modular codebase. The modules include:

- **coffee_maker.py**: Handles the coffee-making process, manages resources, and calculates the cost of each beverage.

- **menu.py**: Defines the menu of available beverages, including their ingredients and costs.

- **money_machine.py**: Manages the financial transactions, including checking for sufficient payment and providing change.

- **main.py**: Acts as the main driver for the program, handling user input and orchestrating the interactions between the different modules.

## File Structure

- **coffee_maker.py**: Contains the `CoffeeMaker` class, responsible for managing resources and brewing coffee.

- **menu.py**: Contains the `Menu` class, which defines the menu of available drinks with their respective ingredients and costs. Each menu item is represented by the `MenuItem class, which includes the name, cost, and ingredients (water, milk, coffee).

- **money_machine.py**: Contains the `MoneyMachine` class, handling financial transactions, including payment and change calculation.

- **main.py**: The main script that utilizes the classes defined in the other files to run the Coffee Machine Simulator.

## Usage

To use the Coffee Machine Simulator, follow these simple steps:

1. Run the `main.py` script.
2. Choose your desired drink: espresso, latte, or cappuccino.
3. If you want to turn off the machine, type "off."
4. To get a report of the current resources and profit, type "report."

For each drink order:

- Check if there are enough resources.
- Insert coins when prompted, specifying the number of quarters, dimes, nickels, and pennies.
- Receive your change if the payment is successful.
- Enjoy your freshly made coffee!

## Reports

You can check the current status of the coffee machine by typing "report." This will display the available resources (water, milk, coffee) and the total profit earned.

## Turning Off the Machine

To turn off the Coffee Machine Simulator, simply type "off" when prompted for a drink choice. This will exit the program.

Feel free to explore and modify the code in each module to enhance or customize the functionality of the Coffee Machine Simulator. Enjoy your coffee-making experience!