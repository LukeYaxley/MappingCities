# GitLab repository for CO2201 Group Projects

<h2>Installation</h2>
<p>In order to install the program from this github repository simply navigate to the 'Final' folder and download the .zip file located there.

From there, extract the file and make sure that whatever python IDE you are using is linked to the venv folder (this will save you having to pip install modules).

Next run the following commands.</p>
<ol>
<li>python manage.py migrate</li>
<li>python manage.py runserver</li>
</ol>
<p>The webapp will then be usable at the root ip address http://127.0.0.1:8000/
 </p>


<h2>About this Project</h2>
<p>This project is a webapp to generate roadmap of a given section of city. This will allow scientists who are looking to graph pollution to overlay pollution data over the top. Unfortunately we were unable to finish by giving the ability to upload pollution data as a csv but that would have been the next story</p>
<h3>Dependencies (libraries you need to have installed)</h3>
<ul>
<li>os</li>
<li>sys</li>
<li>pandas</li>
<li>geopandas</li>
<li>folium</li>
<li>overpy</li>
<li>geopy</li>
<li>Django</li>
<li>numpy </li>
</ul>

