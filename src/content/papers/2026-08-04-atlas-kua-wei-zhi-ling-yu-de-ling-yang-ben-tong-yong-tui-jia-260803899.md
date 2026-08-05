---
title: 'ATLAS: Learning to Recommend Across Unseen Domains'
title_zh: ATLAS：跨未知领域的零样本通用推荐框架
authors:
- Pervez Shaik
- Prosenjit Biswas
- Abhinav Thorat
- Ravi Kolla
- Niranjan Pedanekar
affiliations:
- Sony Research India
arxiv_id: '2608.03899'
url: https://arxiv.org/abs/2608.03899
pdf_url: https://arxiv.org/pdf/2608.03899
published: '2026-08-04'
collected: '2026-08-05'
category: RecSys
direction: 跨域推荐 · 零样本领域泛化
tags:
- Cross-Domain Recommendation
- Zero-Shot Recommendation
- Domain Generalization
- RVQ
- Gromov-Wasserstein Alignment
one_liner: 提出无需目标域适配、不依赖LLM的跨域泛化推荐框架，零样本迁移HR平均提升24%
practical_value: '- 跨品类冷启动推荐可复用三组件对齐架构：item侧对抗训练对齐语义空间+user侧Gromov-Wasserstein对齐交互几何+RVQ码本去噪，无需LLM推理，部署成本远低于大模型推荐方案

  - 新品类冷启动无需目标域数据训练，仅用冻结的Sentence-BERT+预训练投影层、码本即可直接上线，节省新品类适配的标注与训练成本

  - 多品类训练时尽量扩充异构源域覆盖范围，根据源域多样性效应，训练域异质性越高，零样本迁移到新品类的效果越好

  - RVQ离散化表示比连续embedding零样本HR平均高45%，可复用该trick提升跨域检索鲁棒性，同时降低ANN检索开销'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐模型均为域绑定，跨新品类部署需重训或目标域适配，依赖LLM预训练的跨域方案推理成本高，无法直接零样本落地到无任何用户/物品重叠的全新品类。
### 方法关键点
- 定义推荐域泛化（RDG）全新设定：模型仅在多源异构域训练，冻结后直接部署到完全未知域，无需任何参数更新或目标域数据参与
- 三组件对齐架构：1）item侧：冻结Sentence-BERT编码物品语义，叠加对抗训练+梯度反转层让item表示跨域不可区分，过滤域特有语义噪声；2）user侧：融合LightGCN协同表示与交互物品语义均值池化表示，用Gromov-Wasserstein下界对齐不同域的用户交互几何结构，无需用户跨域对应关系；3）共享RVQ残差量化码本，压缩用户/物品表示到离散空间，进一步过滤域特有变异，同时提升检索效率
### 关键实验
基于Amazon 15个品类数据集，5个源域训练，10个完全未知域测试，对比SASRec、BERT4Rec、UniSRec、LLM-based推荐等10+基线；零样本场景下在7/10未知域效果最优，平均HR相对提升24%；RVQ离散表示比连续embedding零样本HR平均高45%；源域数量从2个增加到5个时，未知域零样本HR平均提升143%。
### 核心结论
无需LLM预训练或目标域适配，仅通过多源异构域的交互结构对齐，即可获得强泛化的推荐能力，源域多样性是零样本迁移效果的核心影响因素。
