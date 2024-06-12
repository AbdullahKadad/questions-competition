from http.server import BaseHTTPRequestHandler
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
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
        base_url = "https://opentdb.com/api.php"
        params = {"amount": amount}
        if category:
            params["category"] = category
        response = requests.get(base_url, params=params)
        return response.json()

    def format_questions(self, questions):
        formatted = ""
        for question in questions:
            formatted += f"Category: {question['category']}\n"
            formatted += f"Question: {question['question']}\n"
            formatted += f"Answer: {question['correct_answer']}\n"
            formatted += "\n"
        return formatted


