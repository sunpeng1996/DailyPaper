---
title: 'Moral Safety in LLMs: Exposing Performative Compliance with Puzzled Cues'
title_zh: 大语言模型道德安全：通过模糊提示识别表面合规问题
authors:
- Mohammadamin Shafiei
- Shuyue Stella Li
- Yulia Tsvetkov
affiliations:
- University of Milan
- University of Washington
arxiv_id: '2606.31644'
url: https://arxiv.org/abs/2606.31644
pdf_url: https://arxiv.org/pdf/2606.31644
published: '2026-06-30'
collected: '2026-07-02'
category: LLM
direction: LLM 道德安全评估方法
tags:
- LLM
- Fairness Evaluation
- Safety Alignment
- Robustness
- Bias Detection
one_liner: 提出线索变化方法与线索可见性差距指标，区分LLM真实道德鲁棒性与表面合规
practical_value: '- 做LLM对齐的安全评估时，可复用线索变化方法，把显式规则提示换成隐式场景输入，避免模型过拟合评估范式导致上线后出现偏见

  - 可借鉴Cue Visibility Gap指标，加入现有业务对齐评估体系，量化模型在隐式输入下的合规鲁棒性，规避高风险场景（如信贷准入、商家判罚）的合规隐患

  - 电商/广告推荐的公平性评估可复用该思路，把显式用户性别、年龄标签换成隐式行为特征输入，验证推荐策略是否真的无偏见，而非仅符合评估用例'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM广泛应用于医疗、法律、招聘等高风险场景，现有公平性评估普遍采用显式人口属性标签输入，严重高估模型道德安全性，无法识别仅在评估范式下表现合规的表面合规问题。
### 方法关键点
1. 提出线索变化评估方法，固定道德困境与人口属性，仅改变属性的传递形式（显式标签/隐式线索）
2. 提出模型无关的Cue Visibility Gap鲁棒性指标，可嵌入现有公平性基准，区分真实道德安全与表面合规
### 关键结果
隐藏显式属性标签后，LLM有害决策占比提升+4.4pp，且模型安全排名发生变化；即使模型能正确推理出隐式属性，偏见依然存在，排除归因误差影响。
