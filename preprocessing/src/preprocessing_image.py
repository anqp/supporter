import cv2
import glob


i = 972
for j in range (1, 5) :
	image_list =  glob.glob("../../../models/10" + str(j) + "GOPRO/*.JPG")
	image_list.sort()
	for image_name in image_list:
		print "Processing " + image_name  
		image = cv2.imread(image_name)
		print image.shape

		r = 320.0 / image.shape[1]
		dim = (320, int(image.shape[0] * r))

		# perform the actual resizing of the image and show it
		resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
		print resized_image.shape
		cv2.imwrite("../../../models/images/" + str(i) + ".JPG",resized_image)
		i +=1
print "Done"

