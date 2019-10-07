import axios from 'axios'
import CONST from './const'

export default class Util {
  static getAPI=(url) => {
    url = CONST.APIHOST + url
    return axios
      .get(url)
      .then(response => {
        return response.data.value
      })
      .catch(err => {
        console.error(err)
      })
  }
}
