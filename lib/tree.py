class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
  
    visit = [self.root]
    while len(visit) > 0:
      node = visit.pop()
      if node['id'] == id:
        return node
      if len(node['children']) >0:
        visit.insert(0,node['children'][0])
    return None


# tree = Tree(
#   {
#     'tag_name': 'body',
#     'id': None,
#     'children': [
#       {
#         'tag_name': 'div',
#         'id': 'main',
#         'children': [
#           {
#             'tag_name': 'h1',
#             'id': 'heading',
#             'text_content': 'Title',
#             'children': []
#           },
#           {
#             'tag_name': 'h2',
#             'id': None,
#             'text_content': 'Subitle',
#             'children': []
#           }
#         ]
#       }
#     ]
#   }
# )
