from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

base_url = "https://www.numbeo.com/cost-of-living/in/"

def extract_price(s: str) -> float:
    match = re.search(r"([\d,]+(\.\d{1,2})?)", s)
    if match:
        return float(match.group(1).replace(",", ""))
    return 0.0

def calc_income_minus_expenditure(city: str, income: float, options) -> float:
    page = urlopen(f'{base_url}{city}?displayCurrency={options.get("currency")}')
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    costs = soup.find_all("span", attrs={"class": "emp_number"})

    centre_rent_row = soup.find(lambda tag: tag.name == "tr" and "Apartment (1 bedroom) in City Centre" in tag.text)
    outskirts_rent_row = soup.find(lambda tag: tag.name == "tr" and "Apartment (1 bedroom) Outside of Centre" in tag.text)
    three_bedroom_city_centre_row = soup.find(lambda tag: tag.name == "tr" and "Apartment (3 bedrooms) in City Centre" in tag.text)
    three_bedroom_outskirts_row = soup.find(lambda tag: tag.name == "tr" and "Apartment (3 bedrooms) Outside of Centre" in tag.text)

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

    if options.get("city_centre"):
        return income - single_person_cost - centre_rent
    elif options.get("outskirts"):
        return income - single_person_cost - outskirts_rent
    elif options.get("three_bedroom_city_centre"):
        return income - family_of_four_cost - three_bedroom_city_centre_rent
    elif options.get("three_bedroom_outskirts"):
        return income - family_of_four_cost - three_bedroom_outskirts_rent
    return income - single_person_cost