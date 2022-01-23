from flask import Flask, render_template

from app.sources.cryptocurrency_api_connections.minerstat_api_endpoint import MinerstatApiEndpoint
from app.sources.cryptocurrency_data_analysis.default_analysis_set import get_default_analysis_set, \
    get_annual_energy_consumption_in_j_from_timestamp
from app.sources.cryptocurrency_data_analysis.energy_consumption_calculations import to_twh_from_j, j_to_co2_kg_AVG, \
    TOTAL_ELECTRICITY_CONSUMPTION_UK_J, joule_to_earth_circumventions
from app.sources.cryptocurrency_api_connections.market_cap_api import get_symbol_market_cap_map
from app.sources.cryptocurrency_data_analysis.energy_consumption_calculations import tons_oil_to_earth_circumventions, \
    num_trees_to_offset_co2_amount, j_to_co2_kg_UK, j_to_tonnes_of_oil

app = Flask(__name__)


def format_dollar(num: float, millions=False):
    try:
        if not millions:
            num = format(num, ".2f")
            num += " $"
        else:
            num = format(int(num / 10 ** 6), ",")
            num += " Mil. $"
    except Exception as e:
        num = "N/A"
    return num


def get_energy_representation(energy_joule):
    energy_tw = round(to_twh_from_j(energy_joule), 3)

    if energy_tw < 0.01:
        return format(to_twh_from_j(energy_joule), ".3")
    else:
        return str(energy_tw)


def format_co2(kilos_co2: float):
    return format(int(kilos_co2 / 10 ** 3), ",")


@app.route("/")
@app.route("/home")
def home():
    default_analysis_set = MinerstatApiEndpoint.get_complete_cryptocurrency_set()
    default_analysis_set.sort(key=lambda crypto: -get_annual_energy_consumption_in_j_from_timestamp(crypto))
    currencies = []
    caps = get_symbol_market_cap_map([crypto.metadata.symbol for crypto in default_analysis_set])
    caps = {key: format_dollar(val, True) for key, val in caps.items()}

    total_j = 0
    total_co2 = 0

    for crypto in default_analysis_set:
        ec_j = get_annual_energy_consumption_in_j_from_timestamp(crypto)
        ec_repr = get_energy_representation(ec_j)
        co2_raw = j_to_co2_kg_AVG(ec_j)
        co2_repr = format_co2(co2_raw)
        sym = crypto.metadata.symbol
        cap = caps.get(sym, "N/A")

        perc_uk_energy = round((100 * ec_j / TOTAL_ELECTRICITY_CONSUMPTION_UK_J), 2)
        trips_around_word = format(int(joule_to_earth_circumventions(ec_j)), ",")
        trees = format(int(num_trees_to_offset_co2_amount(co2_raw)), ",")

        total_j += ec_j
        total_co2 += co2_raw

        entry = [sym, ec_repr, co2_repr, format_dollar(crypto.price), cap, perc_uk_energy, trips_around_word, trees]

        currencies.append(entry)

    total_perc_uk_energy = round((100 * total_j / TOTAL_ELECTRICITY_CONSUMPTION_UK_J), 0)
    total_trips_around_word = format(int(joule_to_earth_circumventions(total_j)), ",")
    total_trees = format(int(num_trees_to_offset_co2_amount(total_co2)), ",")

    # Symbol, Energy Consumed, Co2 produced, Market Cap, Energy/£,
    return render_template("home.html", currencies=currencies,
                           totals=[total_perc_uk_energy, total_trips_around_word, total_trees])


# return "<h1>Homepage!</h1>"


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
