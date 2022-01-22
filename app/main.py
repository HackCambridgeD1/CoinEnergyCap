from flask import Flask, render_template
from app.sources.cryptocurrency_data_analysis.default_analysis_set import get_default_analysis_set, get_annual_energy_consumption_in_j_from_timestamp
from app.sources.cryptocurrency_data_analysis.energy_consumption_calculations import to_scientific_notation, to_twh_from_j, j_to_co2_kg_AVG
from app.sources.cryptocurrency_api_connections.market_cap_api import get_symbol_market_cap_map
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  default_analysis_set = get_default_analysis_set()
  currencies = []
  caps = get_symbol_market_cap_map()
  for an in default_analysis_set:
    ec = to_twh_from_j(get_annual_energy_consumption_in_j_from_timestamp(an))
    co2 = to_scientific_notation(j_to_co2_kg_AVG(ec))
    sym = an.metadata.symbol
    cap = caps.get(sym, "N/A")
    entry = [sym, ec, co2, an.price,cap , "TODO"]

    currencies.append(entry)
    # Symbol, Energy Consumed, Co2 produced, Market Cap, Energy/£,
  return render_template("home.html", currencies = currencies)
 # return "<h1>Homepage!</h1>"
  
  
@app.route("/about")
def about():
  return render_template("about.html")
  
  
if __name__ == "__main__":
  app.run(debug=True)

