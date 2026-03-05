SELECT
	strftime('%Y-%m', InvoiceDate) as year_month,
	count(distinct invoiceno) as order_cnt,
	sum(quantity * unitprice) as sales,
	avg(quantity * unitprice) as avg_order_value
	from clean_orders
	GROUP by year_month
	order by year_month;