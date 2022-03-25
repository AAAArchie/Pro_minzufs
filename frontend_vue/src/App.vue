<template>
   <!--vue3中的模板结构可以没有根标签-->
  <div id="app">
    <el-container>
      <el-col :xs="40" :sm="24">
        <el-header>
          <el-menu :default-active="$route.path" class="el-menu-vertical-demo" mode="horizontal" router>
           <el-menu-item index="/Introduction"><i class="el-icon-user-solid"></i><span class="hidden-sm-and-down">项目介绍</span>
            </el-menu-item>

            <el-menu-item index="/"><i class="el-icon-house"></i><span class="hidden-sm-and-down">主页</span>
            </el-menu-item>
<!--                        <el-menu-item  index="/Gather" class="hidden-sm-and-down"><i class="el-icon-edit"></i><span class="hidden-sm-and-down">收集图片</span></el-menu-item>-->
            <el-menu-item index="/Upload"><i class="el-icon-camera-solid"></i><span
                class="hidden-sm-and-down">快速识别</span></el-menu-item>
                <el-menu-item index="/Recognition"><i class="el-icon-crop"></i><span
                class="hidden-sm-and-down">高级识别</span></el-menu-item>
            <el-menu-item index="/List" v-if="isLogin"><i class="el-icon-tickets"></i><span class="hidden-sm-and-down">历史记录</span>
            </el-menu-item>
            <el-menu-item index="/UserCenter" v-if="isLogin"><i class="el-icon-user"></i><span
                class="hidden-sm-and-down">用户中心</span></el-menu-item>

            <el-menu-item><span class="hidden-sm-and-down">若要保存识别记录，{{ variables.username }}!</span>
            </el-menu-item>

            <el-submenu index="1">
              <div>
                <el-menu-item index="/Login" v-if="!isLogin">登录</el-menu-item>
                <el-menu-item index="/Register" v-if="!isLogin">注册</el-menu-item>
                <div v-if="isLogin">
                  <el-menu-item @click="logout">登出</el-menu-item>
                </div>
              </div>
            </el-submenu>
          </el-menu>

        </el-header>
      </el-col>

      <!--Main-->
      <el-main :xs="24">
        <router-view></router-view>
      </el-main>
      <!--Footer-->
      <el-footer>
        <el-affix position="bottom" :offset="0">
          <div id="footer" >
            <span>www.minzufs.cn  Powered by 桂ICP备19009776号</span>
          </div>
        </el-affix>
      </el-footer>

    </el-container>
  </div>

</template>

<script lang="ts">
// 这里这个defineComponent可以理解为是vue3的一个格式文本，就必须这么写就完事儿了
import {computed, defineComponent, reactive, ref} from "vue";
import 'element-plus/lib/theme-chalk/display.css';
// import authorization from '@/utils/authorization';
import {ElMessage} from 'element-plus'
import variables, {logout} from "@/utils/variables";
import router from "@/utils/router";

export default defineComponent({
  name: 'Home',
  // 此处为vue2的形式，但是可以在vue3里头写，不写进setup;(不推荐写vue2代码）
  methods: {
    handleSelect() {
    },
  },
  setup() {
    //以下为实际需要实现的逻辑功能
    const isLogin = computed(() => variables.token !== '')
    const data = reactive({
      src: require('../public/tittle.png'),
    })

    function logoutAndReturnToHome() {
      logout()
      router.push({'name': 'Home'})
    }
    // 返回对象（数据，方法等）渲染界面
    return {isLogin, logout: logoutAndReturnToHome, data, variables}
  }
});

</script>


<style>


#footer {

  left: 0;
  bottom: 0;
  height: 50px;
  width: 100%;
  background: whitesmoke;
  text-align: center;
  font-weight: bold;
}
</style>
