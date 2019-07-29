'''

first step
    
    pip install bokeh 
        or
    pip3 install bokeh 

second step 

pip install jupyter notebook

# run notebook
jupyter notebook

# opening a browser in localhost

'''


'''
jupyter notebook scripts

    # laking a basic Bokeh live graph

    # importing Bokeh

    from bokeh.plotting import figure
    from bokeh.io import output_file, show

    #prepare some date
    x=[1,2,3,4,5]
    y=[6,7,8,9,10]

    #prepare the output file
    output_file("Line.html")

    #freate a figure object 
    f=figure()

    #create line plot
    f.line(x,y)

    # write the plot in the figure object
    show(f)

# Ctrl + Enter

then we can show the Line.html file on the browser.

'''


''' Solution: 195. Plotting Triangles and Circle Glyphs (Practice) 

#Snippet producing the triangle based plot

#Making a basic Bokeh line graph
 
#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
 
#prepare some data
x=[3,7.5,10]
y=[3,6,9]
 
#prepare the output file
output_file("Line.html")
 
#create a figure object
f=figure()
 
#create line plot
f.triangle(x,y)
 
#write the plot in the figure object
show(f)
#Snippet producing the circle based plot

#Making a basic Bokeh line graph
 
#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
 
#prepare some data
x=[3,7.5,10]
y=[3,6,9]
 
#prepare the output file
output_file("Line.html")
 
#create a figure object
f=figure()
 
#create line plot
f.circle(x,y)
 
#write the plot in the figure object
show(f)
'''