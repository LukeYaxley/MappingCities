# GitLab repository for CO2201 Group Projects

<h2>Installation</h2>
<p>In order to install the program from this github repository simply navigate to the 'Final' folder and download the .zip file located there.

From there, extract the file and make sure that whatever python IDE you are using is linked to the venv folder (this will save you having to pip install modules).

If for whatever reason you do not have the virtual environment configured correctly you will be unable to run the following commands. Check the 'Dependencies' section for more information.

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
<p>Just type into the cmd the following command
pip install *name of module*

Only the modules marked in red need to be installed
<p>
<ul>
<li>os</li>
<li>sys</li>
<li style="color:red">pandas</li>
<li style="color:red">geopandas</li>
<li style="color:red">folium</li>
<li style="color:red">overpy</li>
<li style="color:red">geopy</li>
<li style="color:red">django</li>
<li style="color:red">numpy </li>
</ul>

