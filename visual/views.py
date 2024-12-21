# views.py
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse


from .forms import UploadCSVForm

# Global variable to hold the processed DataFrame temporarily
uploaded_data = {}

def upload_csv(request):
    global uploaded_data

    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']

            try:
                # Read the uploaded file into pandas DataFrame
                data = pd.read_csv(csv_file)

                # Save data globally (better approach: use session or database)
                uploaded_data['data'] = data

                # Redirect to insights page after successful upload
                return redirect('data_insights')

            except Exception as e:
                return render(request, 'upload.html', {'form': form, 'error_message': f"Error processing file: {str(e)}"})

    else:
        form = UploadCSVForm()

    return render(request, 'upload.html', {'form': form})


def data_insights(request):
    global uploaded_data

    # Ensure data exists before processing
    if 'data' not in uploaded_data:
        return redirect('home')

    data = uploaded_data['data']

    # Example Insights:
    # 1. Identify numerical columns
    numerical_columns = data.select_dtypes(include=['number']).columns.tolist()
    preview_data = data.head(10)

    # Convert the preview data to HTML for display
    table_html = preview_data.to_html(classes='table table-striped', index=False)    

        # 2. Handle Missing Values
    # Replace missing values with the column mean (or other strategies)
    missing_info = data.isnull().sum()
    for col in data.columns:
        if col in numerical_columns:
            data[col].fillna(data[col].mean(), inplace=True)
        else:
            data[col].fillna("Missing", inplace=True)

    summary_stats = data[numerical_columns].describe().T  # Transposed for readability
    summary_stats['median'] = data[numerical_columns].median()

# Convert to a list of tuples for easier template rendering
    summary_stats = summary_stats.reset_index()
    summary_stats_records = summary_stats.reset_index().to_dict(orient='records')


    # 2. Generate histograms for numerical columns
    histograms = {}
    for col in numerical_columns:
        plt.figure(figsize=(6, 4))
        plt.hist(data[col].dropna(), bins=20, color='blue', alpha=0.7)
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')

        # Save plot to a BytesIO buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        # Encode plot as base64 to embed in HTML
        histograms[col] = base64.b64encode(image_png).decode('utf-8')

        plt.close()

    # Pass insights and visualizations to the template
    return render(request, 'insights.html', {
        'numerical_columns': numerical_columns,
        'missing_info': missing_info.to_dict(),
        'summary_stats': summary_stats_records,
        'histograms': histograms,
        'table_html' : table_html,
    })
