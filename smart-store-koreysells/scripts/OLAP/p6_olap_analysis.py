import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('data/dw/smart_sales.db')

# OLAP Query
query = """
SELECT 
    p.category,
    SUM(s.sales_amount) AS total_sales
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY total_sales DESC;
"""

# Run query
df = pd.read_sql_query(query, conn)

# Close connection
conn.close()

# Plot
plt.figure(figsize=(10,6))
plt.bar(df['category'], df['total_sales'])

plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot
plt.savefig('scripts/OLAP/p6_sales_by_category.png')
plt.show()