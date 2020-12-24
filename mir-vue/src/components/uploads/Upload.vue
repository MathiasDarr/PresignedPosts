<template>
 <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <label>File
        <input type="file" id="file" ref="file" v-on:change="onFileChange()"/>
      </label>
     <v-btn small color="primary" v-on:click="submit()">Primary</v-btn>
    </div>
  </div>
</template>


<script>
/* eslint-disable */
import axios from 'axios';

export default {
  props: ['files'],
  data () {
    return {
      file: ''
    }
  },
  methods: {

        async fetch_presigned_url(file){
            try{

                var name = this.file.name
                var url ='https://ov6pba8qlb.execute-api.us-west-2.amazonaws.com/Prod/signedURL'
                
                var body = {userID:'dakobedbard@gmail.com', filename:name}
                const response = await axios.post(url, body)
                console.log(response.data.presigned)

                var data = response.data.presigned 
            
                let form = new FormData()
                Object.keys(data.fields).forEach(key=>form.append(key, data.fields[key]))
                form.append('file', this.file)

                await fetch(data.url, {method:'POST', body: form})

            }catch(err){
                console.log(err)
            }
        },

        async upload_file(){
            await this.fetch_presigned_url(file)
        },

        submit(){
          
          this.upload_file()
        },

        onFileChange(){
          this.file = this.$refs.file.files[0]
          
          
        }
   },
}
</script>