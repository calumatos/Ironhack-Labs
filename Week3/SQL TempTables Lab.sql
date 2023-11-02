#### SQL TEMPORARY TABLES Lab ####

USE sakila;

# Creating a Customer Summary Report
# In this exercise, you will create a customer summary report that summarizes key information about customers in the Sakila database, 
# including their rental history and payment details. The report will be generated using a combination of views, CTEs, and temporary tables.

# Step 1: Create a View
# First, create a view that summarizes rental information for each customer. The view should include the customer's ID, name, 
# email address, and total number of rentals (rental_count).
CREATE VIEW sumary_customer AS
SELECT customer_id, first_name, last_name, email, COUNT(rental_id)
FROM rental
INNER JOIN customer
USING(customer_id)
GROUP BY customer_id;


# Step 2: Create a Temporary Table
# Next, create a Temporary Table that calculates the total amount paid by each customer (total_paid). 
# The Temporary Table should use the rental summary view created in Step 1 to join with the payment table and calculate the total amount paid by each customer.
CREATE TEMPORARY TABLE total_paid AS
SELECT customer_id, SUM(amount) AS total_amount_paid
FROM sumary_customer
INNER JOIN payment
USING(customer_id)
GROUP BY customer_id; 

# Step 3: Create a CTE and the Customer Summary Report
# Create a CTE that joins the rental summary View with the customer payment summary Temporary Table created in Step 2. 
# The CTE should include the customer's name, email address, rental count, and total amount paid.

WITH summary_report AS (
    SELECT customer_id, first_name, last_name, email, COUNT(rental_id) as rental_count, SUM(amount) AS total_amount_paid
	FROM sumary_customer
	INNER JOIN payment
	USING(customer_id)
	GROUP BY customer_id)
    
SELECT * FROM summary_report;

# Next, using the CTE, create the query to generate the final customer summary report, which should include: 
# customer name, email, rental_count, total_paid and average_payment_per_rental, this last column is a derived column from total_paid and rental_count.

WITH summary_report AS (
    SELECT customer_id, first_name, last_name, email, COUNT(rental_id) as rental_count, SUM(amount) AS total_amount_paid
	FROM sumary_customer
	INNER JOIN payment
	USING(customer_id)
	GROUP BY customer_id)
    
SELECT
    customer_id, first_name, last_name, email, rental_count, total_amount_paid, round(total_amount_paid / rental_count, 2) as average_payment_per_rental
FROM summary_report;