This project prepared for working on Social Analytics which need to work on different social media platform such as YouTube, Facebook, Instagram, Reddit and LinkedIn to scrap the comments from these social media platforms using keywords.

## How to install the requirements for running youtube

```
pip install -r requirements.txt
```  

## Files and their meanings  

<li> <strong> 'raw_files' Folder </strong> </li>
<ul> It has the all raw data each country has folder to her row data  </ul>
<ul><strong> raw_files_youtube  </strong> is the final raw file for all keywords and all countries</ul>


<li><strong> 'utilities' Folder </strong> </li>
<ul> 'buying_signal_utilities.py' file has five function which are signal keywords, cleaning data, lemmatize sentence, matches for checking buying signals and remove duplicates data. You must use object from the class to call the functions  </ul>

<li><strong> 'buying_signal_youtube_unitedstates.csv' </strong> </li>
<ul> This is the  csv file that has the final result for united states which we use in the dash board </ul>


<li><strong> 'raw_file_youtube.ipynb' </strong> </li>
<ul> This file which uses the data from youtube, write it in raw files and made them after that as a one raw file called raw_file_youtube.csv</ul>

<li><strong> 'buying_signal_youtube.ipynb' </strong> </li>
<ul> This file responsible for cleaning the data , drop the duplicates data and make the buying signal the output writen in buying_signal_youtube.csv </ul>

<img width="1186" alt="Screenshot 2023-01-24 at 7 33 14 PM" src="https://user-images.githubusercontent.com/63105388/224153835-e3ddc99c-7821-4895-acd4-4a73f164fe2d.png">

# How to run the code
<ul>
<li>First one needs to run the file raw_file_youtube.py .
</li>
<li>Second one  will have to run the file buying_signal_youtube.py </li>
</ul> 

