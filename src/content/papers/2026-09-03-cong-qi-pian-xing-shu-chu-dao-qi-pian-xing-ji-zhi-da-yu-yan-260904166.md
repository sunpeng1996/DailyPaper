---
title: 'From Deceptive Outputs to Deceptive Mechanisms: A Causal Framework for Language-Model
  Deception Research'
title_zh: 《从欺骗性输出到欺骗性机制：大语言模型欺骗研究的因果框架》
authors:
- Yakov Pyotr Shkolnikov
affiliations:
- Independent Researcher
arxiv_id: '2609.04166'
url: https://arxiv.org/abs/2609.04166
pdf_url: https://arxiv.org/pdf/2609.04166
published: '2026-09-03'
collected: '2026-09-06'
category: LLM
direction: LLM欺骗机制因果分析框架研究
tags:
- LLM
- Causal Inference
- Deception Detection
- Model Safety
- Alignment
one_liner: 提出LLM欺骗研究因果分类框架，明确区分欺骗性表象与真实欺骗机制
practical_value: '- 搭建Agent系统对齐流程时，可借鉴该因果分类法区分虚假行为表象与底层机制，避免过度恐慌或误判模型安全风险

  - 电商导购/客服Agent的合规性校验环节，可引入因果归因逻辑排查欺骗性回复的产生路径，而非仅基于输出内容一刀切处理

  - 模型安全检测时，可参考论文的受控实验范式（猜谜、交易场景）设计测试用例，验证Agent是否存在主动欺骗的底层机制'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前LLM欺骗相关研究与报道常类人化赋予模型心理状态概念，混淆了看似欺骗的行为与底层真实欺骗机制，无法准确评估模型安全风险。
### 方法关键点
提出因果分类框架，核心做四组区分：事前承诺与事后报告、模型偏好与实际输出、虚假偏好与误导接收者的效用敏感性、欺骗行为与生成目标/策略的来源；基于两类开源模型，在受控猜谜游戏、股票交易场景下开展验证实验。
### 关键结果
1. 仅观察到欺骗性行为无法证明底层存在对应欺骗机制；
2. 接收者的信息状态会因果性影响模型的欺骗偏好；
3. 即便验证存在欺骗机制，也不代表模型在欺骗行为中具备主体性。
