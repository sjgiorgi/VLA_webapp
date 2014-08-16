import cv
import cv2
import numpy as np
import sys
import math

class Component:
        
        def set_component(self,type, term1, term2, index):
                self.type = type
                self.term1 = term1
                self.term2 = term2
                self.node1 = -1
                self.node2 = -1
                self.connections = []
                self.value = 0
                self.index = index
                
        def print_component(self):
                print "{" + " Type\t\t => " + str(self.type) + "\t\t}"
                print "{" + " Term1\t\t => " + str(self.term1) + "\t}"
                print "{" + " Term2\t\t => " + str(self.term2) + "\t}"
                print "{" + " Node1\t\t => " + str(self.node1) + "\t\t}"
                print "{" + " Node2\t\t => " + str(self.node2) + "\t\t}"
                print "{" + " Value\t\t => " + str(self.value) + "\t\t}"
                print "{" + " Connections\t => " + str( len(self.connections)) +"\t\t}"
                print "{" + " Index \t => " + str(self.index) + "\t\t}"
                print "------------------------------------------"
                
        def add_connections(self, adj_comp):
                if (self.check_duplicate(adj_comp)):
                    return
                else: 
                    self.connections.append(adj_comp.index)

        def check_duplicate(adj_comp):
                    for x in self.connections:
                          if adj_comp.index == x: return False
                          else: return True

def area_thresholding(thresh):
        thresh_src = np.zeros((thresh.shape[0], thresh.shape[1],3), np.uint8)
        thresh_src[:] = (255,255,255)
        contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        area_thresh = 100
        for x in range(0,len(contours)):
                if len(contours[x]) > 100:
                        cv2.drawContours(thresh_src,contours, x, (0,0,0), 1)
        cv2.imwrite("Area Thresh.png", thresh_src)
	return thresh_src

def calculate_distance(comp1pt1, comp1pt2, comp2pt1, comp2pt2):
        dist_pt11 = math.sqrt(math.pow((comp1pt1[0] - comp2pt1[0]),2) + math.pow((comp1pt1[1] - comp2pt1[1]),2))
	dist_pt12 = math.sqrt(math.pow((comp1pt1[0] - comp2pt2[0]),2) + math.pow((comp1pt1[1] - comp2pt2[1]),2))
        dist_pt21 = math.sqrt(math.pow((comp1pt2[0] - comp2pt1[0]),2) + math.pow((comp1pt2[1] - comp2pt1[1]),2))
	dist_pt22 = math.sqrt(math.pow((comp1pt2[0] - comp2pt2[0]),2) + math.pow((comp1pt2[1] - comp2pt2[1]),2))
        return (dist_pt11,dist_pt12,dist_pt21,dist_pt22)

def check_terminals():

	return;

def check_wires():

	return;

def conjoin_wires():

	return;

def fix_wires():

	return;

def intersection_operations(comp_under_test, comp_list, wire_list):
	# Create individual arrays for each component
	gnd_count = 0; vsrc_count = 0; isrc_count = 0; res_count = 0; ind_count = 0; cap_count = 0;
        
        # Iterate through components
        
	return;

def list_traversal():

	return;



def print_netlist():

	return;

def test_template_method(not_black, templates):
        # Read in RGB img and initialize variables
        src = cv2.imread('Contours.png',-1)
        blank = np.zeros((src.shape[0],src.shape[1],3),np.uint8)
        blank[:] = (255,255,255)
        index = 0
        comp_tup = ([])
        comp_list = []; wire_list = []; super_list = [];
        #Iterate over all template images
        for x in templates:
                # Set type of component
                if "ground" in x       : type = "Gnd"
                elif "capacitor" in x : type = "C"
                elif "inductor" in x   : type = "L"
                elif "resistor" in x    : type = "R"
                elif "vsource" in x   : type = "Vsrc"
                elif "isource" in x    : type = "Isrc"
                elif "wire" in x        : type = "Wire"
                else: type = "none"
                # Apply template matching
                threshold = 0.72
                copycat = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
                template = cv2.imread(x, 0)
                res = cv2.matchTemplate(copycat, template, cv2.TM_CCOEFF_NORMED)
                loc = np.where (res >= threshold)
                w,h = template.shape[::-1]
                loc = np.where( res >= threshold)
                # Iterate over matches, creating rectangles
                for pt in zip(*loc[::-1]):
                        dont_draw = False
                        temp_comp = Component()
                        # Set terminal points
                        if w > h   and "vsource0" not in x:
                                term1 = (pt[0],pt[1]+h/2) 
                                term2 = (pt[0] + w, pt[1] + h/2)
                        else: 
                                term1 =  (pt[0] + w/2, pt[1]) 
                                term2 =  (pt[0] + w/2, pt[1] + h)
                        if "ground" in x:
                                term1 = term2
                        # Iterate over lists, trying to delete any unnecessary wires
                        if type == "Wire":
                                for iter_comp in comp_list:
                                        # If term1[0] (temp_comp X) is between any X and Y, don't draw 
                                        if term2[0] <= iter_comp.term2[0] and term1[0] >= iter_comp.term1[0] and term1[1]  >= iter_comp.term1[1] and term2[1] <= iter_comp.term2[1]:
                                                dont_draw = True
                        if type == "Wire":
                                for iter_wire in wire_list:
                                        # If Both Y are within 2 pix, and starting term within 5 pix, don't draw
                                        if term1[1] - 2 <= iter_wire.term1[1] and term1[1] + 2 >= iter_wire.term1[1] and term1[0] - 5 <= iter_wire.term1[0] and term1[0] + 5 >= iter_wire.term1[0]:
                                                dont_draw = True
                                        # If both X are within 2 pix, and starting term within 5 pix, don't draw
                                        if term1[0] -2 <= iter_wire.term1[0] and term1[0] + 2 >= iter_wire.term1[0] and term1[1] - 5 <= iter_wire.term1[1] and term1[1] + 5 >= iter_wire.term1[1]:
                                                dont_draw = True
                                        # Iterate over comp list to make sure wire is not inside rect 
                                        
                                for iter_comp in comp_list:
                                        if term1[0] in range(iter_comp.vertex[0]-2, iter_comp.vertex[0] + iter_comp.cols+4) and term1[1] in range(iter_comp.vertex[1]-4, iter_comp.vertex[1] + iter_comp.rows+4):
                                                 if term2[0] in range(iter_comp.vertex[0]-2, iter_comp.vertex[0] + iter_comp.cols+4) and term2[1] in range(iter_comp.vertex[1]-4, iter_comp.vertex[1] + iter_comp.rows+4):
                                                         dont_draw = True
                        # Check distance in 
                        for comp in super_list:
                                (pt_11,pt_12,pt_21,pt_22) =  calculate_distance(comp.term1, comp.term2, comp.term1, comp.term2)
				if pt_11 == 0 or pt_12==0 or pt_21==0 or pt_22 == 0:
					continue
				elif pt_11 <= 5 or pt_12 <= 5 or pt_21 <= 5 or pt_22 <= 5:
					dont_draw = True

                        # Ignore components which have triggered one of the if statements
                        if (dont_draw):
                                continue

                        # Add component to the list         
                        temp_comp.set_component(type,term1,term2,index)
                       
                        if type != "Wire":
                                temp_comp.cols = w; temp_comp.rows = h; temp_comp.vertex = pt
                                comp_list.append(temp_comp)
                                super_list.append(temp_comp)
                        else: 
                                wire_list.append(temp_comp)
                                super_list.append(temp_comp)
                        
                        # Draw Rectangles
                        cv2.rectangle(blank, pt, (pt[0] + w, pt[1] + h), (0,0,255),2)
                        cv2.rectangle(src,pt,(pt[0] + w, pt[1] + h), (0,0,255),2)
                        # Increment the index of the component
                        index += 1

                # Write final image:
                cv2.imwrite('res.png', blank)

	return (super_list, blank)

def get_erosion_element():
	return;

def main(argv):
        #Make Template List
        templates = []
        templates.append("capacitor0.png")
        templates.append("capacitor90.png")
        templates.append("inductor0.PNG")
        templates.append("inductor90.png")
        templates.append("inductor180.png")
        templates.append("inductor270.png")
        templates.append("vsource0.png")
        templates.append("vsource90.png")
        templates.append("vsource180.png")
        templates.append("vsource270.png")
        templates.append("isource0.png") 
        templates.append("isource90.png")
        templates.append("isource180.png")
        templates.append("isource270.png")
        templates.append("resistor0.png")
        templates.append("resistor90.PNG")
        templates.append("ground0.png")
        templates.append("ground90.PNG")
        templates.append("ground180.PNG")
        templates.append("ground270.PNG")
        templates.append("wire0.PNG")
        templates.append("wire90.PNG")
        
        # Create color arrays
        black = np.array([0,0,0])
        not_black = np.array([100,100,100])
        white = np.array([255,255,255])
        
        # Read in source
        source = cv2.imread(argv[1],-1)
        width,height = source.shape[:2]
        
        # Create blank matrix
        blank = np.zeros((width,height,3), np.uint8) 
        blank[:] = white
        cv2.imwrite("blank.png",blank)
	
        # Apply thresholding
        hsv =  cv2.cvtColor(source, cv2.COLOR_BGR2HSV)
        upper_thresh = np.array([215,215,215])
        lower_thresh = np.array([0,0,0])
        thresh = cv2.inRange(hsv, lower_thresh,upper_thresh)
        cv2.imwrite("inrange.png", thresh)

        # Draw contours onto copycat image
        copycat = blank.copy()
        contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(copycat,contours, -1, lower_thresh, 1)
        cv2.imwrite("Contours.png", copycat)
	# Apply Template Matching & Area Thresholding
        super_list = []; comp_list = []; wire_list = []
        super_list,matched_src = test_template_method(not_black, templates)
        # Split the lists in to wire and component lists
	for temp_comp in super_list:
                if temp_comp.type == "Wire":
                        wire_list.append(temp_comp)
                else:
                        comp_list.append(temp_comp)
                        temp_comp.print_component()
        # Apply area thresholding to remove text
        thresh_src = area_thresholding(thresh)
        final_src = cv2.addWeighted(thresh_src,0.5,matched_src,0.5,0)
        cv2.imwrite("add weighted.png", final_src)
	#  Connect Components
	intersection_operations(super_list, comp_list, wire_list)

if __name__ == '__main__':
	main(sys.argv)
