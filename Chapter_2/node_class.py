class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)