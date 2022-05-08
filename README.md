# challenge_API_deployment

## property prediction api
A Flask API that predict properties's price with lineer regression.
Data scraping for [immoweb](https://www.immoweb.be/en) in Belgium


An API published by [@saifalbaghdadi](https://www.linkedin.com/in/saif-malkshahi/) and you can find my Frist APP on [Heroku](https://saif99.herokuapp.com/predict).


## Description
The API return the prediction the price of a propertie in Belgium, based on data scrapped from Immoweb. 
For the predictions our Machine Learning model looks at the relationship between the postal code, the state of the construction, the property subtype (apartment, studio, villa, chalet, ...), and existance of a fireplace, terrace, garden and/or fully equiped kitchen, an estimate of the asking price is made.


## Installation

Clone the repository:
```
https://github.com/saifalbaghdadi/challenge_API_deployment.git
```

Install the requirements

```
pip install -r requirement.txt

```

 Specification
```
- win 10
- Pyhton 3.10
- Flask
- Heroku
- Scikit-learn
```

## How it works
1. Processor  
First, the data are cleaned. That means that we drop all the entirely empty rows, string values
are cleaned up, outliers and properties without price and area indication are dropped, duplicates
and columns with the lowest correlation rate are deleted, and some other minor riddances.    

To put everything ready for the rest of the process, the variables that remain are transformed into
features.  

2. Model  
In the second step, the prediction is prepared. Firstly, the price, area, outside space and land
surface are rescaled. This is done in order to apreciate more linealy the relationship between price and area.

Secondly, the database is split and into a train and test dataframe. The first one is used to train the model.  

3. Predictor  
This object is going to be initializated when the app.py is runned. This predictor will load the model which is already trained to make the prediction.  

The data is checked to see if there is any error in the format or/and type, then preprocessed and it columns reformated in order to get a matrix with the required size and pased trough our model to get the prediction.  

4. app.py  
Here is where the `POST` and `GET` requests are processed.   

# The pipeline

1. When you enter on APP in [Heroku](https://saif99.herokuapp.com/).

#### It should show you (I'm alive)

2. Add ( /predict)


#### You will go to the API interface [Heroku](https://saif99.herokuapp.com/predict).

3. User interface :
* Post_Code (The city where you want to search for a house/Apartment).
* Rooms (Number of the rooms).
* area (Total land area).
* Garden ( Do you want a house with a garden: If Yes add ( 1 ) / if No add ( -1 )).
* Terrace ( Do you want a house with Terrace: If Yes add ( 1 ) / if No add ( -1 )).

* When you press RUN, the predicted price will appear to you




```

## Usage
  
For the predictions, send a `POST` request to https://immoanderlecht.herokuapp.com/predict with the following parameters:
  ```
  
  
```json
{
  "data": {
    "area": int,
    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
    "rooms-number": int,
    "zip-code": int,
    "land-area": Optional[int],
    "garden": Optional[bool],
    "garden-area": Optional[int],
    "equipped-kitchen": Optional[bool],
    "full-address": Optional[str],
    "swimming-pool": Optional[bool],
    "furnished": Optional[bool],
    "open-fire": Optional[bool],
    "terrace": Optional[bool],
    "terrace-area": Optional[int],
    "facades-number": Optional[int],
    "building-state": Optional[
      "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
    ]
  }
}

```


Then the result from the API will be:

```json
{
  "prediction": Optional[float],
 
}

```

If there is any error on the type of the data, formatting or fields missing. The result willl be:

  ```json
{
      "error": Optional[str]
}
```
<br>



## Author
SAIF MALKSHAHI
