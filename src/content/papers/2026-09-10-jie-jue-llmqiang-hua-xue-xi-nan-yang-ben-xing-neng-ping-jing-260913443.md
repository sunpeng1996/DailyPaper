---
title: Learning to Solve Hard Problems in RL for LLMs by Never Giving Up
title_zh: 解决LLM强化学习难样本性能瓶颈的NGU自适应采样方法
authors:
- Michael Noukhovitch
- Hamish Ivison
- Nathan Lambert
- Aaron Courville
affiliations:
- Mila, Université de Montréal
- Allen Institute for AI
- University of Washington
- Trillium Labs
arxiv_id: '2609.13443'
url: https://arxiv.org/abs/2609.13443
pdf_url: https://arxiv.org/pdf/2609.13443
published: '2026-09-10'
collected: '2026-09-16'
category: Training
direction: LLM强化学习 · 难样本动态采样优化
tags:
- Reinforcement Learning
- GRPO
- Adaptive Sampling
- LLM Training
- Matthew Effect
one_liner: 提出自适应采样策略NGU，破解LLM强化学习马太效应，同等算力下大幅提升难问题性能
practical_value: '- 做LLM驱动的推荐Agent、导购文案生成、复杂query理解的RL微调时，可复用NGU动态采样逻辑，对长尾品类召回、超长复杂query等难样本多分配算力，避免马太效应导致难任务长期无提升

  - 基于GRPO做RL微调时，无需盲目调大单prompt采样数K，小K+NGU的配置算力效率更高，尤其适合电商推荐等存在大量难易不均用户反馈样本的场景

  - 对有分层约束的任务（如电商合规文案生成、多规则广告素材审核），可复用NGU逐测试迭代采样逻辑，优先分配算力解决最难约束，避免训练停滞在部分满足的状态

  - 可复用NGU的正样本锚定技巧，用窗口期内的历史负样本计算GRPO基准优势，过滤过旧off-policy样本的同时最大化梯度信号有效性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM强化学习存在显著的「马太效应」：RL对模型初始就擅长的易样本提升极大，但对难样本几乎无增益，盲目增大单prompt采样数K不仅无法解决问题，还会浪费大量算力在易样本的冗余采样上，训练效率极低，难以落地到资源受限的业务场景。
### 方法关键点
- 提出NGU自适应采样策略：对每个prompt先采样少量（如K=4）completion，全对则标记为易样本过滤，全错则以概率p_NGU放回采样队列继续采样，直到出现正确样本或触发放弃阈值，算力自动向难样本倾斜
- 适配异步RL架构：易样本快速过滤后即时补充难样本，保证训练批次的难度占比接近帕累托最优
- 正样本锚定优化：保留T步窗口期内的历史负样本计算GRPO基准优势，既放大难样本正确解的梯度权重，又避免过旧off-policy样本带来噪声
### 关键实验结果
- GSM8K数学数据集：NGU相比最优GRPO基线（K=4），超难样本pass@1提升15%以上
- Deepscaler数学竞赛数据集：相同120H100算力下，NGU比K=64的GRPO基线难样本性能提升12%，且易样本无明显损失
- Manufactoria编码任务：标准GRPO完全无法通过所有测试用例，NGU最终可实现100%全测试用例通过率
### 核心结论
LLM强化学习的马太效应本质是算力分配效率问题，而非难样本本身无法学习，动态分配算力比盲目增大采样规模收益高得多
