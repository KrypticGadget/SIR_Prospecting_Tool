from app import app

# This is required for Vercel serverless deployment
def handler(request, response):
    return app(request, response)