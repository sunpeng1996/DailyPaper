---
title: 'Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory,
  and the Tenure Crossover in Memory-Architecture Rankings'
title_zh: 先验真值优先的Agent长时记忆评估框架与架构任期交叉效应研究
authors:
- Quentin Spencer
affiliations:
- Independent Researcher
arxiv_id: '2607.21962'
url: https://arxiv.org/abs/2607.21962
pdf_url: https://arxiv.org/pdf/2607.21962
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: Agent长时记忆架构评估
tags:
- Agent Memory
- Longitudinal Evaluation
- Memory Architecture
- Provenance Tracking
- Ground Truth First
one_liner: 提出真值优先的Agent长时记忆评估基准，发现记忆架构效果排名随交互时长反转
practical_value: '- 搭建长周期用户交互Agent（如电商智能导购、个人助理）时，不要仅依赖短程测试选型：短周期（<3周）、预算有限场景可选curated
  map，长周期场景优先选带provenance追踪的分层存储架构，避免早期用户偏好被淘汰导致召回下降。

  - 记忆写入质量直接决定下游效果：弱写入事实的下游错误率是干净写入的15倍，可投入更多token做两阶段写入校验，写入错误率可降低50%，成本可通过多次读请求摊销。

  - 防prompt注入/记忆投毒无需复杂额外防御：只要在记忆存储时保留来源provenance边界（第三方声明不直接转化为事实），实测对非自适应注入攻击拦截率可达100%，比标签标注方案更可靠。

  - 交互轮次低于150的短程场景，直接送全量上下文的效果和复杂记忆架构无显著差异，可简化方案降低工程成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent记忆基准普遍先生成对话再提取标注，存在6%左右的标签误差、真实实体预训练污染问题，且几乎全部聚焦短交互历史测试，会误导长生命周期Agent（如长期陪伴导购、个人助理）的记忆架构选型。
### 方法关键点
- 翻转标注流程：先通过确定性种子采样器生成带有效期、波动等级、来源通道的虚构用户事实脚本，再用LLM渲染为聊天/邮件文本，校验所有植入事实存在后机械生成问题，标注天然无误差且无预训练泄露风险。
- 覆盖15类问题（含事实查询、时间敏感查询、注入探针等），设置3/6/9周三个长周期测试节点，专门设计早期内容召回探针。
- 固定回答LLM、版本化LLM评委、3次随机重复实验消除随机性，对比5种主流记忆架构+无记忆/全量上下文/等token最近窗口3个基线。
### 关键结果数字
- 短程（3周）场景：预算型curated map准确率94.2%，分层混合架构准确率96.8%，与全量上下文的97.9%无显著差异；等token最近窗口准确率仅73%。
- 长程（9周）场景排名反转：curated map因早期内容被淘汰，早期事实召回从96%降至72%，总准确率78.4%；带provenance的图记忆总准确率升至90.4%，分层混合架构达93.2%，仅需全量上下文一半的输入token成本。
- 写入阶段弱事实的下游错误率达24.2%，是干净写入（1.6%）的15倍；保留来源边界的图记忆对非自适应注入攻击拦截率100%。
### 核心金句
短交互周期的记忆测试结果无法指导长生命周期Agent的架构选型，记忆架构的效果排名会随用户交互时长发生反转。
