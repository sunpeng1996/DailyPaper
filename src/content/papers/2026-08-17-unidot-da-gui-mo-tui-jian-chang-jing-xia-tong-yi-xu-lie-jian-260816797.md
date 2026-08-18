---
title: 'UniDot: A Unified Network for Sequence Modeling and Feature Interaction in
  Large-scale Recommendation'
title_zh: UniDot：大规模推荐场景下统一序列建模与特征交互的网络
authors:
- Rongcheng Lin
- Yan Sun
- Jamey Zhang
- Guanglei Xiong
- Ivan Ji
- Xianjie Chen
- Shujian Bu
affiliations:
- Meta
arxiv_id: '2608.16797'
url: https://arxiv.org/abs/2608.16797
pdf_url: https://arxiv.org/pdf/2608.16797
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: 大规模推荐 · CTR/CVR 统一建模
tags:
- CTR Prediction
- Feature Interaction
- Sequential Modeling
- Factorization Machine
- KDD Cup
one_liner: 以点积为统一原语融合特征交互与序列建模，获2026 KDD Cup工业赛道亚军
practical_value: '- 架构层面可复用双并行总线+FM Highway设计，仅增加极少量计算成本就能显式保留二阶协同过滤信号，避免深度网络稀释FM类交互信号，适配CVR/CTR排序场景

  - 序列编码模块的Conditional Gated SwiGLU trick可直接迁移，候选信息仅注入gate不修改value路径，既保留DIN的目标感知能力，又避免序列内容被污染

  - 训练阶段可复用共享嵌入的多路径互学习方案，仅增加2倍稠密参数即可获得0.1%+AUC提升，推理时可仅用单路径无额外成本，适配线上latency约束场景

  - 高基数ID特征可采用哈希分治+skip embedding直连分类器的方案，降低大嵌入表存储压力的同时不丢失高价值ID信号'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界推荐系统的特征交互模型（如DeepFM、DCN）与用户序列建模（如DIN、SIM）长期独立演进，生产系统多为松耦合拼接，无法充分融合两类信号；同时深度网络容易稀释FM风格的显式二阶交互信号，在稀疏广告/电商场景下泛化性受损。
### 方法关键点
- 统一token化：将非序列化用户/物品多域特征、多域行为序列映射到同一token空间，序列仅在前向传播时编码一次全模型共享，严格控制推理延迟
- 双并行总线架构：每层并行运行token-mixing总线（处理静态特征交互）和sequence-retrieval总线（物品token交叉注意力检索行为序列），通过MLP-Mixer层交换状态
- FM Highway：每层直接将点积交互（query-key点积、Gram矩阵、用户-物品交叉点积）绕过融合层送入分类器，显式保留二阶协同信号
- 训练优化：采用Adagrad+Muon双优化器，增加转化延迟辅助损失，基于共享嵌入表的双路径互学习正则化，提升模型泛化性
### 关键结果
基于2026 KDD Cup工业赛道35M训练样本、12M测试样本，对比官方baseline AUC提升1.82%；最终双路径模型AUC达0.83217获亚军，单路径模型AUC 0.83184仅比双路径低0.033%，推理成本减半；移除FM Highway会带来0.127%的AUC损失，是贡献最大的组件。
> 最值得记住：显式保留FM式二阶点积交互，比完全依赖深度网络隐式学习交互，在推荐场景下泛化性更好、成本更低
