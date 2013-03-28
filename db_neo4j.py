#!/usr/bin/env python

"""
Simple example showing node and relationship creation plus
execution of Cypher queries
"""

from __future__ import print_function

# Import Neo4j modules
from py2neo import neo4j, cypher

# Define a row handler...
def print_row(row):
    a, b = row
    print(a["name"] + " knows " + b["name"])

class db_neo4j():

    def __init__(self):

        # Attach to the graph db instance
        self.graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

    def insert_nodes_relation(self, a, b, rel):

        # Create two nodes
        self.node_a, self.node_b = self.graph_db.create(a, b)

        # Join the nodes with a relationship
        rel_ab = self.node_a.create_relationship_to(self.node_b, rel)

    def alice_bob_test(self):

        # Build a Cypher query
        query = "START a=node({A}) MATCH a-[:KNOWS]->b RETURN a,b"

        # ...and execute the query
        cypher.execute(self.graph_db, query, {"A": self.node_a.id}, row_handler=print_row)


if __name__ == "__main__":

    db = db_neo4j()
    db.insert_nodes_relation({"name": "Alice"}, {"name": "Bob"}, "KNOWS")
    db.alice_bob_test()

