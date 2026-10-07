---
title: 'Wiki-Talkie: Multilingual Benchmarking of Persona-Based Agents on Real-World
  Discussions'
title_zh: Wiki-Talkie：多语言人格化Agent真实讨论场景评测基准
authors:
- Dennis Fucci
- Andrea Bacciu
- Dong Liu
- Weronika Łajewska
- Saab Mansour
affiliations:
- Amazon
arxiv_id: '2610.08513'
url: https://arxiv.org/abs/2610.08513
pdf_url: https://arxiv.org/pdf/2610.08513
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: Agent 人格化交互多语言评测
tags:
- Persona Agent
- Multilingual Benchmark
- Conversational Agent
- Population Fidelity
- LLM Evaluation
one_liner: 构建覆盖5种语言的维基真实对话数据集，评测人格化Agent的群体交互行为保真度
practical_value: '- 搭建电商个性化客服Agent、用户行为模拟系统时，优先用用户历史行为样本做few-shot conditioning，效果优于硬编码的用户属性画像，还可规避隐私合规风险

  - 做Agent交互行为对齐时，需注意当前LLM普遍存在正向偏见，会少生成负面/对抗性言论、多生成请求类内容，做用户负向反馈模拟、差评应对训练时要针对性修正bias

  - 跨多语言市场部署Agent时，高资源欧洲语言的persona对齐效果差异极小，可复用同一套conditioning策略，无需额外做大量语言适配'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有面向persona-based Agent的评测数据集多依赖虚构人设，仅覆盖中英等少数语言，无法验证Agent交互行为是否匹配真实人群的模式；同时单用户级别persona保真度评测存在 impersonation 伦理风险，缺乏面向群体层面的多语言真实交互评测基准。
### 方法关键点
- 构建Wiki-Talkie数据集：覆盖英/德/西/法/意5种语言，抽取维基编辑讨论页真实对话，匹配对应用户的公开自描述画像、历史交互行为特征，全量数据匿名化处理规避隐私风险
- 评测任务为下一轮对话生成，对比5种conditioning策略：基础角色提示、用户画像提示、行为特征提示、带推理的行为特征提示、用户历史评论样本提示
- 评测维度兼顾单样本文本相似度（ROUGE-L、BERTScore）与群体行为保真度（对话行为分布JSD、情感分布Wasserstein距离）
### 关键结果
- 用户历史评论样本作为conditioning效果最优，ROUGE-L最高达0.154，对话行为分布JSD最低达0.085，比抽象画像/行为描述提示效果提升20%以上；用户画像提示反而会劣于基础提示效果
- 所有测试LLM存在一致行为偏差：比人类多生成2%~17.7%的请求、承诺类内容，少生成2%~10.4%的负面言论，跨语言偏差模式稳定
- 5种高资源欧洲语言的评测结果差异极小，英语的行为对齐效果仅比其他语言高5%左右
> 核心结论：对Agent做persona对齐时，展示用户的行为样例远好于描述用户的属性特征
