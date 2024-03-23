# Create a sample class for Mouse defining it’s position on a 2D plane, mouse color, size.
class Mouse:
    def __init__(self, x, y, color, size):
        self.position = (x, y)  # Position on a 2D plane
        self.color = color  # Color of the mouse
        self.size = size  # Size of the mouse

    def get_position(self):
        return self.position

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

# Create a Mouse object
mouse = Mouse(5, 10, 'black', 'small')

# Get mouse properties
print('Position:', mouse.get_position())
print('Color:', mouse.get_color())
print('Size:', mouse.get_size())

