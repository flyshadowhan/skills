# Java 审查检查清单

## 1. Effective Java 模式
- [ ] **不可变性：** 类是否尽可能不可变？（例如 `final` 字段，无 setter）
- [ ] **流与 Optional：** 是否惯用地使用 `Stream` API 和 `Optional` 替代循环和 null 检查？
- [ ] **构建器/工厂：** 复杂对象是否使用创建型模式？

## 2. 并发与线程
- [ ] **线程安全：** 共享可变状态是否正确同步或使用 `java.util.concurrent` 类（如 `ConcurrentHashMap`）？
- [ ] **虚拟线程（Java 21+）：** I/O 密集型任务是否在适当的地方利用虚拟线程？
- [ ] **原子变量：** 是否使用 `AtomicInteger`、`AtomicReference` 等进行无锁同步？

## 3. 资源管理
- [ ] **try-with-resources：** 所有 `AutoCloseable` 资源（流、连接）是否使用 try-with-resources 关闭？
- [ ] **内存：** 是否存在潜在的内存泄漏（如无限增长的静态集合、未关闭的监听器）？

## 4. 异常处理
- [ ] **特异性：** 是否捕获特定异常而不是通用的 `Exception`？
- [ ] **日志：** 异常是否记录堆栈跟踪？避免吞掉异常
- [ ] **自定义异常：** 领域特定错误是否使用自定义异常？

## 6. 项目红线约束 (Hard Rules)
- [ ] **[红线/禁止] 严禁使用 Lombok：** 项目由于历史或架构原因，严禁使用任何 Lombok 注解（如 `@Data`, `@Getter`, `@Setter`, `@RequiredArgsConstructor`, `@AllArgsConstructor`, `@NoArgsConstructor` 等）。
- [ ] **[强制] 构造函数要求：** 由于禁用 Lombok，Getter/Setter 和构造函数必须由 IDE 生成或手动编写，以确保代码的透明度和可调试性。
