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

  static create = (params) => {
    const url = '/api/ddd_sample/create/'
    return Util.postAPI(url, params)
  }

  static update= (params) => {
    const url = `/api/ddd_sample/${params.id}/update/`
    return Util.putAPI(url, params)
  }

  static delete= (id) => {
    const url = `/api/ddd_sample/${id}/delete/`
    return Util.deleteAPI(url)
  }
}
