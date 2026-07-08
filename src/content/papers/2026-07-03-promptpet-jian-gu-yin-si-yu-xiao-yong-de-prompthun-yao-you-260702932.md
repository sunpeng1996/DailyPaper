---
title: 'PromptPET: Privacy-Utility Optimized Prompt Obfuscation'
title_zh: PromptPET：兼顾隐私与效用的Prompt混淆优化框架
authors:
- Ke Yang
- Olivia Figueira
- Umar Iqbal
- Athina Markopoulou
affiliations:
- University of California, Irvine
- Washington University in St. Louis
arxiv_id: '2607.02932'
url: https://arxiv.org/abs/2607.02932
pdf_url: https://arxiv.org/pdf/2607.02932
published: '2026-07-03'
collected: '2026-07-08'
category: Agent
direction: Agent · Prompt隐私效用平衡优化
tags:
- Prompt_Obfuscation
- Privacy_Preservation
- LLM_Agent
- Reinforcement_Learning
- Utility_Optimization
one_liner: 提出基于LLM的Prompt混淆Agent，动态选择最优混淆策略，平衡用户隐私保护与大模型回复效用
practical_value: '- 电商智能导购、个性化推荐等C端LLM应用可复用4种Prompt混淆动作（擦除/抽象/替换/加噪去噪），预处理用户输入的手机号、地址、历史消费等敏感信息，避免被第三方大模型采集画像

  - 可借鉴「数据类型分类体系识别敏感信息+RL启发的规则优化器动态选策略」的框架，快速在隐私保护强度和回复/推荐效用之间找到业务可接受的平衡点

  - 做LLM应用合规适配时可直接复用该用户侧轻量方案，无需改造大模型侧逻辑即可满足部分隐私合规要求，大幅降低改造工作量'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
用户与LLM交互时Prompt常包含显式/隐式敏感信息，易被大模型用于用户画像，现有Prompt混淆方案普遍存在隐私保护与回复效用难以平衡的痛点。
### 方法关键点
1. 梳理对比4种混淆动作：擦除、抽象、替换、自研加噪/去噪方案；
2. 引入数据类型分类体系完成敏感信息识别与混淆适配，决策时显式纳入回复效用指标；
3. 构建LLM-based Agent PromptPET，采用RL启发的规则优化器为每个Prompt敏感片段动态选择最优混淆动作。
### 关键结果
在真实对话数据集上，PromptPET达到单种混淆动作可实现的最优隐私-效用权衡，性能显著优于现有SOTA方案。
