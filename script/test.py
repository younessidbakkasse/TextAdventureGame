class Scene: 
    def __init__(self, template): 
        self.template = template
      
    def __call__(self): 
        # add some gui ele 
        self.template() 
  
  
# adding class decorator to the function 
@Scene
def function(): 
    print("GeeksforGeeks") 
  
function() 