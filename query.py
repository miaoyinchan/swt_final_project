#!/usr/bin/env python

from pprint import pprint

from SPARQLWrapper import SPARQLWrapper, JSON


LEISURE = [
    "bandstand",
    "beach_resort",
    "bird_hide",
    "bowling_alley",
    "dance",
    "dog_park",
    "escape_game",
    "firepit",
    "fishing",
    "fitness_centre",
    "garden",
    "golf_course",
    "hackerspace",
    "horse_riding",
    "ice_rink",
    "nature_reserve",
    "park",
    "picnic_table",
    "playground",
    "resort",
    "sauna",
    "sports_hall",
    "stadium",
    "summer_camp",
    "swimming_area",
    "swimming_pool",
    "tanning_salon",
    "trampoline_park",
    "water_park",
    "wildlife_hide",
    "alphine_hut",
    "apartment",
    "aquarium",
    "artwork",
    "attraction",
    "camp_site",
    "caravan_site",
    "chalet",
    "gallery",
    "guest_house",
    "hostel",
    "hotel",
    "information",
    "motel",
    "museum",
    "theme_park",
    "viewpoint",
    "wilderness_hut",
    "zoo",
    "bar",
    "biergarten",
    "cafe",
    "casino",
    "fast_food",
    "food_court",
    "ice_cream",
    "pub",
    "restaurant",
    "bicycle_rental",
    "boat_rental",
    "car_rental",
]


def get_query(country, interests):
    interests = "({})".format(", ".join(f'"{i}"' for i in interests))

    query  = f"""\
PREFIX osmnode: <https://www.openstreetmap.org/node/>
PREFIX osmway: <https://www.openstreetmap.org/way/>
PREFIX osmrel: <https://www.openstreetmap.org/relation/>
PREFIX osmt: <https://wiki.openstreetmap.org/wiki/Key:>
PREFIX osmm: <https://www.openstreetmap.org/meta/>
PREFIX pageviews: <https://dumps.wikimedia.org/other/pageviews/>
PREFIX osmd: <http://wiki.openstreetmap.org/entity/>
PREFIX osmdt: <http://wiki.openstreetmap.org/prop/direct/>
PREFIX osmp: <http://wiki.openstreetmap.org/prop/>
PREFIX osmps: <http://wiki.openstreetmap.org/prop/statement/>
PREFIX osmpq: <http://wiki.openstreetmap.org/prop/qualifier/>

SELECT ?name ?street ?url ?houseNumber ?city WHERE {{
    SERVICE <https://sophox.org/sparql> {{
        ?subject osmt:name ?name;
                osmt:addr:country "{country}";
                (osmt:tourism|osmt:leisure|osmt:amenity) ?interests;
                osmt:addr:street ?street;
                osmt:website ?url;
                osmt:addr:housenumber ?houseNumber;
                osmt:addr:city ?city .
        FILTER (?interests in {interests})
    }}
}}
LIMIT 5
"""

    return query;


def main():
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    interests = ["museum", "attraction", "hotel", "hackerspace", "restaurant"]
    q = get_query("GB", interests)
    print(q)
    sparql.setQuery(q)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    pprint(results)


if __name__ == "__main__":
    main()

