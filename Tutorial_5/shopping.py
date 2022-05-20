#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:32:07 2021

@author: apple
"""

# Exercise 1
def print_recipe(recipe):
    """Pretty print recipe, which is a dictionary whose keys are
    ingredients and whose values are their corresponding amounts.
    """
    
    for food_name, ingredient in recipe.items():
        print(f'{food_name}: {ingredient}')
        
# Exercise 2
def read_recipe(recipe_file_name):
    """Read recipe file 'recipe_file_name', and return ingredients as a
    dictionary whose keys are ingredients and whose values are the
    corresponding amounts.
    """
    
    recipe_dict = {}
    with open(recipe_file_name, 'r') as infile:
        for line in infile:
            if line == '\n':
                continue
            data = line.strip().split(',')
            food_name1 = data[0].strip()
            food_amount = data[1]
            recipe_dict[food_name1] = int(food_amount)
        
    return recipe_dict

# Exercise 3
def write_recipe(recipe, recipe_file_name):
    """Write recipe to a file named recipe_file_name."""
    with open(recipe_file_name, 'w') as outfile:
        for food_name, ingredient in recipe.items():
            outfile.write(f'{food_name},{ingredient}' + '\n')
    
# Exercise 4
def read_fridge(fridge_file_name):
    """Read fridge file 'fridge_file_name', and return the ingredients
    held in the given fridge as an ingredient=amount dictionary.
    """
    
    fridge_dict = {}
    with open(fridge_file_name, 'r') as infile:
        for line in infile:
            if line == '\n':
                continue
            data = line.strip().split(',')
            food_name1 = data[0].strip()
            food_amount = int(data[1])
            if food_name1 in fridge_dict:
                fridge_dict[food_name1] += food_amount
            else:
                fridge_dict[food_name1] = food_amount
    return fridge_dict

# Exercise 5
def is_cookable(recipe_file_name, fridge_file_name):
    """Return True if the contents of the fridge named fridge_file_name
    are sufficient to cook the recipe named recipe_file_name.
    """
    dic_recipe = read_recipe(recipe_file_name)
    dic_fridge = read_fridge(fridge_file_name)
    
    for food, amount in dic_recipe.items():
        if food not in dic_fridge:
            return False
        elif dic_recipe[food] > dic_fridge[food]:
            return False
        
    return True

# Exercise 6
def add_recipes(recipes):
    """Return a dictionary representing the sum of all of
    the recipe dictionaries in recipes.
    """
    
    result = {}
    for recipe in recipes:
        for food, amount in recipe.items():
            if food not in result:
                result[food] = amount
            else:
                result[food] += amount
    
    return result

# Exercise 7
def create_shopping_list(recipe_file_names, fridge_file_name):
    """Return the shopping list (a dictionary of ingredients and
    amounts) needed to cook the recipes named in recipe_file_names,
    after the ingredients already present in the fridge named
    fridge_file_name have been used.
    """
    lis = []
    for food1 in recipe_file_names:
        lis.append(read_recipe(food1))

    shopping_list = {}
    dic_recipe = add_recipes(lis)
    dic_fridge = read_fridge(fridge_file_name)
    for food, amount in dic_recipe.items():
        if food not in dic_fridge.keys():
            shopping_list[food] = amount
        elif dic_recipe[food] > dic_fridge[food]:
            shopping_list[food] = dic_recipe[food] - dic_fridge[food]
    return shopping_list
            
# Exercise 8
def total_price(shopping_list, market_file_name):
    """Return the total price in millicents of the given shopping_list
    at the market named market_file_name.
    """
    expense = 0
    market = read_recipe(market_file_name)
    for food, amount in shopping_list.items():
        if food in market.keys():
            expense += shopping_list[food] * market[food]
    return expense
            
# Exercise 9 
def find_cheapest(shopping_list, market_file_names):
    """Return the name of the market in market_file_names
    offering the lowest total price for the given shopping_list,
    together with the total price.
    """
    expense_list = []
    for i in range(len(market_file_names)):
        expense_list.append(total_price(shopping_list, market_file_names[i]))
        i += 1
    expense_min = min(expense_list)
    for file_names in market_file_names:
        if total_price(shopping_list, file_names) == expense_min:
            lowest_market = str(file_names)
    return(lowest_market, expense_min)

# Exercise 10
def update_fridge(fridge_name, recipe_names, market_names, new_fridge_name):
    """Compute the shopping list for the given recipes after the ingredients
    present in fridge fridge_name have been used; find the cheapest market;
    and write the new fridge contents to new_fridge_name.
    Print the shopping list, the cheapest market name, and the total amount
    to be spent at that market.
    """
    
    dic_fridge = read_fridge(fridge_name)
    shopping_list = create_shopping_list(recipe_names, fridge_name)
    market_name, expense = find_cheapest(shopping_list, market_names)
    
    for food, amount in shopping_list.items():
        if food not in dic_fridge.keys():
            dic_fridge[food] = amount
        else:
            dic_fridge[food] += amount
    
    print('Shopping list:')
    print_recipe(shopping_list)
    print(f'Market: {market_name}')
    print(f'Total cost: {expense}')
    
    write_recipe(dic_fridge, new_fridge_name)
    
        
    
        
     
    
    
    
    
    
    
    
    