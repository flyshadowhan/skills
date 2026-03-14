# Spring Boot / Spring 审查检查清单

## 1. 依赖注入与配置
- [ ] **依赖注入规范：** 是否根据场景灵活使用 `@Autowired`、`@Resource` 或构造函数进行注入？鉴于项目 **[红线] 禁止使用 Lombok**，允许并建议使用字段注入（Field Injection）以规避手动编写冗长、重复的构造函数，平衡开发效率。
- [ ] **配置属性：** 复杂配置是否使用 `@ConfigurationProperties` 进行类型安全绑定，而非零散的 `@Value`？
- [ ] **Profile 管理：** 特定环境的配置是否正确通过 `@Profile` 或 `application-{profile}.yml` 进行隔离？
- [ ] **Bean 定义：** 组件扫描路径是否合理？避免在 `@Configuration` 类中混杂过多的业务逻辑。

## 2. Web 与 REST API
- [ ] **控制器规范：** 是否使用了 `@RestController`？路由命名是否符合 RESTful 风格（名词复数、中划线等）？
- [ ] **统一响应：** 是否使用了统一的响应包装类或 `ResponseEntity` 来返回状态码 and 数据？
- [ ] **全局异常处理：** 是否通过 `@ControllerAdvice` 和 `@ExceptionHandler` 实现了业务异常的统一捕获与返回？
- [ ] **参数校验：** DTO 是否使用了 Bean Validation 注解（如 `@NotNull`, `@Size`）并在控制器开启了 `@Valid` 校验？

## 3. 数据访问 (JPA / MyBatis)
- [ ] **事务管理：** `@Transactional` 是否正确标注在 Service 层方法上？是否明确了 `readOnly = true` 用于只读操作？
- [ ] **性能优化：** 是否解决了 N+1 查询问题（如使用 `JOIN FETCH` 或 `EntityGraph`）？
- [ ] **分页处理：** 返回列表数据的接口是否强制使用了分页（`Pageable`）以防止内存溢出？
- [ ] **实体隔离：** 是否避免了将 JPA/Hibernate 实体直接暴露在 Controller 层（建议使用 DTO）？

## 4. 安全性
- [ ] **鉴权与授权：** 敏感接口是否通过 Spring Security 或拦截器进行了权限校验？
- [ ] **方法级安全：** 复杂权限逻辑是否使用了 `@PreAuthorize` 或 `@Secured` 注解？
- [ ] **配置泄露：** 敏感信息（如数据库密码、API 密钥）是否已加密或通过环境变量注入，而非硬编码在 `yaml` 中？

## 5. 性能与可观测性
- [ ] **异步处理：** 耗时任务是否使用了 `@Async` 并配置了自定义线程池？
- [ ] **缓存使用：** 合适的场景是否使用了 `@Cacheable`？缓存过期策略是否合理？
- [ ] **监控端点：** 是否集成了 `spring-boot-starter-actuator` 并对敏感监控端点（如 `/env`, `/heapdump`）进行了安全保护？

## 6. 测试
- [ ] **切片测试：** 是否针对不同层使用了合适的测试注解（如 `@WebMvcTest` 测试接口，`@DataJpaTest` 测试持久层）？
- [ ] **模拟依赖：** 单元测试中是否使用了 `@MockBean` 正确模拟外部 Service 或 Repository？

## 7. 编码规范与工具限制
- [ ] **[红线/禁止] 严禁使用 Lombok：** 必须严格遵守项目禁令。出现任何 Lombok 相关的注解（如 `@Data`, `@Getter`, `@Setter`, `@RequiredArgsConstructor`, `@AllArgsConstructor`, `@NoArgsConstructor` 等）均视为 **🔴 Critical** 错误。
