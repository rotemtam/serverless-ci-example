FROM node:4.2.3

# Install Apex
WORKDIR /tmp
RUN wget https://raw.githubusercontent.com/apex/apex/master/install.sh && bash /tmp/install.sh

# Install dependencies
COPY package.json /srv/package.json
WORKDIR /srv
RUN npm i && mkdir /srv/src && mkdir /srv/infra

# Copy code into container
COPY src /srv/src
COPY infra /srv/infra

# Run
WORKDIR /srv/src
CMD ["apex", "deploy"]
