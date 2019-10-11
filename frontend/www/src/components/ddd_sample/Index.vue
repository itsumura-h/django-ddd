<template>
  <div>
    <h1>index</h1>
    <p><v-btn color="green" @click="openCreateDialog"><span class="white--text">新規作成</span></v-btn></p>
    <table border="1">
      <tr>
        <th>id</th><th>名前</th><th>メールアドレス</th><th>年齢</th><th>権限</th><th>削除</th>
      </tr>
      <tr v-for="row in indexData" :key="row.id" @click.stop="openEditDialog(row.id)">
        <td>{{row.id}}</td>
        <td>{{row.name}}</td>
        <td>{{row.email}}</td>
        <td>{{row.age}}</td>
        <td>{{row.permission}}</td>
        <td>
          <v-btn color="red" @click="openDeleteDialog(row.id)">
            <span class="white--text">削除</span>
          </v-btn>
        </td>
      </tr>
    </table>

    <!-- 新規作成画面 -->
    <v-dialog
      v-model="isOpenCreateDialog"
      width="60vw"
    >
      <v-card>
        <v-card-title>
          <span class="headline">ユーザー新規作成</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="名前"
                  v-model="createData.name"
                  required
                />
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Email"
                  v-model="createData.email"
                  required
                />
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="生年月日"
                  v-model="createData.birth_date"
                  required
                />
              </v-col>
              <v-col cols="12">
                <v-select
                  label="権限"
                  v-model="createData.permissions"
                  :items="permissions"
                  item-text="label"
                  item-value="id"
                  required
                  return-object
                />
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="blue" @click="confirm">確認</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 編集画面 -->
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
              <v-col cols="12" :class="{ 'form-group--error': $v.showData.name.$invalid }">
                <v-text-field
                  label="名前"
                  v-model="showData.name"
                  v-model.trim="$v.showData.$model.name"
                  required
                />
              </v-col>
              <v-col cols="12" :class="{ 'form-group--error': $v.showData.email.$invalid }">
                <v-text-field
                  label="Email"
                  v-model.trim="$v.showData.$model.email"
                  required
                />
              </v-col>
              <v-col cols="12" :class="{ 'form-group--error': $v.showData.birth_date.$invalid }">
                <v-text-field
                  label="生年月日"
                  v-model.trim="$v.showData.$model.birth_date"
                  required
                />
              </v-col>
              <v-col cols="12">
                <v-select
                  label="権限"
                  v-model="showData.permission"
                  :items="permissions"
                  item-text="label"
                  item-value="id"
                  required
                  return-object
                />
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="blue" @click="confirm"><span class="white--text">確認</span></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 確認画面 -->
    <v-dialog
      v-model="isOpenConfirmDialog"
      width="60vw"
    >
      <v-card>
        <v-card-title>
          <span class="headline">ユーザー編集確認</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="名前"
                  v-model="showData.name"
                  readonly
                />
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Email"
                  v-model="showData.email"
                  readonly
                />
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="生年月日"
                  v-model.trim="showData.birth_date"
                  readonly
                  class="form__input"
                />
              </v-col>
              <v-col cols="12">
                <v-select
                  label="権限"
                  v-model="showData.permission"
                  :items="permissions"
                  item-text="label"
                  item-value="id"
                  readonly
                />
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="blue" @click="save"><span class="white--text">更新</span></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 削除確認モーダル -->
    <v-dialog
      v-model="isOpenDeleteDialog"
      width="60vw"
    >
      <v-card>
        <v-card-title>
          <span class="headline">ユーザー削除確認</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            ID:{{deleteId}}を削除しますか？
          </v-container>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="blue darken-1" text @click="deleteCancel">キャンセル</v-btn>
          <v-btn color="blue darken-1" text @click="deleteUser">削除</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </div>
</template>

<style scoped>
.form-group--error {
  background-color: lightcoral;
}
</style>

<script>
import API from '../../common/API'
import { 
  required, 
  integer, 
  minLength, 
  maxLength
} from 'vuelidate/lib/validators'

export default {
  name: 'Index',
  data () {
    return {
      permissions: [],
      indexData: [],
      createData: {
        name: '',
        email: '',
        birth_date: '',
        permission: 1
      },
      showData: {},
      isOpenCreateDialog: false,
      isOpenEditDialog: false,
      isOpenConfirmDialog: false,
      isOpenDeleteDialog: false,
      deleteId: 0
    }
  },
  validations: {
    showData: {
      name: {
        required
      },
      email: {
        required
      },
      birth_date: {
        required,
        integer,
        minLength: minLength(8),
        maxLength: maxLength(8)
      }
    }
  },
  mounted () {
    this.getIndex()
  },
  methods: {
    // ==================== index ====================
    getIndex () {
      API.getIndex()
        .then(response => {
          this.permissions = response.meta.display.permissions
          this.indexData = response.data.users
        })
    },
    // ==================== create ====================
    openCreateDialog () {
      console.log('openCreateDialog')
      this.isOpenCreateDialog = !this.isOpenCreateDialog
    },
    // ==================== edit ====================
    openEditDialog (id) {
      this.isOpenEditDialog = !this.isOpenEditDialog
      if (this.isOpenDeleteDialog) {
        this.isOpenEditDialog = false
      }
      API.getShow(id)
        .then(response => {
          this.showData = response.data
          this.permissions = response.meta.display.permissions
        })
    },
    updateShowData (column, value) {
      console.log([column, value])
    },
    confirm () {
      this.isOpenConfirmDialog = !this.isOpenConfirmDialog
    },
    save () {
      API.update(this.showData)
        .then(response => {
          this.getIndex()
          this.isOpenConfirmDialog = !this.isOpenConfirmDialog
          this.isOpenEditDialog = !this.isOpenEditDialog
        })
        .catch(err => {
          console.error(err)
        })
    },
    // ==================== delete ====================
    openDeleteDialog (id) {
      this.isOpenDeleteDialog = !this.isOpenDeleteDialog
      this.deleteId = id
      console.log(this.deleteId)
    },
    deleteUser () {
      console.log('削除')
      this.isOpenDeleteDialog = !this.isOpenDeleteDialog
    },
    deleteCancel () {
      this.isOpenDeleteDialog = !this.isOpenDeleteDialog
    }
  }
}
</script>
