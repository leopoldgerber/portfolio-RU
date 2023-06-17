# Marketing Web Scraping

<code>[1 - Download Data](1%20-%20Download%20Data.py)</code>
<code>[2 - Data Preprocessing](2%20-%20Data%20Preprocessing.py)</code>
<code>[3 - DB Upload](3%20-%20DB%20Upload.py)</code>
<code>[Power BI](Marketing%20Web%20Scraping%20Power%20BI%20Demo.pbix)</code>

- [1 - Информация](#--информация--)
- [2 - Examples from the parsing script](#examples-from-the-parsing-script)
- [3 - Power BI](#power-bi)

<br>

### - Информация -
Analysis of competitor traffic by country. Search for countries for further growth. Analysis of the popularity of the services offered.

### - Expected result -
A compilation of competitor traffic information broken down by country. All information should be visualized on an interactive dashboard.

### - Technical tasks -
- Data parsing
- Build emulation
- Data analysis
- Data preprocessing
- Feature engineering
- Report automation
- Data visualization

### - Comments -
Add a traffic source and split traffic per device. Additional information is welcome.

### - NOTE -
Due to commercial confidentiality, the data has been changed and key points have been removed. The reduction does not affect the skills shown.

<br>

## More information about the used scripts:

#### 1 - Download Data

The main script for downloading reports from an account on the platform. 

Emulates downloading a person, to bypass account blocking. Contains random values for the height of the scroll in both directions, making pauses between transitions and pauses before and after pressing buttons.
Passes through each domain in turn with the reporting categories selected for it. The storage location of the downloaded reports is set by the user. The selected location will be used for further assembly of all reports, including the processing of these reports.

#### 2 - Data Preprocessing

Processing and combining all reports by category. Uses lists of successfully downloaded reports by domains and collects all reports together.
The method of entering months is manual, it can be modified. It is also possible to upload a file with domains. Domains will be processed (some extra characters will be deleted, the list will be cleared of duplicates).
All methods in the class are equal to categories. It is possible to select the desired categories/methods.

#### 3 - DB Upload

Responsible for loading data from the collected reports into the database. Includes connection to the database, processing of column names and types (for proper loading into the database).

<br>

## Power BI
### - Traffic and unique users -
![Power BI 1](https://github.com/leopoldgerber/portfolio/assets/114569329/1c03749e-250c-4923-8429-eea69e8a0a0a)

### - Traffic by device, traffic source and unique users -
![Power BI 2](https://github.com/leopoldgerber/portfolio/assets/114569329/9ce434f9-38f5-4c7b-9c9b-51bcf620c801)


[Scroll up](#marketing-web-scraping)
