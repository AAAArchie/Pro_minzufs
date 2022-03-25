<template>

  <div id="signin">
    <el-divider content-position="center"><h1>登录账号</h1></el-divider>

    <form>
      <div class="form-elem">
        <span>账号：</span>
        <input v-model="signinName" type="text" placeholder="输入用户名">
      </div>

      <div class="form-elem">
        <span>密码：</span>
        <input v-model="signinPwd" type="password" placeholder="输入密码">
      </div>

      <div class="form-elem">
        <button @click="signin">登录</button>
      </div>
    </form>
  </div>

</template>

<script lang="ts">
import {defineComponent, ref} from 'vue';
import Axios from "axios";
import constants from "@/utils/constants";
import router from "@/utils/router";
import {ElMessage} from 'element-plus'
import {login} from "@/utils/variables";

export default defineComponent({
  name: 'Login',

  setup() {
    const signinName = ref('')
    const signinPwd = ref('')

    async function signin(e: any) {
      const url = constants.apiUrl + 'token/obtain/'
      // console.log控制台输出信息，测试用的，上线时应该去掉。
      console.log({
        'name': signinName.value,
        'pwd': signinPwd.value,
      })
      // 第二个参数为指定要发送的数据
      const response = await Axios.post(url, {
        'username': signinName.value,
        'password': signinPwd.value,
      })
      console.log(url)
      console.log(response)
      // 将响应后的数据放到variables的变量中去
      login(response.data)
      // 等待前面执行完毕跳转页面
      await router.push({name: 'Upload'})
      ElMessage({
        message: '欢迎登陆本站！',
        center: true
      });
    }

    return {signinName, signinPwd, signin}
  }
});
</script>


<style scoped>


#signin {
  text-align: center;
}

.form-elem {
  padding: 10px;
}

input {
  height: 35px;
  padding-left: 20px;
}

button {
  height: 35px;
  cursor: pointer;
  border: none;
  outline: none;
  background: green;
  color: whitesmoke;
  border-radius: 5px;
  width: 60px;
}
</style>
