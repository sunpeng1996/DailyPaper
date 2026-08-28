---
title: 'Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage
  than GRPO'
title_zh: LLM推理场景下进化策略（ES）机制解析：推理覆盖度优于GRPO
authors:
- Yunpeng Ba
- Zhi Zheng
- Yue Xie
- Jiaqing Li
- Xialiang Tong
- Tao Zhong
- Mingxuan Yuan
- Zhichao Lu
- Xuyang Wu
- Zhenkun Wang
affiliations:
- Southern University of Science and Technology
- National University of Singapore
- Huawei Noah's Ark Lab
- City University of Hong Kong
- Harbin Institute of Technology, Weihai
arxiv_id: '2608.27351'
url: https://arxiv.org/abs/2608.27351
pdf_url: https://arxiv.org/pdf/2608.27351
published: '2026-08-26'
collected: '2026-08-28'
category: Training
direction: LLM推理后训练范式优化
tags:
- Evolution Strategies
- GRPO
- LLM Reasoning
- Post-training
- Pass@K
one_liner: 系统对比ES与GRPO的LLM推理后训练特性，证明ES推理覆盖更广且无熵塌陷
practical_value: '- 当业务需要兼顾单样本准确率（Pass@1，如搜索query意图识别）和多样本召回率（Pass@K，如推荐理由生成、智能客服多候选回复）时，可优先选择ES后训练替代GRPO，避免熵塌陷导致的候选多样性下降

  - 算力有限的大模型微调场景，可直接复用论文最优ES配置：z-score奖励归一化、单样本估计，1.5B/3B模型仅需16个种群即可达到64个种群的训练效果

  - 若需要平衡Pass@1和Pass@K效果，可采用GRPO→ES或ES→GRPO的串行训练策略，在总训练预算不变的情况下获得更优的帕累托 trade-off

  - ES微调的效果仅集中在7%~22%的大参数更新上，其余小参数更新可直接裁剪以减小模型存储开销，且不会显著降低业务效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
GRPO作为当前主流的LLM推理后训练范式，存在熵塌陷问题：提升单采样准确率Pass@1的同时会导致大K值的Pass@K下降，限制了智能客服多候选生成、推荐理由多样性生产等需要多采样场景的效果。而进化策略（ES）作为无需反向传播、内存友好的后训练方案，其优化机制、灾难性遗忘风险、最优超参配置一直缺乏系统研究，难以明确其相对GRPO的适用场景。
### 方法关键点
- 理论推导ES种群的验证器投影JS多样性可提升Pass@K，提出GRPO与ES串行的混合训练策略，兼顾两者优势
- 分析ES参数更新的幅度分布，验证功能稀疏性：仅小部分大振幅更新贡献了效果提升
- 系统消融超参配置，对比奖励归一化策略、种群规模、估计器选择对ES效果的影响
### 关键结果
实验覆盖GSM8K、DeepScaleR、GPQA、MATH-500等多类推理任务，基线为基础模型、纯GRPO：
1. ES在所有任务上同时提升Pass@1、Pass@16、Pass@32，而GRPO提升Pass@1的同时，15/18的对比场景下Pass@16、Pass@32低于基础模型
2. ES全模型参数漂移是GRPO的40.7~44.1倍，但仅7%~22.4%的大振幅参数更新贡献了全部效果，裁剪其余小幅更新后效果几乎无损失，且无灾难性遗忘，跨任务泛化表现优于GRPO
3. 大模型可使用更小ES种群：0.5B模型需要32个种群才能接近64种群的效果，1.5B/3B模型仅需16个种群即可达到同等水平

ES不是GRPO的低性能内存友好替代方案，而是具备独特推理覆盖优势的独立后训练范式，适合需要多候选采样的推理场景
