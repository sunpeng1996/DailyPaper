---
title: 'SWRouter: Similarity-Contractive Window Routing for Multi-Turn Large Language
  Model Conversations'
title_zh: 面向多轮大语言模型对话的相似收缩窗口路由SWRouter
authors:
- Yu Wang
- Yuchen Li
- Rui Kong
- Xinran Chen
- Jiamin Chen
- Hengyi Cai
- Shuaiqiang Wang
- Jiashu Zhao
- Yulun Zhang
- Zhonghao Lyu
affiliations:
- Shanghai Jiao Tong University
- Baidu Inc.
- Wilfrid Laurier University
- The Hang Seng University of Hong Kong
- York University
arxiv_id: '2609.11414'
url: https://arxiv.org/abs/2609.11414
pdf_url: https://arxiv.org/pdf/2609.11414
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: LLM路由 · 多轮对话上下文优化
tags:
- LLM Routing
- Multi-turn Dialogue
- Context Segmentation
- Contrastive Learning
- Evaluation Framework
one_liner: 提出适配多轮对话的LLM路由框架，联合优化上下文构建、路由决策与解耦评估
practical_value: '- 电商智能客服、导购Agent等多轮交互场景可直接复用相似窗口分割方法：用轻量语义编码器（如mDeBERTaV3）计算相邻用户query的余弦相似度，阈值设0.91做动态窗口切割，既能保留上下文依赖又避免跨主题历史干扰，降低prompt
  token消耗同时减少LLM幻觉

  - 多模型混合调度业务可复用解耦评估框架：拆分construction accuracy（prompt质量）、router performance（路由选模能力）、evaluation
  accuracy（端到端效果）三个指标，避免将prompt质量问题归因为路由能力不足，快速定位系统瓶颈

  - 多模型路由训练可采用双层对比损失（sample-LLM+sample-sample），相比直接拟合模型得分的KL散度效果更优，适配通用大模型、垂类模型、小模型混合调度的异构场景

  - 长对话场景可在窗口分割基础上补充Top-3语义召回补全历史依赖，即使间隔20个无关query，Top-5召回仍达66%以上，开销低且鲁棒性好'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有单轮LLM路由方法直接迁移至多轮对话存在两个核心痛点：一是无合理上下文分割机制，易出现关键历史信息丢失、过时上下文混淆的问题；二是评估阶段无法区分最终效果差是源于prompt构建质量低还是路由决策错误，归因偏差严重，而电商客服、Agent交互等核心业务场景大多为多轮交互，现有方案适配性差。

### 方法关键点
- 语义窗口分割：用轻量编码器编码相邻用户轮次语义，计算余弦相似度，超过阈值τ则合并到当前窗口，否则开启新窗口，构建上下文增强的prompt，平衡上下文保留和冗余
- 路由训练：采用双层对比损失，sample-LLM对比拉进prompt与适配模型的表征距离，sample-sample对比拉进语义相似prompt的表征距离，相比KL拟合分数分布更适配路由目标
- 解耦评估：拆分三类指标，`construction accuracy`衡量prompt整体质量，`router performance`衡量路由选模的相对提升，`evaluation accuracy`衡量端到端最终效果，解决归因偏差问题

### 关键结果
在MTBench、ShareGPT两个多轮对话数据集上，对比7个单模型、Conv-ID上下文路由、ZOOTER基线：
- 比最优单模型的评估准确率提升16.26%，比Conv-ID基线提升8.22%
- OOD场景（数学推理、代码生成、中文知识任务）平均准确率比Conv-ID基线提升2.68%
- 消融实验显示语义窗口是核心贡献点，移除后准确率最高下降46.57%，相似度阈值最优值为0.91

### 核心结论
多轮LLM路由不能直接复用单轮方案，必须联合设计上下文构建和评估机制，而非仅优化路由决策本身
