---
title: Recommender System as Slow and Fast Thinkers
title_zh: 基于快慢思考双系统的自适应序列推荐框架DS-Frame
authors:
- Zichen Yuan
- Xiaoxuan Dong
- Linkun Dai
- Jinwei Yang
- Jining Luan
- Dexu Yu
- Chunxiao Li
- Joemon M. Jose
- Youhua Li
- Hanwen Du
affiliations:
- City University of Hong Kong
- University of Electronic Science and Technology of China
- Shanghai Jiao Tong University
- University of Glasgow
- The Ohio State University
arxiv_id: '2609.02671'
url: https://arxiv.org/abs/2609.02671
pdf_url: https://arxiv.org/pdf/2609.02671
published: '2026-09-02'
collected: '2026-09-03'
category: RecSys
direction: 序列推荐 · 自适应推理优化
tags:
- Sequential Recommendation
- Adaptive Inference
- Dual System
- Conditional Computation
- Recommender System
one_liner: 提出可插拔快慢双系统自适应推理框架，为不同难度用户分配合适计算资源提升推荐精度与效率
practical_value: '- 架构层面可直接复用现有成熟序列推荐主干作为Fast系统，仅需新增轻量Slow迭代精修模块和MLP路由选择器，无需重构现有链路即可快速落地，改造成本极低

  - 路由策略训练方法可直接复用：训练阶段基于快慢系统的损失差+计算成本构造Oracle路由标签，叠加全局算力预算正则，即可学习到样本级的最优路由规则，平衡精度与延迟

  - 业务侧可针对长历史、小众偏好等高价值难预测用户优先分配Slow系统算力，在整体SLA约束下最大化大盘效果提升，尤其适配电商大促等流量波动场景的算力调度

  - 工程侧可通过调整慢路径激活率超参数，灵活适配不同流量峰值下的算力配额，效果优于全量升级大模型的方案，算力投入性价比更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐普遍采用静态单趟推理范式，计算资源平均分配给所有用户请求，对长交互历史、小众偏好等难预测用户群体的效果下降超过20%，既存在算力浪费也无法补齐效果短板。
### 方法关键点
- 提出可插拔DS-Frame框架，包含三大组件：Fast系统直接复用现有成熟推荐主干（如SASRec、BERT4Rec）做高效单趟推理；Slow系统在共享编码结果基础上做K步隐状态迭代精修；轻量MLP选择器实现样本级路由决策。
- 选择器采用Oracle引导训练：训练阶段对比快慢系统的预测损失+计算成本，生成最优路由伪标签，叠加全局慢路径预算正则，确保激活率符合算力约束。
- Slow系统引入三个优化trick：多步推理监督、相邻步分布连续性正则、渐进式温度退火，稳定迭代推理效果。
### 关键结果
在Yelp、亚马逊5个真实推荐数据集上测试，对比主流序列推荐基线：
- 整体效果：SASRec主干NDCG@10平均提升7.5%，BERT4Rec主干NDCG@10平均提升6.7%。
- 分群效果：长历史/小众偏好等难预测用户群NDCG@10提升超8%，是普通用户群提升幅度的2.5倍以上。
- 效率表现：仅启用40%慢路径请求时，效果超过全量使用Slow系统，计算成本仅为全量Slow方案的60%。
### 核心结论
推荐系统的算力应该优先分配给能产生最大边际收益的难预测用户，而非平均分配给所有请求
