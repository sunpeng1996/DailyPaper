---
title: 'Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent
  Trained on Commercial Conversations'
title_zh: 基于真实商业对话训练的销售Agent基准测试与大规模实地随机实验
authors:
- Benjamin Tannenbaum
affiliations:
- Javo, AISO Boost Ltd.
arxiv_id: '2610.25461'
url: https://arxiv.org/abs/2610.25461
pdf_url: https://arxiv.org/pdf/2610.25461
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: 电商销售Agent · 实地A/B测试
tags:
- Sales Agent
- LLM Fine-tuning
- Field Experiment
- Conversational Commerce
- A-B Testing
one_liner: 用460万条真实商业对话微调销售Agent，100个站点随机实验验证收入提升效果
practical_value: '- 训练端：用全量真实商业会话（而非单轮prompt）做SFT+偏好优化，加入合规约束样本，可比相同脚手架下的通用大模型提升21.6%的参与用户转化

  - 评估端：销售类Agent对比必须固定界面、RAG、工具链、prompt、guardrails等脚手架变量，避免把脚手架增益误认为模型本身的效果

  - 设计端：销售Agent对话逻辑对齐「需求挖掘→需求匹配推荐→异议处理→明确下一步行动」四个核心环节，可大幅提升转化效果

  - ROI参考：训练后的销售Agent单会话成本仅为人类客服的1.8%且转化非劣，适合高客单价、重售前咨询的电商/服务场景规模化落地'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有销售Agent评估要么依赖模拟客户的离线benchmark偏差大，要么仅测对人类客服的辅助效果，缺乏通用大模型、专属训练模型、人类客服三者在真实流量下的严格对照，且无法量化模型本身与部署脚手架的增益差异。

### 方法关键点
- 训练数据：460万条合规脱敏的真实商业会话，覆盖零售、文旅、企业服务三大领域，提前过滤测试站点相关数据避免污染
- 训练流程：基于Qwen3-32B做两阶段微调，第一阶段全会话上下文SFT学习销售全流程，第二阶段DPO用转化前/流失前的回复对做偏好优化，加入3.4万条合规约束样本
- 评估框架：固定所有Agent的部署脚手架，仅保留模型权重差异，14个行业100个站点开展5个月随机分流实验，对比无Agent、GPT-5.2、人类客服三组对照

### 关键实验结果
- 相对无Agent组，Javo提升每访客收入10.0%（95% CI 5.1~14.9%）
- 相对相同脚手架的GPT-5.2组，参与用户转化提升21.6%（95% CI 16.9~26.3%）
- 相对人类客服，Javo转化非劣（11.26% vs 11.20%，非劣检验p=0.004），单会话成本仅为人类的1.8%，退货率、投诉率均符合安全阈值

### 核心结论
销售Agent的效果核心来自真实商业会话的领域训练，而非通用大模型的规模，固定脚手架的严格对照是验证模型增益的唯一可靠方法
