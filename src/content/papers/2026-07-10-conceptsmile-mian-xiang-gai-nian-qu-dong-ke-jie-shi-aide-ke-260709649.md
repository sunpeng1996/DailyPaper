---
title: 'ConceptSMILE: Auditing the Trustworthiness of Concept-Based Explainable AI'
title_zh: ConceptSMILE：面向概念驱动可解释AI的可信度审计框架
authors:
- Mohadeseh Mollapour
- Koorosh Aslansefat
- Zeinab Dehghani
- Bhupesh Kumar Mishra
- Tejal Shah
- Zhibao Mian
affiliations:
- University of Hull
- University of Warwick
- Newcastle University
arxiv_id: '2607.09649'
url: https://arxiv.org/abs/2607.09649
pdf_url: https://arxiv.org/pdf/2607.09649
published: '2026-07-10'
collected: '2026-07-13'
category: Eval
direction: 可解释AI可信度量化评估
tags:
- XAI
- Trustworthiness Auditing
- Concept-based Explanation
- Model Agnostic
- Surrogate Model
one_liner: 提出模型无关的扰动式审计框架ConceptSMILE，量化评估基于概念的可解释AI输出可信度
practical_value: '- 做LLM4Rec/生成式推荐的概念级解释时，可复用扰动测试逻辑量化解释可信度，避免虚假解释误导运营与用户

  - 校验VLM生成的商品语义标签（风格、材质等）可靠性时，可套用XGBoost surrogate拟合局部概念行为的方法，快速排查错标问题

  - 搭建推荐系统可解释性合规校验流程时，可直接复用其5维评估指标（归因准确性、保真度、忠实度、稳定性、一致性）'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
基于概念的可解释AI可大幅提升模型推理的人类可理解性，但概念级输出的可信度缺乏统一量化方案，无法支撑高风险场景的合规与可靠性要求。
### 方法关键点
1. 提出模型无关的扰动式审计框架ConceptSMILE，将原有SMILE的特征/区域级扰动逻辑扩展到概念解释层
2. 核心流程：扰动输入区域→度量概念响应偏移→局部加权→拟合XGBoost surrogate近似局部概念行为
3. 从归因准确性、surrogate fidelity、faithfulness、稳定性、一致性5个维度量化概念解释的可靠性
### 关键结果
在视网膜眼底图像数据集测试，MedSAM生成的视觉概念surrogate fidelity $R^2$ 达0.8503、加权$R^2$达0.8465，空间归因表现更优；VLM生成的语义概念在血管特征faithfulness、人工干扰下的稳定性表现更好
