from neo4j import GraphDatabase

class DBinteraction:
    def __init__(self, uri="neo4j://localhost:7687", user="neo4j", password="password", database=None):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.database = database


    def close(self):
        self.driver.close()

    def send_query(self,query,data=None):
        try:
            answer = self.driver.execute_query(query, database_=self.database,parameters_=data)
        finally:
            self.close()

        return answer.records
