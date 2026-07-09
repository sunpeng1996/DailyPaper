---
title: 'MMAgent-R$^2$: Learning to Rerank and Reject for Agentic mRAG'
title_zh: MMAgent-R²：面向智能体多模态RAG的重排序与拒识学习
authors:
- Tao Zhang
- Ziqi Zhang
- Zongyang Ma
- Yuxin Yang
- Bing Li
- Chunfeng Yuan
- Kang Rong
- Fengyun Rao
- Jing Lyu
- Weiming Hu
affiliations:
- 中科院自动化所
- 中国科学院大学
- 腾讯微信视觉
- PeopleAI
- 上海科技大学
arxiv_id: '2607.07383'
url: https://arxiv.org/abs/2607.07383
pdf_url: https://arxiv.org/pdf/2607.07383
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: 多模态RAG智能体检索优化
tags:
- mRAG
- VLM
- GRPO
- KB-VQA
- Reinforcement Learning
one_liner: 将视觉重排序与主动拒识融入多模态RAG智能体，通过GRPO联合优化实现多模态VQA任务SOTA
practical_value: '- 多模态RAG场景可复用「视觉重排序+主动拒识」机制，替换现有仅文本级后处理流程，解决电商同款商品识别、广告素材匹配等场景下相似视觉实体召回不准的问题

  - 训练Agent工具调用能力时可参考分层复合奖励设计，除最终结果、格式奖励外增加细粒度步骤级验证奖励，大幅降低RL训练难度，可迁移到电商导购Agent、搜索query意图识别等场景

  - 工程上可参考超参调优结论：候选批次大小K=5、最大拒识次数2可在多数场景平衡准确率与推理成本，避免无限制检索带来的token开销上升

  - 动态召回扩展设计可迁移到搜索推荐召回链路，首屏召回无高置信匹配项时自动触发下一批次召回，提升长尾query、小众商品的匹配准确率'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有多模态RAG（mRAG）依赖全局视觉特征做召回，当知识库存在大量视觉相似实体时易混入错误候选，且后续处理局限于固定候选集，召回误差会直接传导到最终结果，在KB-VQA、多跳推理等复杂场景下性能瓶颈尤为突出。

### 方法关键点
- 构建Agent化mRAG框架，动作空间分为三类：外部检索（图像/文本搜索，连续调用返回非重叠候选批次）、内部验证（视觉重排序直接比对查询与候选图像特征，主动拒识无匹配候选时触发下一批次召回）、答案生成
- 采用GRPO做强化学习训练，设计复合奖励函数：结果奖励（答案正确度）+格式奖励（输出合规性）+步骤级验证奖励（正确重排序/拒识的细粒度激励），训练时屏蔽环境返回的检索内容token，仅优化智能体自身的推理与决策部分

### 关键实验
在InfoSeek、E-VQA、MMhops三个KB-VQA基准上全面取得SOTA：E-VQA（2M页大规模知识库）较最优基线提升7.2个点，MMhops多跳推理任务中Bridging/Comparison赛道分别提升13.2/10.4个点；实体识别准确率较基础召回器Recall@1最高提升14.1个点。

### 核心结论
给多模态RAG智能体赋予视觉层面的主动验证与错误修正能力，是突破大规模知识库下相似实体识别瓶颈的核心路径。
