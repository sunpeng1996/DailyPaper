---
title: Does Reasoning Make Language Models Agree?
title_zh: 推理能力会让大语言模型的输出更一致吗？
authors:
- Mila Gorecki
- Moritz Hardt
affiliations:
- Max Planck Institute for Intelligent Systems, Tübingen
- Tübingen AI Center
arxiv_id: '2610.41691'
url: https://arxiv.org/abs/2610.41691
pdf_url: https://arxiv.org/pdf/2610.41691
published: '2026-10-30'
collected: '2026-11-02'
category: Reasoning
direction: 大语言模型 · 推理一致性研究
tags:
- LLM Reasoning
- Model Agreement
- Algorithmic Monoculture
- Model Multiplicity
- Chain-of-Thought
one_liner: 区分推理作为干预与观测行为两种场景，揭示其对大语言模型间输出一致性的双向作用规律
practical_value: '- 做电商客服、订单审核类Agent时，开启推理可提升多模型投票的输出一致性，降低重复审核成本

  - 可将query触发的推理链长度作为不确定性信号，对长推理链query触发多模型融合校验，减少决策错误

  - 多模型Ensemble做广告/内容审核时，注意开启推理会提升共同错误占比，需搭配规则兜底避免系统性漏判

  - 高价值用户风险判定、大额订单审核等高风险场景，不要完全依赖多模型切换兜底，长推理query仍有概率所有模型同时犯错'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前大语言模型推理已广泛落地于审核、决策、复杂问题求解等场景，但推理对跨模型输出一致性的影响存在认知矛盾：既可能因模型锚定相似特征、遵循趋同推理路径提升一致性，也可能因中间步骤的随机性引入额外分歧，同时算法单文化（monoculture）与多模型结果冲突（multiplicity）两大风险的平衡也亟需明确推理的实际作用，因此亟需厘清不同场景下推理对一致性的影响规律。
### 方法关键点
- 明确区分两种研究视角：推理作为干预（控制模型的推理开关、effort等级参数，固定模型与prompt对比一致性变化）、推理作为观测行为（固定推理设置下，按样本触发的推理链长度分组统计一致性）
- 采用accuracy-adjusted κ作为核心一致性指标，消除模型准确率差异对统计结果的干扰，同时基于独立错误假设构建基线，度量超出随机预期的一致性增量
- 从模型对层面的两两一致性、个体样本层面的recourse（切换模型获得正确结果的概率）两个维度综合评估
### 关键实验结果
- 实验覆盖9款来自OpenAI、阿里云的推理模型，在ACSIncome、ACSEmployment、SIPP三个二分类任务上验证
- 开启推理后，跨模型的median κ提升0.06~0.14，同时所有模型共同错判的样本占比提升2.0~2.4个百分点
- 固定推理设置下，触发最短推理链的样本的κ接近1（几乎完全一致），触发最长推理链的样本的κ仅为0.31~0.39
### 最值得记住的结论
主动要求模型推理会提升跨模型输出一致性，而样本触发的推理链越长，跨模型输出的分歧越高
