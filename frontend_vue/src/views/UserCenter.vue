<template>
  <div id="user-center">
    <h3>修改密码</h3>
    <form>
      <div class="form-elem">
        <span>新密码：</span>
        <input v-model="data.password" type="password" placeholder="输入密码">
      </div>
      <div class="form-elem">
        <button @click="updatePassword">修改密码</button>
      </div>
    </form>
  </div>
</template>

<script>
import {reactive} from "vue";
import constant from "@/utils/constants";
import Axios from "axios";
import {ElMessage} from "element-plus";
import variables from "@/utils/variables";


export default {
  name: 'UserCenter',
  setup() {
    const data = reactive({
      password: '',
    })

    async function updatePassword() {
      const url = `${constant.apiUrl}user/${variables.userId}/`
      const headers = {Authorization: `JWT ${variables.token}`}
      try {
        const response = await Axios.patch(url, {
          'password': data.password,
        }, {
          headers
        })
        ElMessage('密码已修改')
      } catch (e) {
        ElMessage('密码修改失败')
      }
    }

    return {data, updatePassword}
  },
}
</script>

<style scoped>
#user-center {
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
  width: 200px;
}
</style>
