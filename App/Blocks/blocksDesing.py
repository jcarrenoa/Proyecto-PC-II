from PyQt6.QtCore import QPointF

def drawPointsConnections(self, block_type, x, y,width):
    if block_type== 'On_Start' :
        # Points of connection
        self.connection_points = {
            'condition': QPointF(x + 10, y + self.header_height + 10),
            'true': QPointF(x + width - 10, y + self.header_height + 5),
            'false': QPointF(x + width - 10, y + self.header_height + 25)
        }

        # Draw connection points and labels
        self.add_connection_point('condition', "condition")
        self.add_connection_point('true', "true")
        self.add_connection_point('false', "false")

    if block_type== 'On_Update' :
        # Points of connection
        self.connection_points = {
            'flow': QPointF(x + 10, y + self.header_height + 10),
            'flow_out': QPointF(x + width - 10, y + self.header_height + 5),

        }

        # Draw connection points and labels
        self.add_connection_point('flow', "flow")
        self.add_connection_point('flow_out', "flow_out")