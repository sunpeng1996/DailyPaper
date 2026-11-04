---
title: Neologism Inoculation Prompting
title_zh: 新词接种提示（NIP）：阻断用户触发LLM不良行为的轻量训练方法
authors:
- David Demitri Africa
- Cameron Holmes
affiliations:
- Resolution
- UK AI Security Institute
arxiv_id: '2611.04260'
url: https://arxiv.org/abs/2611.04260
pdf_url: https://arxiv.org/pdf/2611.04260
published: '2026-11-03'
collected: '2026-11-04'
category: Training
direction: LLM对齐 · 自定义token训练优化
tags:
- Neologism
- Inoculation Prompting
- LLM Alignment
- LoRA
- Model Safety
one_liner: 用用户无法输入的自定义新token做接种提示，部署时删嵌入，将不良触发率从32%降至0.1%
practical_value: '- 电商/广告Agent敏感操作管控：可将大额优惠券发放、高危API调用等敏感行为绑定自定义不可输入token，部署时删除token嵌入，避免用户prompt注入触发敏感操作，防护成本远低于规则拦截

  - 生成式推荐（GenRec）合规管控：将虚假宣传、违规折扣承诺等不良生成特征绑定自定义token，比普通系统prompt防护难绕过10倍以上，同时保留正常商品推荐、文案生成能力

  - 轻量化LLM语义绑定需求：仅需训练2个嵌入向量（约20KB），用文中的5类匹配对训练范式即可快速让模型掌握自定义语义，比LoRA微调更轻量化，适合需要快速新增控制标签的场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
常规接种提示通过将不良行为与英文系统提示绑定，降低部署时不良输出概率，但用户可直接输入对应英文prompt重新触发不良行为，存在严重安全漏洞，无法用于高风险场景。
### 方法关键点
- 向词表新增1个用户无法输入的自定义token `<z>`，输入输出嵌入初始化为无关通用词（如`thing`），冻结大模型权重仅训练这2个嵌入向量，总参数量仅约20KB
- 采用5类任务（命名、识别、比较、反事实、描述）的正负匹配对训练`<z>`，让模型精准关联`<z>`与目标不良行为的语义
- 微调LoRA时，所有不良样本的系统提示仅使用`<z>`，混合50%干净样本以保留正常业务能力；部署时直接删除`<z>`对应的嵌入行，彻底切断用户触发不良行为的路径
### 关键实验
在Qwen3.6-27B、Gemma-4-31B、OLMo-3.1-32B三款开源大模型上测试，对比SIP（分层接种提示）、GRAFT（梯度路由）等基线：
- 极端运动风险建议场景下，NIP将用户输入触发不良行为的比例从SIP的32%降至0.1%，同时保留与SIP相当的正常能力（历史背景信息保留率89% vs SIP的77%）
- 效果优于密码锁定SIP等方案，安全表现与GRAFT相当，但比GRAFT多保留20%以上的目标有用能力，无GRAFT的输出不连贯问题
- 对奖励黑客、硬编码类场景有效，对谄媚、骚扰类场景效果不佳
### 核心结论
NIP的核心是将不良行为绑定到用户不可达的token空间，而非直接删除行为本身，更适合需要保留双用能力给可信内部调用方的场景
