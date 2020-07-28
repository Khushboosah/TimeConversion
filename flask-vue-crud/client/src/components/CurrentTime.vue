<template>
  <div class="container">
        <Header />
        <br>
        <p> {{msg}} : {{timestamp}}</p>
        <br><br>
        <select v-model="tz" class="select-css">
          <option v-for="t in timeZones" :key="t">{{ t }}</option>
        </select>
        &nbsp;
        <button type="submit" value="Submit" @click="getnewTimeZone()">Submit</button>
  </div>
</template>

<script>
import axios from 'axios';
import Header from './Header.vue';

export default {
  name: 'CurrentTime',
  components: {
    Header,
  },
  data() {
    return {
      timestamp: '',
      timeZones: [],
      tz: '',
      msg: 'Your Local Time',
    };
  },
  methods: {
    getLocalTime() {
      const path = 'http://localhost:5000/get_new_time';
      axios.get(path)
        .then((res) => {
          this.timestamp = res.data.current_time;
          this.timeZones = res.data.time_zones;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getnewTimeZone() {
      const path = 'http://localhost:5000/get_timezone?tz=' + this.tz;
      axios.get(path)
        .then((res) => {
          this.timestamp = res.data.current_time;
          this.msg = 'Your Selected New Time';
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getLocalTime();
  },
};
</script>

<style scoped>
p {
  color: red;
  font: bold 30px sans-serif;
}
button{
  background-color: #32313b;
  border: none;
  color: white;
  padding: .6em 1.4em .5em .8em;
  border-radius: 12px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  margin: 4px 2px;
  cursor: pointer;
  font: bold 20px sans-serif;
}
.select-css {
    font: 700 18px sans-serif;
    color: #444;
    line-height: 1.3;
    padding: .6em 1.4em .5em .8em;
    margin: 0;
    border: 1px solid #aaa;
    box-shadow: 0 1px 0 1px rgba(0,0,0,.04);
    border-radius: .5em;
    -moz-appearance: none;
    -webkit-appearance: none;
    appearance: none;
    background-color: #fff;
}
</style>
