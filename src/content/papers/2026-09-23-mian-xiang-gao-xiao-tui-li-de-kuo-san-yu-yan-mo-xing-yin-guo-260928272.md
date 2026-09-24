---
title: 'Towards Efficient Reasoning: Learning Causal Shortcuts for Diffusion Language
  Models'
title_zh: 面向高效推理的扩散语言模型因果捷径学习方法
authors:
- Dian Jin
- Kairong Han
- Baohong Li
- Xinpeng Dong
- Zijing Hu
- Nuanqiao Shan
- Fei Wu
- Kun Kuang
affiliations:
- Zhejiang University
- Shanghai AI Laboratory
arxiv_id: '2609.28272'
url: https://arxiv.org/abs/2609.28272
pdf_url: https://arxiv.org/pdf/2609.28272
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: 扩散大语言模型 · 推理效率优化
tags:
- Diffusion Language Model
- Conditional Mutual Information
- Causal Shortcut
- SFT
- Efficient Reasoning
one_liner: 提出基于条件互信息的因果捷径学习框架，提升扩散语言模型推理效率与准确率
practical_value: '- 可将条件互信息（CMI）作为token重要性打分指标，迁移到生成式推荐的SFT阶段，优先给引导用户决策的关键token（如价格、卖点、权益）分配更高训练权重，提升推荐理由、营销文案的生成准确率

  - Step-by-step的token提取策略可复用在搜索query改写、商品标题生成场景，解决高价值token聚类在序列前端的问题，保证关键信息覆盖完整的生成逻辑链

  - 并行优先掩码的训练思路可适配DLM架构的生成式推荐模型，避免传统随机掩码下模型优先学习高频无意义token的问题，降低长文案生成的误差累积'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Diffusion Language Models（DLMs）凭借双向注意力和并行生成优势具备强推理潜力，但随机掩码策略下探索空间呈指数级膨胀，模型难以聚焦引导推理的关键token；现有基于熵/损失的重加权方法混淆了“难度”和“推理重要性”，易过度关注不确定性高但无推理价值的token，导致推理收敛慢、准确率低、长序列误差累积严重。

### 方法关键点
- 提出Conditional Mutual Information（CMI）分数衡量单个token对其余掩码token的信息增益，将高CMI token组成的全序列覆盖token链定义为因果捷径，可为推理提供明确路径引导
- 设计Step-by-step因果捷径提取流程：迭代选择当前CMI最高的token并解锁，动态更新CMI分布，解决one-step提取时高CMI token聚类在序列前端、无法覆盖完整推理轨迹的问题；通过滑动窗口搜索+轻量CMI打分模型优化提取复杂度，从O(L²)降至O(L)
- 训练阶段采用并行优先掩码策略：对因果捷径token始终开启掩码优化梯度，其余token沿用随机掩码，既强化模型对推理关键路径的学习，又避免并行掩码破坏强依赖token的关联关系

### 关键结果
在7个数学推理、2个代码生成基准上测试，基于LLaDA-8B-Instruct和LLaDA-1.5B两个基座，对比SFT、DiffusionBert、MGDM等6个基线：平均推理准确率较纯SFT提升1.92%，MATH-500数据集最高提升4.20%，代码生成任务平均提升2.30%；解码阶段熵衰减速度提升4.7%~8.7%，长序列累积熵最高降低17.26，有效减少误差累积。

> 最值得记住的结论：不要将token的不确定性等价于推理重要性，基于因果信息增益筛选关键路径的训练方式，能以极低额外成本显著提升生成模型的推理效率与准确率
