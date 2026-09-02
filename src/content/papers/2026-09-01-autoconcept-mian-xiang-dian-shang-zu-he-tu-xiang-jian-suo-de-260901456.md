---
title: 'AutoConcept: Training-Free Concept-Guided Reranking for Metadata-Available
  Composed Image Retrieval'
title_zh: AutoConcept：面向电商组合图像检索的免训练概念引导重排方法
authors:
- Tianyu Wang
- Tianjiao Wu
affiliations:
- Soochow University
- INSTITUT NATIONAL DES SCIENCES APPLIQUEES DE LYON
arxiv_id: '2609.01456'
url: https://arxiv.org/abs/2609.01456
pdf_url: https://arxiv.org/pdf/2609.01456
published: '2026-09-01'
collected: '2026-09-02'
category: RecSys
direction: 多模态商品检索 · 免训练概念引导重排
tags:
- Composed Image Retrieval
- Reranking
- Training-free
- Concept Memory
- E-commerce Retrieval
one_liner: 免训练可即插即用的概念记忆重排模块，显著提升电商组合图像检索头部召回效果
practical_value: '- 可直接复用这套免训练重排框架，在现有召回池基础上用商品元数据（属性、标签、标题）做二次重排，无需额外训练成本，快速提升多模态检索的头部召回效果

  - 借鉴其query自适应权重设计：根据召回池首、次名得分差判断基础检索置信度，置信度高时少调整、置信度低时多引入概念匹配得分，避免过度修正原有合理排序

  - 复用概念过滤与激活规则，从用户query、历史行为中提取正负概念约束，过滤噪声概念后通过余弦相似度匹配商品元数据，可直接落地到电商以图搜图、文本改图的检索场景

  - 其可解释的概念记忆机制可直接对接用户显式反馈（比如用户标注的喜欢/不喜欢的属性），快速响应用户个性化需求，不需要重新训练检索模型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有组合图像检索（CIR）大多直接基于多模态嵌入相似度排序，无法有效利用电商商品库普遍存在的结构化元数据（属性、标签、标题），且排序逻辑黑盒化，难以响应用户显式的概念约束（如颜色、款式、材质的偏好/排斥）；同时现有二次重排模块大多需要额外标注训练，落地成本高，难以快速适配不同基础检索模型，因此亟需免训练、可解释、可即插即用的重排方案。
### 方法关键点
- 不修改基础CIR模型，仅对其输出的top-K召回池做二次重排，仅使用召回池内商品的元数据，不引入额外信息
- 从训练侧商品文本或用户修改文本中提取概念短语，通过预设过滤规则（去通用词、冲突概念、弱概念、低grounding概念）构建显式正负概念记忆库
- 计算query修改文本与概念的余弦相似度，通过自适应阈值门限激活query相关的正负概念
- 动态分配权重：根据召回池top1与top2的基础得分差判断基础检索置信度，置信度高时更多保留基础得分，置信度低时更多引入正概念匹配得分与负概念惩罚，融合得到最终重排得分
### 关键结果
在FashionIQ数据集上，基于WeiMoCIR召回池，Recall@10从0.1125提升至0.1379（+22.5%），MRR提升22.3%；基于LinCIR召回池，Recall@10从0.2605提升至0.3009（+15.5%），MRR提升15.7%；仅从query提取概念的轻量化版本也优于直接文本匹配、属性匹配等基线，额外推理开销仅0.3ms/query。
### 核心结论
结构化元数据充足的电商多模态检索场景下，免训练的显式概念记忆重排可以用极低的成本带来显著的头部召回收益，同时具备强可解释性
