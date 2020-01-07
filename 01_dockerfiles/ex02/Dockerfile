FROM ruby:latest

RUN	gem install rails sqlite3 &&\
	apt update &&\
	apt install nodejs -y &&\
    curl -o- -L https://yarnpkg.com/install.sh | bash
    


ONBUILD ADD	app /opt/app
ONBUILD WORKDIR	/opt/app
ONBUILD EXPOSE 3000
ONBUILD RUN	bundle install &&\
			bundle exec rake db:migrate &&\
			bundle exec rake db:seed


## ------ Usage --------
# docker build -t ft-rails:on-build . — Build an image from your Dockerfile
# docker build -t ex02 . — Build an image from Dockerfile provided by task
# docker run -it --rm -p 3000:3000 --network="host" ex02 /bin/bash — Run created image

## ------ Testing --------
#mkdir projects
#cd projects
#rails new blog
#cd blog
#rails server
#open new terminal : docker exec -it <container_name> /bin/bash
#curl -I "localhost:3000"