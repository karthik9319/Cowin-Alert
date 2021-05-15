FROM python:3.8.5-slim

# streamlit-specific commands
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
    [general]\n\
    email = \"\"\n\
    " > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
    [server]\n\
    enableCORS = false\n\
    " > /root/.streamlit/config.toml'

COPY requirements.txt ./
COPY data/ ./
COPY main/ ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
