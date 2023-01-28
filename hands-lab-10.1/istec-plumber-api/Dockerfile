FROM rstudio/plumber:latest

WORKDIR /app

# Copy Files
ADD requirements.r .
ADD plumber.R .

# Installing R Libraries
RUN Rscript requirements.r

# Run the API
CMD ["/app/plumber.R"]
