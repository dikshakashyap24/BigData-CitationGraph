# BigData-CitationGraph

This project demonstrates the creation of a citation graph using **Neo4j**, using the <a href="https://snap.stanford.edu/data/com-DBLP.html">DBLP Dataset</a> .It uses Neo4j, where
- **Nodes** represent academic papers.
- **Edges** represent citation relationships.

The graph is constructed from a dataset where each row specifies a citing paper and its references. The pipeline involves building the graph in Neo4j, running the **SimRank algorithm** to compute paper similarity, and reporting the most similar papers for given query nodes.

## Pipeline Overview

The project follows these main steps:

1. **Convert JSON to CSV** 
2. **Load CSV Files into Neo4j (Nodes and Edges)**  
3. **Initialize SparkSession for Neo4j**  
4. **Load Graph from Neo4j**  
5. **Construct NetworkX Graph**  
6. **Compute Similarity Using SimRank**  

<p align="center">
  <img src="https://github.com/user-attachments/assets/a6358fe1-19eb-4b3b-aaaa-74598bdf1a50" alt="pipeline" width="200px" />
</p>

## Steps

### 1. Preprocessing and Converting JSON to CSV
The raw JSON dataset is preprocessed to fix errors and extract relevant information, such as:  
- **Paper metadata** (e.g., paper ID, venue, authors, labels).  
- **Citation relationships** to create nodes and edges for the graph.

Did some basic pre-processing like fixing errors(missing quotes, extra commas, or unbalanced brackets), and extracted key information for nodes and edges. 

### 2. Creating the Graph in Neo4j
The processed data is loaded into **Neo4j** to create a citation graph.  
- Constraints and indexes are applied to optimize query performance:  
  ```cypher
  CREATE CONSTRAINT ON (p:Paper) ASSERT p.paper_id IS UNIQUE;
  ```
### 3. Neo4j authenticatoin and SparkSession configuration
The authentication details(database URL, username, password, and database name) needs to be stored in a `credentials.json` file. Using this file, a **SparkSession** is created and is configured to connect to Neo4j. This is how a subset of the graph looks:

<p align="center">
  <img src="https://github.com/user-attachments/assets/bc6db9ef-8530-4373-83b4-dbaebd066111" alt="graph" width="60%" />
</p>

### 4. Loading and Constructing the Graph
Nodes and edges are extracted from Neo4j using **Cypher queries** and processed with Spark.  

### 5. Similarity Ranking Using SimRank
The **SimRank algorithm** calculates the similarity between the query node and other nodes in the citation graph.  
The algorithm is executed for three different **importance factors**:  
- `C = 0.7`  
- `C = 0.8`  
- `C = 0.9`

The top-k most similar nodes are ranked for each factor, and results are reported for further analysis.

## Results
 <b>Query Node: 1556418098 </b>
 <br>
 The similarity results for the query node 1556418098 are summarized in Tables
 1, 2, and 3, which show the top 10 nodes for importance factors c = 0.7, c = 0.8,
 and c = 0.9, respectively. Following are the results, for different values of c.
<p align="center">
  <img src="https://github.com/user-attachments/assets/840423d0-afe3-4ccf-af72-950bf1a7c399" alt="results" width="60%" />
</p>

## References

## [Stanford Network Analysis Project](http://snap.stanford.edu/index.html)

```bibtex
@misc{snapnets,
  author       = {Jure Leskovec and Andrej Krevl},
  title        = {{SNAP Datasets}: {Stanford} Large Network Dataset Collection},
  howpublished = {\url{http://snap.stanford.edu/data}},
  month        = jun,
  year         = 2014
}
 
