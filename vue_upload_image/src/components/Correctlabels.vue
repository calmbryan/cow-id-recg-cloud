<template>
  <div>
    <h5> Update the label of an image </h5>
    <br>
    <form>
        <input type="text" v-model="newlabel" placeholder="Type the correct label" required>
        <input type="file" required @change="getFile($event) ">
    </form>
    <br>
    <button class="btn btn-success" @click="correct">Submit</button>
 
    <div class="alert alert-light" role="alert"> {{ message }}  </div>
</div>
</template>

<script>
import UploadService from "../services/UploadFilesService";

export default {
  name: "correct-files",
  data() {
    return {
      file: "",
      newlabel: "",
      message: ""
    };
  },
    methods: {
        getFile(event) {
            this.file = event.target.files[0];
            this.message = ""
        },
        correct() {
            UploadService.correct(this.file, this.newlabel)
            .then(response => {
                console.log(response.data)
                this.message = response.data
            })
            .catch(error=>{
                console.log(error);
                alert('Something Wrong!');
            })
        }    
    }
};

</script>
