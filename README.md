# ML-project-2

## Project Description

This project implements a chatbot interface that provides detailed Indian cuisine recipes with pretty images of the dishes and YouTube video links for the recipes. The chatbot interface is built using Streamlit and interacts with the Google Gemini LLM to fetch the recipes.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/SrikerJoshi/ML-project-2.git
   cd ML-project-2
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Dependencies

- streamlit
- requests
- pillow

## Usage Instructions

1. Open the Streamlit app in your web browser.
2. Enter the name of the Indian dish you want to cook in the text input field.
3. The chatbot will provide a detailed recipe, an image of the dish, and a YouTube video link for the recipe.

## Troubleshooting

- If the app fails to start, ensure that all dependencies are installed correctly.
- If you encounter any issues with fetching images or YouTube links, check your internet connection.

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.
