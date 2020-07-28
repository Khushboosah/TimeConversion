# TimeZoneConversion
In this project I have shown how to get the current time from the various time-zones which can be selected.

The project is developed using Python running on Flask as the API backend.
The front-end is in vue.js.

## Project setup

#### Steps to create "server" enviornment
```
$ python3.7 -m venv env
$ source env/bin/activate
```

#### Install Flask and Flask-CORS
```
$ pip install Flask==1.0.2 Flask-Cors==3.0.7
```

### Vue Setup
#### Install npm and run following commands

#### Steps to create vue client
```
npm install -g @vue/cli@3.7.0
```

#### Use the down arrow key to highlight "Manually select features", and then press enter. select "Babel", "Router", and "Linter / Formatter"
```
Vue CLI v3.7.0
? Please pick a preset: Manually select features
? Check the features needed for your project: Babel, Router, Linter
? Use history mode for router? Yes
? Pick a linter / formatter config: Airbnb
? Pick additional lint features: Lint on save
? Where do you prefer placing config for Babel, PostCSS, ESLint, etc.? In package.json
? Save this as a preset for future projects? (y/N) No
```
#### Install the axios library to send AJAX requests
```
$ npm install axios@0.18.0 --save
```

### Steps to run the Projects

#### Checkout this git repository 

#### Open a terminal.Navigate to server folder. Run the following command 
```
(env)$ python app.py
```

#### Open a terminal.Navigate to "client" directory then run below command, which compiles and hot-reloads for development
```
npm run serve
```
#### To avoid prettier's unneccessary errors and warning, use following command
```
npm run serve --fix
```

### In the browser http://localhost:8080
#### On load you will see this page 
![Before image](https://github.com/Khushboosah/TimeZoneConversion/blob/master/client/src/assets/Screen%20Shot%202020-07-27%20at%208.47.33%20PM.png)

#### Post selection of timezone you should see below updated page 
![After image](https://github.com/Khushboosah/TimeZoneConversion/blob/master/client/src/assets/Screen%20Shot%202020-07-27%20at%208.48.10%20PM.png)
