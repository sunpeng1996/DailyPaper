---
title: 'Consensus vs. Dissent: Dynamic LLM Modeling of Subjective Preferences in Group
  Recommenders'
title_zh: 群体推荐中基于LLM的主观偏好动态建模：平衡共识与分歧
authors:
- Cedric Waterschoot
- Nava Tintarev
- Francesco Barile
affiliations:
- Maastricht University
arxiv_id: '2607.10235'
url: https://arxiv.org/abs/2607.10235
pdf_url: https://arxiv.org/pdf/2607.10235
published: '2026-07-11'
collected: '2026-07-14'
category: RecSys
direction: 群体推荐 · LLM动态聚合策略选择
tags:
- Group_Recommender
- LLM_as_Judge
- LoRA
- Preference_Aggregation
- Fine_Tuning
one_liner: 微调LLM实现群体推荐聚合策略的动态选择，大幅提升用户感知公平性与共识得分
practical_value: '- 做家庭账号、多人拼团选品、好友出游推荐等群体场景时，可复用「多策略生成候选+微调LLM类人评估选优」的架构，效果优于单一静态聚合策略

  - 小样本微调LLM做主观评估时，可采用「少量人类标注+大模型蒸馏生成多样化CoT扩增训练数据」的方案，大幅降低标注成本同时对齐人类评估分布

  - 线上落地时可先对不同群体结构（共识型/少数派型/分裂型）预设最优聚合策略规则兜底，结合轻量LoRA微调小模型做实时打分，平衡效果与 latency'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统群体推荐依赖静态的社会选择偏好聚合策略（如最小痛苦、最大快乐等），无法适配不同群体的偏好分布差异，且用户主观感知的公平性、满意度、共识等指标难以集成到实时推荐链路，缺乏可扩展的方案提前预测用户对推荐结果的主观感受。

### 方法关键点
- 数据层：基于1152份用户标注的群体推荐主观评估数据，用DeepSeek-V3.1生成多样化CoT推理链，将训练样本扩增到5318条，全程保留原始人类标注的公平性、满意度、共识得分
- 模型层：用LoRA对Llama3.1-8B、OLMo-3-7B做4bit量化微调，自定义loss掩码仅计算CoT与得分部分的损失，得到Judgmental系列模型，对齐人类评估分布
- 链路层：对给定群体先生成6种传统聚合策略的候选推荐，调用微调后的模型对每个候选做5次打分取平均，选综合得分最高的策略输出最终推荐

### 关键实验
- 离线评估：微调后的Judgmental OLMo在公平性、满意度、共识三个维度的Wasserstein距离分别降至0.70、0.68、0.82，远优于基线模型，标准差接近人类评估的1.6水平
- 用户研究（n=284）：动态选择方案的公平性得分0.82、共识得分0.81，均为所有方法最高，满意度得分0.68排第二，仅比最高的FAI策略低0.02；在分裂型、少数派型等复杂群体场景下，显著优于所有静态聚合策略

### 核心结论
静态聚合策略没有通用最优解，基于类人主观评估的动态适配是提升复杂群体推荐体验的核心路径
