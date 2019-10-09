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

  static update= (params) => {
    const url = `/api/ddd_sample/${params.id}/update/`
    return Util.putAPI(url, params)
  }
}
