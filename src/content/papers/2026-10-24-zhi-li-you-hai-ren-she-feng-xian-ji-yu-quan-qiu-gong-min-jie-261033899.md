---
title: 'When Personas Become Harmful: Guiding LLMs with Global Citizenship Values
  Alignment'
title_zh: 治理有害人设风险：基于全球公民价值观的LLM对齐方法
authors:
- Siqi Shen
- Lajanugen Logeswaran
- Moontae Lee
- Honglak Lee
- Rada Mihalcea
affiliations:
- University of Michigan
- LG AI Research
- University of Illinois at Chicago
arxiv_id: '2610.33899'
url: https://arxiv.org/abs/2610.33899
pdf_url: https://arxiv.org/pdf/2610.33899
published: '2026-10-24'
collected: '2026-10-27'
category: LLM
direction: LLM价值观对齐 · 多目标可控生成
tags:
- LLM Alignment
- Persona
- Red Teaming
- Controllable Generation
- Value Alignment
one_liner: 提出基于UNESCO全球公民价值观的LLM对齐框架，平衡人设遵从度与生成安全
practical_value: '- 业务侧个性化Agent（如电商虚拟导购、定制客服）可复用多目标可控对齐方案，通过推理时控制参数动态平衡人设定制需求与内容安全，避免违规话术

  - 红队测试环节可借鉴迭代式Agent管线思路，针对争议性商品/话题搭配不同价值观用户人设，提前发现生成式推荐、个性化文案的安全风险

  - 对齐训练时可采用行业通用共识性规范（如平台治理规则、消费者权益保护条例）作为最小安全边界，既尊重用户多元偏好，又符合合规要求

  - 可控对齐模型可通过LoRA快速微调实现，仅需给样本标注安全/遵从度标签并加入控制token，无需全量训练，适合业务快速落地'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM对齐方法主要针对显式恶意请求，无法处理Persona引导下非恶意争议话题的生成风险：要么直接拒绝合法的个性化价值表达，要么盲目遵从人设输出歧视、仇恨等有害内容；同时现有对齐规则多偏向WEIRD社会价值观，缺乏跨文化通用的安全边界。
### 方法关键点
- 构建11k争议话题+价值观人设数据集：话题覆盖全球8国本地新闻、公开辩论门户，人设映射到Schwartz价值观量表10个维度，覆盖多元文化价值取向
- 迭代式Agent红队管线：自动迭代优化话题与人设，诱导已对齐商业LLM输出有害内容，攻击成功率超47%
- 以UNESCO全球公民价值观作为通用安全边界，区分合法价值表达与有害行为；训练可控SFT（CSFT）模型，推理时通过两个控制参数动态调整安全等级与人设遵从度
### 关键结果
- 传统SFT/DPO对齐后，LLM有害率最高下降0.371，同时保持人设遵从度高于0.63；通用毒性下降23%，指令遵循能力无损失
- 可控对齐模型输出与目标安全、遵从度的相关系数最高达0.725，Pareto frontier面积比普通对齐方案提升27.5%，63.8%的样本表现优于基线
### 核心结论
LLM个性化对齐的核心是在尊重多元价值表达的同时，守住跨文化共识的最小安全边界，而非强制统一价值取向
