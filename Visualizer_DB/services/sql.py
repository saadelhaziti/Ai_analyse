import re
from collections import defaultdict

def generate_complete_join_query(schema_text: str) -> str:
    # Extraire les relations du schéma
    relation_pattern = re.compile(r"- (\w+)\.(\w+) → (\w+)\.(\w+)")
    relations = relation_pattern.findall(schema_text)

    if not relations:
        return "Aucune relation détectée."

    # Construire un graphe bidirectionnel
    graph = defaultdict(list)
    all_tables = set()

    for src_table, src_col, tgt_table, tgt_col in relations:
        graph[src_table].append((tgt_table, src_col, tgt_col))
        graph[tgt_table].append((src_table, tgt_col, src_col))  # liaison inverse
        all_tables.update([src_table, tgt_table])

    visited = set()
    joins = []
    seen_pairs = set()

    def dfs(current_table):
        visited.add(current_table)
        for neighbor, from_col, to_col in graph[current_table]:
            key = tuple(sorted([current_table, neighbor]))
            if neighbor not in visited and key not in seen_pairs:
                joins.append(
                    f"JOIN {neighbor} ON {current_table}.{from_col} = {neighbor}.{to_col}"
                )
                seen_pairs.add(key)
                dfs(neighbor)

    # Démarrer depuis une table racine (choisie arbitrairement)
    start_table = sorted(all_tables)[0]
    dfs(start_table)

    # Générer la requête
    query = f"SELECT *\nFROM {start_table}\n" + "\n".join(joins) + ";"
    return query



