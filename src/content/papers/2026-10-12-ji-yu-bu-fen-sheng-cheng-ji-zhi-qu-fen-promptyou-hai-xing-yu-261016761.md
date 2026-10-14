---
title: Separating Prompt Harmfulness from Interaction Safety via Partial Generation
title_zh: 基于部分生成机制区分Prompt有害性与LLM交互安全性
authors:
- Ram Vikas Mishra
- Shashank Aggarwal
- Jahnavi Kumar
- Amit Awekar
affiliations:
- Indian Institute of Technology Guwahati
arxiv_id: '2610.16761'
url: https://arxiv.org/abs/2610.16761
pdf_url: https://arxiv.org/pdf/2610.16761
published: '2026-10-12'
collected: '2026-10-14'
category: LLM
direction: LLM安全 · 安全护栏机制优化
tags:
- LLM Safety
- Guardrails
- Partial Generation
- Interaction Safety
- Prompt Injection
one_liner: 量化Prompt有害性与交互安全性的差异，用部分响应提前判断LLM交互安全
practical_value: '- 电商生成式导购、Agent客服的安全护栏可替换原prompt级拦截逻辑：先放行请求生成前1/3响应再做安全判断，大幅降低对正常用户需求的误拦率，提升体验

  - 生成式搜索/推荐场景的内容审核可复用1/3响应提前判断的方案，不用等待全响应生成再审核，降低审核延迟与算力浪费，适配流式输出场景

  - 微调安全分类器时可直接复用论文的样本不平衡处理策略：加权损失、过采样至有害样本占比20%、Focal Loss等，针对低有害率场景的分类效果提升明显

  - 多LLM并行部署的业务系统不要统一设置prompt拦截规则，同个prompt不同模型的输出安全率差异可达4倍，可针对单个模型适配不同的安全阈值'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM安全护栏存在两类缺陷：prompt级拦截策略保守，误拦率极高，大量被判定为有害的prompt实际会得到安全响应，浪费用户正常需求；全响应生成后审核的策略则延迟高、算力浪费严重，在生成式搜索、电商导购等流式交互场景下体验与成本问题尤为突出。

### 方法关键点
- 构建跨模型标注数据集：选取7个开源LLM（Llama、Gemma、Qwen三个家族）对6000个覆盖正常请求、有害请求、prompt注入的公开prompt生成响应，共产出41944对标注样本，明确区分prompt有害性（query固有属性）与交互安全性（prompt+模型输出共同属性）两个核心概念
- 测试5类主流安全分类器：包括DeBERTa-v3、Prompt-Guard-2、Llama Guard 3、WildGuard、LAYA，对比零样本、微调效果，以及不同响应前缀长度的分类性能
- 针对3.66%的低有害样本率，采用加权损失、过采样、Focal Loss等6种策略解决样本不平衡问题

### 关键结果
- Prompt标签与交互标签的一致性仅为50.46%，Cohen's κ仅0.06；能让至少一个模型输出有害响应的prompt中，仅3.5%会让全部7个模型输出有害内容
- 微调后的Llama Guard 3 8B交互安全分类效果最优，AUPRC达0.885，F1达0.807
- 仅用前30%的响应token即可达到全响应分类AUPRC的85%-95%，安全信号在生成早期就已充分暴露

### 核心结论
Prompt有害性不等于交互安全性，仅基于prompt的安全拦截会误拦绝大多数正常交互需求，提前检测部分响应就能平衡安全、体验与成本。
