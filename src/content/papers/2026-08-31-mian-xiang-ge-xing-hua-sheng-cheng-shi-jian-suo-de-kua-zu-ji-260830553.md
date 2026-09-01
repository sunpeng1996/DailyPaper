---
title: 'Preference Shapes Relevance: Cross-component Hierarchical Semantic Alignment
  for Personalized Generative Retrieval'
title_zh: 面向个性化生成式检索的跨组件层级语义对齐框架CHAP
authors:
- Gaoming Zhang
- Angqing Jiang
- Jianchun Song
- Kena Qi
- Dayao Chen
- Wei Lin
- Defu Lian
affiliations:
- University of Science and Technology of China
- Meituan
arxiv_id: '2608.30553'
url: https://arxiv.org/abs/2608.30553
pdf_url: https://arxiv.org/pdf/2608.30553
published: '2026-08-31'
collected: '2026-09-01'
category: GenRec
direction: 生成式检索 · Semantic ID 个性化优化
tags:
- Generative Retrieval
- Semantic ID
- Personalized Search
- E-commerce Search
- Inference Optimization
one_liner: 通过层级语义对齐和残差级联生成，兼顾生成式检索的准确率与推理效率
practical_value: '- 生成式检索语义对齐可复用HSA模块的三类损失（跨样本对齐、层级对比学习、软概率蒸馏），无需调整预训练物品codebook即可缓解query-item语义gap，同时避免codebook坍塌

  - 推理加速可直接复用残差级联生成机制，将多步Transformer Decoder改为单通推理+轻量残差块解码，QPS提升近1倍且几乎无精度损失，适配低延迟要求的电商搜索/推荐场景

  - 个性化建模可采用「离散SIDs+连续向量」双视图序列输入方案，既保留SIDs的结构约束降低训练难度，又能通过连续特征补全用户历史意图，大幅提升歧义/长尾query的匹配精度

  - 生成式检索落地可先在召回层部署，美团线上验证该方案仅替换召回模块即可拿到UV-CTR+0.77%、转化率+2.09%、订单量+2.98%的业务收益，落地风险低见效快'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式检索（GR）的Semantic ID仅基于物品内容训练，存在动态query意图与静态物品表示的语义gap，且大多未建模用户行为序列，自回归解码的高推理延迟也无法满足工业级部署要求，亟需兼顾准确率、个性化能力、推理效率的GR方案。

### 方法关键点
- 层级语义对齐（HSA）模块：冻结预训练物品codebook，通过跨样本对齐损失、层级感知对比学习、软概率蒸馏三类损失，将query隐空间拉齐到物品量化空间，缓解语义gap同时避免codebook漂移
- 双视图个性化序列建模：输入序列同时拼接离散SIDs（结构引导）和连续物品向量（细粒度语义补全），联合优化稀疏生成损失和稠密对比损失，提升个性化匹配精度
- 残差级联生成机制：Transformer Decoder仅做单通推理，层级SIDs生成交由轻量残差块完成，大幅降低多步解码延迟同时减少信息损失

### 关键实验
在ESCI、KuaiSearch、Amazon、美团本地生活4个数据集上对比14个SOTA基线，本地生活数据集上R@10达0.5803、MRR@10达0.3302，相对最优GR基线COBRA分别提升15.6%、17.5%；推理QPS达78.9，是传统自回归解码的1.95倍；美团线上14天A/B测试，UV-CTR提升0.77%，UV-CXR提升2.09%，支付订单量提升2.98%。

### 核心结论
生成式检索落地的核心瓶颈是语义对齐和推理效率，通过层级结构复用和稀疏稠密双视图融合，可以在几乎不增加部署成本的前提下同时解决这两个问题。
