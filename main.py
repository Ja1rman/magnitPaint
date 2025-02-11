from tkinter import *
from ElectricityCluster import *
from Electricity import *
from VectorField import *


class PaintApp:
    Cluster = ElectricityCluster()
    VecFil = VectorField()
    drawing_tool = "inside"
    left_button = "up"
    x_position, y_position = None, None

    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

    @staticmethod
    def quit_app(event=None):
        root.quit()

    def __init__(self, root):
        self.drawing_area = Canvas(root, width=500, height=500, bg="white")
        self.drawing_area.pack()

        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.left_button_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.left_button_up)

        the_menu = Menu(root)

        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_command(label="Inside", command=self.set_inside_drawing_tool)
        file_menu.add_command(label="Outside", command=self.set_outside_drawing_tool)

        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit_app)

        the_menu.add_cascade(label="Options", menu=file_menu)
        root.config(menu=the_menu)

    def set_inside_drawing_tool(self):
        self.drawing_tool = "inside"

    def set_outside_drawing_tool(self):
        self.drawing_tool = "outside"

    def left_button_down(self, event=None):
        self.left_button = "down"
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    def left_button_up(self, event=None):
        self.left_button = "up"
        self.x_position = None
        self.y_position = None

        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if self.drawing_tool == "inside":
            self.inside_draw(event)
        if self.drawing_tool == "outside":
            self.outside_draw(event)

    def motion(self, event=None):
        self.x_position = event.x
        self.y_position = event.y

    def inside_draw(self, event=None):
        if None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            diameter = 12.5
            centerX = min(self.x1_line_pt, self.x2_line_pt)+diameter
            centerY = min(self.y1_line_pt, self.y2_line_pt)+diameter
            NewElec = Electricity(x=centerX, y=centerY, clockwise=1)
            self.Cluster.add_electricity(NewElec)
            self.build_Vector_field(event)

    def outside_draw(self, event=None):
        if None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
            diameter = 15
            centerX = min(self.x1_line_pt, self.x2_line_pt) + diameter
            centerY = min(self.y1_line_pt, self.y2_line_pt) + diameter
            NewElec = Electricity(x=centerX, y=centerY, clockwise=0)
            self.Cluster.add_electricity(NewElec)
            self.build_Vector_field(event)

    def build_Vector_field(self, event):
        self.drawing_area.delete("all")
        for elec in self.Cluster.get_cluster():
            x = elec.get_x()
            y = elec.get_y()
            if (elec.get_clockwise() == 0):
                event.widget.create_oval(x-15, y-15, x+15,
                                         y+15, fill="blue", outline="black", width=1)
                event.widget.create_oval(x-7.5, y-7.5,
                                         x+7.5, y+7.5,
                                         fill="black", width=1)
            else:
                event.widget.create_oval(x-15, y-15, x+15,
                                         y+15, fill="red", outline="black", width=1)
                event.widget.create_line(x, y-7.5,
                                         x, y+7.5,
                                         fill="black",
                                         width=4)
                event.widget.create_line(x-7.5, y,
                                         x+7.5, y,
                                         fill="black",
                                         width=4)
        for vector in self.VecFil.get_VectorField():
            x = vector.get_X()
            y = vector.get_Y()
            len = 0
            angle = 0
            len2 = 0
            
            for elec in self.Cluster.get_cluster():
                temp_len = elec.get_vector_length(vector_x=x, vector_y=y)
                
                temp_angle = elec.get_vector_angle(vector_x=x, vector_y=y)
                
                if angle == 0:
                    len = temp_len
                    angle = temp_angle
                    len2 = len
                else:
                    num = math.pi-angle+temp_angle
                    cos = math.cos(num)
                    sin = math.sin(num)
                    len2 = temp_len*temp_len + len*len - 2*temp_len*len*cos
                    if(len == 0 or len2 == 0):
                        angle = 0
                        len2 = 0
                    else:
                        len2 = math.sqrt(len2)
                        angle = math.asin(sin * temp_len/len2) + temp_angle

            vector.set_length(len2)
            vector.set_angle(angle)
            vector.draw(event)


root = Tk()
paint_app = PaintApp(root)
root.mainloop()
