from backend.services.analysis_service import AnalysisService


def get_analysis_service() -> AnalysisService:
    return AnalysisService()
