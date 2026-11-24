---
title: 'TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming'
title_zh: TowerBridge：基于权重空间编程缓解双编码器模态间隙问题
authors:
- Hani Alomari
- Md Atabuzzaman
- Chris Thomas
affiliations:
- Virginia Tech
arxiv_id: '2611.31233'
url: https://arxiv.org/abs/2611.31233
pdf_url: https://arxiv.org/pdf/2611.31233
published: '2026-11-23'
collected: '2026-11-24'
category: Multimodal
direction: 跨模态检索 · 双编码器优化
tags:
- Dual-Encoder
- CLIP
- Modality Gap
- Weight-Space Programming
- Cross-Modal Retrieval
one_liner: 提出无梯度闭式优化方法TowerBridge，提升CLIP类双编码器跨模态检索效果无额外推理成本
practical_value: '- 电商跨模态搜索/推荐场景可直接复用TowerBridge优化CLIP类召回模型：仅需万级配对标注数据，无需梯度训练、不改变模型架构、无推理开销，平均可提15%+跨模态召回准确率，还可与现有重排序策略叠加使用

  - 做LLM驱动的模型优化时可借鉴「Agent探索+规则蒸馏」范式：先用Agent在少量样本上自由探索最优编辑策略，再将通用策略蒸馏为可批量落地的闭式规则，既降低Agent推理成本，又解决Agent输出不稳定的问题

  - 针对召回/排序场景的hard negative hubness问题，可复用配对统计量D的设计定位误导性特征方向，采用轻度衰减而非完全移除的方式优化，避免破坏模型原有零样本泛化能力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
CLIP类双编码器的图文嵌入存在天然模态间隙，常导致检索时hub图像（被大量无关query召回的图像）排名高于正确匹配；直接消除模态间隙会大幅降低零样本性能，而常规梯度微调存在调参成本高、测试时重排序存在推理开销大的问题，亟需低成本通用优化方案。
### 方法关键点
- 设计配对统计量$D$，量化特征空间不同方向上双编码器对匹配对和hard negative的一致性差异，负特征值对应的方向即为放大hard negative得分的误导方向
- 先用LLM Agent Astra在13个CLIP checkpoint上探索无梯度权重编辑策略，发现对输出投影层的误导方向做轻度衰减收益最高
- 蒸馏Agent编辑策略为三步闭式方法TowerBridge：1）用2.5万标注配对数据计算$D$，取1/4维度的误导方向；2）对图文两个输出投影层对应方向做10%衰减；3）重挖hard negative更新统计量，再做5%二次衰减
### 关键实验
在21个不同架构/预训练来源的CLIP checkpoint（含8个Agent从未见过的checkpoint）上测试，COCO测试集RSUM平均提升16.8，Flickr30k平均提升6.6，ImageNet零样本准确率下降不超过0.5个百分点，效果优于LLM Agent直接编辑和多数重排序方法，无任何推理开销。
### 核心结论
针对模型的系统性偏差，轻度衰减误导性特征方向的收益远高于完全移除对应方向，既能解决业务问题又能保留模型原有泛化能力。
