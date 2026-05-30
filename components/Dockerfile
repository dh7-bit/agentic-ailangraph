FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install uv
RUN uv pip install --system -r requirements.txt

COPY . .

CMD ["langgraph", "dev", "--host", "0.0.0.0", "--port", "2024"]