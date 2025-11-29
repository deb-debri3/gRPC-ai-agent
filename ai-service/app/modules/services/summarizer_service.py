# from google import genai
# from google.genai import types
# from app.config.gemini import GEMINI_API_KEY, GEMINI_MODEL
# from ..schemas import SummarizerRequestSchema
# from ..exceptions import ErrorSummarizing
#
#
# client = genai.Client(api_key=GEMINI_API_KEY)
#
#
# class SummarizerServices:
#     """
#     Service class for generating text summaries
#     """
#
#     async def generate_summary(self, payload: SummarizerRequestSchema) -> str:
#         prompt = (
#             f"summarize the content into {payload.line}. "
#             f"Make sure to give a similar context with the same meaning but with a small explanation and no point only in paragraph. "
#             f"{payload.text}"
#         )
#
#         try:
#             response = client.models.generate_content(
#                 model=GEMINI_MODEL,
#                 contents=prompt,
#                 config=types.GenerateContentConfig(
#                     temperature=0.5, max_output_tokens=200
#                 ),
#             )
#
#             return response.text
#
#         except Exception as e:
#             raise ErrorSummarizing() from e
#
#
# def get_summarizer_service() -> SummarizerServices:
#     return SummarizerServices()


from google import genai
from google.genai import types
from app.config.gemini import GEMINI_API_KEY, GEMINI_MODEL
from ..schemas import SummarizerRequestSchema
from ..exceptions import ErrorSummarizing


class SummarizerServices:
    """
    Service class for generating text summaries
    """

    def __init__(self):
        self.client = None  # don't initialize here

    async def generate_summary(self, payload: SummarizerRequestSchema) -> str:
        # initialize client lazily
        if self.client is None:
            self.client = genai.Client(api_key=GEMINI_API_KEY)

        prompt = (
            f"summarize the content into {payload.line}. "
            f"Make sure to give a similar context with the same meaning but with a small explanation and no point only in paragraph. "
            f"{payload.text}"
        )

        try:
            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.5, max_output_tokens=200
                ),
            )
            return response.text

        except Exception as e:
            raise ErrorSummarizing() from e


def get_summarizer_service() -> SummarizerServices:
    return SummarizerServices()
