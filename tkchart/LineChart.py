import tkinter
from .RequredGeometry import RequredWidth
from .RequredGeometry import RequredHeight
from .Line import *



class LineChart():
   def __init__(self, master=None, width=300, height=150,
                bar_size=2, bar_color="#909090",bg_color="#202020", chart_color="#151515",
                sections_color="#909090",
                x_values_decimals=1, y_values_decimals=1,
                y_labels_count=5, x_labels_count=5,
                y_data="", y_data_max=1, y_sections_count=0, y_values_color="#909090", y_data_color="#909090",
                x_data="", x_data_min_max=(0,10) ,x_sections_count=0, x_values_color="#909090", x_data_color="#909090",
                x_y_data_font=("arial", 9, "normal"),
                x_y_values_font=("arial", 9, "normal"),
                line_width=None, line_width_auto=True, *args)->None:
      
      if master != None:
         self.master = master
      if len(args) > 0:
         self.master = args[0]
      
      
      self.height = height
      self.width = width
      
      self.__lines = []
      self.__line_width = line_width
      self.__line_width_auto=True
      if line_width != None:
         self.__line_width_auto=False
      
      
      self.__bg_color = bg_color
      self.__chart_color = chart_color
      self.__y_values_color = y_values_color
      self.__y_data_color = y_data_color
      self.__x_values_color = x_values_color
      self.__x_data_color = x_data_color
      
      self.__sections_color = sections_color

      
      self.__bar_size = bar_size
      self.__bar_color = bar_color   
      
      self.__x_sections_count = x_sections_count
      self.__y_sections_count = y_sections_count
      self.__x_labels_count = x_labels_count
      self.__y_labels_count = y_labels_count
      
      
      self.__y_data = y_data
      self.__x_data = x_data
      
      self.__y_data_max = y_data_max
      self.__x_data_min = x_data_min_max[0]
      self.__x_data_max = x_data_min_max[1]
      self.__x_data_min_max = x_data_min_max
   
      self.__x_y_data_font = x_y_data_font
      self.__x_values_decimals = x_values_decimals
      self.__y_values_decimals = y_values_decimals
      
      self.__x_y_values_font = x_y_values_font
   
      self.__main_frame = tkinter.Frame(master=master)
      
      self.__y_bar = tkinter.Frame(master=self.__main_frame)
      self.__x_bar = tkinter.Frame(master=self.__main_frame)
      
      self.__y_values = tkinter.Frame(master=self.__main_frame)
      self.__x_values = tkinter.Frame(master=self.__main_frame)
      
      self.__y_data_text = tkinter.Label(master=self.__main_frame)
      self.__x_data_text = tkinter.Label(master=self.__main_frame)
      
      self.__output_frame = tkinter.Frame(master=self.__main_frame)
      self.__output = tkinter.Canvas(master=self.__output_frame, highlightthickness=0)
      
      self.__force_to_stop_show_data = False
      self.___show_data_working = False
      
      
      self.__place_x = 0
      self.__real_height = 0
      self.__real_width = 0
      
      
      self.__place_info_x = 0
      self.__place_info_y = 0
      self.__place_info_rely = 0
      self.__place_info_relx = 0
      self.__place_info_anchor = 0
      
      self.__pack_info_pady = 0
      self.__pack_info_padx = 0
      self.__pack_info_before = 0
      self.__pack_info_after = 0
      self.__pack_info_side = 0
      self.__pack_info_ipadx = 0
      self.__pack_info_ipady = 0
      self.__pack_info_anchor = 0
      
      self.__grid_info_column = 0
      self.__grid_info_columnspan = 0
      self.__grid_info_ipadx = 0
      self.__grid_info_ipady = 0
      self.__grid_info_padx = 0
      self.__grid_info_pady = 0
      self.__grid_info_row = 0
      self.__grid_info_rowspan = 0
      self.__grid_info_sticky = 0
      
      
      self.__get_required_widget_size()
      self.__set_widget_geomatry()
      self.__place_widget()
      self.__get_line_width()
      self.__create_y_labels()
      self.__create_x_labels()
      self.__create_y_sections()
      self.__create_x_sections()
      self.__set_widget_colors()
      self.__set_widget_font()
      self.__set_text()
      self.__reset_chart_info()
   
   
      
   def __add_decimals(self, float_val:float, decimals:int)->float:
      if decimals:
         float_val = round(float(float_val),decimals)
         float_val = str(float_val) + ((decimals-len(str(float_val).split(".")[-1]))*"0")
         return float_val
      else:
         return int(float_val)
   
   def __set_widget_colors(self)->None:
      self.__y_bar.configure(bg=self.__bar_color)
      self.__x_bar.configure(bg=self.__bar_color)
      self.__y_values.configure(bg=self.__bg_color)
      self.__x_values.configure(bg=self.__bg_color)
      
      self.__main_frame.configure(bg=self.__bg_color)
      self.__output_frame.configure(bg=self.__chart_color)
      self.__output.configure(bg=self.__chart_color)
      
      self.__y_data_text.configure(bg=self.__bg_color, fg=self.__y_data_color)
      for label in self.__x_values.winfo_children() :
         if type(label) == tkinter.Label:
            label.configure(bg=self.__bg_color, fg=self.__x_values_color)
      
      self.__x_data_text.configure(bg=self.__bg_color, fg=self.__x_data_color)
      for label in self.__y_values.winfo_children():
         if type(label) == tkinter.Label:
            label.configure(bg=self.__bg_color, fg=self.__y_values_color)
            
      for section_frame in self.__output_frame.winfo_children():
         if type(section_frame) == tkinter.Frame:
            section_frame.configure(bg=self.__sections_color)
      
   def __set_widget_geomatry(self)->None:
      self.__main_frame.configure(width=self.width, height=self.height)
      self.__y_bar.configure(width=self.__bar_size)
      self.__x_bar.configure(height=self.__bar_size)

      self.__y_values.configure(width=self.__y_value_req_space, height=self.height)
      self.__x_values.configure(height=self.__x_value_req_space, width=self.width)
   
   def __set_widget_font(self)->None:
      self.__y_data_text.configure(font=self.__x_y_data_font)
      self.__x_data_text.configure(font=self.__x_y_data_font)
      
      for label in self.__x_values.winfo_children() + self.__y_values.winfo_children() :
         if type(label) == tkinter.Label:
            label.configure(font = self.__x_y_values_font)
   
   def __set_text(self)->None:
      self.__y_data_text.configure(text=self.__y_data)
      
      if self.__y_labels_count>0:
         for i,label in enumerate(self.__y_values.winfo_children()):
            value = (self.__y_data_max - (self.__y_data_max/self.__y_labels_count)*i)
            value = self.__add_decimals(value,self.__y_values_decimals)
            label.configure(text=value)
         
      self.__x_data_text.configure(text=self.__x_data)
    
      if self.__x_labels_count>0:
         for i,label in enumerate(self.__x_values.winfo_children()):
            value = self.__x_data_max- (((self.__x_data_max-self.__x_data_min)/self.__x_labels_count)*i)
            value = self.__add_decimals(value,self.__x_values_decimals)
            label.configure(text=value)
      
      
      
   def __place_widget(self)->None:
      self.__y_data_text.place(x=0, y=0)
      self.__x_data_text.place(rely=1, relx=1, x=-self.__x_data_req_space, y=-self.__y_data_req_space)
      self.__y_bar.place(x=self.__y_value_req_space, y=self.__y_data_req_space, relheight=1, height=-self.__y_data_req_space+-self.__x_value_req_space)
      self.__x_bar.place(x=self.__y_value_req_space, rely=1, y=-self.__bar_size+-self.__x_value_req_space, relwidth=1,
                         width=-self.__x_data_req_space+-self.__y_value_req_space+-self.__x_value_req_width)
      
      self.__output_frame.place(x=self.__y_value_req_space+self.__bar_size, relwidth=1,
                                width=-self.__x_data_req_space*2+-self.__y_value_req_space+-self.__bar_size+-self.__x_value_req_width,
                          relheight=1, y=self.__y_data_req_space*1.5, height=-self.__bar_size+-self.__x_value_req_space+-self.__y_data_req_space*1.5)
      
      self.__real_width = self.width - (self.__y_value_req_space+self.__bar_size+self.__x_data_req_space*2+self.__x_value_req_width)
      self.__real_height = self.height - (self.__y_data_req_space+self.__bar_size+self.__x_value_req_space*1.5)
      self.__output.place(y=0, x=0, height=self.__real_height, width=self.__real_width)
      
      
   
   def __get_line_width(self)->None:
      if self.__line_width_auto==True:
         self.__line_width = int(self.__real_width / abs(self.__x_data_max - self.__x_data_min))
         
         
   def __get_required_widget_size(self)->None:
      self.__y_data_req_space = RequredHeight(text=self.__y_data, font=self.__x_y_data_font)
      self.__x_data_req_space = RequredWidth(text=self.__x_data, font=self.__x_y_data_font)
      
      self.__y_value_req_space = RequredWidth(text=self.__add_decimals(self.__y_data_max, self.__y_values_decimals), font=self.__x_y_values_font) 
      self.__x_value_req_space = RequredHeight(text=self.__add_decimals(self.__x_data_max, self.__x_values_decimals), font=self.__x_y_values_font)
      
      self.__x_value_req_width = RequredWidth(text=self.__add_decimals(self.__x_data_max, self.__x_values_decimals), font=self.__x_y_values_font) 
      
   def __create_y_labels(self)->None:
      if self.__y_labels_count >0:
         self.__y_values.place(x=0, y=1)
         y = self.__y_data_req_space*1.5
         for i in range(self.__y_labels_count):
            tkinter.Label(master=self.__y_values, justify="right" ).place(y=y, x=0, anchor="w" ,width=self.__y_value_req_space)
            
            y += (self.height - (self.__y_data_req_space*1.5 + self.__x_value_req_space + self.__bar_size ) ) / self.__y_labels_count 
   
   def __destroy_y_labels(self)->None:
      for y_value in self.__y_values.winfo_children():
         y_value.place_forget()
         y_value.destroy()
         
   def __create_x_labels(self)->None:
      if self.__x_labels_count >0:
         self.__x_values.place(x=0, rely=1, y=-self.__x_value_req_space)
         x = self.width - self.__x_data_req_space*2 - self.__x_value_req_width
         for i in range(self.__x_labels_count + 1):
            tkinter.Label(master=self.__x_values).place(rely=1, y=-self.__x_value_req_space, x=x, anchor="n")
            x -= (self.width - (self.__x_data_req_space*2 + self.__y_value_req_space + self.__bar_size + self.__x_value_req_width) ) / self.__x_labels_count
            
         
   def __destroy_x_labels(self)->None:
      for x_value in self.__x_values.winfo_children():
         x_value.place_forget()
         x_value.destroy()
         
      
   def __create_y_sections(self)->None:
      y = 0
      for i in range(self.__y_sections_count):
         tkinter.Frame(master=self.__output_frame, height=1, width=self.width, bg=self.__sections_color).place(y=y, anchor="w")
         y += (self.height - (self.__y_data_req_space*1.5 + self.__x_value_req_space + self.__bar_size ) ) / self.__y_sections_count 
         
   def __destroy_y_x_sections(self)->None:
      for widget in self.__output_frame.winfo_children():
         if type(widget) == tkinter.Frame:
            widget.place_forget()
            widget.destroy()
   
   def __create_x_sections(self)->None:
      if self.__x_sections_count != 0:
         x = (self.width - (self.__x_data_req_space*2+self.__y_value_req_space+self.__bar_size + self.__x_value_req_width)  ) / self.__x_sections_count - 1
      for i in range(self.__x_sections_count):
         tkinter.Frame(master=self.__output_frame, height=self.height, width=1,bg=self.__sections_color).place(x=x, anchor="n")
         x += (self.width - (self.__x_data_req_space*2+self.__y_value_req_space+self.__bar_size + self.__x_value_req_width)  ) / self.__x_sections_count
         
         
   def configure(self, width=False, height=False, y_data_max=False, x_data_min_max=False, bar_size=False,
                 x_values_decimals=False, y_values_decimals=False,
                 x_data=False, x_y_data_font=False, x_y_values_font=False,
                 bg_color=False, bar_color=False, chart_color=False,
                 y_values_color=False, x_values_color=False,
                 y_data_color=False, x_data_color=False,
                 y_data=False, y_labels_count=None, x_labels_count=None,
                 y_sections_count=None, x_sections_count=None,sections_color=False,
                 line_width=False,line_width_auto=None):  
      
      chart_reset_req = False
      chart_color_change_req = False
      chart_y_values_change_req = False
      chart_x_values_change_req = False
      chart_sections_change_req = False
      

         
      if width:
         if width != self.width:
            self.width = width
            chart_reset_req = True
      
      if height:
         if height != self.height:
            self.height = height
            chart_reset_req = True
      
      if y_data_max:
         if y_data_max != self.__y_data_max:
            self.__y_data_max = y_data_max
            chart_reset_req = True
      
      if bar_size:
         if bar_size != self.__bar_size:
            self.__bar_size = bar_size
            chart_reset_req = True
      
      if type(y_values_decimals) != bool:
         if y_values_decimals != self.__y_values_decimals:
            self.__y_values_decimals = y_values_decimals
            chart_reset_req = True
      
      if x_data!=False:
         if x_data != self.__x_data:
            self.__x_data = x_data
            chart_reset_req = True
            
      if x_y_data_font:
         if x_y_data_font != self.__x_y_data_font:
            self.__x_y_data_font = x_y_data_font
            chart_reset_req = True
            
      if x_y_values_font:
         if x_y_values_font != self.__x_y_values_font:
            self.__x_y_values_font = x_y_values_font
            chart_reset_req = True
            
      
      if bg_color:
         if bg_color != self.__bg_color:
            self.__bg_color = bg_color
            chart_color_change_req = True
            
      if bar_color:
         if bar_color != self.__bar_color:
            self.__bar_color = bar_color
            chart_color_change_req = True
            
      if chart_color:
         if chart_color != self.__chart_color:
            self.__chart_color = chart_color
            chart_color_change_req = True
            
      if bg_color:
         if bg_color != self.__bg_color:
            self.__bg_color = bg_color
            chart_color_change_req = True
            
      if y_values_color:
         if y_values_color != self.__y_values_color:
            self.__y_values_color = y_values_color
            chart_color_change_req = True
            
      if x_values_color:
         if x_values_color != self.__x_values_color:
            self.__x_values_color = x_values_color
            chart_color_change_req = True
            
      if y_data_color:
         if y_data_color != self.__y_data_color:
            self.__y_data_color = y_data_color
            chart_color_change_req = True
            
      if x_data_color:
         if x_data_color != self.__x_data_color:
            self.__x_data_color = x_data_color
            chart_color_change_req = True

      if sections_color:
         if sections_color != self.__sections_color:
            self.__sections_color = sections_color
            chart_color_change_req = True
            
            
      if y_labels_count!=None:
         if y_labels_count != self.__y_labels_count:
            self.__y_labels_count = y_labels_count
            chart_y_values_change_req = True
      
  
      if x_labels_count!=None:
         if x_labels_count != self.__x_labels_count:
            self.__x_labels_count = x_labels_count
            chart_x_values_change_req = True
      
      if x_sections_count!=None:
         if x_sections_count != self.__x_sections_count:
            self.__x_sections_count = x_sections_count
            chart_sections_change_req = True
            
      if y_sections_count!=None:
         if y_sections_count != self.__y_sections_count:
            self.__y_sections_count = y_sections_count
            chart_sections_change_req = True
            
      
            
      if y_data != False:
         if y_data != self.__y_data:
            self.__y_data = y_data
            self.__set_text()
            
      if x_data_min_max:
         if x_data_min_max != self.__x_data_min_max:
            if ((self.__x_data_min_max[1]-self.__x_data_min_max[0]) != (x_data_min_max[1]-x_data_min_max[0]) ):
               self.__x_data_min_max = x_data_min_max
               self.__x_data_min = x_data_min_max[0]
               self.__x_data_max = x_data_min_max[1]
               self.__get_line_width()
               self.__set_text()
               self.__re_show_data()
            else:
               self.__x_data_min_max = x_data_min_max
               self.__x_data_min = x_data_min_max[0]
               self.__x_data_max = x_data_min_max[1]
               self.__set_text()
               
      
      if type(x_values_decimals) != bool:
         if x_values_decimals != self.__x_values_decimals:
            self.__x_values_decimals = x_values_decimals
            self.__set_text()
            
      if line_width_auto!=None and line_width==False:
         if line_width_auto != self.__line_width_auto:
            self.__line_width_auto = line_width_auto
            self.__get_line_width()
            self.__re_show_data()
      
      if line_width and line_width_auto==None:
         if line_width != self.__line_width:
            self.__line_width = line_width
            self.__line_width_auto = False
            self.__re_show_data()
            
      
      if chart_reset_req :
         self.__destroy_y_labels()
         self.__destroy_x_labels()
         self.__destroy_y_x_sections()
         self.__get_required_widget_size()
         self.__set_widget_geomatry()
         self.__place_widget()
         self.__get_line_width()
         self.__create_y_labels()
         self.__create_x_labels()
         self.__set_widget_colors()
         self.__set_widget_font()
         self.__set_text()
         self.__create_x_sections()
         self.__create_y_sections()
         self.__force_to_stop_show_data = True
         while  self.___show_data_working:
            pass
         self.__force_to_stop_show_data = False
         self.__re_show_data()
         
         
      if chart_color_change_req :
         self.__set_widget_colors()
      if chart_y_values_change_req:
         self.__destroy_y_labels()
         self.__create_y_labels()
         self.__set_widget_colors()
         self.__set_widget_font()
         self.__set_text()
      if chart_x_values_change_req:
         self.__destroy_x_labels()
         self.__create_x_labels()
         self.__set_widget_colors()
         self.__set_widget_font()
         self.__set_text()
     
      if chart_sections_change_req:
         self.__destroy_y_x_sections()
         self.__create_y_sections()
         self.__create_x_sections()

   
   def __reset_chart_info(self)->None:
      self.__output.delete("all")
      self.__real_width = self.width - (self.__y_value_req_space+self.__bar_size+self.__x_data_req_space*2+self.__x_value_req_width)
      self.__real_height = self.height - (self.__y_data_req_space+self.__bar_size+self.__x_value_req_space*1.5)
      self.__place_x = 0
      self.__output.place(y=0, x=0, height=self.__real_height, width=self.__real_width)
      self.__output.configure(height=self.__real_height, width=self.__real_width)

      
   def __re_show_data(self)->None:
      lines_values = [len(line._Line__data) for line in  self.__lines]
      if len(lines_values) > 0:
         self.__reset_chart_info()
         
         maximum_data = max(lines_values)
         max_support = int(self.__real_width/self.__line_width)+1
         
         for line in  self.__lines:
            if maximum_data>max_support:
               line._Line__temp_data = line._Line__data[maximum_data-(max_support)::]
            else:
               line._Line__temp_data = line._Line__data
            line._Line__reset()
         
         lines = self.__lines
         self.lines =[]
         
         for line in lines:
            self.show_data(line=line, data=line._Line__temp_data)
   
   
   def show_data(self, line:Line, data:list)->None:
      re_show_data = False
      if line not in self.__lines:
         self.__lines.append(line)
      line._Line__data += data
      
      if line._Line__hide_state != True :
         for d in data:
            self.___show_data_working = True
            if not self.__force_to_stop_show_data:
               x_start = line._Line__x_end
               y_start = line._Line__y_end
      
               line._Line__x_end += self.__line_width
               line._Line__y_end = (self.__real_height - (self.__real_height/100)*(d/self.__y_data_max*100)) 
               
               if line._Line__x_end > self.__real_width and self.__real_width < 20000:
                  self.__place_x -= self.__line_width
                  
                  self.__output.place(x=self.__place_x,
                                    width=self.__real_width+self.__line_width)
                  
                  self.__real_width += self.__line_width;
               
               elif self.__real_width > 15000:
                  re_show_data = True
                  break;
               if not re_show_data:
                  if line._Line__mode  == "dash":
                     dash_width = line._Line__mode_style[0]
                     space_width = line._Line__mode_style[1]
                     total_width = dash_width+space_width
                     real_line_width = ((abs(y_start - line._Line__y_end)**2) + (self.__line_width**2)) ** (1/2)

                     dash_count = real_line_width/total_width
                     dash_count = (dash_count)
                     space_count = real_line_width/total_width
                     space_count = (space_count)

                     dash_space_y_change = (abs(y_start - line._Line__y_end))/ (space_count)

                     dash_y_change  = dash_space_y_change *(dash_width/total_width)
                     dash_y_change = (dash_y_change)

                     space_y_change  = dash_space_y_change *(space_width/total_width)
                     space_y_change = (space_y_change)
 
                     dash_x_change = (dash_width**2-dash_y_change**2)**(1/2)
                     dash_x_change = (dash_x_change)
                     
                     space_x_change = (space_width**2-space_y_change**2)**(1/2)
                     space_x_change = (space_x_change)

                     terminate = False
                     while (line._Line__x_end>x_start):
                        x_end = x_start + dash_x_change
                        if y_start > line._Line__y_end :
                           to_up = True
                           to_down = False
                           y_end = y_start - dash_y_change
                        else:
                           y_end = y_start + dash_y_change
                           to_up = False
                           to_down = True
                        
                        if x_end>line._Line__x_end:
                           x_end = x_end - (x_end-line._Line__x_end)
                           terminate = True
                        if y_end<line._Line__y_end and to_up:
                           y_end = y_end - (y_end-line._Line__y_end)
                           terminate = True
                        if y_end>line._Line__y_end and to_down:
                           y_end = y_end - (y_end-line._Line__y_end)
                           terminate = True
                       
                        self.__output.create_line(x_start, y_start, x_end, y_end
                                                      ,fill=line._Line__color ,width=line._Line__size)
                        if terminate:
                           break
                        x_start = x_end
                        y_start = y_end
                        x_end = x_start + space_x_change
                        if y_start > line._Line__y_end :
                           y_end = y_start - space_y_change
                        else:
                           y_end = y_start + space_y_change
                        
                        if x_end>line._Line__x_end:
                           x_end = x_end - (x_end-line._Line__x_end)
                           terminate = True
                        if y_end<line._Line__y_end and to_up:
                           y_end = y_end - (y_end-line._Line__y_end)
                           terminate = True
                        if y_end>line._Line__y_end and to_down:
                           y_end = y_end - (y_end-line._Line__y_end)
                           terminate = True

                        x_start = x_end
                        y_start = y_end
                        
                        if terminate:
                           break

                  elif  line._Line__mode=="circle":
                     circle_size = line._Line__mode_style[0]
                     space_width = line._Line__mode_style[1]
                     total_width = circle_size+space_width
                     real_line_width = ((abs(y_start - line._Line__y_end)**2) + (self.__line_width**2)) ** (1/2)

                     circle_count = real_line_width/total_width
                     circle_count = (circle_count)
                     space_count = real_line_width/total_width
                     space_count = (space_count)

                     circle_space_y_change = (abs(y_start - line._Line__y_end))/ (space_count)

                     circle_y_change  = circle_space_y_change *(circle_size/total_width)
                     circle_y_change = (circle_y_change)

                     space_y_change  = circle_space_y_change *(space_width/total_width)
                     space_y_change = (space_y_change)

                     circle_x_change = (circle_size**2-circle_y_change**2)**(1/2)
                     circle_x_change = (circle_x_change)
                     
                     space_x_change = (space_width**2-space_y_change**2)**(1/2)
                     space_x_change = (space_x_change)
  
                     terminate = False
                    
                     while (line._Line__x_end>x_start):
                        x_end = x_start + circle_x_change
                        if y_start > line._Line__y_end :
                           to_up = True
                           to_down = False
                           y_end = y_start - circle_y_change 
                        else:
                           y_end = y_start + circle_y_change 
                           to_up = False
                           to_down = True
                           
                        if x_end>line._Line__x_end:
                           x_end = x_end - (x_end-line._Line__x_end)
                           terminate = True
                        if y_end<=line._Line__y_end and to_up:
                           y_end = y_end - (y_end-line._Line__y_end)
                           terminate = True
                        if y_end>line._Line__y_end and to_down:
                           y_end = y_end - (y_end-line._Line__y_end)
                           terminate = True
                        
                        self.__output.create_oval(x_start-circle_size/2,
                                                  y_start-circle_size/2,
                                                  x_start+circle_size-circle_size/2,
                                                  y_start+circle_size-circle_size/2,
                                                  fill=line._Line__color, outline=line._Line__color )
                        if terminate:
                           break
                        x_start = x_end
                        y_start = y_end
                        x_end = x_start + space_x_change
                        if y_start > line._Line__y_end :
                           y_end = y_start - space_y_change
                        else:
                           y_end = y_start + space_y_change
                        if x_end>line._Line__x_end:
                           x_end = x_end - (x_end-line._Line__x_end)
                           terminate = True
                        if y_end<line._Line__y_end and to_up:
                           y_end = y_end - (y_end-line._Line__y_end)
                           terminate = True
                        if y_end>line._Line__y_end and to_down:
                           y_end = y_end - (y_end-line._Line__y_end)
                           terminate = True
                       
                        x_start = x_end
                        y_start = y_end
                        
                        if terminate:
                           break

                  elif line._Line__mode=="line":
                     self.__output.create_line(x_start, y_start, line._Line__x_end, line._Line__y_end
                                                      ,fill=line._Line__color ,width=line._Line__size)
                  
                  
            else:
               break
         
         if re_show_data:
            self.__re_show_data()
         self.___show_data_working = False
      
      
   def place(self, x=None, y=None, rely=None, relx=None, anchor=None):
      self.__main_frame.place(x=x, y=y, rely=rely, relx=relx, anchor=anchor)
      self.__place_info_x = x
      self.__place_info_y = y
      self.__place_info_rely = rely
      self.__place_info_relx = relx
      self.__place_info_anchor = anchor
      
      
   def pack(self, pady=None, padx=None, before=None, after=None,
            side=None, ipadx=None, ipady=None, anchor=None):
      self.__main_frame.pack(pady=pady, padx=padx, before=before, 
                after=after, side=side, ipadx=ipadx, ipady=ipady, anchor=anchor)
      self.__pack_info_pady = pady
      self.__pack_info_padx = padx
      self.__pack_info_before = before
      self.__pack_info_after = after
      self.__pack_info_side = side
      self.__pack_info_ipadx = ipadx
      self.__pack_info_ipady = ipady
      self.__pack_info_anchor = anchor
      
      
   def grid(self, column=None, columnspan=None, ipadx=None, ipady=None,  padx=None,  pady=None, row=None, 
            rowspan=None, sticky=None):
      self.__main_frame.grid(column=column, columnspan=columnspan, ipadx=ipadx, ipady=ipady, 
               padx=padx,  pady=pady, row=row, rowspan=rowspan, sticky=sticky)
      self.__grid_info_column = column
      self.__grid_info_columnspan = columnspan
      self.__grid_info_ipadx = ipadx
      self.__grid_info_ipady = ipady
      self.__grid_info_padx = padx
      self.__grid_info_pady = pady
      self.__grid_info_row = row
      self.__grid_info_rowspan = rowspan
      self.__grid_info_sticky = sticky
      
   def place_forget(self):
      self.__main_frame.place_forget()
   def pack_forget(self):
      self.__main_frame.pack_forget()
   def grid_forget(self):
      self.__main_frame.grid_forget()
      
   def place_back(self):
      self.__main_frame.place(x=self.__place_info_x, y=self.__place_info_y,
                              rely=self.__place_info_rely, relx=self.__place_info_relx,
                              anchor=self.__place_info_anchor)
   def pack_back(self):
      self.__main_frame.pack(pady=self.__pack_info_pady, padx=self.__pack_info_padx,
                             before=self.__pack_info_before, after=self.__pack_info_after,
                             side=self.__pack_info_side, 
                             ipadx=self.__pack_info_ipadx, ipady=self.__pack_info_ipady,
                             anchor=self.__pack_info_anchor)
   def grid_back(self):
      self.__main_frame.grid(column=self.__grid_info_column, columnspan=self.__grid_info_columnspan, 
                           ipadx=self.__grid_info_ipadx, ipady=self.__grid_info_ipady, 
                           padx=self.__grid_info_padx,  pady=self.__grid_info_pady,
                           row=self.__grid_info_row, rowspan=self.__grid_info_rowspan, sticky=self.__grid_info_sticky)
      
   def hide(self, line:Line, state:bool):
      if line._Line__hide_state != state:
         line._Line__hide_state = state
         self.__re_show_data()
      
      
   def hide_all(self,state:bool):
      if state == True:
         self.__output.place_forget()
      self.__force_to_stop_show_data = True
      while self.___show_data_working :
            pass
      for line in self.__lines:
         line._Line__hide_state = state
      self.__force_to_stop_show_data = False
      self.__re_show_data()
