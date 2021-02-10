# Shortest path between two pixels within an intensity range

This program uses [Djikstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to determine the shortest path between two pixels in an image within a range of intensities.

## Installation

Use the package manager pip to install Opencv and Numpy

```bash
pip install opencv-python
pip install numpy
```

## Usage

After running the program in Python, several prompts will appear.

```
Type file name with file extension of image you'd like to test:
```

Enter an absolute or relative path for your image.

For this example, we will be using the included 5x5 pixel image. Below represents the intensities of each pixel in the image:

[[1. 0. 1. 1. 1.]  
 [0. 2. 3. 4. 0.]  
 [1. 2. 0. 2. 0.]  
 [1. 0. 1. 3. 0.]  
 [0. 0. 1. 1. 1.]]

You can type 'test.png'

```
Type a value between 0 and 255 to be included in set V. Type 'Done' when no more values need to be added:
```

A path is determined valid if starting pixel intensity and the neighboring pixel intensities are values contained within set V.

For this example, you can type '0' and then press the ENTER key. Then, type '1' and then press the ENTER key. Then, type 'Done' and then press the ENTER key.

```
Enter a valid x coordinate for p:
Enter a valid y coordinate for p:
```

p is the starting pixel location. Origin, (0,0), is the top left pixel in the image. Enter valid x and y coordinates.
NOTE: x is positive going right of the origin in an image. y is positive going below the origin in an image.

For this example, type '1' and then press the ENTER key for the x coordinate. Then, type '3' and then press the ENTER key for the y coordinate. Below represents the p coordinate in the image:

[[1. 0. 1. 1. 1.]  
 [0. 2. 3. 4. 0.]  
 [1. 2. 0. 2. 0.]  
 [1. p. 1. 3. 0.]  
 [0. 0. 1. 1. 1.]]

```
Enter a valid x coordinate for q:
Enter a valid y coordinate for q:
```

q is the ending pixel location. Enter valid x and y coordinates.

For this example, type '4' and then press the ENTER key for the x coordinate. Then, type '0' and then press the ENTER key for the y coordinate. Below represents the q coordinate in the image:

[[1. 0. 1. 1. q.]  
 [0. 2. 3. 4. 0.]  
 [1. 2. 0. 2. 0.]  
 [1. 0. 1. 3. 0.]  
 [0. 0. 1. 1. 1.]]

```
1 - 4-path
2 - 8-path
3 - m-path
Type a number for the pixel neighbor relationship you'd like to select:
```

4-path means that only neighboring pixels in cardinal directions will be evaluated.  
8-path means that neighboring pixels both cardinal and intercardinal directions will be evaluated.  
m-path means that the path for neighboring pixels in cardinal directions will be evaluted first. If a valid pixel in the cardinal direction does not exist, then neighboring pixels in the intercardinal directions will be evaluated.

For this example, type '1' and then press the ENTER key.

If following the examples above, the following result should be returned:

```
The length of the shortest path is 8:
[[4. 5. 6. 7. 8.]
 [3. 0. 0. 0. 7.]
 [2. 0. 2. 0. 6.]
 [1. 0. 1. 0. 5.]
 [2. 1. 2. 3. 4.]]
```

p (1,3) has a value of 0  
q (4,0) has a value of 8  
The shortest path(s) from p to q will start from 0 and count up to the number in the q. In the example, there are 3 shortest paths
