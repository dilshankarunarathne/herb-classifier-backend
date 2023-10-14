from pyswip import Prolog

# Initialize the Prolog engine and load the knowledge base
prolog = Prolog()
prolog.consult("knowledge_base.pl")  # Replace with the actual path to your Prolog file

def get_diagnosis(symptoms):
    # Build a query for diseases based on symptoms
    query = "has_symptom(Disease, {})".format(",".join(map(str, symptoms)))

    # Query the Prolog knowledge base
    solutions = list(prolog.query(query))

    # Extract disease names from solutions
    diseases = [solution["Disease"] for solution in solutions]

    return diseases

# Example usage
user_symptoms = ['difficulty_swallowing', 'pain_in_thorax_and_ear']
possible_diseases = get_diagnosis(user_symptoms)

if possible_diseases:
    print("Possible Diseases:", possible_diseases)
    for disease in possible_diseases:
        # Query Prolog for treatments based on the diagnosed disease
        treatments_query = "treatment({}, Treatment)".format(disease)
        treatments = list(prolog.query(treatments_query))
        if treatments:
            print("Treatment for", disease + ":", treatments[0]["Treatment"])
        else:
            print("No specific treatment found for", disease)
else:
    print("No matching disease found for the given symptoms.")
