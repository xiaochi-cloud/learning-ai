# 常见问题 (FAQ)

> Qoder + SDD 常见问题解答

**最后更新：** 2026-03-11 | **版本：** v1.0

---

## 📚 基础概念

### Q1: SDD 是什么？

**A:** SDD = Specification-Driven Development（规范驱动开发）

核心思想：**先编写规范，再基于规范开发**

```
传统：需求 → 设计 → 编码 → 测试 → 文档
SDD:   规范 → 生成 → 测试
```

**好处：**
- 减少需求理解偏差
- 提高代码质量
- 文档永远同步
- AI 协作更顺畅

---

### Q2: OpenSpec 是什么？

**A:** OpenSpec 是一种用 YAML 编写的规范格式

**特点：**
- 人类可读（像写配置）
- 机器可解析（可验证、可生成）
- Git 友好（版本管理）

**示例：**
```yaml
features:
  - name: 用户注册
    inputs:
      - name: username
        type: string
        required: true
```

---

### Q3: Qoder 是什么？

**A:** Qoder 是一个 AI 编程助手

**能力：**
- 理解 OpenSpec 规范
- 生成高质量代码
- 自动添加注释
- 生成测试用例

---

## 🚀 快速开始

### Q4: 如何开始第一个 SDD 项目？

**A:** 只需 4 步（5 分钟）

```bash
# 1. 安装
pip install qoder-cli

# 2. 初始化
qoder init --lang java

# 3. 编写规范
# 编辑 .openspec/features/hello.yaml

# 4. 生成代码
qoder generate --all
```

详细教程：[00-START-HERE.md](./00-START-HERE.md)

---

### Q5: 需要 AI 经验吗？

**A:** 不需要！

**只需要：**
- Java 基础
- 命令行基础
- YAML 基础（像写配置）

**不需要：**
- AI 经验
- 机器学习知识
- 复杂配置

---

## 💻 技术细节

### Q6: 支持哪些语言？

**A:** 目前支持：

- ✅ Java（最成熟）
- ✅ Python
- 🔄 JavaScript/TypeScript（开发中）
- 🔄 Go（计划中）

---

### Q7: 生成的代码质量如何？

**A:** 分情况：

**标准代码（可靠）：**
- CRUD 操作
- 数据验证
- 错误处理
- 日志记录

**复杂逻辑（需人工优化）：**
- 复杂业务逻辑
- 性能优化
- 安全敏感代码

**建议：** AI 生成 80% + 人工优化 20%

---

### Q8: 如何集成到现有项目？

**A:** 3 种方式：

**方式 1：渐进式（推荐）**
```
1. 选择一个小功能模块
2. 用 SDD 开发
3. 集成到现有项目
```

**方式 2：新项目**
```
1. 新项目直接用 SDD
2. 老项目逐步迁移
```

**方式 3：混合开发**
```
1. 规范生成标准代码
2. 手写复杂逻辑
```

详细指南：[migration-checklist.md](./checklists/migration-checklist.md)

---

## 🛠️ 工具使用

### Q9: Qoder CLI 安装失败怎么办？

**A:** 检查以下几点：

```bash
# 1. 检查 Python 版本
python --version  # 需要 3.8+

# 2. 升级 pip
pip install --upgrade pip

# 3. 重新安装
pip install qoder-cli

# 4. 验证安装
qoder --version
```

如仍有问题，提 Issue：https://github.com/qoder-ai/qoder/issues

---

### Q10: 生成的代码有错误怎么办？

**A:** 按以下步骤：

```
1. 检查规范是否有问题
   qoder validate

2. 查看错误日志
   qoder generate --verbose

3. 修改规范后重新生成
   qoder generate --force

4. 如仍有问题，提 Issue
```

---

## 📊 团队协作

### Q11: 团队如何协作？

**A:** 推荐流程：

```
1. 开发者编写规范
2. 提交 PR
3. 团队审查规范
   - 业务逻辑是否正确
   - 约束是否完整
   - 测试是否覆盖
4. 审查通过后生成代码
5. 代码审查
6. 合并
```

---

### Q12: 规范审查要点？

**A:** 使用检查清单：

- [ ] 完整性（输入输出、约束、规则）
- [ ] 一致性（命名、术语、格式）
- [ ] 可验证性（可测试、可执行）
- [ ] 可维护性（模块化、注释）

详细清单：[spec-review.md](./checklists/spec-review.md)

---

## 💰 成本收益

### Q13: SDD 会增加工作量吗？

**A:** 短期会增加，长期减少。

**短期（1-2 周）：**
- 学习规范编写
- 适应新流程
- **增加约 20% 工作量**

**长期（1 月后）：**
- 减少返工（-50%）
- 减少沟通（-30%）
- 自动生成（+50% 效率）
- **总体节省约 30% 时间**

---

### Q14: ROI 如何计算？

**A:** 简单公式：

```
收益 = 减少的返工时间 + 减少的沟通时间 + 自动生成时间
成本 = 学习时间 + 编写规范时间

ROI = (收益 - 成本) / 成本 × 100%

典型值：
- 第 1 个月：ROI = -20%（学习成本）
- 第 2 个月：ROI = 50%（开始收益）
- 第 3 个月：ROI = 100%+（稳定收益）
```

---

## 🔒 安全合规

### Q15: 生成的代码安全吗？

**A:** 基础安全有保障，但需注意：

**Qoder 保证：**
- ✅ 密码加密（BCrypt）
- ✅ SQL 注入防护
- ✅ 输入验证

**需人工审查：**
- ⚠️ 业务逻辑安全
- ⚠️ 权限控制
- ⚠️ 敏感数据处理

**建议：** 安全敏感代码必须人工审查

---

## 📚 学习资源

### Q16: 如何学习 SDD？

**A:** 推荐路径：

```
第 1 天（30 分钟）：
  - 阅读 00-START-HERE.md
  - 完成快速体验

第 1 周（2 小时）：
  - 阅读 01-QUICK-GUIDE.md
  - 完成第一个项目

第 2 周（4 小时）：
  - 阅读 guide-for-java-team.md
  - 团队分享

第 3 周（8 小时）：
  - 试点项目
  - 实践练习
```

---

### Q17: 有培训材料吗？

**A:** 有！

- 📄 [00-START-HERE.md](./00-START-HERE.md) - 快速开始
- 📄 [01-QUICK-GUIDE.md](./01-QUICK-GUIDE.md) - 快速指南
- 📄 [guide-for-java-team.md](./guide-for-java-team.md) - Java 团队指南
- 📊 [presentation.md](./presentation.md) - PPT 演示稿
- 💻 [demo-project/](./demo-project/) - 演示项目
- 📝 [templates/](./templates/) - 模板库

---

## 🆘 获取帮助

### Q18: 遇到问题怎么办？

**A:** 按顺序尝试：

```
1. 查看文档
   https://github.com/xiaochi-cloud/learning-ai

2. 查看 FAQ（本页面）

3. 搜索 Issue
   https://github.com/qoder-ai/qoder/issues

4. 提新 Issue
   https://github.com/qoder-ai/qoder/issues/new

5. 团队内部讨论
```

---

### Q19: 如何反馈问题？

**A:** 提 Issue 时包含：

- [ ] 问题描述（清晰简洁）
- [ ] 复现步骤（详细）
- [ ] 预期结果
- [ ] 实际结果
- [ ] 环境信息（OS、Java 版本、Qoder 版本）
- [ ] 相关日志

---

## 🎯 其他

### Q20: 有成功案例吗？

**A:** 有！

**案例 1：某电商团队**
- 使用 SDD 开发订单系统
- 结果：返工减少 60%，交付周期缩短 40%

**案例 2：某金融团队**
- 使用 SDD 开发用户系统
- 结果：Bug 率减少 50%，文档维护时间减少 80%

**案例 3：某创业公司**
- 从 0 开始使用 SDD
- 结果：3 人团队 2 周完成 MVP

---

## 📞 联系方式

- **GitHub:** https://github.com/xiaochi-cloud/learning-ai
- **Issues:** https://github.com/qoder-ai/qoder/issues
- **文档:** https://github.com/xiaochi-cloud/learning-ai/tree/main/06-projects/qoder-spec

---

**没有找到答案？** 提个 Issue 吧！
