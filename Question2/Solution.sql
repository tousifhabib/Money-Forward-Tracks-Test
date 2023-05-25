-- Step 1: Show the list of shops that have a restroom.
-- Select all distinct shop ids, names, prefectures, and cities from the shops table where the restroom column is 1.
SELECT DISTINCT id, name, prefecture, city
FROM shops
WHERE restroom = 1;

-- Step 2: Add a item
-- Insert a new item into the items table with the given name, category, price, and tax rate.
INSERT INTO items (name, category, price, tax_rate)
VALUES ('4-Color Ballpoint Pen', 1, 198, 0.10);

-- Step 3: Change the tax rate to 0.10 for items in the category are not food
-- Update the tax rate of all items in the items table where the category is not equal to 0 to 0.10.
UPDATE items
SET tax_rate = 0.10
WHERE category != 0;

-- Step 4: Delete items in the food category for which the price without tax is 1000 yen or over
-- Delete all items from the items table where the category is 0 (food) and the price
DELETE FROM items
WHERE category = 0 AND price >= 1000;

-- Step 5: Show the list of shops in the Kanto region ('Ibaraki', 'Tochigi', 'Gunma', 'Saitama', 'Chiba', 'Tokyo', 'Kanagawa')
-- Select all distinct shop ids, names, prefectures, and cities from the shops table where the prefecture column is one of the specified Kanto prefectures.
SELECT DISTINCT id, name, prefecture, city
FROM shops
WHERE prefecture IN ('Ibaraki', 'Tochigi', 'Gunma', 'Saitama', 'Chiba', 'Tokyo', 'Kanagawa');

-- Step 6: List the top 20 cheapest foods
-- Select the first 20 distinct items' ids, names, and prices from the items table where the category is 0 (food), ordered by price and then by id if prices are the same.
SELECT DISTINCT id, name, price
FROM items
WHERE category = 0
ORDER BY price, id
LIMIT 20;

-- Step 7: Count up the total number of items for each category
-- Select distinct categories and the count of items for each category from the items table, grouped by category.
SELECT category, COUNT(*) as item_count
FROM items
GROUP BY category;

-- Step 8: Show the list of prefectures having five or more shops
-- Select distinct prefectures from the shops table, grouped by prefecture, where the count of shops in each prefecture is greater than or equal to 5.
SELECT DISTINCT prefecture
FROM shops
GROUP BY prefecture
HAVING COUNT(*) >= 5;