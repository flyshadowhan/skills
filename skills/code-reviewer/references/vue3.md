# Vue 3 (Composition API) 审查检查清单

## 1. 组合式 API 与逻辑组织
- [ ] **`<script setup>`：** 是否优先使用了 `<script setup>` 语法糖以简化组件定义？
- [ ] **逻辑提取 (Composables)：** 复杂的业务逻辑是否提取到了独立的 `useXxx` 函数中以实现跨组件复用？
- [ ] **响应式 API 选择：** 是否合理区分了 `ref`（基本类型、单一对象）和 `reactive`（复杂对象、表单集）的使用场景？
- [ ] **解构响应式对象：** 使用 `reactive` 对象时，是否使用了 `toRefs` 或 `toRef` 进行解构以保持其响应式特性？

## 2. 组件特性与通信
- [ ] **宏命令使用：** 在 `<script setup>` 中是否正确使用了 `defineProps`, `defineEmits`, `defineExpose`？
- [ ] **多根节点 (Fragments)：** 是否利用了 Vue 3 支持多根节点的特性，避免了不必要的包裹层 `<div>`？
- [ ] **v-model 多绑定：** 是否利用了 Vue 3 支持多个 `v-model` 绑定的特性（例如 `v-model:title` 和 `v-model:content`）？
- [ ] **Teleport：** 弹窗、模态框等全局 UI 元素是否使用了 `<Teleport>` 挂载到正确的 DOM 节点（如 `body`）？

## 3. 性能与响应式优化
- [ ] **Shallow API：** 对于大型不可变数据集或第三方实例（如地图、图表），是否使用了 `shallowRef` 或 `shallowReactive` 来减少深度响应式的开销？
- [ ] **watch vs watchEffect：** 是否根据需求选择了正确的侦听器？`watch` 适用于需要新旧值对比的场景，`watchEffect` 适用于自动追踪依赖的副作用。
- [ ] **计算属性只读性：** `computed` 是否仅用于派生状态？是否避免了在计算属性中直接修改其他响应式状态。

## 4. 生命周期与资源管理
- [ ] **生命周期钩子：** 是否正确使用了 `onMounted`, `onUnmounted`, `onUpdated` 等组合式钩子？
- [ ] **副作用清理：** 在 `onUnmounted` 或 `watchEffect` 的清除函数中，是否正确清理了定时器、全局监听器或第三方库实例？

## 5. 指令与模板规范
- [ ] **v-if 与 v-for 优先级：** 开发者是否意识到 Vue 3 中 `v-if` 的优先级现在高于 `v-for`？是否避免了在同一元素上混合使用它们？
- [ ] **组件样式：** 是否使用了 Vue 3 特有的 CSS 变量绑定功能（`v-bind` in CSS）来实现动态样式？
- [ ] **Suspense：** 处理异步组件加载时，是否考虑使用 `<Suspense>` 提供更好的加载状态体验？

## 6. 生态与工具链
- [ ] **状态管理：** 是否优先使用了 **Pinia** 替代 Vuex？
- [ ] **TypeScript：** 是否充分利用了 Vue 3 优秀的 TS 支持？Props 和 Emits 是否带有类型定义？
- [ ] **Vue Router 4：** 路由导航守卫和跳转是否使用了 `useRouter` 和 `useRoute` 钩子？
