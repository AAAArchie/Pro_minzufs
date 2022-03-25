import {reactive} from "vue";

// 设置用户变量
const variables = reactive({
    userId: -1,
    username: '请登录',
    token: '',
})

// 将浏览器传上来的用户数据放到变量中去
export function login(data: { username: string, token: string, id: number }) {
    variables.username = data.username
    variables.token = data.token
    variables.userId = data.id
}

// 清除掉用户变量数据
export function logout() {
    variables.username = '请登录'
    variables.token = ''
    variables.userId = -1
}

export default variables
