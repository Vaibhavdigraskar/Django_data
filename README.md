# Data Preprocessing and Visualization Web Application

This project is a Django-based web application that allows users to upload CSV files, preprocess the data, and view insights and visualizations. It provides features for:

- File upload and preview.
- Data cleaning (handling missing values).
- Calculating summary statistics (mean, median, standard deviation).
- Visualizing numerical columns (e.g., histograms).

---

## Features

1. **File Upload**: Users can upload CSV files directly from the homepage.
2. **Data Preprocessing**:
   - Handles missing values.
   - Identifies numerical and categorical columns.
3. **Data Insights**:
   - Displays summary statistics for numerical columns.
   - Provides visualizations such as histograms.
4. **Interactive Interface**: A visually appealing UI for both the upload page and insights page.

---

## Prerequisites

Ensure the following are installed on your system:

1. Python (>= 3.9)
2. pip (Python package manager)
3. Virtual environment (optional but recommended)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Django_VE3.git
cd Django_VE3
```

### 2. Create and Activate a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate   # For Linux/MacOS
venv\Scripts\activate    # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Run the following command to set up the database:

```bash
python manage.py migrate
```

### 5. Run the Development Server

Start the server using:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

---

## File Structure

```
project-root/
├── dataPreprocess/          
│   ├── settings.py          
│   ├── urls.py              
├── visual/                  
│   ├── views.py             
│   ├── templates/           
│   │   ├── upload.html      
│   │   ├── insights.html 
├── static/                  
├── requirements.txt         
├── manage.py                
```

---

## Brief Explanation

### Upload Page

The homepage allows users to upload a CSV file. Once uploaded, the file is processed, and the user is redirected to the insights page.

### Insights Page

The insights page displays:

- **Data Summary**: Numerical statistics like mean, median, and standard deviation.
- **Visualizations**: Histograms for numerical columns.
- **Processed Data**: A preview of the preprocessed dataset.

---

## Future Enhancements

- Adding support for more file formats (e.g., Excel).
- Providing additional data visualization options.

---

## Contact

For questions or issues, please contact:

- **Name**: Vaibhav Digraskar
- **Email**: [digraskarvaibhav668@gmail.com](mailto\:digraskarvaibhav668@gmail.com)

---


