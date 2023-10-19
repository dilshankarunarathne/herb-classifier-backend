from pyes.expert_sys import process_user_query

user_query = input("Please enter your query: ")

results = list(process_user_query(user_query))

if results:
    print("Results:")
    for result in results:
        print(result)
else:
    print("No matching information found.")
