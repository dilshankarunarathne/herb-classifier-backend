from pyswip import Prolog

prolog = Prolog()
prolog.consult("knowledge_base.pl")


async def diagnose(symptom: str):
    try:
        # Query the Prolog knowledge base for the disease related to the given symptom
        query = f"has_symptom(Disease, {symptom})"
        diseases = list(prolog.query(query))

        if diseases:
            # Assuming there's only one disease for the given symptom
            disease = diseases[0]['Disease']
            # Query the Prolog knowledge base for the treatment of the diagnosed disease
            treatment_query = f"treatment({disease}, Treatment)"
            treatments = list(prolog.query(treatment_query))

            if treatments:
                treatment = treatments[0]['Treatment']
            else:
                treatment = "No specific treatment found."

            return {"disease": disease, "treatment": treatment}
        else:
            return {"error": "No disease found for the given symptom."}
    except Exception as e:
        return {"error": str(e)}


if __name__ == '__main__':
    print(diagnose("normal_fever"))


