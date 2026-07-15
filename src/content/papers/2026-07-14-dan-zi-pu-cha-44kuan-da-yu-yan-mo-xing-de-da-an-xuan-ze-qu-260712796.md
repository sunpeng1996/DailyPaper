---
title: 'The One-Word Census: Answer-Choice Conformity Across 44 Language Models'
title_zh: 单字普查：44款大语言模型的答案选择趋同性研究
authors:
- Tapan Parikh
arxiv_id: '2607.12796'
url: https://arxiv.org/abs/2607.12796
pdf_url: https://arxiv.org/pdf/2607.12796
published: '2026-07-14'
collected: '2026-07-15'
category: LLM
direction: 大语言模型行为特性量化评估
tags:
- LLM Behavior
- Model Conformity
- Low-cost Evaluation
- Open-ended Generation
one_liner: 设计单字普查工具，量化44款大模型开放式单答案选择的趋同特征与分布规律
practical_value: '- 业务侧LLM生成一致性校验可复用该低cost评估范式，用精确匹配替代高成本人工/embedding打分，单模型仅需1美元即可完成测试

  - 选型业务用LLM时可参考趋同性指标：主流旗舰模型输出稳定可控适合标准化场景，个性化微调模型输出多样性高适合创意类场景

  - 电商/广告普适性文案生成可选高趋同性旗舰模型，输出内容更符合大众认知，降低违规或偏离用户预期的概率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有LLM趋同性研究缺乏极简、低成本的量化工具，无法精准衡量不同模型在等概率开放答案选择场景下的行为差异
**方法关键点**：设计One-Word Census评估范式，采用31道单轮开放类单字回答Prompt（如「Name a tree」），无系统提示词下每款模型重复测试4次，通过归一化token精确匹配统计结果，单模型测试成本仅约1美元；定义surprisal得分（留一法下其他模型答案池的平均$-\log2$概率）量化模型趋异度
**关键结果**：44款模型被要求「任选一个词」时，41%的结果为serendipity；31个测试类别中7个类别的Top1答案占比超80%；不同模型趋异度差异超4倍，个性化/社区微调模型最趋异，主流旗舰模型最趋同，同一模型族迭代中趋同性先升后降；18/20可比类别中模型输出集中度远高于人类
