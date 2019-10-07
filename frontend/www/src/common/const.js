const DEV = {
  mode: 'dev',
  APIHOST: 'http://localhost:8001'
}

const PROD = {
  mode: 'prod',
  APIHOST: window.location.origin
}

let CONST = null
if (process.env.NODE_ENV === 'development') {
  CONST = DEV
} else if (process.env.NODE_ENV === 'production') {
  CONST = PROD
}

export default CONST
