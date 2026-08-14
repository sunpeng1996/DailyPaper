---
title: Generative Universal Multimodal Retrieval with Dual-role Identifiers
title_zh: 基于双角色标识符的通用生成式多模态检索框架
authors:
- Kaipeng Li
- Haitao Yu
- Xuanchen Zhou
affiliations:
- Independent Researcher, Japan
- University of Tsukuba, Japan
arxiv_id: '2608.12987'
url: https://arxiv.org/abs/2608.12987
pdf_url: https://arxiv.org/pdf/2608.12987
published: '2026-08-13'
collected: '2026-08-14'
category: GenRec
direction: 生成式多模态检索 · 双角色标识符设计
tags:
- Generative Retrieval
- Multimodal Retrieval
- Semantic ID
- Residual Quantization
- Hybrid Reranking
one_liner: 设计兼具序列生成与集合匹配能力的双角色标识符，提升通用多模态生成式检索性能
practical_value: '- 商品/内容的Semantic ID设计可复用双角色思路：首token标品类/模态，后续token分层编码语义，同时支持序列生成与无序集合匹配，降低自回归解码前缀错误率

  - 生成式检索+小范围稠密重排的混合架构可直接迁移到多模态电商搜索场景：先生成TopK候选保证效率，再用稠密向量精排弥补量化信息损失，平衡时延与效果

  - 多模态嵌入编码可复用「单字压缩」prompt策略：引导LMM将图像/文本/图文混合输入压缩为统一语义向量，降低跨模态匹配难度

  - 训练阶段的查询-目标插值增强技巧可直接复用：通过Beta分布采样混合查询与正样本向量，提升模型对语义相似query的泛化性'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式检索（GIR）存在三大瓶颈：一是自回归左到右解码对前缀错误高度敏感，一旦前缀被剪枝相关候选就无法恢复，容易陷入局部最优；二是绝大多数方案仅支持单模态检索，缺乏对文本、图像、图文混合输入的指令感知适配；三是离散ID类GIR虽推理效率高，但效果显著落后于SOTA稠密检索方案，无法满足通用多模态检索场景需求。
### 方法关键点
- 双角色ID设计：为每个多模态候选分配单个残差量化ID，序列角色下作为有序序列，首token显式编码模态，后续token分层编码细粒度语义，支持自回归解码；集合角色下视为无序token集合，提供前缀无关的相关性先验，引导约束波束搜索缓解局部最优
- 混合检索架构：生成式检索先高效输出TopK候选，再用原始稠密向量相似度重排，弥补离散量化的信息损失
- 训练优化：引入查询-目标插值增强、判别式排序损失，提升模型泛化性与排序一致性
### 关键实验结果
在M-BEIR通用多模态检索基准、Flickr30K、MSCOCO数据集验证，对比SOTA生成式基线GENIUS：本地池检索平均Recall相对提升28.8%（从29.5到38.0），全局池检索平均Recall相对提升27.3%（从28.6到36.4）；搭配LamRA稠密重排的DrIG-LT平均Recall达50.4，接近稠密检索SOTA LamRA的63.7，推理效率远高于全库稠密检索。
### 核心结论
生成式检索无需额外设计多套ID体系，单ID复用序列+集合双属性即可大幅降低前缀错误，搭配小范围稠密重排可实现效率与效果的最优平衡。
