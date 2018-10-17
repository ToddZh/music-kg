from kg import insert_to_neo4j

def add_node(tx):
    tx.run("CREATE ( n:歌手{name:\"周杰伦\"} )")

if __name__ == '__main__':

    # '''
    # insert_to_neo4j.driver_add_node('jj','歌手','身高','175cm','高度')
    # insert_to_neo4j.driver_add_node('Neo4j', 'artist', 'SAYS','okok!','')
    # insert_to_neo4j.driver_add_node('jay', 'artist', 'heigh','175cm','heigh')

    # '''
    graph = insert_to_neo4j.GraphNeo4j()
    graph.driver_add_node("周杰伦","歌手")
    graph.driver_add_node("Jay","专辑")
    graph.driver_add_relation("周杰伦","歌手", "专辑", "Jay","专辑")

