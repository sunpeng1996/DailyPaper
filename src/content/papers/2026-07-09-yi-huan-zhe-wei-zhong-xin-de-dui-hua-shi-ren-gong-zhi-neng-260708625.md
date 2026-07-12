---
title: The complexities of patient-centred conversational artificial intelligence
title_zh: 以患者为中心的对话式人工智能的复杂性
authors:
- João Matos
- Olivia Buege
- Donny Cheung
- Gary S. Collins
- Paula Dhiman
- Nan Li
- Bingyu Mao
- Benjamin W. Nelson
- Michail Ouroutzoglou
- Paul Varghese
affiliations:
- Verily Health
- University of Oxford
- University of Birmingham
- NIHR Birmingham Biomedical Research Centre
- Harvard Medical School
arxiv_id: '2607.08625'
url: https://arxiv.org/abs/2607.08625
pdf_url: https://arxiv.org/pdf/2607.08625
published: '2026-07-09'
collected: '2026-07-12'
category: Eval
direction: 对话式AI · 真实场景鲁棒性评估
tags:
- Conversational AI
- LLM Evaluation
- User Simulator
- Persona Modeling
- Real-world Testing
one_liner: 分析2053条真实医患对话，开发多维度用户模拟器，验证沟通风格显著影响LLM分诊结果
practical_value: '- 开发面向用户的对话Agent（如电商导购、智能客服）的用户模拟器时，可拆分内容、情绪、对话策略、沟通风格4个维度独立建模，生成的模拟交互更接近真实场景，提升测试覆盖度

  - 评估LLM对话系统上线效果时，需覆盖不同表达能力、情绪状态的用户persona，避免仅基于理想用户的评估结果和线上实际表现出现大幅偏差

  - 设计C端对话交互系统时，需专门适配不同沟通风格的用户需求，降低因用户表达差异带来的服务效果落差，减少体验分层问题'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前C端LLM对话系统（如健康问诊chatbot）的开发与评估普遍基于理想化、表达清晰的模拟用户，未覆盖真实用户的沟通多样性，上线后易出现性能衰减甚至公平性问题。
### 方法关键点
1. 分析2053条真实患者与chatbot的交互数据，验证用户沟通模式、情绪表达存在极大异质性
2. 开发多维度患者模拟器，独立建模临床内容、情绪状态、对话策略、沟通风格4个核心维度
3. 采用类图灵测试验证模拟器真实性，基于5类差异化用户persona生成1164个clinician标注的病例，评估4款LLM的分诊性能
### 关键结果
- 15名人类标注者区分模拟与真实对话的准确率仅55%，模拟器生成的交互几乎以假乱真
- 用户沟通风格会显著改变LLM的分诊结果，基于理想交互训练的系统上线后易出现性能下降，甚至放大服务差异
