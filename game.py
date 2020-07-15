from tkinter import *
'''
    Rule:
    5 balls move around in the canvas frame. They can come in collision with 
    the other balls or the edge of the frame (the wall). When they come in contact 
    with another ball or wall, they will move in the opposite direction, in the same veloity. 
    the scale is used to change the speed of the balls. 
'''
__author__ = {'author' : 'Rebecca Wang',
              'Email' : 'zhaoyue.wang@mail.mcgill.ca',
              'Created' : '2020-07-15',
              'Version' : '1.0.0'}

class Clash(Frame):
    def createWidgets(self):
        self.scaling = 100.0
        self.canvas_width = 7
        self.canvas_height = 5
        self.draw = Canvas(self, width=(self.canvas_width * self.scaling),
                           height=(self.canvas_height * self.scaling),
                           bg='white')

        ## scale to control the speed of the balls 
        self.speed = Scale(self, activebackground='#FFFBC9', orient=VERTICAL, label="ball1 speed",
                           from_=0, to=200)
        self.speed.pack(anchor=E)                   
        #self.speed.pack(side=BOTTOM, fill=X)


        #ball1 dimension 
        self.ball_d = 1.0
        
        #range of where the balls can move
        self.scaling_left = round(self.ball_d / 2, 1)
        self.scaling_right = self.canvas_width - self.scaling_left
        self.scaling_bottom = self.canvas_height - self.scaling_left
        self.scaling_top = self.scaling_left
 
        self.scale_value = self.speed.get()
 
        #to store the balls
        self.balls = []
        #to store the x values of the balls
        self.ball_x = []
        #to store the y values of the balls
        self.ball_y = []
        #to store the vx values of the balls
        self.ball_v_x = []
        #to store the vy values of the balls
        self.ball_v_y = []

        # the balls
        self.ball1 = self.draw.create_oval("0.60i", "0.60i", "1.60i", "1.60i",
                                          fill='#FFB8F9')
        self.ball2 = self.draw.create_oval("2.0i", "2.0i", "3.0i", "3.0i",
                                                 fill='#F08080')
        self.ball3 = self.draw.create_oval("4.0i", "4.0i", "5.0i", "5.0i",
                                                 fill='#CD5C5C')
        self.ball4 = self.draw.create_oval("6.0i", "2.0i", "7.0i", "3.0i",
                                                 fill='#BA9EC0')
        self.ball5 = self.draw.create_oval("8.0i", "3.0i", "9.0i", "4.0i",
                                                 fill='#C8ACE9')

        self.balls.append(self.ball1)
        self.balls.append(self.ball2)
        self.balls.append(self.ball3)
        self.balls.append(self.ball4)
        self.balls.append(self.ball5)

        self.x = 1.1        
        self.y = 1.1
        self.velocity_x = -0.2
        self.velocity_y = 0.1
        self.ball2_x = 2.5
        self.ball2_y = 2.5
        self.ball2_v_x = 0.1
        self.ball2_v_y = -0.2
        self.ball3_x = 4.5
        self.ball3_y = 4.5
        self.ball3_v_x = -0.1
        self.ball3_v_y = -0.2
        self.ball4_x = 6.5
        self.ball4_y = 2.5
        self.ball4_v_x = 0.1
        self.ball4_v_y = -0.2
        self.ball5_x = 8.5
        self.ball5_y = 3.5
        self.ball5_v_x = 0.1
        self.ball5_v_y = 0.2

        self.update_ball_x_y()
        self.draw.pack(side=LEFT)

    def update_ball_x_y(self, *args):
        self.ball_x.append(self.x)
        self.ball_y.append(self.y)
        self.ball_v_x.append(self.velocity_x)
        self.ball_v_y.append(self.velocity_y)
        self.ball_x.append(self.ball2_x)
        self.ball_y.append(self.ball2_y)
        self.ball_v_x.append(self.ball2_v_x)
        self.ball_v_y.append(self.ball2_v_y)
        self.ball_x.append(self.ball3_x)
        self.ball_y.append(self.ball3_y)
        self.ball_v_x.append(self.ball3_v_x)
        self.ball_v_y.append(self.ball3_v_y)
        self.ball_x.append(self.ball4_x)
        self.ball_y.append(self.ball4_y)
        self.ball_v_x.append(self.ball4_v_x)
        self.ball_v_y.append(self.ball4_v_y)
        self.ball_x.append(self.ball5_x)
        self.ball_y.append(self.ball5_y)
        self.ball_v_x.append(self.ball5_v_x)
        self.ball_v_y.append(self.ball5_v_y)
 
    def update_ball_velocity(self, index, *args):
        self.scale_value = self.speed.get() * 0.1
        #if the balls come in contact with the edge of the frame(aka the wall)
        if (self.ball_x[index] > self.scaling_right) or (self.ball_x[index] < self.scaling_left):
            self.ball_v_x[index] = -1.0 * self.ball_v_x[index]
        if (self.ball_y[index] > self.scaling_bottom) or (self.ball_y[index] < self.scaling_top):
            self.ball_v_y[index] = -1.0 *  self.ball_v_y[index]

        for n in range(len(self.balls)):
            #collision: (x2 - x1)^2 + (y2 - y1)^2 <= (r + R)^2
            if (round((self.ball_x[index] - self.ball_x[n])**2 + (self.ball_y[index] - self.ball_y[n])**2, 2) <= round(self.ball_d**2, 2)):
                #swap velocity 
                temp_vx = self.ball_v_x[index]
                temp_vy = self.ball_v_y[index]
                self.ball_v_x[index] = self.ball_v_x[n]
                self.ball_v_y[index] = self.ball_v_y[n]
                self.ball_v_x[n] = temp_vx
                self.ball_v_y[n] = temp_vy
        #print(self.ball_v_x, self.ball_v_y)
 
    def get_ball_deltax(self, index, *args):
        deltax = (self.ball_v_x[index] * self.scale_value / self.scaling)
        self.ball_x[index] = self.ball_x[index] + deltax
        return deltax

    def get_ball_deltay(self, index, *args):
        deltay = (self.ball_v_y[index] * self.scale_value / self.scaling)
        self.ball_y[index] = self.ball_y[index] + deltay
        return deltay
 
    def moveBall(self, *args):
        self.update_ball_velocity(0)       
        deltax = self.get_ball_deltax(0)
        deltay = self.get_ball_deltay(0)
        self.draw.move(self.ball1,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.moveBall)
    def move_ball2(self, *args):
        self.update_ball_velocity(1)       
        deltax = self.get_ball_deltax(1)
        deltay = self.get_ball_deltay(1)        
        self.draw.move(self.ball2,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.move_ball2)
    def move_ball3(self, *args):
        self.update_ball_velocity(2)       
        deltax = self.get_ball_deltax(2)
        deltay = self.get_ball_deltay(2)
        self.draw.move(self.ball3,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.move_ball3)
    def move_ball4(self, *args):
        self.update_ball_velocity(3)       
        deltax = self.get_ball_deltax(3)
        deltay = self.get_ball_deltay(3)
        self.draw.move(self.ball4,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.move_ball4)
    def move_ball5(self, *args):
        self.update_ball_velocity(4)       
        deltax = self.get_ball_deltax(4)
        deltay = self.get_ball_deltay(4)
        self.draw.move(self.ball5,  "%ri" % deltax, "%ri" % deltay)
        self.after(10, self.move_ball5)
            
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()
        self.after(10, self.moveBall)
        self.after(10, self.move_ball3)
        self.after(10, self.move_ball4)
        self.after(10, self.move_ball5)
        self.after(10, self.move_ball2)
 
        
game = Clash()
game.mainloop()
