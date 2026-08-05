---
title: 'PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in
  Personal Agents'
title_zh: PAST-Bench：个人智能体递归自我改进能力评测基准
authors:
- Shuhan Xue
- Zixin Ding
- Yichen Shen
- Yinjie Wang
- Zhenfei Yin
- Yingcheng Wu
- Yuxin Chen
- Mengdi Wang
- Ling Yang
arxiv_id: '2608.04003'
url: https://arxiv.org/abs/2608.04003
pdf_url: https://arxiv.org/pdf/2608.04003
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: 智能体自进化 · 基准评测
tags:
- Agent Benchmark
- Self-Improvement
- Persistent Memory
- Procedural Reuse
- Agent Framework
one_liner: 首个支持经验复用可归因的个人智能体自进化基准，配套优化Hermes+提升效果与机制一致性
practical_value: '- 搭建电商个性化导购/客服Agent的自进化评估，可直接复用PAST-Bench的开关对照设计，隔离持久化能力，区分经验复用增益与base
  model、prompt等其他因素的贡献，避免误判记忆/召回优化效果

  - 优化Agent记忆模块时可复用Hermes+的5个改造点：计划阶段加预查询校验、结构化记忆绑定、可补丁化技能存储、回答前置检索校验、会话关闭时同步刷新旧状态

  - 电商用户偏好记忆、购物流程复用、过时规则更新3类核心场景，可直接匹配PAST-Bench的Memory、Procedural Reuse、Update三个能力维度的测试case设计逻辑

  - 评估Agent记忆优化效果时不要只看任务得分，要叠加机制归因得分（记忆读写、技能调用等链路trace），避免增益来自数据泄露而非真实经验复用'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有个人智能体已支持跨会话持久化记忆、技能、历史交互，但无法区分性能提升是来自真实的历史经验复用、base model能力、prompt优化还是其他干扰因素，缺少可归因的轨迹级评测体系，难以定位自进化失败根因，严重阻碍自进化Agent的落地迭代。
### 方法关键点
- 轨迹级评测范式：每组任务家族包含冷启动、学习、评估、对照4个阶段，会话间清空上下文，仅允许通过持久层传递经验，对比持久化开关的得分差作为自进化增益
- 覆盖4类核心自进化能力：记忆、流程复用、信息主动检索、状态更新，共26个场景204个测试用例
- 双指标评估体系：任务得分衡量最终效果，机制证据得分基于持久化读写trace、技能调用日志等，判断增益是否来自预期经验复用路径
- 基于诊断结果优化得到Hermes+，在Agent循环的Plan/Render/Route/Gate/Close5个阶段各添加1个针对性干预机制
### 关键结果
测试7个主流大模型、4个Agent框架，基础Hermes框架下各模型自进化增益Δ在0.13~0.24区间；同样Δ=0.13的两个框架Hermes和nanobot的机制得分分别为0.64和0.57；Hermes+相对基础Hermes整体Δ从0.13提升到0.15，机制得分从0.64提升到0.73，更新类任务Δ从0.12提升到0.24。
### 核心结论
个人智能体的自进化增益不能只看最终任务效果，必须结合复用路径归因判断是否来自真实的经验复用链路，否则可能是虚假增益。
