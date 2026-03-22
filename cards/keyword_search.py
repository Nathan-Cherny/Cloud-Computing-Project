from __future__ import annotations
from functools import reduce

def apply_keyword_search(queryset, keyword: str):
    # filter query sets for attributes listed in attributes_to_check, then return merged queryset
    attributes_to_check = ["title", "tags", "description"]
    querysets = []
    
    for attribute in attributes_to_check:
        arguments = {attribute+"__icontains": keyword}
        querysets.append(queryset.filter(**arguments))
    
    return reduce(merge_query_sets, querysets)

def merge_query_sets(qs1, qs2):
    return qs1 | qs2