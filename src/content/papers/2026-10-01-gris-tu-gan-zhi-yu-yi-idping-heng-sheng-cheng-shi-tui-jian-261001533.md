---
title: 'Neither Black nor White: Balancing Semantic and Collaborative Signals with
  Graph-Informed Semantic IDs (GrIS)'
title_zh: GrIS：图感知语义ID平衡生成式推荐的语义与协同信号
authors:
- Aleksei Medvedev
- Alejandro Ariza-Casabona
- Steven Derby
- Gonzalo Fiz Pontiveros
- Xinyang Shao
- Florian Spiess
affiliations:
- Huawei Ireland Research Centre
arxiv_id: '2610.01533'
url: https://arxiv.org/abs/2610.01533
pdf_url: https://arxiv.org/pdf/2610.01533
published: '2026-10-01'
collected: '2026-10-02'
category: GenRec
direction: 生成式推荐 · Semantic ID构造
tags:
- Semantic ID
- Generative Recommendation
- Graph Neural Network
- Residual Quantization
- Hierarchical Clustering
one_liner: 将Semantic ID构造重构为层次图划分问题 双组件可配置 最高提升Hit@10达52%
practical_value: '- 可将Semantic ID构造拆分为「图构建+层次划分」两个独立模块迭代，无需整体重构原有管线：仅在现有RQ-VAE量化流程中新增子图采样的图重构损失，即可快速获得协同信号增益

  - 中小规模物品库（万级SKU垂直品类）优先选用RecDMoN，其均衡的簇分配可提升SID前缀的推荐区分度；百万级以上大库选用RQ-GAE，在RQ-VAE基础上加APPNP邻域传播即可兼顾效果与扩展性

  - 构造SID时可低成本引入弱监督协同信号：无需依赖预训练CF embedding，仅用用户交互序列的相邻共现边构建item-item图，即可显著提升SID与用户行为的对齐度

  - SID层次结构优先选择「小分支因子+更深层级」配置（如4层每层6个code），比浅层高分支因子的结构更适配生成式推荐的自回归解码逻辑'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐的Semantic ID（SID）普遍将构造过程视为纯表征量化问题，仅依赖语义特征或零散添加协同约束，缺乏统一框架，无法系统平衡语义相似性与用户行为协同性，当两类信号不一致（如同品类商品面向不同人群）时，生成的SID与推荐目标对齐度差，效果受限。
### 方法关键点
- 提出GrIS统一框架，将SID构造正式定义为层次图划分问题，拆分为两个独立可配置模块：①图构建：从用户交互序列生成带权item-item图，边可定义为共现、顺序跳转等，权重对应关联强度；②层次划分：对图递归划分生成层级SID，纯语义SID方法是空图的特殊情况。
- 落地两种实例：①RecDMoN：用可微分图池化递归聚类，直接从分区路径生成SID，簇分配更均衡；②RQ-GAE：在RQ-VAE基础上新增APPNP图传播编码协同信号，加子图采样的图重构损失约束量化空间，适配大规模场景。
### 关键实验
覆盖电商、新闻、本地生活6个跨域数据集，固定下游生成式推荐主干，对比TIGER、LETTER等SOTA SID方法：RecDMoN在中小数据集上Hit@10最高提升52%，RQ-GAE在百万级图书数据集上Hit@10较S2GR提升16.5%、较LETTER提升34.1%。
### 核心结论
Semantic ID的核心价值不是语义压缩，而是对物品空间做符合推荐目标的层次划分，协同结构和语义特征一样是划分的核心依据
