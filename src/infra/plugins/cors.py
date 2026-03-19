from fastapi.middleware.cors import CORSMiddleware


class Cors:
    def __init__(self, app):
        self.app = app

    def configure(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
