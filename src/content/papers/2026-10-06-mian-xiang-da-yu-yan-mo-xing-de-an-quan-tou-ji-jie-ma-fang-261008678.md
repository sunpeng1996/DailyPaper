---
title: Secure Speculative Decoding for Large Language Models
title_zh: 面向大语言模型的安全投机解码方法
authors:
- Yichi Zhang
- Zhiqi Wang
- Neil Gong
- Yuchen Yang
affiliations:
- The Pennsylvania State University
- Duke University
arxiv_id: '2610.08678'
url: https://arxiv.org/abs/2610.08678
pdf_url: https://arxiv.org/pdf/2610.08678
published: '2026-10-06'
collected: '2026-10-07'
category: LLM
direction: LLM推理优化 · 安全投机解码
tags:
- Speculative Decoding
- LLM Inference
- Jailbreak Defense
- Prompt Injection
- LLM Security
one_liner: 提出位置感知的SECURESD投机解码方法，在保留推理效率与效用的同时大幅降低越狱、提示注入攻击成功率
practical_value: '- 电商/Agent业务若用投机解码加速LLM生成（如客服回复、商品文案、导购话术），可直接复用SECURESD的位置感知校验逻辑，仅对前1~8个token做严格无损校验，几乎不损失推理速度即可显著降低恶意请求越狱风险

  - 业务侧做LLM服务性能优化时，不能仅评估PPL、任务准确率等效用指标，必须补充安全指标评测：损失式投机解码下安全性能下降速度远快于效用，等效用出现明显下降时安全漏洞已经非常严重

  - 采用小模型草稿+大模型校验的生成架构时，可复用论文的η插值校验策略，根据业务对安全、速度的要求灵活调整严格校验的token长度L，实现自定义的安全-效率tradeoff'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有投机解码方案聚焦效率与效用的平衡，完全忽略安全隐患：损失式投机解码通过放松校验规则提升推理速度的同时，会导致越狱、提示注入攻击成功率大幅上升，且安全性能下降速度远快于效用下降，常规效用评测无法发现该风险，会给面向C端的LLM业务（如电商客服、Agent导购）带来严重安全隐患。

### 方法关键点
- 理论分析得出安全降级主要源自草稿模型生成的早期token：早期token的偏差会直接引导生成方向从拒绝恶意请求转向合规响应，对安全结果的影响远高于中后段token
- 设计SECURESD位置感知校验机制，对解码早期位置的草稿token应用更严格的校验规则，通过η插值策略在无损校验和现有宽松校验之间动态切换，无需修改原有投机解码的核心逻辑即可集成
- 支持step、线性、幂律三种校验调度策略，可灵活调整严格校验的token长度L，适配不同模型、不同业务的安全要求

### 关键结果
在Jailbreak-SD、OpenPromptInjection、HumanEval、GSM8K、AgentDojo共5个基准测试上，对比6种现有损失式投机解码方案，SECURESD可将越狱和提示注入攻击成功率最高降低92.4%，同时保留99.8%的解码加速比，效用指标仅下降最高1.6%。

### 核心结论
损失式投机解码存在显著的安全-效用不对称性，攻击成功率上升速度远快于常规效用指标的下降速度，仅优化效率-效用tradeoff完全无法保障生成安全，安全敏感场景下必须对早期token采用更严格的校验规则
