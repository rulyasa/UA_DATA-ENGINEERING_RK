/*
 Завдання на SQL до лекції 03.
 */


/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/
-- SQL code goes here...
-- Підрахунок кількості фільмів у кожній категорії
SELECT
    c.name AS category,
    COUNT(fc.film_id) AS film_count
FROM
    category AS c
    JOIN film_category AS fc
        ON c.category_id = fc.category_id
GROUP BY
    c.name
ORDER BY
    film_count DESC;


/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
-- SQL code goes here...
-- Підраховуємо скільки разів були взяті фільми в прокат кожного актора, обмежуючи вивід 10 позиціями по спаданню
SELECT
    a.actor_id,
    a.first_name,
    a.last_name,
    COUNT(r.rental_id) AS total_rentals
FROM
    actor AS a
    JOIN film_actor AS fa
        ON a.actor_id = fa.actor_id
    JOIN inventory AS i
        ON fa.film_id = i.film_id
    JOIN rental AS r
        ON i.inventory_id = r.inventory_id
GROUP BY
    a.actor_id,
    a.first_name,
    a.last_name
ORDER BY
    total_rentals DESC
LIMIT 10;


/*
3.
Вивести категорія фільмів, на яку було витрачено найбільше грошей
в прокаті
*/
-- SQL code goes here...
-- CTE рахує суму всіх платежів за оренду фільмів у розрізі категорій
WITH category_payments AS (
    SELECT
        c.category_id,
        c.name AS category_name,
        SUM(p.amount) AS total_amount
    FROM
	-- Беремо кожну категорію. Через film_category знаходимо всі фільми, які до неї належать. Без цієї таблиці ми не знаємо, які фільми входять у конкретну категорію.
        category AS c
        JOIN film_category AS fc
            ON c.category_id = fc.category_id
	-- Підтягуємо дані фільмів, тут вони нам потрібні, щоб далі вийти на inventory. Один фільм може бути в кількох категоріях.
        JOIN film AS f
            ON fc.film_id = f.film_id
	-- Фільм не здається в оренду «абстрактно» — здається конкретна копія в магазині. Таблиця inventory — це саме копії фільмів. Кожен запис в inventory = 1 фізична копія в конкретному магазині.
        JOIN inventory AS i
            ON f.film_id = i.film_id
	-- Кожен прокат (rental) посилається на конкретну копію (inventory_id). Тут ми вже отримуємо всі факти прокату фільмів певної категорії.
        JOIN rental AS r
            ON i.inventory_id = r.inventory_id
	-- В payment.amount лежать реальні гроші, які нас цікавлять.
        JOIN payment AS p
            ON r.rental_id = p.rental_id
    GROUP BY
        c.category_id,
        c.name
)
-- На виході CTE отримуємо табличку, з якої селектимо тільки 1 (топ) результат відсортований по спаданню, таким чином отримуючи ім'я категорії та суму всіх прокатів 
SELECT
    category_name,
    total_amount
FROM
    category_payments
ORDER BY
    total_amount DESC
LIMIT 1;


/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/
-- SQL code goes here...
-- Знаходимо фільми, які не представлені в жодному магазині. Використовуємо LEFT JOIN, таким чином відфільтрувавши фільми в яких не проставляється значення inventory_id числом (при такому джоін в них буде значення NULL)
SELECT
    f.film_id,
    f.title
FROM
    film AS f
    LEFT JOIN inventory AS i
        ON f.film_id = i.film_id
WHERE
    i.inventory_id IS NULL
ORDER BY
    f.title;

/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
-- SQL code goes here...
-- Стандартний JOIN на всі зв'язані таблиці, фільтруючи по категорії "Children", сортуємо за спаданням і виводимо тільки 3 актора з найбільшою кількістю.
SELECT
    a.actor_id,
    a.first_name,
    a.last_name,
    COUNT(*) AS film_count
FROM
    actor AS a
    JOIN film_actor AS fa
        ON a.actor_id = fa.actor_id
    JOIN film AS f
        ON fa.film_id = f.film_id
    JOIN film_category AS fc
        ON f.film_id = fc.film_id
    JOIN category AS c
        ON fc.category_id = c.category_id
WHERE
    c.name = 'Children'
GROUP BY
    a.actor_id,
    a.first_name,
    a.last_name
ORDER BY
    film_count DESC
LIMIT 3;