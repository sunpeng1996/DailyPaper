---
title: 'Asking for What Was Never Requested: Horizontal and Vertical Proactivity in
  Agents'
title_zh: Agent 横向与纵向主动信息获取能力研究
authors:
- Ido Levy
- Asaf Yehudai
- Segev Shlomov
- Asaf Adi
- Leshem Choshen
affiliations:
- IBM
- Weizmann Institute of Science
arxiv_id: '2609.37236'
url: https://arxiv.org/abs/2609.37236
pdf_url: https://arxiv.org/pdf/2609.37236
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 主动信息获取优化
tags:
- Proactive Agent
- DPO
- Question Generation
- RAG
- Multi-hop Reasoning
one_liner: 定义Agent主动信息获取的横/纵向维度，提出无奖励模型的Q&D训练框架，小模型性能超越15倍大的提示模型
practical_value: '- 电商客服Agent可复用Q&D训练范式，无需人工标注奖励，直接基于多轮交互的后续结果训练主动提问模块，减少用户需提供的信息，提升订单修改、退换货等场景的任务完成率，避免反复索要订单号、邮箱等用户记不清的信息

  - 多跳检索类场景（如电商商品多属性匹配、用户复杂需求召回）可借鉴横向/纵向主动性的评估指标，用need graph评估检索效率，避免盲目增加检索次数凑效果

  - 小参数模型做Agent核心决策模块时，可复用DPO结合后果对比的训练方法，在检索/提问决策场景下超越大10倍以上的通用大模型prompt效果，降低推理成本

  - 主动停止决策的训练技巧可复用在RAG的停止检索判断模块，获取足够信息时及时停止，减少不必要的检索开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有主动Agent研究大多关注要不要主动行动，极少关注应该主动获取什么信息，导致Agent要么频繁询问用户降低体验，要么检索冗余信息效率低，且评估时容易把「问得多」等同于「问得好」，缺乏对主动信息获取内容维度的量化评估方法。

### 方法关键点
- 定义两类主动信息获取：横向主动性指获取当前上下文已能明确识别的未声明信息，纵向主动性指获取只有之前检索到的证据才能推导出来的潜在需求
- 提出need graph量化评估主动能力，无需模型打分，直接用交互转录文本和需求依赖的匹配关系计算覆盖率、深度加权召回等指标
- 提出Q&D（Questioner and Drafter）训练框架，将Agent拆分为提问模块和固定的草稿整理模块，通过分叉同状态下的不同提问候选，对比后续检索到的有效证据量做DPO训练，无需额外奖励模型或人工标注

### 关键实验
在MuSiQue、StrategyQA、2WikiMultiHopQA三个多跳QA基准测试，对比同参数prompted模型、15倍大的GPT-OSS-120B等baseline：同等检索开销下，8B训练模型的需求证据覆盖率分别提升11.2、7.0、5.0个百分点，在MuSiQue上达到90% vs 基线的78%；迁移到零售客服场景，任务成功率从13%提升到34%，比15倍大的模型高17个百分点，用户跟进轮次少1.6次。

最值得记住的一句话：Agent的主动能力不仅取决于要不要主动行动，更取决于主动选择获取什么信息以及何时停止。
