# https://fishdata-17370ae93936.herokuapp.com/

### README.md

```markdown
# Fish Market Prediction

This repository contains a Flask web application that predicts the weight and species of fish based on input features. The application is deployed on Heroku and can be accessed [here](https://fishdata-17370ae93936.herokuapp.com/).

## Project Overview

The Fish Market Prediction app allows users to input specific features of fish and get predictions for both the weight and species of the fish. The application is built using Flask and includes two machine learning models:

1. **Regression Model**: Predicts the weight of the fish.
2. **Classification Model**: Predicts the species of the fish.

## Dataset

The dataset used for this project is the Fish Market dataset, which includes various features of different fish species. The features used in this model include:

- Length1
- Length2
- Length3
- Height
- Width

## Application Structure


### Files

- **app.py**: Main Flask application file.
- **templates/index.html**: HTML file for the web interface.
- **regression_model.pkl**: Serialized regression model.
- **classification_model.pkl**: Serialized classification model.
- **scaler.pkl**: Serialized scaler for preprocessing.
- **label_encoder.pkl**: Serialized label encoder for decoding species predictions.
- **requirements.txt**: List of dependencies.
- **Procfile**: Instructions for Heroku to run the app.
- **runtime.txt**: Specifies the Python runtime version.
- **.gitignore**: Lists files and directories to ignore in the Git repository.

## Setup and Deployment

### Prerequisites

- Python 3.9
- Flask
- Gunicorn
- Joblib
- Numpy
- Scikit-learn

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the Flask application locally:
   ```sh
   python app.py
   ```

### Deployment on Heroku

1. Create a new Heroku app:
   ```sh
   heroku create your-app-name
   ```

2. Add the Heroku remote:
   ```sh
   git remote add heroku https://git.heroku.com/your-app-name.git
   ```

3. Deploy the application:
   ```sh
   git push heroku master
   ```

4. Scale the application:
   ```sh
   heroku ps:scale web=1
   ```

5. Open the application in your browser:
   ```sh
   heroku open
   ```

## Usage

Visit the [Fish Market Prediction App](https://fishdata-17370ae93936.herokuapp.com/) and input the features of the fish to get predictions for the weight and species.

### Predict Weight

- Length1
- Length2
- Length3
- Height
- Width

### Predict Species

- Length1
- Length2
- Length3
- Height
- Width

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The Fish Market dataset used in this project.
- The Flask framework for building the web application.
- Heroku for hosting the application.

```


