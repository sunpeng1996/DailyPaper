---
title: 'Highlight-Then-Summarize: Learning to Compress Evidence for Long-Context Understanding'
title_zh: Highlight-Then-Summarize：面向长上下文理解的证据压缩方法
authors:
- Zhaoyuan Xia
- Qinghongbing Xie
- Yung Xiang Hue
- Jianguang Jiang
- Gaofeng Lu
- Zhenyu Jiao
- Xing Yuan
- Dai Dai
- Tong Mo
- Long Zeng
affiliations:
- 北京大学
- 百度
- 清华大学
arxiv_id: '2609.31382'
url: https://arxiv.org/abs/2609.31382
pdf_url: https://arxiv.org/pdf/2609.31382
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: LLM长上下文优化 · 证据压缩推理
tags:
- Long-Context-Understanding
- Evidence-Compression
- Reinforcement-Learning
- Summarization
- LLM
one_liner: 提出高亮证据再生成问题导向摘要的压缩推理范式，大幅提升长上下文LLM推理性能
practical_value: '- 电商长商品详情页QA、广告用户多轮咨询场景可直接复用H2S范式：先高亮与用户query相关的商品属性、历史交互证据，再生成问题导向摘要，降低无关信息干扰，提升回复准确率与可信度

  - 可复用H2S-RL的无LLM判分奖励设计：对RAG、长用户行为序列建模等任务，同时设计最终结果、中间证据召回、摘要质量的多维度程序式奖励，大幅降低RL训练的推理成本

  - 长序列推荐场景可借鉴该范式：先高亮与当前候选item相关的历史行为证据，再压缩为用户动态兴趣摘要，既降低长序列推理开销，也能为推荐结果提供可解释的证据支撑'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM长上下文推理普遍面临无关冗余信息干扰、任务相关证据稀疏分散的痛点，仅靠扩展上下文窗口无法解决有效信息利用率低的问题；且现有长上下文优化方法仅聚焦证据检索，未实现多段分散证据的有效整合，导致推理准确率低、生成冗余度高，无法适配低输出预算的业务场景。
### 方法关键点
- 提出H2S（Highlight-Then-Summarize）压缩推理范式，将长上下文推理拆分为「证据高亮→问题导向摘要生成→最终回答」三个串行步骤，所有步骤由单个自回归模型完成，既保留证据的原文可溯源性，也将分散证据整合为紧凑的推理就绪状态
- 构建包含6647条样本的H2S-Dataset，覆盖11类长上下文任务，平均上下文长度43.9K tokens，每条样本包含证据块、问题导向摘要、最终答案的结构化监督信号，支持SFT与RL训练
- 设计H2S-RL强化学习训练方法，采用程序式多维度奖励，同时评估最终回答准确率、证据溯源正确性、摘要质量、输出结构合规性，无需依赖在线LLM判分，降低训练成本
### 关键实验
在覆盖检索、推理、摘要等7类任务的H2S-Bench上评测，相同128K输入、4K输出预算下，H2S-14B平均得分32.60，比参数更大的Qwen3.8-27B高10.17分，比QwenLong-L1-32B高5.01分，在所有参评开源模型中排名第一；仅用4K输出预算就能保留16K输出预算下97.1%的性能，大幅降低生成开销。
> 最值得记住的一句话：长上下文推理的核心不是盲目扩大窗口容纳更多信息，而是先过滤无关内容，再把分散的相关证据组织成问题导向的紧凑表示，用更少的有效信息实现更高的推理准确率
