---
title: Catalyzing Interactive HTML Generation Capabilities via High-Fidelity Reinforcement
  Learning
title_zh: 基于高保真强化学习的交互式HTML生成能力提升框架
authors:
- Xujia Wang
- Yixuan Liu
- Shaohan Huang
- Furu Wei
- Lei Hou
- Bin Xu
- Juanzi Li
affiliations:
- Tsinghua University
- Microsoft Research
arxiv_id: '2611.05151'
url: https://arxiv.org/abs/2611.05151
pdf_url: https://arxiv.org/pdf/2611.05151
published: '2026-11-03'
collected: '2026-11-04'
category: Training
direction: LLM代码生成 · 高保真强化学习
tags:
- Reinforcement Learning
- HTML Generation
- GRPO
- Code LLM
- Reward Calibration
- Credit Assignment
one_liner: 提出WebCatalyst高保真RL框架，仅用不到1K样本即超过Claude Opus 4.7的HTML生成平均排名
practical_value: '- 生成电商互动小游戏、营销活动页HTML时，可复用GUI Assessor的分层交互评估逻辑，引入实际浏览器运行+用户操作轨迹评分，替代仅静态代码校验的评估方式，避免生成可渲染但交互失效的页面

  - 基于RL的生成任务优化可引入Visual Anchor机制，用高质量参考输出做视觉退化惩罚，解决RL训练中的reward hacking问题，适配电商页面对视觉风格一致性的高要求

  - 代码/结构化生成任务的RL训练中，可复用Action-Trace Credit的细粒度credit分配思路，通过运行时调用栈把全局奖励映射到对应生成token，可提升收敛速度1.8倍以上，大幅降低训练数据需求量'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有代码LLM生成HTML仅能保证语法可渲染，无法保障交互过程中的功能可用性与视觉质量，现有RL监督多针对特定静态网页任务优化，对需要持续交互的复杂HTML（如互动小游戏、营销活动页）支持不足，存在交互评估深度浅、VLM reward hacking、全局奖励分配粒度粗三大核心问题。

### 方法关键点
- 构建WebCatalyst浏览器交互RL框架，三大核心组件：1. Game-Level GUI Assessor：通过ReAct模式执行Agent完成持续多步交互，分层聚合操作结果与截图评估得到页面级奖励，用生产者消费者队列降低评估延迟；2. Visual Anchor：对比生成页面与高质量参考页面截图，惩罚视觉退化，避免reward hacking；3. Action-Trace Credit：通过Chrome DevTools Protocol捕获成功交互的JS调用栈，按调用深度衰减将全局奖励映射到对应生成token，实现细粒度credit分配。
- 基于GRPO算法做策略优化，训练数据仅为不到1K条Reddit上的HTML开发请求（以游戏类为主）。

### 关键实验
在WebGen-Bench（常规网页）、Cookie-Bench Mini Games（互动小游戏）基准测试，对比Qwen3.6-35B-A3B基线、Claude Opus 4.7等闭源模型：1. 仅用640条训练请求，Mini Games总分从68.8提升至75.3，WebGen-Bench准确率从48.8提升至56.9；2. 平均排名4.0，超过Claude Opus 4.7的4.7，为开源模型最佳水平；3. 消融实验显示Visual Anchor可将美学评分从71.3拉回82.3，Action-Trace Credit可提升训练收敛速度1.84倍。

### 核心结论
提升反馈保真度是大幅推进交互式生成任务能力的核心关键，少量高反馈质量的训练数据远胜大量低质量标注。
