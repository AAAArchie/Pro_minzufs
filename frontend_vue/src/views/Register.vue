<template>

  <div id="signup">
    <el-divider content-position="center"><h1>注册账号</h1></el-divider>
    <form>
      <div class="form-elem">
        <span>账号：</span>
        <input v-model="signupName" type="text" placeholder="输入用户名">
      </div>

      <div class="form-elem">
        <span>密码：</span>
        <input v-model="signupPwd" type="password" placeholder="输入密码">
      </div>

      <div class="form-elem">
        <button @click="signup">提交</button>
      </div>
    </form>
  </div>


</template>

<script lang="ts">
import {defineComponent, ref} from 'vue';
import Axios from "axios";
import constants from "@/utils/constants";
import router from "@/utils/router";
import {ElMessage} from "element-plus";
import {login} from "@/utils/variables";

export default defineComponent({
  name: 'Register',
  setup() {
    const signupName = ref('')
    const signupPwd = ref('')

    async function signup(e: any) {
      const url = constants.apiUrl + 'user/'
      const response = await Axios.post(url, {
        'username': signupName.value,
        'password': signupPwd.value,
      })
      // login(response.data)

      ElMessage({
        message: '注册成功，请登入！',
        center: true
      });
      await router.push({name: 'Login'})
    }

    return {signupName, signupPwd, signup}
  }
});
</script>


<style scoped>

#signup {
  text-align: center;
}

.form-elem {
  padding: 10px;
}

input {
  height: 25px;
  padding-left: 10px;
}

button {
  height: 35px;
  cursor: pointer;
  border: none;
  outline: none;
  background: gray;
  color: whitesmoke;
  border-radius: 5px;
  width: 60px;
}
</style>
