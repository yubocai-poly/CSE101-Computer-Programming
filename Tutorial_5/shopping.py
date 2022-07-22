#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSE101 - Computer Programming 
Tutorial 5 - The Intelligent Fridge
Created on Wed Sep 29 21:01:01 2021

@author: Yubo Cai
"""


# Exercise 1 - Printing a Recipe
def print_recipe(recipe):
    """
    Pretty print recipe, which is a dictionary whose keys are
    ingredients and whose values are their corresponding amounts.
    """
    for key, value in recipe.items():
        print(f'{key}: {value}')


# Exercise 2 - Reading a Recipe from a File
def read_recipe(recipe_file_name):
    """
    Read recipe file 'recipe_file_name', and return ingredients as a
    dictionary whose keys are ingredients and whose values are the
    corresponding amounts.
    """
    with open(recipe_file_name, 'r') as infile:
        recipe = {}
        for line in infile:
            if line == '\n':
                continue
            name, amount = line.strip().split(',')[0].strip(), int(
                line.strip().split(',')[1].strip())
            recipe[name] = amount

    return recipe


# Exercise 3 - Writing a Recipe to a File
def write_recipe(recipe, recipe_file_name):
    """
    Write recipe to a file named recipe_file_name.
    """
    with open(recipe_file_name, 'w') as outfile:
        for key, value in recipe.items():
            outfile.write(f'{key}, {value}\n')


# Exercise 4 - Introducing Fridges
def read_fridge(fridge_file_name):
    """
    Read fridge file 'fridge_file_name', and return the ingredients
    held in the given fridge as an ingredient=amount dictionary.
    """
    fridge_dict = {}
    with open(fridge_file_name, 'r') as infile:
        for line in infile:
            if line == '\n':
                continue
            name, amount = line.strip().split(',')[0].strip(), int(
                line.strip().split(',')[1].strip())
            if name in fridge_dict:
                fridge_dict[name] += amount
            else:
                fridge_dict[name] = amount

    return fridge_dict


# Exercise 5 - Can I Cook a Given Dish?
def is_cookable(recipe_file_name, fridge_file_name):
    """
    Return True if the contents of the fridge named fridge_file_name
    are sufficient to cook the recipe named recipe_file_name.
    """
    recipe_dict = read_recipe(recipe_file_name)
    fridge_dict = read_fridge(fridge_file_name)

    for name, amount in recipe_dict.items():
        if name not in fridge_dict:
            return False
        if fridge_dict[name] < amount:
            return False

    return True


# Exercise 6 - Adding up recipes
def add_recipes(recipes):
    """
    Return a dictionary representing the sum of all of
    the recipe dictionaries in recipes.
    """
    result = {}
    for el in recipes:
        for name, amount in el.items():
            if name in result:
                result[name] += amount
            else:
                result[name] = amount

    return result


# Exercise 7 - Creating a Shopping List
def create_shopping_list(recipe_file_names, fridge_file_name):
    """
    Return the shopping list (a dictionary of ingredients and
    amounts) needed to cook the recipes named in recipe_file_names,
    after the ingredients already present in the fridge named
    fridge_file_name have been used.
    """
    result = {}
    need_lis = []

    # 我们先把所有的食材都加入到一个列表里面，然后合并到一个字典里面
    for el in recipe_file_names:
        need_lis.append(read_recipe(el))
    need_dict = add_recipes(need_lis)

    # 找到我们现在冰箱里有的内容
    fridge_dict = read_fridge(fridge_file_name)

    # 把冰箱里的内容和需要的内容合并, 得出我们的购物清单
    for name, amount in need_dict.items():
        if name not in fridge_dict:
            result[name] = amount
        elif need_dict[name] > fridge_dict[name]:
            result[name] = amount - fridge_dict[name]
    return result


# Exercise 8 - Computing Total Prices
def total_price(shopping_list, market_file_name):
    """
    Return the total price in millicents of the given shopping_list
    at the market named market_file_name.
    """
    total_price = 0
    for name, amount in shopping_list.items():
        with open(market_file_name, 'r') as infile:
            for line in infile:
                if line == '\n':
                    continue
                if line.strip().split(',')[0].strip() == name:
                    total_price += amount * int(
                        line.strip().split(',')[1].strip())

    return total_price


# Exercise 9 - Where Should I Shop?
def find_cheapest(shopping_list, market_file_names):
    """
    Return the name of the market in market_file_names
    offering the lowest total price for the given shopping_list,
    together with the total price.
    """
    cheapest_market = ''
    cheapest_price = 100000000
    for market in market_file_names:
        price = total_price(shopping_list, market)
        if price < cheapest_price:
            cheapest_price = price
            cheapest_market = market

    return (cheapest_market, cheapest_price)


# Exercise 10 - Putting Things Together
def update_fridge(fridge_name, recipe_names, market_names, new_fridge_name):
    """
    Compute the shopping list for the given recipes after the ingredients
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
    print(f'Market: {market_name}\nTotal cost: {expense}')

    write_recipe(dic_fridge, new_fridge_name)


# Exercise 11 (optional) - Distributed Shopping
def market_to_list(market_file_names):
    """辅助函数将market_file_names转换为一个列表"""
    lis = []
    for market in market_file_names:
        with open(market, 'r') as infile:
            market_dict = {}
            for line in infile:
                if line == '\n':
                    continue
                name, amount = line.strip().split(',')[0].strip(), int(
                    line.strip().split(',')[1].strip())
                market_dict[name] = amount
            lis.append(market_dict)
    return lis


def distributed_shopping_list(shopping_list, market_file_names):
    """
    Distribute shopping_list across the markets named in market_file_names
    to minimize the total cost.
    """
    # shopping_list是一个字典，里面的key是食材，value是数量
    # market_file_names是一个列表，里面的元素是文件名

    optimal_list = {}
    market_list = market_to_list(market_file_names)
    
    # 我们先建一个list，方便我们访问数据以及比较
    list_cheapest = []
    for i in range(len(market_list)):
        list_cheapest.append(f'market{i+1}.txt')
        list_cheapest.append({})
    print(list_cheapest)
        
    # 我们通过循环，把最便宜的市场放到list_cheapest里面
    for name, amount in shopping_list.items():
        index = 0
        price = 100000000
        for i in range(len(market_list)):
            if name in market_list[i]:
                if market_list[i][name] < price:
                    price = market_list[i][name]
                    index += 1
        list_cheapest[index * 2 - 1][name] = amount

    # 我们将list_cheapest转换为一个字典, 最后呈现给用户
    for i in range(len(list_cheapest)//2):
        optimal_list[list_cheapest[i*2]] = list_cheapest[i*2+1]
        
    return optimal_list
        
