---
title: 'LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning'
title_zh: LACUNA：面向大语言模型遗忘的定位精度评估测试集
authors:
- Matteo Boglioni
- Thibault Rousset
- Siva Reddy
- Marius Mosbach
- Verna Dankers
affiliations:
- Mila - Quebec Artificial Intelligence Institute
- McGill University
arxiv_id: '2607.02513'
url: https://arxiv.org/abs/2607.02513
pdf_url: https://arxiv.org/pdf/2607.02513
published: '2026-07-02'
collected: '2026-07-03'
category: Eval
direction: LLM 遗忘能力参数级评估工具
tags:
- LLM Unlearning
- Evaluation Testbed
- PII Protection
- Parameter Localization
- Privacy Preserving
one_liner: 首个带参数级真值标注的LLM遗忘测试集，可验证遗忘是否真擦除参数层面知识
practical_value: '- 业务LLM（如客服、文案生成LLM）做敏感数据遗忘时，可复用LACUNA的评估逻辑，验证unlearning是否真的擦除参数层面知识，避免仅做输出屏蔽被恢复攻击泄露隐私

  - 做LLM合规微调（如满足GDPR被遗忘权要求）时，可参考结论优先精准定位知识存储的对应参数，再做梯度遗忘，效果优于全参数调整，且抗恢复攻击能力更强

  - 对合规要求高的电商/广告业务，可基于LACUNA搭建内部LLM遗忘效果校验流程，满足监管对用户隐私数据删除的要求'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
LLM训练时会记忆PII等敏感数据，现有SOTA unlearning普遍采用「先定位参数、后执行遗忘」范式，但传统评估仅校验输出层效果，无法确认是真擦除参数知识还是仅混淆输出，极易被恢复攻击破解，存在隐私风险。
### 方法关键点
提出LACUNA，首个带参数级真值标注的unlearning测试集：通过掩码持续预训练，将合成的个人PII注入1B、7B参数量的OLMo模型的预定义参数中，可直接验证unlearning方法是否精准命中存储目标知识的权重。
### 关键结果
1. 现有SOTA unlearning方法即使输出层表现达标，参数定位精度极低，普遍易受恢复攻击；
2. 若参数定位精准，仅用简单梯度based unlearning即可实现强知识擦除，且对恢复攻击的鲁棒性大幅提升。
