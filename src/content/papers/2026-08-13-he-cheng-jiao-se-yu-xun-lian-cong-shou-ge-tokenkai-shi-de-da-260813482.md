---
title: 'Synthetic Persona Pretraining: Alignment from Token Zero'
title_zh: 合成角色预训练：从首个Token开始的大模型对齐
authors:
- Julian Minder
- Viktor Moskvoretskii
- Raghav Singhal
- Difan Jiao
- Andy Arditi
- Shaobo Cui
- Yiderigun Borjigin
- Kartik Bali
- Stefan Krsteski
- Harsh Raj
affiliations:
- EPFL
- MATS
- University of Toronto
- Northeastern University
- SJTU
arxiv_id: '2608.13482'
url: https://arxiv.org/abs/2608.13482
pdf_url: https://arxiv.org/pdf/2608.13482
published: '2026-08-13'
collected: '2026-08-14'
category: Training
direction: 大模型训练 · 预训练阶段对齐
tags:
- Pre-training Alignment
- Synthetic Persona
- LLM Safety
- Jailbreak Robustness
- Value Alignment
one_liner: 在预训练全流程注入价值观对齐的第一人称反思，从首个Token植入目标助手角色，提升对齐鲁棒性
practical_value: '- 做定制化Agent（如电商客服、导购Agent）时，可在增量预训练阶段注入目标角色的第一人称价值观/话术反思，相比仅依赖SFT加系统提示，角色一致性更强、抗jailbreak能力更高

  - 做合规类大模型（如电商内容审核、广告合规校验）时，将合规规则转化为反思数据注入预训练早期，可提升OOD场景下的合规判断准确率，对齐效果更难被后续微调侵蚀

  - 若核心需求仅为提升jailbreak鲁棒性，无需全预训练流程注入反思，仅在预训练末期（midtraining）注入即可达到最优效果，可大幅节省计算资源

  - 做角色对齐时，SFT数据分布必须和预训练注入的角色数据风格匹配，才能完成有效「角色绑定」，发挥预训练对齐的增益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有大模型对齐方案普遍在预训练完成后通过SFT/RLHF注入助手身份与价值观，本质是在已成型的行为先验上叠加薄补丁，容易被后续微调侵蚀，也难以抵御jailbreak攻击。而预训练阶段接触的数据量远大于后训练，早期注入的信息对模型行为的影响更持久、泛化性更强，因此需要探索预训练阶段的原生对齐方案。

### 方法关键点
- 基于预设的价值观宪法，为约10%的预训练文档（全部高风险文档+等量随机良性文档）生成第一人称价值观反思，用`<assistant>`特殊标记前缀插入文档随机位置
- 预训练阶段同时对原始文档和反思文本计算交叉熵损失，在预训练语料的海量角色中植入目标助手角色
- 后训练阶段使用匹配该角色风格的SP-SFT对话数据微调，完成「角色绑定」，将预训练学到的角色与助手身份关联

### 关键结果
训练3B参数模型在500B tokens上验证，对比Vanilla预训练、过滤有害数据的基线：
- 从token zero开始注入反思的SPP{T0}在ConstitutionEval上准确率达66.8%，比基线高11.6pp；OOD道德困境下的错配率29.5%，比基线低23.8pp
- 所有SPP变体的jailbreak攻击成功率均低于13.6%，比基线低3pp以上，仅在预训练末期注入的变体即可达到最优的jailbreak鲁棒性
- 从token zero注入的对齐优势随预训练预算提升而扩大，3B/500B规模下比1.7B/100B规模的OOD对齐增益高15pp以上

> 最值得记住的结论：大模型的深层价值观对齐必须从预训练早期开始植入，而非等到预训练结束后再修正，早期注入的价值优先级更稳定、泛化性更强
