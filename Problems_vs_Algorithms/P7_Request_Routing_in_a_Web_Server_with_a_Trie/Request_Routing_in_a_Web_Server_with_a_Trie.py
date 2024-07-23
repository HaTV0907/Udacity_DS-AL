class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None


class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, path_parts, handler):
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                current_node.children[part] = RouteTrieNode()
            current_node = current_node.children[part]
        current_node.handler = handler

    def find(self, path_parts):
        current_node = self.root
        for part in path_parts:
            if part in current_node.children:
                current_node = current_node.children[part]
            else:
                return None
        return current_node.handler


class Router:
    def __init__(self):
        self.routes = RouteTrie()
        self.not_found_handler = "404 Not Found"

    def add_handler(self, path, handler):
        path_parts = self.split_path(path)
        self.routes.insert(path_parts, handler)

    def lookup(self, path = None):
        if None == path or 0 == len(path):
            print("Invalid path")
            return -1
        
        if path.endswith('/'):
            path = path[:-1]  # Remove trailing slash
        path_parts = self.split_path(path)
        handler = self.routes.find(path_parts)
        return handler if handler else self.not_found_handler

    def split_path(self, path):
        return [part for part in path.split('/') if part]


router = Router()

router.add_handler("/about", "About Page Handler")
print(router.lookup("/about"))  # Should return "About Page Handler"
print(router.lookup("/about/"))  # Should also return "About Page Handler"
print(router.lookup("/notfound"))  # Should return "404 Not Found"
print(router.lookup(""))
print(router.lookup())
