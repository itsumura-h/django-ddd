import Util from './util'

export default class API {
  static getIndex= () => {
    const url = '/api/ddd_sample/'
    return Util.getAPI(url)
  }

  static getShow= (id) => {
    const url = `/api/ddd_sample/${id}/`
    return Util.getAPI(url)
  }
}
