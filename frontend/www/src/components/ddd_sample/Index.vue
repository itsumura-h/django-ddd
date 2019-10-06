<template>
  <div>
    <p>index</p>
  </div>
</template>

<script>
import API from '../../common/API'

export default {
  name: 'Index',
  data: ()=>{
    return {
      indexData: {}
    }
  },
  mounted() {
    this.getIndex()
  },
  methods: {
    getIndex: ()=>{
      this.indexData = API.index()
    }
  },
}
</script>
