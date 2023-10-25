from os import open, close, dup, O_WRONLY

from pyswip import Prolog

from pyes.data import getdata

prolog = Prolog()
prolog.consult('pyes/knowledge_base.pl')

query_mappings = {
    "What are the symptoms of semgedi?": "get_symptoms(semgedi).",
    "What are the symptoms of normal_fever?": "get_symptoms(normal_fever).",
    "What are the symptoms of unknown?": "get_symptoms(unknown).",
    "What are the treatments for pain_in_heart?": "get_treatment(pain_in_heart).",
    "What are the treatments for cystitis?": "get_treatment(cystitis).",
    "What are the treatments for unknown?": "get_treatment(unknown).",
    "What diseases have cough as a symptom?": "has_symptom(Disease, cough).",
    "What diseases have tiredness as a symptom?": "has_symptom(Disease, tiredness).",
    "What diseases have vomiting as a symptom?": "has_symptom(Disease, vomiting).",
    "What are the severe diseases?": "severity_level(Disease, severe).",
    "What are the moderate diseases?": "severity_level(Disease, moderate).",
    "What are the mild diseases?": "severity_level(Disease, mild).",
    "What are the dietary recommendations for semgedi?": "dietary_recommendation(semgedi, Recommendation).",
    "What are the dietary recommendations for normal_fever?": "dietary_recommendation(normal_fever, Recommendation).",
    "What are the dietary recommendations for unknown?": "dietary_recommendation(unknown, Recommendation).",
    "Which diseases cause pain in the thorax and ear?": "has_symptom(Disease, 'pain_in_thorax_and_ear').",
    "Which diseases cause abnormal heart rhythm?": "has_symptom(Disease, 'abnormal_heart_rhythm').",
    "Which diseases cause bloating?": "has_symptom(Disease, bloating).",
    "Which diseases cause severe pain on either side of the lower back?": "has_symptom(Disease, "
                                                                          "'severe_pain_on_either_side_of_your_lower_back').",
    "Which diseases cause loss of appetite?": "has_symptom(Disease, 'loss_of_appitite').",
    "Which diseases cause sore throat?": "has_symptom(Disease, 'sore_thorat').",
    "Which diseases cause change in voice?": "has_symptom(Disease, 'change_in_voice').",
    "Which diseases cause regurgitation?": "has_symptom(Disease, regurgitation).",
    "Which diseases cause weight loss?": "has_symptom(Disease, 'weight_loss').",
    "Which diseases cause swelling around your anus?": "has_symptom(Disease, 'swelling_around_your_anus').",
    "Which diseases cause pain or discomfort?": "has_symptom(Disease, 'pain_or_discomfort').",
    "Which diseases cause abnormal pain?": "has_symptom(Disease, 'abnormal_pain').",
    "Which diseases cause urine that smells bad?": "has_symptom(Disease, 'urine_that_smells_bad').",
    "Which diseases cause pain and burning or stinging when you pee?": "has_symptom(Disease, "
                                                                       "'pain_and_burning_or_stining_when_you_pee').",
    "Which diseases cause abnormal bloating?": "has_symptom(Disease, 'abnormal_bloating').",
    "Which diseases cause stools that are dry and hard?": "has_symptom(Disease, 'stools_are_dry_and_hard').",
    "Which diseases cause pain_low_down_in_your_tummy?": "has_symptom(Disease, 'pain_low_down_in_your_tummy').",
    "Which diseases cause urine that is dark and cloudy or strong-smelling?": "has_symptom(Disease, "
                                                                              "'urine_that_dark_and_cloudy_or_strong_smelling').",
    "Which diseases cause difficulty swallowing?": "has_symptom(Disease, 'difficulty_swallowing').",
    "Which diseases cause a bad taste in the mouth?": "has_symptom(Disease, 'bad_taste_in_the_mouth').",
    "Which diseases cause a cough with mucus?": "has_symptom(Disease, 'cough_with_mucus').",
    "Which diseases cause shortness of breath?": "has_symptom(Disease, 'shortness_of_breath').",
    "Which diseases cause pain and discomfort in the abdomen?": "has_symptom(Disease, "
                                                                "'pain_and_discomfort_in_the_abdomen').",
    "Which diseases cause fatigue?": "has_symptom(Disease, 'fatigue').",
    "Which diseases cause weakness?": "has_symptom(Disease, 'weakness').",
    "Which diseases cause a loss of appetite?": "has_symptom(Disease, 'loss_of_appetite').",
    "Which diseases cause nausea?": "has_symptom(Disease, 'nausea').",
    "Which diseases cause abdominal pain and bloating?": "has_symptom(Disease, 'abdominal_pain_and_bloating').",
    # Add more query mappings as needed
}


def translate_to_prolog_query(verbal_query):
    return query_mappings.get(verbal_query, "Unknown query.")


def remove_special_chars(input_str: str) -> str:
    input_str = input_str.replace('\n', '')  # Remove newline characters
    input_str = input_str.replace(':', '')  # Remove colons
    input_str = input_str.replace('_', ' ')  # Replace underscores with spaces
    return input_str

def process_user_query(query: str):
    prolog_query = translate_to_prolog_query(query)

    old = dup(1)
    close(1)
    open("pyes/data.txt", O_WRONLY)

    results = list(prolog.query(prolog_query))

    close(1)
    dup(old)  # should dup to 1
    close(old)  # get rid of left overs

    # Apply remove_special_chars to each result
    for i in range(len(results)):
        if isinstance(results[i], dict):
            for key in results[i]:
                results[i][key] = remove_special_chars(results[i][key])
        elif isinstance(results[i], list):
            results[i] = [remove_special_chars(item) for item in results[i]]
        else:
            results[i] = remove_special_chars(results[i])

    results.append(getdata())

    return results
