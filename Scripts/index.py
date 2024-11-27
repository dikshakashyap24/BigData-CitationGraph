import json
import csv

# Input JSON file
input_file = f"~/Data/train.json"

# Output CSV files
papers_file = f"~/Data/papers.csv"
citations_file = f"~/Data/citations.csv"

# Initialize sets to store unique papers and citation relationships
papers_set = set()
citations_list = []

# Open the input file and read each line as a JSON object
with open(input_file, 'r') as f:
    for line in f:
        data = json.loads(line)
        
        # Extract the paper ID
        paper_id = data.get("paper")
        if paper_id:
            # Add the paper to the set (to ensure uniqueness)
            papers_set.add(paper_id)
            
            # Extract the references (if any)
            references = data.get("reference", [])
            for ref_id in references:
                # Store each citation as a tuple (citing_paper_id, cited_paper_id)
                citations_list.append((paper_id, ref_id))
                # Also, ensure cited papers are in the nodes set
                papers_set.add(ref_id)

# Write unique papers to papers.csv
with open(papers_file, 'w', newline='') as pf:
    writer = csv.writer(pf)
    writer.writerow(['paper_id'])  # Header
    for paper_id in papers_set:
        writer.writerow([paper_id])

# Write citations to citations.csv
with open(citations_file, 'w', newline='') as cf:
    writer = csv.writer(cf)
    writer.writerow(['citing_paper_id', 'cited_paper_id'])  # Header
    for citing_paper, cited_paper in citations_list:
        writer.writerow([citing_paper, cited_paper])

print(f"Data has been successfully written to {papers_file} and {citations_file}.")
