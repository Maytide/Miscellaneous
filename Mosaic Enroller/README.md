# Mosaic Enroller

Automate attempts to enroll in mosaic when the class is full. **Not a web-based solution: requires full attention of the computer.** It is window-size invariant, but probably doesn't work well in extreme cases. Will run indefinitely (ie, does not stop when enrolment is successful, because I was too lazy to add that)

It requires the three template images of the buttons (highlighted in red in below images), which aren't hard to make. Or PM me if interested.

Source of most of the template matching: https://www.pyimagesearch.com/2015/01/26/multi-scale-template-matching-using-python-opencv/

## Instructions:
0. Install python and all the library dependencies. 
1. Make sure the courses are in your shopping cart.
2. Go to mosaic &rarr; enroll &rarr; add
3. Open cmd and run 
```
python mosaic_enroller.py
``` 
then quickly return to the browser with mosaic open.

4. Leave the computer be. If you want it to enroll quicker per attempt, play with the 
```time.sleep()``` 
values.

Screen 1: 
![alt text](https://i.imgur.com/tLOMg33.png)

Screen 2: 
![alt text](https://i.imgur.com/SXEm7y4.png)

Screen 3: 
![alt text](https://i.imgur.com/tHZRekg.png)
