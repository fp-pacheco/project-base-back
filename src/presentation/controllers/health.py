from datetime import datetime, timezone

from src.core.settings import Settings


class HealthController:
    async def check(self) -> dict:
        return {
            "status": "ok",
            "version": Settings.API_VERSION,
            "environment": Settings.APP_ENV,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
