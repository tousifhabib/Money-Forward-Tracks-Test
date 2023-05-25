# Description
In this challenge you will use a database having information for convenience stores.
The database has four tables, a shops table having the shop information, an employees table having employee information, an items table having information on items for sale, and a sales table having information on sales history.
The data structure for the tables will be written in init/create_db.sql.

## create_db.sql:
```
DROP TABLE IF EXISTS shops;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS sales;
```


## Table that contains information for each shops
```
CREATE TABLE shops (
    id         integer PRIMARY KEY AUTOINCREMENT, -- shop id
    name       varchar NOT NULL,                  -- the shop name
    prefecture varchar NOT NULL,                  -- prefecture
    city       varchar NOT NULL,                  -- city
    restroom   boolean NOT NULL                   -- with(1) or without(0) restroom
);
```

## Table that contains information for each items
```
CREATE TABLE items (
    id       integer PRIMARY KEY AUTOINCREMENT, -- item id
    name     varchar            NOT NULL,       -- the item name
    category integer            NOT NULL,       -- item category (0: food, 1: stationery, 2: daily products, 3: cigarettes, 4: other items)
    price    integer            NOT NULL,       -- price without tax (yen)
    tax_rate float DEFAULT 0.10 NOT NULL        -- tax arte (0.08 or 0.10)
);

```

## Table that contains information for each employees
```
CREATE TABLE employees (
    id      integer PRIMARY KEY AUTOINCREMENT, -- employee id
    name    varchar NOT NULL,                  -- the name of employee
    age     integer NOT NULL,                  -- the age of employee
    shop_id integer NOT NULL                   -- id of the shop the employee belongs to
);
```

## Table that contains information for each sales
```
CREATE TABLE sales (
    id      integer PRIMARY KEY AUTOINCREMENT, -- sales id
    item_id integer NOT NULL,                  -- id of the item which was purchased
    shop_id integer NOT NULL                   -- id of the shop where the item was sold
);
```


# Steps

## Step 1
List the shops that have a restroom.
Write an SQL query to select all the shops that have a restroom in step1.sql.
You will query the columns id (the shop id), name (the shop name), prefecture, and city from the shops table.
The output order of the records can be random but make sure the output results are distinct.

## Step 2
You are adding a new item to the database.
Write an SQL query to add the following item to the items table in step2.sql.
item name: 4-Color Ballpoint Pen
item category: stationery
price without tax: 198 yen
tax rate: 0.10
Use the primary key for the item id.

## Step 3
The tax rate for the items in the database is now 0.08. However the tax rate is changing to 0.10 for items that are not food.
Write an SQL query to change the tax rate for items in the category are not food in step3.sql.

## Step 4
Due to results of sales research, shops are going to stop selling food that is over 1000 yen.
Write an SQL query to delete items in the food category for which the price without tax is 1000 yen or over in step4.sql.

## Step 5
Make a list of shops in the Kanto region (‘Ibaraki’, ’Tochigi’, ‘Gunma’, ‘Saitama’, ‘Chiba’, ‘Tokyo’, ‘Kanagawa’).
Write an SQL query to select all the shops in the Kanto region in step5.sql.
You will query the columns id (the shop id), name (the shop name), prefecture, and city from the shops table.
The output order of the records can be random but make sure the output results are distinct.

## Step 6
List the top 20 cheapest foods. Write an SQL query to sort the items in the food category by price before tax, from lowest price to highest, and return the first 20 items from the items table in step6.sql.
You will query the columns id, name, and price from the items table. Make sure the output results are distinct.
If the prices without tax are the same, put them in the order of smaller id first.
There are guaranteed to be over 20 food items in the database.

## Step 7
Count up the total number of items for each category in the items table.
Write the SQL query in step7.sql.
You will query the columns category and item_count, which is the total number for that category from the items table.
The output order of the records can be random but make sure the output results are distinct.

## Step 8
Make a list of prefectures having five or more shops.
Write an SQL query to select all the matching prefectures in step8.sql.
You will query the prefecture column from the shops table.
The output order of the records can be random but make sure the output results are distinct.