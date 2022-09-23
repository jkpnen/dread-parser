<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- ABOUT THE PROJECT -->

## About The Project

Dread Parser is a tool for parsing the [Dread's](https://en.wikipedia.org/wiki/Dread_(forum)) 
comments section from HTML files and analysing drug related strings and their occurrences in the comments.
The tool is built for my Master's thesis, where I study the Finnish dark web drug trade.

The aim of the algorithm is to calculate the prevalence of different strings and to estimate the 
prevalence of drugs nationwide as well as regionally. Instances are calculated based on the beginning of 
the words and predefined keywords and exceptions (stop words).

The script goes through the messages one string at a time. For example, the first message could be a 
sentence _I sell weed_. The script takes the first word _I_, which is not a keyword. Next, the script 
looks ast the word _sell_, which is also not a keyword. Finally, the word _weed_ comes in, which in turn 
is found among the keywords. The occurrence found is added to the **Cannabis** category in the list. 
The script then moves to the next string or continues to the next message.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Abstarct -->

## Abstract

My Master's thesis examines Finnish drug trafficking in the dark web using data analytics. The research 
questions deal with the prevalence of drugs in the dark web, and based on the research results, the 
prevalence of drugs in Finland is estimated. The result obtained is compared with the wastewater study 
carried out by THL that is Finnish Institute for Health and Welfare (THL) is a research and development 
institute under the Finnish Ministry of Social Affairs and Health.

The data of the study (N ≈ 8500) has been collected by means of data mining and a statistical analysis has
been prepared using the classifier algorithm and confusion matrices. This is a case study and 
classification was chosen as the method of analysis. Based on the results of the study, cannabis, 
amphetamines and medicines are the most abundant in the Finnish drug trade. Ecstasy and subutex are also
relatively common. Hallucinogens and cocaine account for a small proportion of the distribution and heroin 
is almost non-existent. The result is not about the quantitative prevalence of drugs, but more about the 
overall prevalence or trend. The research result and other findings are in line with previous research data.

The study is socially significant and provides information on the prevalence of drugs in Finland. In 
addition, the drug trade on the dark web is in a constant state of flux, so research provides up-to-date 
information on its current state. The study also looks at the actions taken by the authorities on the dark 
web and provides ideas that will benefit them. In addition, the study presents topics for further research
and considers the future of drug trafficking in the dark side of the web.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

The latest version of Python 3.8.x

### Installation

**Note:** The code is tested only with the PyCharm IDE.

1. Clone the repo
   ```sh
   git clone https://github.com/jkpnen/dread-parser.git
   ```
2. Install Python packages. Use the pip package installer or whatever you prefer.
   ```sh
   pip install pandas
   pip install xlsxwriter
   pip install pathlib
   pip install typing
   pip install bs4
   pip install matplotlib
   ```
3. Set the target folder (containing HTML-files) such as C:/DATASET/ as an argument and
   run the **main.py** to get the dread messages as **.csv** and **.xslx** files
   ```
   python3 main.py C:/HTML_FILES_FOLDER/
   ```
4. Run the **drug_parser.py** to get plots and result.
   ```
   python3 drug_parser.py
   ```

---
**consts.py** contains **STOPWORDS**, **DRUG_CATEGORIES** and **DRUGS** variables. Feel free to
modify these (to your own language) to get different results:

1. **STOPWORDS** is a list of words to ignore because they would otherwise be
   classified as incorrect keywords. For example a word _weed_ belongs to a set of
   keywords but a word _weeder_ does not.
2. **DRUG_CATEGORIES** is a list of the main categories into which the drug-related
   strings found are classified.
3. **DRUGS** is a dictionary of drug strings that make up a set of keywords.

---

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->

## Contributing

Any contributions you make are **greatly appreciated**. If you have a suggestion that would
make this better, please fork the repo and create a pull request. You can also simply open an
issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->

## License

Distributed under the GNU General Public License v2.0. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->

## Contact

Joonas Koponen - jkpnen@gmail.com

Project Link: [https://github.com/jkpnen/dread-parser](https://github.com/jkpnen/dread-parser)

<p align="right">(<a href="#top">back to top</a>)</p>
