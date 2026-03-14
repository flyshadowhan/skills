# Next.js 审查检查清单

## 1. App Router 与 React 服务器组件（RSC）
- [ ] **组件策略：** 组件默认是否为服务器组件？是否仅在必要时使用 `"use client"`（交互性、hooks、浏览器 API）？
- [ ] **数据获取：** 是否尽可能在服务器端获取数据？
- [ ] **缓存：** `fetch` 请求是否正确利用 Next.js 缓存和重新验证？

## 2. 性能与优化
- [ ] **next/image：** 是否使用 `Image` 组件进行自动优化和防止布局偏移？
- [ ] **next/link：** 是否使用 `Link` 进行客户端导航？
- [ ] **流式传输：** 是否使用 `Suspense` 进行细粒度加载状态（流式传输）？
- [ ] **动态导入：** 大型客户端组件是否使用 `next/dynamic` 导入？

## 3. SEO 与元数据
- [ ] **Metadata API：** 是否使用静态或动态 `metadata` 对象而不是 `<Head>`（App Router）？
- [ ] **Sitemaps/Robots：** 是否实现 `sitemap.ts` 和 `robots.ts`？

## 4. 服务器操作
- [ ] **安全性：** 服务器操作是否受授权检查保护？
- [ ] **验证：** 输入数据是否在操作内进行验证（如使用 Zod）？
