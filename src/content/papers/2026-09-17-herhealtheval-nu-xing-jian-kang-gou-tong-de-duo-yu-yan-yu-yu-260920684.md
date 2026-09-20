---
title: 'HerHealthEval: Evaluating Multilingual and Register-Sensitive Understanding
  of Women''s Health Communication'
title_zh: HerHealthEval：女性健康沟通的多语言语域敏感理解评估基准
authors:
- Hassan Saeed Hassan Albattra
- Mazen Mohammed Bahgat
- Rahatara Ferdousi
- Hana Essam Sayed Ahmed Amrya
- Mariam Mousa
affiliations:
- SD-AI ERA, School of Computing, Queen’s University, Kingston, Ontario, Canada
arxiv_id: '2609.20684'
url: https://arxiv.org/abs/2609.20684
pdf_url: https://arxiv.org/pdf/2609.20684
published: '2026-09-17'
collected: '2026-09-20'
category: Eval
direction: LLM医疗场景多语言评估基准
tags:
- LLM Evaluation
- Multilingual LLM
- Healthcare NLP
- QLoRA
- Risk Calibration
one_liner: 提出面向女性健康场景的多语言多语域LLM理解评估框架，揭示聚合指标掩盖的安全类失效问题
practical_value: '- 垂类Agent评估可复用多语域case构造方法，覆盖官方话术、用户口语、模糊提问等不同表述形式，避免仅测试标准query导致的漏判

  - 跨境多语言垂类模型QLoRA微调时，可采用源端派生的语言不变标签训练，能显著降低低风险漏判率，适配电商多语言客服/导购场景

  - 垂类模型评估不要仅参考聚合准确率，需单独测试信息不全query的澄清触发能力，可用于优化电商场景用户表述不全时的主动追问逻辑'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM医疗沟通场景评估多侧重回复质量，默认用户诉求已被正确理解，缺乏针对多语言、不同用户表述语域的理解能力专项评估，易隐藏安全类失效问题。
### 方法关键点
构建HerHealthEval可控评估框架，覆盖英、法、现代标准阿拉伯语3种语言，每类临床病例对应6种表述形式（标准、临床术语、用户口语、委婉模糊、带情绪、信息不全），前5种信息一致，第6种用于测试模型澄清触发能力；从诉求分类、风险校准、澄清行为、解析合规、跨表述一致性5维度评估多语言指令模型及QLoRA微调变体。
### 关键结果
聚合准确率和一致性会掩盖安全相关失效；语言非对称风险监督下的多语言适配模型在法、阿拉伯语场景under-triage达0.994，改用源端派生的语言不变风险标签重训后，该指标分别降至0.572和0.558
