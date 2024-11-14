def verify_syntax(tree):
    stack = [tree]
    while stack:
        node = stack.pop()
        if node['type'] == 'DECLARE':
            return False
        elif node['type'] == 'USE':
            if not any(child['type'] == 'DECLARE' and child['value'] == node['value'] for child in node['parent']['children']):
                return False
        elif node['type'] == 'COM':
            if node['type'] == 'COM' and any(child['type'] == 'DECLARE' for child in node['children']):
                return False
        stack.extend(node['children'])
    return True 

vars = {}

print(vars['a'])