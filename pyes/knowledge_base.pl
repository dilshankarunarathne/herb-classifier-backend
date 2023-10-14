% Predicates
disease(semgedi).
disease(pain_in_heart).
disease(normal_fever).
disease(bade_kakkuma).
disease(gastric).
disease(constipation).
disease(hemorrhoids).
disease(worm_diseases).
disease(cystitis).
disease(uninary_stones).
disease(unknown).

symptom(semgedi,difficulty_swallowing ).
symptom(semgedi,pain_in_thorax_and_ear ).
symptom(semgedi,sore_thorat ).
symptom(semgedi,change_in_voice ).
symptom(pain_in_heart,tiredness ).
symptom(pain_in_heart,abnormal_heart_rhythm ).
symptom(pain_in_heart,shortness_of_breath ).
symptom(pain_in_heart,cough ).
symptom(normal_fever,abnormal_body_temparature).
symptom(normal_fever,trembling).
symptom(normal_fever,tiredness).
symptom(normal_fever,appette).
symptom(bade_kakkuma,bade_wedanawa ).
symptom(bade_kakkuma,bada_korawima ).
symptom(gastric,gastric_burning ).
symptom(gastric,bloating ).
symptom(gastric,regurgitation ).
symptom(gastric,loss_of_appitite ).
symptom(gastric,headache ).
symptom(constipation,abnormal_bloating ).
symptom(constipation,decreased_appetite ).
symptom(constipation,stools_are_dry_and_hard ).
symptom(hemorrhoids,pain_or_discomfort ).
symptom(hemorrhoids,swelling_around_your_anus ).
symptom(hemorrhoids,bleeding ).
symptom(worm_diseases,tiredness ).
symptom(worm_diseases,weakness ).
symptom(worm_diseases,abnormal_pain ).
symptom(worm_diseases,weight_loss ).
symptom(cystitis,pain_and_burning_or_stining_when_you_pee ).
symptom(cystitis,urine_that_dark_and_cloudy_or_strong_smelling ).
symptom(cystitis,pain_low_down_in_your_tummy ).
symptom(uninary_stones,severe_pain_on_either_side_of_your_lower_back ).
symptom(uninary_stones,more_vague_pain ).
symptom(uninary_stones,vomiting ).
symptom(uninary_stones,urine_that_smells_bad ).



treatment(sem_gedi, 'kaluduru grind pottani and put it in the throat to turn phlegm ').
treatment(pain_in_heart, 'drink one teaspoon of kubuk powder with raw milk').
treatment(pain_in_heart,'tippili is fried in a pan, crushed and mixed with honey and rubbed on the tongue').
treatment(normal_fever, 'ginger boiled with coriander and drink with sugar').
treatment(normal_fever, 'ginger and pathpadagam boiled well and drink').
treatment(bade_kakkuma, 'grind pottani and put it in the throat to turn phlegm').
treatment(bade_kakkuma, 'ginger puree, lime puree and salt mixed well and drink').
treatment(gastric, 'beli leaves boiled well and drink').
treatment(gastric, 'vishnukanthi leaves boiled well and drink').
treatment(constipation, 'aralu leaves boiled well and drink with sukiri').
treatment(constipation, 'vishnukanthi leaves boiled well and drink').
treatment(hemorrhoids, 'mukunuwanna and mung bean boiled and drink').
treatment(worm_diseases, 'bata dalu mallum').
treatment(worm_diseases, 'elabudu leaves mallum').
treatment(cystitis, 'drinking akkapana leaves juice').
treatment(cystitis, 'the leaves of the penala are cropped,squeezed, and the drink').
treatment(uninary_stones, ' kekiri seeds and akkapana boiled water with honey and drink').



% Rules and Queries
has_symptom(X, Symptom) :- symptom(X, Symptom).

get_symptoms(Condition) :-
    has_symptom(Condition, Symptom),
    write('Symptom: '), write(Symptom), nl,
    fail.

get_treatment(Condition) :-
    treatment(Condition, Treatment),
    write('Treatment: '), write(Treatment), nl,
    fail.

prompt_condition :-
    write('Enter the disease: '),
    read(Condition),
    get_symptoms(Condition),
    get_treatment(Condition).

get_symptoms(_).
get_treatment(_).
