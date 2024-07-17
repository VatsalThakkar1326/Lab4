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

To deploy the application on Heroku using the Heroku user interface, follow these detailed steps:

### Deployment on Heroku Using the Heroku User Interface

1. **Create a Heroku Account**:
   If you don't have a Heroku account, you can create one [here](https://signup.heroku.com/).

2. **Login to Heroku**:
   Go to [Heroku](https://www.heroku.com) and log in to your account.

3. **Create a New Heroku App**:
   - Click on the "New" button at the top right corner of the dashboard.
   - Select "Create new app".
   - Enter a unique app name.
   - Choose your region.
   - Click "Create app".

4. **Connect to GitHub**:
   - In the "Deploy" tab, find the "Deployment method" section.
   - Select "GitHub".
   - Click on "Connect to GitHub".
   - Authenticate with GitHub if required.
   - Search for your repository name and connect it.

5. **Automatic Deploys (Optional)**:
   - If you want Heroku to automatically deploy new commits, enable "Automatic deploys".
   - This ensures that every time you push new changes to the main branch, Heroku will redeploy the app.

6. **Manual Deploy**:
   - In the "Manual deploy" section, select the branch you want to deploy.
   - Click "Deploy Branch".

7. **Check Build Logs**:
   - Heroku will now start building your application.
   - You can monitor the build progress in the build logs.
   - If the build is successful, your app will be deployed.

8. **Configure Environment Variables**:
   - Go to the "Settings" tab.
   - Click on "Reveal Config Vars".
   - Add any necessary environment variables (if needed).

9. **Open the App**:
   - Once the deployment is successful, you can open your app by clicking the "Open app" button on the top right.

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


