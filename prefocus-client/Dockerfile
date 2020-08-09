 # base image
FROM node:9.6.1

# set working directory
RUN mkdir /usr/src/prefocus-client
WORKDIR /usr/src/prefocus-client

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/prefocus-client/node_modules/.bin:$PATH

# install and cache app dependencies
COPY . /usr/src/prefocus-client
RUN npm install
RUN npm install react-scripts@1.1.1 -g

# start app
CMD ["npm", "start"]
