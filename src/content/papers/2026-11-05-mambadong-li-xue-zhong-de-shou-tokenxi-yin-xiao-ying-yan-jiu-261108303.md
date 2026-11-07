---
title: First-Token Attraction in Mamba Dynamics
title_zh: Mamba动力学中的首Token吸引效应研究
authors:
- Trinh T. Nguyen
- Minh-Khoi Nguyen-Nhat
- Duy-Tung Pham
- Hoang-Son Do
- Tan Minh Nguyen
- Thieu N. Vo
affiliations:
- Shanghai Jiao Tong University
- National University of Singapore
- Northeastern University
- Vietnam Academy of Science and Technology
- University of Bath
arxiv_id: '2611.08303'
url: https://arxiv.org/abs/2611.08303
pdf_url: https://arxiv.org/pdf/2611.08303
published: '2026-11-05'
collected: '2026-11-07'
category: LLM
direction: 大模型基础特性 · Mamba动力学分析
tags:
- Mamba
- TokenDynamics
- SequenceModeling
- SSM
- AttentionSink
one_liner: 提出新分析框架揭示Mamba等序列模型存在首Token吸引后续Token的动力学特性
practical_value: '- 基于Mamba做长序列用户行为建模时，可将用户长期兴趣锚点设为首Token，放大长期兴趣对序列表征的影响，提升推荐一致性

  - 电商RAG导购场景下，可将最高优先级的召回商品/规则放在输入序列首位，利用首Token吸引效应提升生成结果的相关性

  - 基于Mamba的电商Agent决策序列建模可将核心任务目标作为首Token，减少多步决策偏移，提升任务完成率'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
Mamba作为优于Transformer的长序列建模新范式，内部矩阵交互系数无正定性保证，现有Transformer分析方法无法直接复用，其token动力学机制尚未被明确解释，限制了模型优化与落地。
### 方法关键点
引入基于高维不变盒与精确退出时间论证的全新分析框架，推导得到有效符号正定性，可精准刻画token轨迹的极限点与指数收敛速率，突破Mamba动力学分析的原有瓶颈。
### 关键结果数字
- Falcon-Mamba-7B实验验证：首Token关注度随模型深度提升而升高，在深层网络中占绝对主导
- 该首Token吸引机制可扩展到SSM、因果注意力、经典时序模型等多类序列建模架构，具有普适性
