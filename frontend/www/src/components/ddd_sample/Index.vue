<template>
  <div>
    <h1>index</h1>
    <table border="1">
      <tr>
        <th>id</th><th>名前</th><th>メールアドレス</th><th>年齢</th>
      </tr>
      <tr v-for="row in indexData" :key="row.id" @click.stop="dialog = true">
        <td>{{row.id}}</td><td>{{row.name}}</td><td>{{row.email}}</td><td>{{row.age}}</td>
      </tr>
    </table>

    <!-- モーダル -->
    <v-dialog
      v-model="dialog"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">Use Google's location service?</v-card-title>

        <v-card-text>
          Let Google help apps determine location. This means sending anonymous location data to Google, even when no apps are running.
        </v-card-text>

        <v-card-actions>
          <div class="flex-grow-1"></div>

          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import API from '../../common/API'

export default {
  name: 'Index',
  data () {
    return {
      indexData: [],
      dialog: false
    }
  },
  mounted () {
    this.getIndex()
  },
  methods: {
    getIndex () {
      API.getIndex()
        .then(response => {
          this.indexData = response
        })
      console.log(this.indexData)
    }
  }
}
</script>
