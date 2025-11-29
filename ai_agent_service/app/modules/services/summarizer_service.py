from google import genai
from google.genai import types
from app.configs.gemini import GEMINI_API_KEY, GEMINI_MODEL

client = genai.Client(api_key=GEMINI_API_KEY)


class SummarizerService:
    """
    Service class for generating text summaries.

    Handles:
    - Running the Gemini summarization model

    # INFO: can extend for future methods and testing.
    """

    # for grpc can't use schema have to define string rather than a SummarizeRequestSchema
    # def generate_summary(text: SummarizeRequestSchema) -> str:
    def generate_summary(self, text: str) -> str:
        """
        a service to summarizer router. it takes the text prompt those text in gemini and respond with the response came from gemini
        """
        try:
            prompt = f"Summarize the following text in 1-2 sentences. make sure it should be the same context i gave you i mean it should have the same meaning but with a small explanation:\n{text}"
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.5, max_output_tokens=200
                ),
            )

            return response.text
        except Exception as e:
            # TODO: have to set the logger if any further issue appear
            return "Some issue occur for sure"

    def calculate(self, a: int, b: int, c: int, operation: str = "add") -> int:
        """
        this is just a test for protobuff which takes multiple arguement.
        specially the area like in request and response we have to define the no of arguementj for that testing this is a testing service

        - Performs a simple operation on 3 numbers
        """
        if operation == "add":
            return a + b + c
        elif operation == "multiply":
            return a * b * c
        else:
            raise ValueError("Unsupported operation")


def get_summarizer_service() -> SummarizerService:
    """
    returns an instance of Summarizer
    """
    return SummarizerService()
