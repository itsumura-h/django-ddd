<template>
  <div>
    <h1>index</h1>
    <table border="1">
      <tr>
        <th>id</th><th>名前</th><th>メールアドレス</th><th>年齢</th><th>権限</th>
      </tr>
      <tr v-for="row in indexData" :key="row.id" @click.stop="openEditDialog(row.id)">
        <td>{{row.id}}</td><td>{{row.name}}</td><td>{{row.email}}</td><td>{{row.age}}</td><td>{{row.permission}}</td>
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
                <v-text-field
                  label="名前"
                  v-model="showData.name"
                  required
                />
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Email"
                  v-model="showData.email"
                  required
                />
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="生年月日"
                  v-model="showData.birth_date"
                  required
                />
              </v-col>
              <v-col cols="12">
                <v-select
                  label="権限"
                  v-model="showData.permission"
                  :items="info"
                  required
                />
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="blue darken-1" text @click="save">更新</v-btn>
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
      info: [],
      indexData: [],
      showData: {},
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
        // permissionだけの配列にする
        this.info = response.info.map(row => row.permission)
      })
    },
    updateShowData (column, value) {
      console.log([column, value])
    },
    save () {
      console.log(this.showData)
      this.isOpenEditDialog = !this.isOpenEditDialog
    }
  }
}
</script>
