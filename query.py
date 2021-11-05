#!/usr/bin/env python

from pprint import pprint
from SPARQLWrapper import SPARQLWrapper, JSON

import interests
import countries


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

