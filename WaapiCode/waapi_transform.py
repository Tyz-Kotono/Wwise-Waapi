# === transform ===

# For each object, select the parent object.

selectParent: str = "parent"

# For each object, select the list of child objects.

selectChildren: str = "children"

# For each object, recursively select all descendant objects.

selectDescendants: str = "descendants"

# For each object, recursively select ancestor objects.

selectAncestors: str = "ancestors"

# For each object, select all objects that reference this object.

selectReferencesTo: str = "referencesTo"


# === Core Where ===

# Case-insensitive text search on the object name.

nameContains: str = "name:contains"

# Case-insensitive regular expression search on the object name.

nameMatches: str = "name:matches"

# Filter the previous iterator results, keeping only objects of specific types. See Wwise object reference for type list.

typeIsIn: str = "type:isIn"

# Filter the previous iterator results, keeping only objects of specific categories.

categoryIsIn: str = "category:isIn"

# Filter the previous iterator results, keeping only unique objects.

distinct: str = "distinct"
