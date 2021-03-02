export const state = () => ({
  BASE_URL: 'https://cms.aiotlab.hk',
  drawer: false,
  auth: {
    loggedIn: false,
    username: '',
    jwt: '',
    avatar: '',
    team: '',
    email: '',
  },
  projectInfo: {
    Pid: '',
    person: '',
    photo: '',
    status: '',
    team: '',
    title: '',
    updated_at: '',
    description: '',
    youtube: '',
    category: '',
  },
})
export const mutations = {
  logout(state) {
    state.auth.loggedIn = false
    state.auth.username = ''
    state.auth.jwt = ''
    state.auth.avatar = ''
    state.auth.team = ''
  },
  userInfo(state, result) {
    state.auth.loggedIn = true
    state.auth.username = result.user.username
    state.auth.jwt = result.jwt
    if (result.user.avatar === null) state.auth.avatar = ''
    else state.auth.avatar = state.BASE_URL + result.user.avatar.url
    state.auth.team = result.user.team
    state.auth.email = result.user.email
  },
  projectInfo(state, result) {
    state.projectInfo.Pid = result.data.id
    state.projectInfo.person = result.data.person
    if (result.data.photo.length !== 0)
      state.projectInfo.photo = result.data.photo[0].url
    else state.projectInfo.photo = ''
    state.projectInfo.status = result.data.status
    state.projectInfo.team = result.data.team
    state.projectInfo.title = result.data.title
    state.projectInfo.updated_at = result.data.updated_at
    state.projectInfo.description = result.data.description
    if (result.data.youtube != null)
      state.projectInfo.youtube = result.data.youtube
    else state.projectInfo.youtube = ''
    state.projectInfo.category = result.data.Category
  },
  SET_DRAWER(state, payload) {
    state.drawer = payload
  },
}
export const getters = {
  getuserInfo: (state) => {
    return state.auth
  },
  getprojectInfo: (state) => {
    return state.projectInfo
  },
}
export const actions = {}
export const modules = {}
