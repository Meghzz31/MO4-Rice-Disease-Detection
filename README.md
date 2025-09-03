RiceLeaf Disease Detection
Overview

RiceLeaf Disease Detection is a web-based application that identifies diseases in rice leaves using machine learning and deep learning techniques. The project helps farmers detect leaf diseases early and take preventive measures to protect their crops.

Features

Upload an image of a rice leaf.

Predict the disease type (e.g., Brown Spot, Leaf Smut, etc.).

User-friendly interface with real-time results.

Dataset and trained model integrated into the application.

Technologies Used

Backend: Python, Django

Machine Learning: Keras, TensorFlow

Frontend: HTML, CSS, JavaScript, Bootstrap

Database: SQLite (default for Django)

Project Structure
RiceLeafApplication/
├─ RiceLeaf/                 # Django project folder
├─ RiceLeafApp/              # Django app containing views, models, templates
├─ dataset/                  # Dataset of rice leaf images
├─ RasaModel/                # Optional: Rasa chatbot integration
├─ manage.py                 # Django management script
├─ requirements.txt          # Python dependencies
├─ README.md                 # Project documentation
└─ .gitignore

Installation

Clone the repository:

git clone https://github.com/Meghzz31/MO4-Rice-Disease-Detection.git


Navigate to the project folder:

cd RiceLeafApplication


Create a virtual environment and activate it:

python -m venv venv
.\venv\Scripts\activate  # Windows


Install dependencies:

pip install -r requirements.txt


Run migrations:

python manage.py migrate


Start the server:

python manage.py runserver


Open your browser at http://127.0.0.1:8000/ to access the application.

Usage

Upload an image of a rice leaf.

Click Predict.

The system will display the predicted disease and suggestions for treatment.

Dataset

The dataset/ folder contains images of healthy and diseased rice leaves used to train the model.

Contributing

Feel free to fork the repository and submit pull requests. Please follow the standard GitHub workflow.

License

This project is licensed under the MIT License.
