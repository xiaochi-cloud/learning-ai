# Qoder 项目规范指南

> 使用 OpenSpec 格式和 SDD 最佳实践，让 AI 理解并生成高质量代码

---

## 🚀 快速开始

### 1. 下载 Qoder IDE

访问官网下载安装：
- **官网：** https://qoder.com/download
- **支持平台：** Windows / macOS / Linux

### 2. 登录账号

- 打开 Qoder IDE
- 点击右上角用户图标
- 使用 Google 或 GitHub 账号登录

### 3. 打开项目

- 打开本地项目
- 或克隆 GitHub 项目

### 4. 使用 Quest Mode

1. 点击左上角 **Editor/Quest** 切换到 Quest Mode
2. 点击 **New Quest** 创建新任务
3. 选择场景：
   - **Spec 驱动** — 复杂功能开发
   - **搭建网站** — 0-1 创建网站
   - **原型探索** — 快速验证想法
4. 描述任务（自然语言或 OpenSpec）
5. Quest 生成 Spec（如选择 Spec 驱动）
6. 审核 Spec 并点击运行
7. 验收结果（Accept/Reject）

### 5. 学习资源

- **快速开始：** [00-START-HERE.md](./00-START-HERE.md)
- **完整指南：** [01-QUICK-GUIDE.md](./01-QUICK-GUIDE.md)
- **官方文档：** https://docs.qoder.com/zh

---

## 📁 项目结构

```
my-project/
├── .openspec/              # OpenSpec 规范
│   ├── project.yaml        # 项目规范
│   ├── features/           # 功能规范
│   ├── models/             # 数据模型
│   └── apis/               # API 规范
│
├── src/                    # 源代码
│   ├── generated/          # AI 生成的代码
│   └── custom/             # 手写代码
│
├── tests/                  # 测试
│   ├── unit/               # 单元测试
│   └── integration/        # 集成测试
│
├── docs/                   # 文档
│
└── README.md
```

---

## 📚 文档导航

| 文档 | 说明 |
|------|------|
| [QODER-SPEC.md](./QODER-SPEC.md) | 完整规范指南 |
| [example-todo-app.yaml](./example-todo-app.yaml) | 完整示例项目 |

---

## 🎯 核心概念

### SDD (Specification-Driven Development)

**规范驱动开发** — 先编写规范，再基于规范生成代码。

```
传统：需求 → 设计 → 编码 → 测试
SDD:   规范 → AI 生成 → 测试 → 迭代
```

### OpenSpec

**开放的规范格式** — 用 YAML/Markdown 编写机器可读的规范。

```yaml
meta:
  name: 项目名称
  version: 1.0.0

spec:
  features: [...]
  models: [...]
  apis: [...]
```

### AI 协作

**人机协作** — AI 理解规范，生成代码，人类审查和优化。

---

## ✅ 最佳实践

### 规范编写

1. **规范先行** — 先写规范，再生成代码
2. **清晰明确** — 避免模糊描述
3. **版本管理** — 规范纳入 Git
4. **持续更新** — 规范与代码同步

### AI 协作

1. **分步生成** — 功能 → 模块 → 代码
2. **审查输出** — 不盲目信任
3. **迭代优化** — 根据反馈调整

### 质量保证

1. **规范审查** — 同行评审
2. **自动化测试** — 单元测试 + 集成测试
3. **持续集成** — CI/CD 流水线

---

## 🔧 工具链

| 工具 | 用途 |
|------|------|
| qoder-cli | 代码生成 |
| openspec-validator | 规范验证 |
| qoder-lint | 代码检查 |
| qoder-test | 测试运行 |

---

## 📊 检查清单

### 规范审查

- [ ] 元数据完整
- [ ] 功能定义清晰
- [ ] 输入输出明确
- [ ] 约束条件完整
- [ ] 业务规则无歧义
- [ ] 验收标准可测试

### 代码生成

- [ ] 代码符合规范
- [ ] 类型注解完整
- [ ] 错误处理正确
- [ ] 测试覆盖关键路径

---

## 🎓 学习路径

```
入门 → 基础 → 进阶 → 实战
  ↓      ↓      ↓      ↓
了解    编写    复杂    完整
概念    规范    规范    项目
```

### 推荐顺序

1. 阅读 [QODER-SPEC.md](./QODER-SPEC.md)
2. 学习 [example-todo-app.yaml](./example-todo-app.yaml)
3. 创建自己的项目
4. 迭代优化

---

## 🤝 参与贡献

欢迎 Issue、PR、讨论！

- GitHub: [xiaochi-cloud/learning-ai](https://github.com/xiaochi-cloud/learning-ai)
- 问题反馈：提 Issue

---

## 📬 联系方式

- 作者：池少
- 项目：[learning-ai](https://github.com/xiaochi-cloud/learning-ai)

---

**📊 难度：** ⭐⭐⭐⭐☆  
**📝 预计时间：** 60 分钟  
**🏷️ 标签：** #qoder #sdd #openspec #guide

**最后更新：** 2026-03-11 | **版本：** v0.1
