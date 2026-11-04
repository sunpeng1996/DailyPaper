---
title: 'SourceFlow: Collaborative Source Coupling for Flow-Based Recommendation'
title_zh: SourceFlow：面向流匹配推荐的协同源耦合方法
authors:
- Chenghao Wu
- Yongqi Zhou
- Jin Chen
- Yifeng Zhou
- Jinchang Zhu
- Junwei Pan
- Chao Zhou
- Zhixiang Feng
- Chengguo Yin
- Menglin Yang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Tencent Inc.
arxiv_id: '2611.04455'
url: https://arxiv.org/abs/2611.04455
pdf_url: https://arxiv.org/pdf/2611.04455
published: '2026-11-03'
collected: '2026-11-04'
category: GenRec
direction: 生成式推荐 · 流匹配协同过滤
tags:
- Collaborative Filtering
- Flow Matching
- Generative Recommendation
- Top-K Recommendation
one_liner: 为流匹配协同过滤设计带用户偏好的协同训练源，较SOTA流基线Recall@10平均提升15.7%
practical_value: '- 现有流匹配推荐模型可直接复用训练源优化逻辑：将全局采样源替换为用户历史物品的协同邻域生成源，推理流程完全不变即可获得涨点，适合快速迭代业务模型

  - 可落地Stretched Restoration调度技巧：延长训练时协同替换物品的留存时间，强化模型从部分交互线索恢复用户偏好的能力，对电商新用户、长尾商品等稀疏场景增益更显著

  - 协同共识加权逻辑可离线预计算：基于历史交互预计算多跳协同支持度，一次计算全量复用，无额外训练/推理开销，适配大规模推荐系统

  - 偏好组留存验证方法可复用：通过SVD聚类用户偏好组，评估输入扰动设计是否保留用户偏好属性，可用于所有生成式推荐的扰动策略验证'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有流匹配协同过滤（Flow-based CF）的训练源从全局物品频率独立采样，与用户目标历史无关联，缺乏个性化偏好引导，限制模型性能上限；而扩散类生成推荐的高斯噪声会破坏隐式反馈的二进制属性，推理步骤多、效率低，难以落地大规模业务。
### 方法关键点
- Neighborhood Coupling：以用户历史交互物品为锚点，从其共现相似度Top-K协同邻域采样未交互物品做替换，生成保留用户偏好的二进制训练源
- Collaborative Consensus：基于交互过锚点的其他用户的全量历史，计算多跳协同支持度，重加权替换概率，进一步提升替代物品的偏好匹配度
- Stretched Restoration：调整训练时间步的替换物品留存策略，让替换物品在更晚的流时间步仍保留，增加模型从协同线索恢复原交互的训练机会
- 仅修改训练源构造和插值逻辑，预测网络、2步推理流程完全和基线一致，无额外推理开销
### 关键实验
在Sports、Toys、Video、Beauty、Yelp 5个公开推荐数据集上，对比ItemKNN、LightGCN、DiffRec、FlowCF、CoFlowCF等12个主流基线，相比最强流匹配基线CoFlowCF，Recall@10平均相对提升15.7%，其中长尾商品Hit@10最高提升超200%，训练/推理耗时与基线基本持平。
### 核心结论
流匹配推荐的性能提升不需要修改模型结构，仅优化训练源的协同耦合设计，就能在不增加推理成本的前提下获得大幅收益。
