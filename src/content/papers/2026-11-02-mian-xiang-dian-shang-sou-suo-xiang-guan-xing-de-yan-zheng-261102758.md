---
title: 'Learning to Adjudicate: Verifier-Guided Multi-Agent Reasoning for E-Commerce
  Relevance'
title_zh: 面向电商搜索相关性的验证器引导多智能体推理框架
authors:
- Shi Shu
- Hao Chen
- Baopu Qiu
- Chao Wei
- Weiru Zhang
- Xiu Li
- Xiaoyi Zeng
affiliations:
- 清华大学深圳国际研究生院
- 阿里巴巴国际数字商业集团
arxiv_id: '2611.02758'
url: https://arxiv.org/abs/2611.02758
pdf_url: https://arxiv.org/pdf/2611.02758
published: '2026-11-02'
collected: '2026-11-03'
category: RecSys
direction: 电商搜索相关性 · 多智能体推理
tags:
- Multi-Agent
- Relevance Modeling
- Knowledge Distillation
- Reinforcement Learning
- E-commerce Search
one_liner: 提出CADRE多智能体框架解决电商相关性判断的证据冲突问题，蒸馏轻量模型上线获显著业务收益
practical_value: '- 多角色智能体分工可直接复用：拆分为属性分析、用户意图、业务规则3个独立专家，共享冻结LLM backbone仅训练验证器，大幅降低多智能体训练成本，适配相关性审核等多维度判断场景

  - 选择性辩论机制可平衡效果与成本：仅当3个专家标签不一致时触发1轮定向提问，避免无效多轮交互，适合落地时控制推理耗时

  - 成功经验回放的GRPO训练方案可复用：留存正确判决的完整交互轨迹，与新采样轨迹混合训练，解决难例样本成功轨迹稀缺的问题，提升RL训练效率

  - 推理蒸馏方案可直接落地：用大模型多智能体的CoT作为监督信号，对齐轻量学生模型<[BOS_never_used_51bce0c785ca2f68081bfa7d91973934]>表示与CoT语义向量，既保留大模型推理能力，又满足线上低延迟要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索相关性是搜索推荐的核心基础，现有单LLM推理方案在处理query-产品对的冲突证据时（如属性匹配但用户意图不匹配、业务规则有特殊要求），容易出现单一视角覆盖关键证据导致误判的问题；同时难例样本的正确推理轨迹稀缺，RL训练效率低，大模型推理成本高难以直接上线。

### 方法关键点
- 3个冻结的专家Agent分别负责属性维度匹配、用户行为意图分析、业务规则适配，独立输出分析结果和相关性标签，避免单一上下文的视角偏差
- 可训练Verifier接收3个专家的报告，仅当专家标签不一致时触发1轮定向提问辩论，收集专家修订意见后输出最终判决，大幅减少无效交互
- 用多轮GRPO优化Verifier，引入成功经验回放机制，留存正确判决的完整交互轨迹，和新采样轨迹混合训练，提升难例训练效率
- 大模型作为离线教师，蒸馏CoT推理信号到轻量mBERT学生模型，学生模型仅需输入query和产品即可输出标签，满足线上低延迟要求

### 关键实验
离线实验基于阿里内部7.9万训练、1.87万测试的多语言电商query-产品对数据集，对比单LLM baseline，CADRE教师模型七分类准确率提升3.73个百分点，Macro-F1提升13.64个百分点；蒸馏后的学生模型7天线上A/B测试相比生产基线，RPM提升1.69%，CTR提升0.76%，相关性满意度绝对提升0.3个百分点。

最值得记住的一句话：多维度分析和判决权分离的多智能体架构，配合大模型离线推理+小模型蒸馏上线的模式，是复杂业务规则下LLM落地电商场景的高性价比路径
