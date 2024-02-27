# Linear Algebra Lab
_Labs 0-4 are introductory labs based on the numpy library. The remainder of the course is based on OpenCV and machine-learning libraries._

## Lab 0: Introduction to Jupyter Notebooks
_In this lab, the students learn the basics of Python, Markdown, and Jupyter Notebooks._

**Syllabus**
- Read the syllabus and ask questions.

### <span style="color:red;"> Exercise </span>
- Create a Markdown cell 
- Write your name and email

### <span style="color:red;"> Exercise </span>
- Create a code cell
- Write a Python script that prints "Hello, World!"

### <span style="color:red;"> Exercise </span>
- Create a markdown cell and convert it to code.

### <span style="color:red;"> Exercise </span>
- Use Markdown to write the Gaussian integral in $\LaTeX$. 

### <span style="color:red;"> Exercise </span>
- Import matplotlib and numpy.
- Write a function of the gaussian integral. 
- Plot the function.

**Breadboards**
- Follow the instructions to wire an LED on a breadboard.


## Lab 1: Image processing in Python I
_This lab replaces the Intro to Python lab with an emphasis on image processing._

### <span style="color:blue;"> TODO </span>
- This lab is too long. Remove some of the unecessary examples. 
- Emphasize how to use lists vs numpy arrays, and when it is appropriate to use each. 
- Emphasize list comprehension and for loops. 
- Emphasize how to make functions. 
- Emphasize how to make test cases. 
- _Note: In this lab, the students should be partially graded on test cases. It decreases the chance of error and makes things easier on the grader._

### <span style="color:red;"> Exercise </span>
_The purpose of this exercise is to show how to write test cases._
- Write a function that calculates the factorial of a number.
- Write test cases for the function.
    - Negative numbers
    - Zero
    - Positive numbers
    - Non-integer numbers

### <span style="color:red;"> Exercise </span>
_The purpose of this exercise is to show how to load an image as a numpy array and display it using matplotlib._

### <span style="color:red;"> Exercise </span>
_The purpose of this exercise is to show how to loop through an image, which is done many times in the course. People need to know how to do it right._
- Convert an image to a numpy array.
- Efficiently loop through the array and change the color of the image.

### <span style="color:red;"> Exercise </span>
_The purpose of this exercise is to show how to handle lists of images._
- Create a video from a collection of images. 
- Use the 'cv2' library to view the video. 

### <span style="color:red;"> Exercise </span>
_The purpose of this exercise is to show how to flatten and reshape images._
- Write a function that flattens an image and constructs a histogram of the pixel values.
- Write test cases for hand-made matrices to show that the function works.
    - Print the matrices and plot the histograms
- Create a histogram for the real image in the GitHub repository.

### <span style="color:red;"> Exercise </span>
_The purpose of this exercise is to demonstrate more sophisticated manipulation of images._
_Note: The answer key is given in "lab_02_prob_freq.ipynb" of the Probability lab in DSLabs._
- Create a function that calculates the LBP of an image.
- Write test cases for hand-made matrices to show that the function works.


## Lab 2: Introduction to the Raspberry Pi
_In this lab, the students use the onboard temperature sensor to collect temperature data._

**Install Raspberry Pi Pico firmware**
- Place the RPi on a breadboard.
- Use the instructions on the RPi website to install the Micropython firmware on the Pico.

**Collect temperature data**
- Download the pico_temperature.py script from the class GitHub.
- Use Thonny to upload the script to the Pico and collect temperature data.

### <span style="color:red;"> Exercise </span> 
- Collect 1,000 temperature measurements. 
- Plot the raw data using Python.
- _Skill: Data visualization_

### <span style="color:red;"> Exercise </span>
- Create a function that converts the raw temperature data to degrees Celsius.
- _Skill: Functions_

### <span style="color:red;"> Exercise </span>
- Create a function that converts the raw temperature data to degrees Fahrenheit.
- _Skill: Functions_


## Lab 3: Image processing in Python II
_This lab is a continuation of Lab 1. The students learn how to interpolate and perform transformations in numpy. The students also learn how to use the OpenCV library._

### <span style="color:red;"> Exercise </span>
_The purpose of this exercise is to recall how to write test cases._
- Write a function that calculates the factorial of a number.
- Write test cases for the function.
    - Negative numbers
    - Zero
    - Positive numbers
    - Non-integer numbers

**Interpolation in 1D**
- Use the numpy library to interpolate a 1D array.

### <span style="color:red;"> Exercise </span>
- Use the numpy library with interpolation to scale a 1D array up and down.

**Scaling an image**
- Use grid interpolation to scale an image.

### <span style="color:red;"> Exercise </span>
- Use the numpy library with interpolation to scale an image up and down (more pixels and fewer pixels).

**Applying linear transformations to an image**
- Use the numpy library to apply linear transformations to an image.

**The OpenCV library**
- Learn the basic functions of the OpenCV library.

### <span style="color:red;"> Exercise </span>
- use the OpenCV library to scale an image. 
- Use the OpenCV library to apply linear transformations to an image.

## Lab 4: Convolution
_The purpose of this lab is to show how much image processing can be accomplished with convolution. The second purpose is to show how convolution can be expressed as matrix multiplication._

**Convolution**
- Explain the concept of convolution.

**Blurring an image**
- Convolve with a Gaussian kernel to blur an image.

**Convolution with the Sobel kernel**
- Convolve with the Sobel kernel to find the edges of an image.

### <span style="color:red;"> Exercise </span>
- Come up with a new kernel and convolve it with an image.
- Can you come up with a kernel that sharpens an image?

### <span style="color:blue;"> TODO </span>
- I don't like the sections on finding corners with the Harris algorithm. It is too complicated for this course.

**Convolution as matrix multiplication**
- Derive the formula for convolution as matrix multiplication.

### <span style="color:red;"> Exercise </span>
- Write a function that accepts an image and a kernel and convolves the image with the kernel using matrix multiplication.
- Write test cases for hand-made matrices to show that the function works.


## Lab 5: Template matching
_The purpose of this lab is to show how to use template matching to find objects in an image._

**Template matching**
- Describe the concept of template matching.

### <span style="color:red;"> Exercise </span>
- Implement template matching in numpy. 
- Use matrix multiplication, as in the convolution lab. 

### <span style="color:red;"> Exercise </span>
- Implement template matching in OpenCV.

### <span style="color:red;"> Exercise </span>
- Use the template matching algorithm in OpenCV to find the location of the eyes in an image of a face.
- Apply the algorithm to all of the provided images. 


## Lab 6: Motion tracking
_The purpose of this lab is to extend the concept of template matching to track objects in a video._

**Motion tracking**
- Describe the concept of motion tracking.

### <span style="color:red;"> Exercise </span>
- Use the template matching algorithm to track a bouncing ball in a video.


## Lab 7: Graphics
## Lab 8: Reverse 3D projection
## Lab 9: Error correction
## Lab 10: Introduction to accelerometers
## Lab 11: Image compression
## Lab 12: Finite difference equations
## Lab 13: Neural networks