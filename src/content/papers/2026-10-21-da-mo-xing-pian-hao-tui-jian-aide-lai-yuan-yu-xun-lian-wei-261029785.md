---
title: Where Do LLMs Learn to Recommend AI?
title_zh: 大模型偏好推荐AI的来源：预训练、微调与Prompt影响分析
authors:
- Benaya Trabelsi
- Jonathan Shaki
- Sarit Kraus
affiliations:
- Bar-Ilan University
arxiv_id: '2610.29785'
url: https://arxiv.org/abs/2610.29785
pdf_url: https://arxiv.org/pdf/2610.29785
published: '2026-10-21'
collected: '2026-10-22'
category: LLM
direction: LLM行为分析 · 推荐偏向溯源
tags:
- LLM Bias
- Recommendation Bias
- Instruction Tuning
- DPO
- Prompt Engineering
one_liner: 量化拆解LLM偏好推荐AI的四大来源，明确训练与推理阶段的影响幅度
practical_value: '- 若运营AI相关商品/课程/服务的推荐Agent，可在用户query中加入「最佳」「当下」类修饰词，或在系统提示词中标注自身为AI顾问，可提升AI相关内容推荐占比；

  - 微调电商/内容推荐LLM时，若要降低特定品类的过度推荐，仅过滤训练集中7%左右的对应品类相关样本，就能实现14pp左右的推荐率下降，性价比极高；

  - 做LLM推荐效果评估时，必须覆盖多套同义Prompt变体，避免因「最佳」「当下」等修饰词存在导致评估结果偏离真实业务场景；

  - 用DPO做偏好对齐时，若要避免过度推送热门赛道内容，可引入多样化用户偏好训练数据，而非仅用通用有帮助性偏好数据，可降低热门内容推荐率约9pp。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM在开放咨询场景（学习、职业、创业、科研等）会高频推荐AI相关选项，该倾向直接影响用户决策，但此前没有研究明确该偏好的来源是预训练、微调还是推理阶段的Prompt设置，对可控推荐的落地造成阻碍。

### 方法关键点
- 提出4个假设：预训练自带偏好、后训练改变偏好、AI身份上下文强化偏好、Prompt措辞（最高级/时间词）强化偏好
- 覆盖5个模型家族的10组Base/Instruct配对模型，额外用6种微调策略（通用SFT、去AI样本SFT、Helpfulness DPO、Persona DPO等）训练11组模型做对照
- 设计4个领域共20个问题，每个问题10种paraphrase，用双LLM过滤器识别推荐内容中的显式AI/ML术语，统计推荐占比

### 关键结果
预训练Base模型的AI推荐率为27%，官方Instruct版本升至59%；通用SFT几乎不改变AI推荐率，过滤掉7%的AI相关训练样本后，AI推荐率下降14pp，低于预训练基线；Helpfulness DPO使AI推荐率升9pp，采用多样化用户偏好的Persona DPO则降9pp；推理阶段，用户query加「最佳」类最高级使AI推荐率升8pp，加「当下」类时间词升18pp，系统提示词标注AI身份仅升4pp。

最值得记住的一句话：LLM的AI推荐偏向本质是训练数据特征与Prompt触发的共同结果，而非AI本身的「自我偏好」，开发者可通过训练数据过滤、偏好数据选择、Prompt管控灵活调节特定品类的推荐占比。
