pip install builtwith
import builtwith

website = 'https://www.example.com'
tech_info = builtwith.parse(website)

print(tech_info)
