<style scoped>
.container2 {  
    max-width: 620px; 
    min-width: 420px;
    margin: 40px auto;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 0.9em;
    color: #888;
}

.tabs {
    overflow: hidden;
    margin-left: 5px;
    margin-bottom: -2px;
}

.tabs ul {
    list-style-type: none;
    margin-left: 20px;
}

.tabs a{
    float: left;
    cursor: pointer;
    padding: 12px 24px;
    transition: background-color 0.2s;
    border: 1px solid #ccc;
    border-right: none;
    background-color: #f1f1f1;
    border-radius: 10px 10px 0 0;
    font-weight: bold;
}
.tabs a:last-child { 
    border-right: 1px solid #ccc;
}

/* Change background color of tabs on hover */
.tabs a:hover {
    background-color: #aaa;
    color: #fff;
}

/* Styling for active tab */
.tabs a.active {
    background-color: #fff;
    color: #484848;
    border-bottom: 2px solid #fff;
    cursor: default;
}

/* Style the tab content */
.tabcontent {
    padding: 30px;
    border: 1px solid #ccc;
    border-radius: 10px;
  box-shadow: 3px 3px 6px #e1e1e1
}
</style>
<template>
 <div id="app">
  <div class="container" style="width:600px">

     <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <div class="container">
        <span class="navbar-brand">Cow Recognition System</span>
      </div>
    </nav>
      <br>   
      <br>
      <br>
      <br>
   
  <div id="tabs" class="container2">
    <div class="tabs">
        <a v-on:click="activetab=1" v-bind:class="[ activetab === 1 ? 'active' : '' ]">Predict Image</a>
        <a v-on:click="activetab=2" v-bind:class="[ activetab === 2 ? 'active' : '' ]">Update Label</a>
        <a v-on:click="activetab=3" v-bind:class="[ activetab === 3 ? 'active' : '' ]">Video Stream</a>
    </div>

    <div class="content">
        <div v-if="activetab === 1" class="tabcontent">
              <UploadFiles></UploadFiles>
        </div>
        <div v-if="activetab === 2" class="tabcontent">
              <Correctlabels></Correctlabels>
        </div>
        <div v-if="activetab === 3" class="tabcontent">
           <h5>Video stream </h5>
        </div>
    </div>
  </div>


 </div>
 </div>
</template>

<script>
import UploadFiles from "./components/UploadFiles";
import Correctlabels from "./components/Correctlabels";


export default {
  name: "App",
 data() {
    return {
      activetab: 1
    };
  },
  components: {
    UploadFiles,
    Correctlabels
  }
};
</script>

