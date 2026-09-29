---
title: 'SPRINT: Single-Step Generative Recommendation via Average Probability Velocity'
title_zh: SPRINT：基于平均概率速度的单步生成式推荐
authors:
- Zhuo Cai
- Shoujin Wang
- Peilin Zhou
- Min Xu
- Julian McAuley
- Fang Chen
affiliations:
- University of Technology Sydney
- New York University Abu Dhabi
- University of California, San Diego
arxiv_id: '2609.34306'
url: https://arxiv.org/abs/2609.34306
pdf_url: https://arxiv.org/pdf/2609.34306
published: '2026-09-28'
collected: '2026-09-29'
category: GenRec
direction: 生成式推荐 · 单步Semantic ID生成
tags:
- Generative Recommendation
- Semantic ID
- Single-step Generation
- Flow Matching
- Contrastive Learning
one_liner: 提出基于平均概率速度的单步Semantic ID生成框架，同时提升生成式推荐的效率与准确率
practical_value: '- 单步生成方案可直接落地低延迟生成式推荐场景：仅需1次前向传播生成完整Semantic ID，对比现有多步方案获得8~10倍推理提速，适配电商首页推荐、广告召回等高并发低延迟要求场景

  - 双级流对比损失可直接复用：同时在token级别优化单token预测精度、在SID级别建模token间的组合语义一致性，解决并行生成的语义漂移问题，相比单纯逐token交叉熵损失可提升约7%的推荐准确率

  - Semantic ID量化器选型技巧：单步并行生成场景优先选用OPQ（优化乘积量化）而非RQ系列量化器，OPQ的各子空间独立特性更适配无依赖的并行预测，可避免RQ的序列依赖导致的性能下降

  - 训练参数配置经验：负采样数N设为100可平衡训练效率与效果，训练样本中锚定全掩码输入的比例ρ设为0.75~1时，模型收敛速度和推理精度最优'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式推荐分为自回归（AR）和非自回归（NAR）两类，均需要多次前向传播生成完整ID，推理延迟高，无法满足电商/广告推荐等对延迟敏感的业务场景；直接将现有NAR方案压缩为单步生成会损失90%以上的准确率，且已有单步方案存在ID过长、嵌入表过大、需要额外搜索步骤等问题。
### 方法关键点
- 从平均概率速度视角建模SID生成：将SID生成视为从全掩码序列到目标ID的概率流，理论证明平均速度仅由每个位置的平均生成概率决定，可通过双向Transformer单次前向传播生成所有位置的token概率
- 双级流对比损失设计：token级别对比优化每个位置的目标token生成概率高于负样本对应位置，SID级别将整个ID的token拼接后做全局对比，建模token间的组合一致性，解决并行生成的语义紊乱问题
- 轻量工程设计：选用OPQ量化器生成4个token的短SID，搭配1层编码器+4层解码器的轻量双向Transformer架构，无额外掩码调度、数据增强模块，部署成本低
### 关键实验结果
在8个公开真实数据集（Amazon多品类、Yelp等）上对比14个SOTA基线，平均准确率较第二名提升7.77%，推理速度较第二快的方案提升8.39~10.04倍，较自回归方案提速最高达125倍。
### 核心结论
生成式推荐的落地瓶颈核心是推理延迟，单步生成架构在不损失准确率的前提下，将生成式推荐的推理成本降到了可大规模落地的水平。
