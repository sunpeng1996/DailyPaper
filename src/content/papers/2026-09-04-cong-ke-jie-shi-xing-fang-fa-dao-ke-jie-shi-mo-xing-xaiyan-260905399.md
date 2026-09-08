---
title: From Interpretability Methods to Interpretable Models
title_zh: 《从可解释性方法到可解释模型：XAI研究重心的范式转移》
authors:
- Julien Colin
- Nuria Oliver
- Thomas Serre
affiliations:
- ELLIS Alicante
- Brown University Carney Institute for Brain Science
- Brown University Department of Cognitive and Psychological Sciences
arxiv_id: '2609.05399'
url: https://arxiv.org/abs/2609.05399
pdf_url: https://arxiv.org/pdf/2609.05399
published: '2026-09-04'
collected: '2026-09-08'
category: Other
direction: 可解释AI · 研究范式转向
tags:
- XAI
- Interpretability
- Model Evaluation
- Trustworthy AI
- Human-centric AI
one_liner: 提出将XAI研究重心从可解释方法构建转向面向非专家使用者的可解释模型评测与体系建设
practical_value: '- 复用XAI成熟工具盒（归因、概念分析等）对业务上线的推荐/排序/Agent大模型做特征表征对齐、bad case归因排查，降低黑盒风险

  - 做模型可解释性验证时需覆盖非技术运营/审核/监管对接人员的认知测试，不要仅算法专家自证，符合合规要求同时降低业务事故率

  - 高风险业务（金融信贷推荐、医疗内容推荐等）的模型选型优先引入可解释性量化评估指标，作为上线准入门槛'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前CV领域XAI已积累归因、特征可视化、概念/电路级分析等成熟工具，但绝大多数研究投入集中在可解释方法的构建与对比，忽略了核心目标：模型本身的可解释性水平、以及模型迭代中可解释性是否提升；同时现有可解释性验证多面向算法专家，未覆盖真正依赖模型的非专业使用者，无法支撑合规与信任要求。

### 方法关键点
提出将XAI研究重心从方法转向模型，两条路径并行：1）复用现有成熟工具，量化对比不同模型的表征与计算逻辑差异；2）新增面向独立非专家评估者的可解释性实测环节，不可仅靠方法推导结论。研究类比系统神经科学范式，梳理了现有少批量模型对比研究，提出了模型中心的XAI研究议程。

### 关键结论
当前XAI工具链已完全支撑上述两类研究方向，现有模型可解释性对比类研究占比极低，存在大量待探索空白。
