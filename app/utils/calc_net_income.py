from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

base_url = "https://www.numbeo.com/cost-of-living/in/"

def extract_price(s: str) -> float:
    match = re.search(r"([\d,]+(\.\d{1,2})?)", s)
    if match:
        return float(match.group(1).replace(",", ""))
    return 0.0

def calc_costs(city: str, options: dict) -> dict:
    page = urlopen(f'{base_url}{city}?displayCurrency={options.get("currency")}')
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    costs = soup.find_all("span", attrs={"class": "emp_number"})

    centre_rent_row = soup.find(lambda tag: tag.name == "tr" and "1 Bedroom Apartment in City Centre" in tag.text)
    outskirts_rent_row = soup.find(lambda tag: tag.name == "tr" and "1 Bedroom Apartment Outside of City Centre" in tag.text)
    three_bedroom_city_centre_row = soup.find(lambda tag: tag.name == "tr" and "3 Bedroom Apartment in City Centre" in tag.text)
    three_bedroom_outskirts_row = soup.find(lambda tag: tag.name == "tr" and "3 Bedroom Apartment Outside of City Centre" in tag.text)

    if centre_rent_row:
        centre_rent = extract_price(centre_rent_row.find_all('td')[1].text)
    else:
        centre_rent = 0

    if outskirts_rent_row:
        outskirts_rent = extract_price(outskirts_rent_row.find_all('td')[1].text)
    else:
        outskirts_rent = 0

    if three_bedroom_city_centre_row:
        three_bedroom_city_centre_rent = extract_price(three_bedroom_city_centre_row.find_all('td')[1].text)
    else:
        three_bedroom_city_centre_rent = 0

    if three_bedroom_outskirts_row:
        three_bedroom_outskirts_rent = extract_price(three_bedroom_outskirts_row.find_all('td')[1].text)
    else:
        three_bedroom_outskirts_rent = 0

    single_person_cost = extract_price(costs[1].text)
    family_of_four_cost = extract_price(costs[0].text)
    costs_summary = summarize_costs_by_category(soup)

    return {
        "single_person_cost": single_person_cost,
        "family_of_four_cost": family_of_four_cost,
        "centre_rent": centre_rent,
        "outskirts_rent": outskirts_rent,
        "three_bedroom_city_centre_rent": three_bedroom_city_centre_rent,
        "three_bedroom_outskirts_rent": three_bedroom_outskirts_rent,
        "costs_summary": costs_summary
    }

def summarize_costs_by_category(soup: BeautifulSoup) -> dict:
    cost_table = soup.find("table", class_="data_wide_table")
    costs_summary = {}
    current_category = None  # Track the current category

    if not cost_table:
        print("No cost table found.")
        return costs_summary

    rows = cost_table.find_all("tr")

    for row in rows:
        # Check if this row is a category header
        category_header = row.find("div", class_="category_title")
        if category_header:
            current_category = category_header.text.strip()
            costs_summary[current_category] = 0  # Initialize category sum
        
        # Extract cost items under the current category
        columns = row.find_all("td")
        if len(columns) >= 2 and current_category:
            price = extract_price(columns[1].text)
            costs_summary[current_category] += price  # Sum up category costs

    return costs_summary

def calc_income_minus_expenditure(city: str, income: float, options: dict) -> float:
    costs = calc_costs(city, options)

    if options.get("city_centre"):
        return income - costs['single_person_cost'] - costs['centre_rent']
    elif options.get("outskirts"):
        return income - costs['single_person_cost'] - costs['outskirts_rent']
    elif options.get("three_bedroom_city_centre"):
        return income - costs['family_of_four_cost'] - costs['three_bedroom_city_centre_rent']
    elif options.get("three_bedroom_outskirts"):
        return income - costs['family_of_four_cost'] - costs['three_bedroom_outskirts_rent']
    return income - costs['single_person_cost']