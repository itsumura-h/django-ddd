import Util from './util'

export default class API {
  static getIndex= () => {
    const url = '/api/ddd_sample/'
    return Util.getAPI(url)
  }
}
