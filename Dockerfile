FROM ubuntu

# Copy the app
COPY . /

RUN ls 

# Install dependencies
RUN apt update
RUN apt install -y python3 python3-pip ffmpeg software-properties-common git
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip install -r /requirements.txt

# RUN the app
CMD [ "python3", "/run.py" ]