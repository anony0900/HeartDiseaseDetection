# Heart Disease Detection Web Application

This is a machine learning-based web application that predicts heart disease conditions based on user inputs. The application uses a trained model to analyze data and provides predictions through a user-friendly interface.

## Features
- User-friendly UI built with HTML and CSS
- Predicts heart disease based on input features
- Uses trained machine learning models (Neural Network and Random Forest)
- Interactive prediction page

## Technologies Used
- Frontend: HTML, CSS
- Backend: Flask (Python)
- Machine Learning Models: Neural Network (NN_model.pkl) & Random Forest (RF_model.pkl)
- Data Preprocessing: Scikit-learn (scaler.pkl)
- Dataset: `heart.csv` (sourced from Kaggle)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/anony0900/HeartDiseaseDetection.git
   ```
2. Navigate to the project directory:
   ```sh
   cd HeartDiseaseDetection
   ```
3. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```
4. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Start the Flask backend:
   ```sh
   python app.py
   ```
6. Open the browser and visit `http://127.0.0.1:5000` to use the application.

## File Structure
- `static/css/` - Contains stylesheets (Style.css, all.min.css)
- `templates/` - Contains HTML files (original.html, predict.html)
- `HeartDisease.ipynb` - Jupyter notebook for model training
- `NN_model.pkl` - Trained Neural Network model
- `RF_model.pkl` - Trained Random Forest model
- `scaler.pkl` - Scaler used for preprocessing input data
- `heart.csv` - Dataset used for training the model
- `app.py` - Flask application for handling UI and predictions
- `test.py` - Testing script for model evaluation

## Usage
1. Enter patient health details in the form.
2. Submit the form to get a prediction.
3. The model will process the inputs and display results indicating the likelihood of heart disease.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Author
[anony0900](https://github.com/anony0900)

