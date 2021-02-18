# web-scraping-challenge
Missions_to_Mars

<img src='./Images/mission_to_mars.PNG'>


This homework was very instructive as it afforded the opportunity to put into practice the concepts taught in class about webscrapping and the many uses it affords any individual in the web development field of data analytics. The focus is on Mars. The capacity of science to investigate the unknown has been at the core of human development especially over the last century. Mars is a planet with lots of intrigues and reaching out for this "red" plannet is a principal endeavor of mankind, especially the science community.

Step 1
The first part of the homework involved the scrapping exercise. Using Jupyter Notebook, BeautifulSoup, Pandas library and Requests/Splinter, as key tools, the website: [NASA Mars News Site](https://mars.nasa.gov/news/) code named NASA Mars News Site was scrapped and the latest News Title and Paragraph text was obtained and passed to reference variables.The obtained variables are news_title and news_par for the latest news title and the latest paragraph text respectively.

The JPL Mars Space Images part involved visiting this website: [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars). Used splinter to navigate the site and found the image url for the current featured Mars image and assigned the url string to a variable called 'featured_image_url', also ensured the full size '.jpg' image was obtained. Presented a complete url string for the image.

Mars Facts: This part involved visiting the USGS Astrogeology website [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) and obtained high resolution images for each of Mar's hemispheres contained on the site. Used splinter to click on the images on the parent webpage and obtained all 4 images in '.jpg' format. Each image url string for the full resolution hemisphere image and the corresponding titles were saved using a python dictionary with the keys: 'img_url' and 'title' for the images and titles of each image respectively.

Here are the 4 respective images scrapped from the site:

1. Cerberus Hemisphere Enhanced Image:
<img src='./Images/Cerberus_Hemisphere_image.JPG'>

2. Schiaparellis Hemisphere Enhanced Image:
<img src='./Images/Schiaparellis_Hemisphere_image.JPG'>

3. Syrtis Major Hemisphere Enhanced Image:
<img src='./Images/Syrtis_Major_Hemisphere_image.JPG'>

4. Valles Marineris Hemisphere Enhanced Image:
<img src='./Images/Valles_Marineris_Hemisphere_image.JPG'>

