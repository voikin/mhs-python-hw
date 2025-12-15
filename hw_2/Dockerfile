FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-recommended \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir latex-generator-dazaii

RUN mkdir -p artefacts

COPY generate_pdf.py .

COPY artefacts/itmo.png artefacts/itmo.png

CMD ["python", "generate_pdf.py"]
