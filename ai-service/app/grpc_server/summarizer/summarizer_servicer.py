from ...proto import ai_agent_pb2, ai_agent_pb2_grpc
from ...modules.services.summarizer_service import SummarizerServices


class SummarizerServicer(ai_agent_pb2_grpc.SummarizerServicer):
    async def Summarize(self, request, context):
        service = SummarizerServices()
        summary = await service.generate_summary(payload=request)
        return ai_agent_pb2.SummarizeResponse(summary=summary)
