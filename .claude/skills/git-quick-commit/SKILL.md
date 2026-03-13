---
name: git-quick-commit
description: Git 快速提交工作流 Skill。当用户提到"git提交"、"提交代码"、"commit"、"快速提交"、"帮我提交"、"生成commit message"、"推送代码"、"push代码"等关键词时，立即使用此 Skill。适用于：自动分析代码变更并生成规范的 Conventional Commits 格式 commit message、执行暂存和提交操作、可选推送到远程仓库。即使用户只是模糊地说"提交一下"或"commit 代码"，也应触发此 Skill。
---

# Git 快速提交 Skill

帮助用户快速、规范地完成 Git 提交流程：分析变更 → 生成 commit message → 暂存 → 提交 → （可选）推送。

---

## 工作流程

### 第一步：检查 Git 状态

```bash
git status
git diff --stat
git diff --cached --stat
```

- 若工作区干净（无变更），告知用户并退出
- 若有未跟踪文件，询问用户是否要一并加入

### 第二步：分析变更内容

```bash
# 查看未暂存的变更
git diff

# 查看已暂存的变更
git diff --cached

# 查看新文件内容
git diff --no-index /dev/null <new-file>   # 若需要
```

理解变更的核心内容：
- 改了什么文件？改了什么功能？
- 是修复、新增、重构还是文档更新？
- 变更规模（行数、文件数）

### 第三步：生成 Commit Message

遵循 **Conventional Commits** 规范：

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

**type 选择规则：**

| type | 场景 |
|------|------|
| `feat` | 新功能 |
| `fix` | Bug 修复 |
| `docs` | 文档变更 |
| `style` | 代码格式（不影响功能） |
| `refactor` | 重构（非新功能、非修复） |
| `perf` | 性能优化 |
| `test` | 测试相关 |
| `chore` | 构建/工具/依赖等杂项 |
| `ci` | CI/CD 配置 |
| `revert` | 回滚提交 |

**subject 写作规则：**
- 用中文或英文（跟随项目已有风格）
- 动词开头，简明扼要（≤72字符）
- 不加句号

**示例：**
```
feat(auth): 添加微信登录支持

fix(api): 修复用户列表分页数据错乱问题

refactor: 将 utils 模块拆分为独立功能文件

chore(deps): 升级 axios 至 1.6.0
```

若变更涉及多个独立功能，建议拆分为多次提交并告知用户。

### 第四步：展示并确认

向用户展示：
1. 将要暂存的文件列表
2. 生成的 commit message
3. 询问是否确认，或是否需要修改

格式示例：
```
📋 即将执行以下提交：

暂存文件：
  - src/auth/wechat.ts（新增）
  - src/auth/index.ts（修改）

Commit message：
  feat(auth): 添加微信登录支持

是否确认提交？(是/否/修改message)
```

### 第五步：执行提交

根据用户确认后执行：

```bash
# 暂存（根据情况选择）
git add .                    # 全部暂存
git add <specific-files>     # 指定文件

# 提交
git commit -m "<message>"

# 若 message 有 body，使用多行形式
git commit -m "<subject>" -m "<body>"
```

### 第六步：询问是否推送

提交成功后询问：

```
✅ 提交成功！

是否推送到远程仓库？
  当前分支：feature/wechat-login → origin/feature/wechat-login
```

若用户同意：
```bash
git push origin <current-branch>

# 若是新分支：
git push -u origin <current-branch>
```

---

## 特殊情况处理

### 存在冲突或错误
- 若 `git add` / `git commit` 报错，输出错误信息并给出建议
- 常见问题：pre-commit hook 失败 → 提示用户检查 lint/格式化

### 用户已有暂存区内容
- 先问用户：只提交已暂存的文件，还是追加新变更？

### 用户直接提供 message
- 若用户说"提交，message 是 xxx"，直接使用用户提供的 message，跳过生成步骤

### 大型变更（>20个文件）
- 提示用户考虑拆分提交
- 按模块/功能分组建议

### 空提交
- 若用户要求空提交（如触发 CI），使用 `git commit --allow-empty`

---

## 输出风格

- 使用 emoji 增强可读性：✅ 成功、❌ 错误、📋 信息、⚠️ 警告、🚀 推送
- 每步操作前显示将要执行的命令
- 操作完成后显示结果摘要
- 遇到问题给出明确的解决建议，不要只报错

---

## 参考资料

需要深入了解规范时，参考：
- `references/conventional-commits.md` — Conventional Commits 详细规范
- `references/git-tips.md` — 常用 Git 命令速查