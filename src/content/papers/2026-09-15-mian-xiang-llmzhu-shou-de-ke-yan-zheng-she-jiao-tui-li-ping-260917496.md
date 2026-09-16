---
title: Verifiable Social Reasoning for LLM Assistants
title_zh: 面向LLM助手的可验证社交推理评估框架Fuse
authors:
- Amir Taubenfeld
- Zorik Gekhman
- Avigail Grinstein-Dabush
- Itay Laish
- Ariel Goldstein
- Marian Croak
- Avinatan Hassidim
- Yossi Matias
- Amir Feder
affiliations:
- Google Research
- Hebrew University
- University of Cambridge
arxiv_id: '2609.17496'
url: https://arxiv.org/abs/2609.17496
pdf_url: https://arxiv.org/pdf/2609.17496
published: '2026-09-15'
collected: '2026-09-16'
category: Eval
direction: Agent仿真 · LLM社交推理评估
tags:
- MultiAgent Simulation
- Social Reasoning
- LLM Evaluation
- Synthetic Dataset
- User Mediated Interaction
one_liner: 提出多Agent仿真框架Fuse，可验证评估LLM在用户主观转述场景下的社交推理能力
practical_value: '- 构建电商导购/客服Agent的意图识别、用户情绪/诉求推理benchmark时，可复用Fuse的多Agent仿真生成带真值的用户转述场景，省去人工标注海量主观场景的高成本

  - 训练客服/导购Agent时，可借鉴框架的可控变量设计，生成带用户偏见、低信息粒度的对抗训练样本，提升模型对用户情绪化、片面表述的鲁棒性，避免过度迎合用户错误认知

  - 多轮对话设计可参考实验结论：超过4轮后模型性能不再提升甚至下降，可将主动追问轮次限制在2-4轮，优先在前期收集关键信息，既降低用户交互成本，也避免被用户后续的偏见表述带偏'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM助手已被广泛用于日常社交咨询场景，但现有社交推理评估范式均给模型输入全量客观场景信息，与真实部署中模型仅能获取用户主观、片面、带偏见的场景转述的情况严重不符；且日常社交场景中第三方的真实动机无明确标注真值，无法开展标准化、可验证的性能评估。

### 方法关键点
- Fuse多Agent仿真框架基于Concordia框架生成多角色社交互动场景，预先设定目标角色的隐藏动机作为可验证真值，模拟用户基于自身记忆、偏见、叙事粒度向助手转述事件
- 评估流程：助手仅基于用户转述预测目标角色的隐藏动机，用LLM-as-judge判定结果为正确/错误/弃权，定义MSR分数综合衡量性能（弃权得0.75倍正确分，平衡谨慎性与实用性）
- 支持可控变量调节：可独立控制用户偏见程度、叙事细节粒度、对话轮次，隔离不同因素对模型性能的影响

### 关键实验
生成21k带真值的用户转述样本，覆盖5类社交心理状态，用24k人工标注验证仿真场景真实度达97%，人类基于首条用户消息的推理准确率达88%。评测12款主流LLM发现：最优模型Gemini 3.7 Flash的MSR仅83.7，比人类基线低6.1分；用户转述会让模型准确率平均下降15%以上，引入用户偏见会让模型MSR平均下降7.7分（是人类下降幅度的2倍）；多轮对话超过4轮后性能不再提升甚至下降，仅19%的初始错误预测会在多轮后修正。

### 核心结论
LLM的社交推理能力不仅受本身推理水平限制，更会被用户的主观转述和偏见大幅削弱，即使是前沿模型在日常社交咨询场景的表现仍有很大提升空间。
