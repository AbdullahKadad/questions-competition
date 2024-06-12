from http.server import BaseHTTPRequestHandler
import requests

class handler(BaseHTTPRequestHandler):
    """
    A request handler for the trivia questions API. This handler processes GET requests to retrieve trivia questions
    from the Open Trivia Database and returns the questions as plain text.

    Supported query parameters:
    - amount: The number of trivia questions to retrieve (maximum 50).
    - category: The category ID for the trivia questions.

    If the category ID is 33 or higher, a special message "You have just 32 category" is returned.
    """

    def do_GET(self):
        """
        Handles GET requests by parsing query parameters, fetching trivia questions from the Open Trivia Database,
        and returning the formatted questions as plain text.
        """
        query_params = self.path.split('?')[-1].split('&')
        params = {param.split('=')[0]: param.split('=')[1] for param in query_params if '=' in param}

        amount = int(params.get('amount', 10))
        category = params.get('category', None)

        if amount > 50:
            amount = 50

        if category and int(category) >= 33:
            response_body = "You have just 32 category"
        else:
            trivia_data = self.get_trivia_questions(amount, category)
            response_body = self.format_questions(trivia_data['results'])

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_body.encode())

    def get_trivia_questions(self, amount=10, category=None):
        """
        Fetches trivia questions from the Open Trivia Database API.

        Parameters:
        - amount (int): The number of trivia questions to retrieve (default is 10).
        - category (str): The category ID for the trivia questions (default is None).

        Returns:
        - dict: The JSON response from the API containing the trivia questions.
        """
        base_url = "https://opentdb.com/api.php"
        params = {"amount": amount}
        if category:
            params["category"] = category
        response = requests.get(base_url, params=params)
        return response.json()

    def format_questions(self, questions):
        """
        Formats the trivia questions into a plain text string.

        Parameters:
        - questions (list): A list of trivia questions in JSON format.

        Returns:
        - str: The formatted string containing the questions and answers.
        """
        formatted = ""
        for question in questions:
            formatted += f"Category: {question['category']}\n"
            formatted += f"Question: {question['question']}\n"
            formatted += f"Answer: {question['correct_answer']}\n"
            formatted += "\n"
        return formatted