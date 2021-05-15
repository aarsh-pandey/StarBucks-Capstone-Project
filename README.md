# StarBucks Capstone Project

This is the Udacity's DataScience Capstone Project.


### Table of Contents

1. [Installation](#installation)
2. [Description of Project](#description)
3. [Motivation of the project](#motivation)
2. [File Descriptions](#files)
3. [Results](#results)
4. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

To work with this repository, you just need to clone it to your local machine.

```
$ git clone https://github.com/aarsh-pandey/StarBucks-Capstone-Project.git
```

This project works with Python 3.* , to install dependencies just execute

```
$ pip install -r requirements.txt
```

or you can also install required packages separately by executing

```
$ pip install numpy
$ pip install pandas
$ pip install matplotlib
$ pip install seaborn
```

if pip doesn't work for you, just try `pip3` instead of `pip`

## Description of Project <a name="description"></a>
This is the Analysis of the Behavior of the StarBucks’ user on the offer, For this analysis, Starbucks has provided the DataSet that contains simulated data that mimics customer behavior on the Starbucks rewards mobile app.

In these data set Starbucks sends an offer to their users over the given period of time and they have collected each event happened as a log in a file, an offer can either be Discount, Bogo, or Informational. In an informational offer, there is no reward, but neither is there a requisite amount that the user is expected to spend. some user might receive the same offer again, some might not receive the same offer.

Types of offer :
* Discount: Discount on some amount of purchase
* Bogo: Buy one get one free offer
* Informational: Just an Advertisement 

## Motivation of the project <a name="motivation"></a>

In this project my main motivation was to know how people with demographic group are responding to an offer.

The Questions that I had were 

* How did the people with different 
  1. age group get influenced by the offer?
  1. income group get influenced by the offer?
  1. gender get infulensed by the offer?
  1. membership year get infulensed by the offer?

## File Descriptions <a name="files"></a>

<pre>
<code>.
├── <b>README.md</b>
├── <b>Starbucks_Capstone_notebook.ipynb</b> : Analysis of the DataSet.
├── <b>data</b>
│   ├── <b>portfolio.json</b> : DataSet containing all information about each offer.
│   ├── <b>profile.json</b> : DataSet containing all informaton about each user.
│   └── <b>transcript.json</b> : DataSet containing each event log.
├── <b>helper.py</b> : This file contains some of the helper functions used to clean the file.
├── <b>DatasetDescription.md</b> : Markdown file explaining each column of the dataset.
├── <b>pic1.png</b>
└── <b>pic2.png</b>
 </code>
</pre>

To get description of each column in the dataset click [here](https://github.com/aarsh-pandey/StarBucks-Capstone-Project/blob/master/DatasetDescription.md).

## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://aarshpandey.medium.com/how-starbucks-users-behave-on-offer-ffbc17367094).

#### Results that look interesting to me are :

* The most viewed offer is Bogo but the most completed offer is a Discount.
* No one has completed the Informational offer.
* As time is passing, people are getting inactive towards offers.

and For me, the analysis part was interesting, as it gave me some of the results that I was not expecting.


## Licensing, Authors, Acknowledgements<a name="licensing"></a>
**Starbucks** has provided the DataSet that contains simulated data that mimics customer behavior on the Starbucks rewards mobile app.