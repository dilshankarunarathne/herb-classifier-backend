from pyswip import Prolog

# Initialize Prolog engine and consult the knowledge base
prolog = Prolog()
prolog.consult("knowledge_base.pl")

# Mapping of verbal queries to Prolog predicates
query_mappings = {
    "What are the symptoms of pain in the heart?": "has_symptom(pain_in_heart, Symptom).",
"What are the common symptoms of semgedi?": "has_common_symptom(semgedi, Symptom).",
"How severe is pain_in_heart?": 
    # Add more query mappings as needed
}


def translate_to_prolog_query(verbal_query):
    return query_mappings.get(verbal_query, "Unknown query.")


# Get user input in verbal language
user_query = input("Please enter your query: ")

# Translate verbal query to Prolog query
prolog_query = translate_to_prolog_query(user_query)

# Query the Prolog knowledge base
results = list(prolog.query(prolog_query))

# Process and display results
if results:
    print("Results:")
    for result in results:
        # Process result dictionary and display relevant information
        print(result)
else:
    print("No matching information found.")
