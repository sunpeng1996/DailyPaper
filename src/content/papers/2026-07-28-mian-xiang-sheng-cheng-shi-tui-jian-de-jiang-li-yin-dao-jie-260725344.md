---
title: Reward Guided Decoding for Generative Recommendation
title_zh: 面向生成式推荐的奖励引导解码框架RGD
authors:
- Ruochen Yang
- Yusheng Huang
- Youfeng Zheng
- Shuang Wen
- Liangliang Chen
- Pengbo Xu
- Xiaoyu Zhang
- Shijun Wang
- Shuang Yang
- Zhaojie Liu
affiliations:
- Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Kuaishou Technology
- Peking University
arxiv_id: '2607.25344'
url: https://arxiv.org/abs/2607.25344
pdf_url: https://arxiv.org/pdf/2607.25344
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · 奖励引导解码
tags:
- Generative Recommendation
- Reward Guided Decoding
- Semantic ID
- Beam Search
- LLM4Rec
one_liner: 无需重训生成式推荐基座，在解码阶段逐步骤注入业务奖励信号提升推荐业务价值
practical_value: "- 业务目标频繁迭代的场景优先考虑解码侧对齐方案：无需重训基座，仅调整奖励模型或温度参数$\beta$即可适配新的业务偏好，切换成本远低于DPO/GRPO等训练侧对齐方案\n\
  - 生成概率与业务奖励的融合直接采用推导的闭式规则$\text{log}P + R/\beta$，避免自定义启发式插值，$\beta$作为单一控制旋钮可快速平衡个性化与业务价值，可解释性强、调参成本低\n\
  - 工程落地优先选择hybrid推理模式：仅在Semantic ID生成的第一层做pre-merge奖励打分，后续层采用post-merge，效果接近最优pre-merge模式，额外推理延迟仅比基线高28%，性价比最高\n\
  - 奖励模型无需单独搭建双塔架构，复用基座解码器的隐藏层输出加轻量MLP打分头即可，训练和推理的算力开销都极低，落地门槛低"
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐基于最大似然训练，beam search仅以生成概率为搜索依据，高业务价值但低生成概率的候选易被提前剪枝，和下游业务目标存在固有mismatch。训练侧偏好对齐方案（如DPO、GRPO）需要重训基座模型，业务目标切换成本高；后处理重排仅能调整已生成候选的顺序，无法召回已被剪枝的高价值样本，缺乏灵活低成本的业务对齐方案。
### 方法关键点
- 将价值引导解码建模为KL正则化的奖励最大化问题，推导出闭式解码评分规则：$score = 	ext{log}P + R/eta$，其中$eta$为控制奖励强度的温度参数，融合逻辑有理论支撑，避免启发式分数插值
- 奖励模型复用基座解码器的隐藏层输出，新增轻量链式Bottleneck MLP打分头，和基座联合训练但梯度完全隔离，不会破坏基座已学习的语义和个性化能力
- 支持pre-merge、post-merge、hybrid三种推理模式，可根据算力预算灵活选择；支持动态调整多目标奖励权重与$eta$，无需重训基座即可切换业务目标
### 关键实验
离线在Amazon 3个公开数据集上，相较最优生成式推荐基线，Recall@10最高提升11.49%，NDCG@10最高提升8.30%；快手直播工业数据集上，对比训练侧对齐方案DPO/GRPO，HitRate@604损失不到0.7%，对应业务奖励指标提升幅度更高；线上A/B测试实现CTR+0.392%、直播观看时长+0.689%、观看次数+0.349%的显著收益。
### 核心结论
生成式推荐的业务对齐不一定非要调整基座参数，解码侧的轻量奖励注入是性价比更高的落地方案。
