from pyes.expert_sys import process_user_query


async def query_knowledge_base(query: str):
    return process_user_query(query)