---
title: Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations
title_zh: 4D高斯表示下复杂对象分割的查询重写方法
authors:
- Thanh-Khoi Nguyen
- Thien-Phuc Tran
- Minh-Triet Tran
affiliations:
- University of Science, Ho Chi Minh City, Vietnam
- Viet Nam National University, Ho Chi Minh City, Vietnam
arxiv_id: '2609.02664'
url: https://arxiv.org/abs/2609.02664
pdf_url: https://arxiv.org/pdf/2609.02664
published: '2026-09-02'
collected: '2026-09-04'
category: QueryRec
direction: 查询重写 · 免训练语义精简
tags:
- Query Rewriting
- Training-free
- Semantic Alignment
- 4D Gaussian Splatting
- Language-guided Segmentation
one_liner: 提出免训练的长查询精简策略，将冗余描述查询转为关键词锚定形式，大幅提升4D高斯分割性能
practical_value: '- 电商搜索、多模态商品检索场景可复用免训练query改写思路：将用户verbose的自然语言查询转为核心关键词组合，在不微调检索模型的前提下提升召回准确率

  - 做LLM驱动的Agent任务规划、RAG查询生成时，可参考语义锚保留策略：过滤冗余描述的同时保留和目标对象/任务强相关的核心语义单元，降低噪声干扰

  - 多模态召回的排序优化可复用结论：短、关键词聚焦的query能得到更稳定的特征相似度分布，可作为query预处理的统一规则上线'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有基于4D高斯表示的语言引导动态场景理解方案，对携带冗余上下文的冗长叙事类查询敏感度极高，而真实用户输入普遍存在描述冗余、语义零散问题，直接调用现有方案性能衰减严重。
### 方法关键点
受RAG与关键词引导查询重构思路启发，免训练的查询重解释策略可分步过滤查询中的语言学噪声，同时完整保留与对象中心表示强相关的语义锚点，将长描述查询转换为精简的关键词锚定形式。
### 关键结果
在HyperNeRF、Neu3D数据集验证，无需额外微调的前提下，平均时序准确率从60.92%提升至92.21%，平均vIoU从20.08%提升至76.94%；消融实验证实，短、关键词聚焦的查询可输出更稳定的视频特征相似度分布，与对象中心高斯表示的对齐效果更优。
