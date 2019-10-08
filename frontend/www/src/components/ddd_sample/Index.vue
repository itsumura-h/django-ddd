<template>
  <div>
    <h1>index</h1>
    <table border="1">
      <tr>
        <th>id</th><th>名前</th><th>メールアドレス</th><th>年齢</th>
      </tr>
      <tr v-for="row in indexData" :key="row.id" @click.stop="openEditDialog(row.id)">
        <td>{{row.id}}</td><td>{{row.name}}</td><td>{{row.email}}</td><td>{{row.age}}</td>
      </tr>
    </table>

    <!-- モーダル -->
    <v-dialog
      v-model="isOpenEditDialog"
      width="60vw"
    >
      <v-card>
        <v-card-title>
          <span class="headline">ユーザー編集</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field label="名前*" :value="showData.name" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="Email*" :value="showData.email" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="生年月日*" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-select
                  :items="info"
                  label="権限*"
                  required
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="dialog = false">Save</v-btn>
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
      showData: {},
      info: {},
      items: [],
      isOpenEditDialog: false
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
    },
    openEditDialog (id) {
      this.isOpenEditDialog = !this.isOpenEditDialog
      API.getShow(id)
      .then(response => {
        this.showData = response.data
        this.info = response.info.map(row => row.permission)
      })
    }
  }
}
</script>
