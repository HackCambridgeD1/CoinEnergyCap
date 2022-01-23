from flask import Flask, render_template
from app.sources.cryptocurrency_data_analysis.default_analysis_set import get_default_analysis_set, get_annual_energy_consumption_in_j_from_timestamp
from app.sources.cryptocurrency_data_analysis.energy_consumption_calculations import to_scientific_notation, to_twh_from_j, j_to_co2_kg_AVG
from app.sources.cryptocurrency_api_connections.market_cap_api import get_symbol_market_cap_map
from app.sources.cryptocurrency_data_analysis.energy_consumption_calculations import tons_oil_to_earth_circumventions, num_trees_to_offset_co2_amount, j_to_co2_kg_UK, j_to_tonnes_of_oil
app = Flask(__name__)
import math

@app.route("/")
@app.route("/home")
def home():
  default_analysis_set = get_default_analysis_set()
  currencies = []
  caps = get_symbol_market_cap_map()

  total_j = 0
  total_co2 = 0

  for an in default_analysis_set:
    ec_j = get_annual_energy_consumption_in_j_from_timestamp(an)
    ec = round(to_twh_from_j(ec_j),3)
    co2_raw = j_to_co2_kg_AVG(ec_j)
    co2 = to_scientific_notation(co2_raw)
    sym = an.metadata.symbol
    cap = caps.get(sym, "N/A")

    perc_uk_energy = j_to_co2_kg_UK(ec_j)
    trips_around_word = tons_oil_to_earth_circumventions(j_to_tonnes_of_oil(ec_j))
    trees = num_trees_to_offset_co2_amount(co2_raw)

    total_j += ec_j
    total_co2 += co2_raw

    entry = [sym, ec, co2, an.price,cap, perc_uk_energy, trips_around_word, trees]

    currencies.append(entry)

    total_perc_uk_energy = j_to_co2_kg_UK(total_j)
    total_trips_around_word = tons_oil_to_earth_circumventions(j_to_tonnes_of_oil(total_j))
    total_trees = num_trees_to_offset_co2_amount(total_co2)


    # Symbol, Energy Consumed, Co2 produced, Market Cap, Energy/£,
  return render_template("home.html", currencies = currencies, totals = [total_perc_uk_energy, total_trips_around_word, total_trees])
 # return "<h1>Homepage!</h1>"
  
  
@app.route("/about")
def about():
  return render_template("about.html")
  
  
if __name__ == "__main__":
  app.run(debug=True)

