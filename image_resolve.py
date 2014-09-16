import os
resolutions = ['640x1136','640x960','320x480','1536x2048','768x1024','480x800','720x1280']
origin_image_path = './image';
origin_images = os.listdir(origin_image_path);
for resolution  in resolutions:
	if not os.path.exists('./'+resolution):
		os.mkdir('./'+resolution)
	for image in origin_images:
		print image
		image_name = os.path.basename(image)
		os.popen('convert -resize ' +resolution+'! '+ './image/'+image+' ./'+resolution+'/'+image)	

	