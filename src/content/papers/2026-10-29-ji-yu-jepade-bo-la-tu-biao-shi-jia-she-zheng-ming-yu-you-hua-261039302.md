---
title: Proving and Improving the Platonic Representation Hypothesis with JEPAs
title_zh: 基于JEPA的柏拉图表示假设证明与优化方法
authors:
- Randall Balestriero
- Yann LeCun
affiliations:
- Brown University
- New York University
- AMI Labs
arxiv_id: '2610.39302'
url: https://arxiv.org/abs/2610.39302
pdf_url: https://arxiv.org/pdf/2610.39302
published: '2026-10-29'
collected: '2026-10-30'
category: Multimodal
direction: 多模态表示对齐 · JEPA自监督训练
tags:
- JEPA
- Platonic Representation Hypothesis
- Cross-modal Alignment
- Self-supervised Learning
- Next-token Prediction
one_liner: 证明柏拉图表示假设为定理，提出的good-view JEPA跨模态对齐效率超next-token 42倍
practical_value: '- 跨模态商品召回/图文匹配场景可直接复用good-view JEPA训练范式：将同个商品的多个标题、描述、买家评价作为正pair训练文本编码器，无需跨模态配对数据，对齐效率比next-token预训练高42倍，可大幅降低预训练成本

  - 多模态电商Agent的世界模型构建：将同一场景的不同模态观测（用户浏览商品图、点击标题、咨询话术）作为good-view正pair训练JEPA，无需标注即可得到跨模态统一的世界表示，提升Agent的语义理解与决策一致性

  - 快速适配多模态预训练模型：仅需k个跨模态配对样本，即可用正交Procrustes方法求出不同模态编码器间的旋转矩阵，无需全量微调即可实现跨模态对齐，可快速上线新增的视频、3D商品等模态的检索能力

  - 语义召回/Query理解场景优化：将同个Query的不同改写、同个搜索意图的不同输入作为good-view正pair训练文本编码器，相比传统MLM/next-token预训练得到的表示语义一致性更高，可提升召回准确率'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
柏拉图表示假设（PRH）仅观测到大模型缩放后不同模态的表示会趋于对齐，但缺乏理论支撑，也没有高效的落地路径；业界长期依赖堆参数、堆训练数据提升跨模态对齐效果，next-token预训练的LLM对齐效率极低，成本居高不下。
### 方法关键点
- 证明柏拉图表示定理：多个独立训练的JEPA，只要正pair是同一场景的不同观测（good view），学到的表示仅相差一个旋转矩阵，天然跨模态对齐；若正pair是同一观测的扰动（bad view，如next-token的前缀与后缀、单文本掩码片段），则会引入模态专属噪声，难以对齐
- 证明next-token预测本质是bad-view JEPA，解释了LLM需要极大规模才能实现有限跨模态对齐的底层原因
- 提出可落地的good-view JEPA训练范式：同一场景的多组描述/多帧图像作为正pair，配合轻度裁剪、掩码，加梯度裁剪防止训练崩溃
### 关键结果
- 在9.4亿网页图文的文本数据集上训练，good-view JEPA达到与next-token相同的跨模态对齐度仅需1/42的训练样本；109M参数的text JEPA与DINOv2、CLIP图像编码器的对齐度超过所有参数量最高达72B的LLM
- 仅用k个配对样本求出旋转矩阵即可实现无训练的图像caption，COCO数据集上CIDEr达0.838；无配对零样本ImageNet-100 top-5准确率达64%，超过8B参数LLM的56%

**核心结论**：跨模态对齐的核心是正pair的语义一致性而非单纯缩放规模，good-view JEPA可以用极小成本获得远超大模型的跨模态对齐效果
