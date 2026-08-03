---
title: 'Fewer Clarifications, Better Code: Benchmarking Cross-Session Personalized
  Ambiguity Adaptation in Coding Assistants'
title_zh: 少澄清更准确：编码助手跨会话个性化歧义适配基准测试
authors:
- Zijian Xu
- Wenshuo Zhang
- Zisen Qin
- Rui Sheng
- Yushi Sun
- Huamin Qu
- Chuhan Shi
affiliations:
- Southeast University
- The Hong Kong University of Science and Technology
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2607.26611'
url: https://arxiv.org/abs/2607.26611
pdf_url: https://arxiv.org/pdf/2607.26611
published: '2026-07-28'
collected: '2026-08-03'
category: Agent
direction: 编码Agent · 跨会话个性化歧义适配
tags:
- Coding Agent
- Personalization
- Cross-session Memory
- Ambiguity Resolution
- Benchmark
one_liner: 提出编码助手跨会话个性化歧义适配任务与CAPA基准，以及轻量同用户历史门控推理方法
practical_value: '- 跨会话个性化歧义处理思路可迁移到电商客服/导购Agent，复用用户历史已澄清的歧义模式减少重复提问，大幅提升交互体验

  - 轻量推理端历史门控方法可直接复用到现有大模型应用的记忆模块，无需微调即可提升历史信息利用率，落地成本极低

  - 受控歧义注入的数据集构建pipeline可复用在自定义Agent个性化能力评测集构建场景，降低人工标注成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有编码助手歧义消解仅针对当前会话独立处理，频繁向用户发起澄清，未挖掘同用户跨会话已解决的历史歧义模式，该方向无统一的任务定义与评测基准。
### 方法关键点
1. 定义个性化歧义适配新任务：基于同用户历史已解决会话，识别重复歧义模式生成符合用户意图的代码，最小化澄清次数
2. 构建CAPA基准：覆盖6种个性化歧义机制，通过3阶段生成pipeline将歧义注入无歧义任务，共包含600个会话、60组均衡的用户-歧义单元，其中300个为留出评估集
3. 提出推理端轻量同用户历史门控方法，优化历史信息的召回与利用效率
### 关键结果数字
评测12款主流LLM，接入同用户历史后，首轮成功率平均提升18%，完成任务所需交互轮次平均降低27%
