RiceLeaf Disease Detection

Overview
A web app to detect diseases in rice leaves using deep learning. Helps farmers identify leaf diseases early.

Features
Upload rice leaf images.
Predict disease type (e.g., Brown Spot, Leaf Smut).
Real-time results with a simple interface.

Tech Stack
Backend: Python, Django
ML: TensorFlow, Keras
Frontend: HTML, CSS, JS, Bootstrap

Setup
git clone https://github.com/Meghzz31/MO4-Rice-Disease-Detection.git
cd RiceLeafApplication
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Dataset
Contains images of healthy and diseased rice leaves for model training.
