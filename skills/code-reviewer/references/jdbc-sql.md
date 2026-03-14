# JDBC SQL 审查检查清单

## 1. 安全性 (Security)
- [ ] **严禁字符串拼接：** 绝对禁止通过字符串拼接（`+` 或 `StringBuilder.append`）来构造包含用户输入变量的 SQL 语句。
- [ ] **强制使用 PreparedStatement：** 所有带有参数的查询必须使用 `PreparedStatement` 和占位符 `?`，以防止 SQL 注入。
- [ ] **动态结构校验：** 对于无法使用占位符的部分（如动态表名、排序字段名），必须在 Java 代码中进行严格的白名单校验，严禁直接透传前端参数。
- [ ] **敏感数据：** 检查 SQL 语句中是否涉及明文存储的敏感信息，确保符合脱敏要求。

## 2. 性能优化 (Performance)
- [ ] **禁止 SELECT *：** 必须明确指定所需的列名，减少数据传输量并提高索引覆盖的可能性。
- [ ] **批处理优化：** 对于大批量数据插入或更新，必须使用 `addBatch()` 和 `executeBatch()`，并合理设置批次大小（通常为 500-1000）。
- [ ] **结果集处理：** 避免在循环中执行 SQL 查询（N+1 问题），应尽可能使用 `IN` 子句或 `JOIN` 进行一次性查询。
- [ ] **索引利用：** 确保 `WHERE`、`ORDER BY`、`GROUP BY` 中的字段有合适的索引，且查询条件不破坏索引效能（如避免对索引列使用函数）。

## 3. 资源管理 (Resource Management)
- [ ] **强制关闭资源：** `ResultSet`、`Statement/PreparedStatement` 以及 `Connection` 必须在使用完毕后关闭。
- [ ] **Try-with-resources：** 优先使用 Java 7+ 的 `try-with-resources` 语法，确保即使发生异常，资源也能被正确释放。
- [ ] **连接池使用：** 严禁手动频繁创建和销毁物理连接，必须通过数据源（DataSource）从连接池获取连接。

## 4. 结果映射与规范 (Mapping & Standards)
- [ ] **按列名获取：** 从 `ResultSet` 获取数据时，优先使用列名（如 `rs.getString("user_name")`）而非索引（如 `rs.getString(1)`），以增强代码的可读性和健壮性。
- [ ] **类型匹配：** `setXXX` 方法的参数类型应与数据库列类型严格匹配，避免隐式类型转换带来的性能损失或精度问题。
- [ ] **SQL 可读性：** 复杂的 SQL 建议使用 Java 15+ 的文本块（Text Blocks）或清晰的换行拼接，并配以必要的业务逻辑注释。

## 5. 项目红线约束 (Hard Rules)
- [ ] **[红线/禁止] 严禁在业务逻辑中硬编码复杂存储过程：** 除非有极端性能需求，否则禁止通过 JDBC 调用复杂的数据库私有逻辑，以保持应用的可移植性。
- [ ] **[强制] 手动事务一致性：** 在执行多条更新 SQL 时，必须显式调用 `connection.setAutoCommit(false)`，并在所有操作成功后 `commit()`，捕获到异常时必须执行 `rollback()`。
- [ ] **[强制] 异常细化：** 必须捕获 `SQLException` 并记录详细的 SQL 状态码（SQLState）和错误码，严禁静默忽略 SQL 异常。
