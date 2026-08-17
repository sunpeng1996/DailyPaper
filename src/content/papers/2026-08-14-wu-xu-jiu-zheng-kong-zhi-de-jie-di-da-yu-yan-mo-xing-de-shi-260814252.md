---
title: 'Grounding Without Corrective Control: Truth-Tracking Profiles for Large Language
  Models'
title_zh: 无需纠正控制的接地：大语言模型的事实追踪路径Profile
authors:
- Brett Reynolds
affiliations:
- Humber Polytechnic
- University of Toronto
arxiv_id: '2608.14252'
url: https://arxiv.org/abs/2608.14252
pdf_url: https://arxiv.org/pdf/2608.14252
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: 大语言模型事实性 · 接地与纠正控制
tags:
- LLM
- Grounding
- Truth-Tracking
- Corrective Control
- Epistemic Architecture
one_liner: 提出基于路径Profile的LLM事实追踪分析框架，区分历史继承约束与实时纠正能力
practical_value: '- 搭建Agent/RAG链路时，可用文中提出的5项纠正控制特征定位事实性缺陷：如RAG查不到最新数据属于「目标访问」不达标，工具返回结果不被模型采纳属于「有效摄入」不足

  - 生成式推荐/电商文案场景下，需为动态属性（库存、价格、物流时效）匹配实时查询活路径，不能依赖模型训练的继承约束，避免输出过时错误信息

  - 评估LLM事实性时不要只看静态准确率，要匹配路径与任务：纯文本生成可依赖预训练继承约束，涉及实时数据/感知的任务必须加对应活路径，单独用RLHF无法提升客观事实准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM接地研究多聚焦符号是否具备真实语义，忽略了部署场景下的实时纠错路径差异，既无法解释已实现接地的LLM仍在动态事实、小众场景频繁出现幻觉的问题，也不能为事实性增强的干预方案选型提供结构化指导。

### 方法关键点
- 以LLM+提示/工具/检索/校验的完整部署单元为分析对象，提出「路径Profile」框架记录所有约束输出的路径及其耦合关系
- 区分两类可回答性：派生可回答性（训练数据继承的历史修正约束，无法响应训练后发生的事实变化）、实时可回答性（当前活路径可检测并修正最新事实偏差）
- 定义纠正控制的5项分级核心特征：目标访问、偏差可检测性、检查路径独立性、偏差可归因性、修正有效摄入，只有全部满足才具备完整实时纠错能力
- 明确不同增强方案的适配边界：RAG适合依赖静态存档的任务，工具调用适合需要计算/测量的任务，多模态输入适合感知类任务，RLHF仅能提升对话流畅度，无法替代独立事实校验

### 关键结果
本文为理论框架类研究，暂未公布落地实验数值，提出双分离验证范式：检索仅对存档依赖类任务有增益，测量工具仅对实时测量类任务有增益，若不符合该规律则框架失效。

> 最值得记住的一句话：表面效果提升与事实追踪能力提升可能完全脱节，不存在通用的事实性增强方案，需针对任务需要匹配对应活路径。
