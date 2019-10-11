import axios from 'axios'
import CONST from './const'

export default class Util {
  static getAPI=(url) => {
    url = CONST.APIHOST + url
    return axios
      .get(url)
      .then(response => {
        return response.data
      })
      .catch(err => {
        console.error(err)
      })
  }

  static putAPI=(url, params) => {
    url = CONST.APIHOST + url
    return axios
      .put(url, params)
      .then(response => {
        return response.data
      })
      .catch(err => {
        console.log(err)
      })
  }
}
