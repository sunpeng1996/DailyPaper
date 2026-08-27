---
title: A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks
title_zh: 可自进化的多智能体框架抵御大语言模型越狱攻击
authors:
- Tongyan Hu
- Bryan Hooi
affiliations:
- National University of Singapore
arxiv_id: '2608.26008'
url: https://arxiv.org/abs/2608.26008
pdf_url: https://arxiv.org/pdf/2608.26008
published: '2026-08-26'
collected: '2026-08-27'
category: Agent
direction: 多智能体 LLM越狱攻击自适应防御
tags:
- Multi-Agent
- LLM Safety
- Jailbreak Defense
- Test-Time Adaptation
- External Memory
one_liner: 基于跨交互持久化方法级规则记忆，无需参数更新的LLM越狱自适应测试时防御框架
practical_value: '- 电商客服/内容生成类Agent可复用该规则记忆机制，将恶意用户诱导生成虚假宣传、违规话术的绕过模式抽象为方法级规则，动态更新防御规则无需微调模型，大幅降低违规输出风险

  - 三级规则触发策略（标签匹配→LLM语义相似召回→关键词fallback）可直接复用在搜索/推荐的query安全审核场景，平衡审核准确率和性能，避免全量规则匹配的耗时损耗

  - 「违规检测→规则抽象→防御触发」的自进化闭环可迁移到广告素材审核系统，自动学习新型违规素材绕过模式，无需人工频繁更新审核规则库，降低运营成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM防御机制多为静态，部署后安全行为固定，无法累积防御经验适配不断演化的越狱攻击策略，角色扮演、混淆、代码转换等新型绕过模式极易突破静态对齐、固定安全prompt、外部分类器等方案，且静态方案无法复用同类型攻击的防御经验，每次新攻击出现都需要重新微调或更新规则，响应成本高、滞后性强。

### 方法关键点
- 核心为跨交互持久化规则记忆，规则仅抽象攻击的结构wrapper（如嵌套角色扮演、代码混淆）而非有害话题，单条规则可泛化到同攻击家族所有样本
- 无需任何参数更新，完全通过外部记忆和prompt实现，适配开源和黑盒API模型
- 4个协作Agent实现全流程：规则触发Agent分类输入、检索相关规则；策略决策Agent判定输出策略（允许/软拒绝/硬拒绝）；响应生成Agent按策略输出；自反射Agent检测到违规后抽象新规则更新记忆库，规则会做语义去重、单标签容量限制避免冗余
- 规则触发采用三级匹配，单次最多触发2条规则，避免干扰正常请求

### 关键结果
基于Advbench 520条有害prompt、MMLU/GSM8K测良性效用，对比无防御、固定安全prompt、Self-reminder、AutoDefense等基线：在4类越狱攻击下，ASR-gpt（攻击成功率）相比基线最高下降98%，Gemini-3-Flash-Preview上ASR-gpt最低降至0.1%；良性任务效用下降<2%；记忆积累后过拒率仅9.6%；冷启动下仅需1轮交互即可学到对应攻击家族规则，后续ASR降至接近0。

最值得记住的一句话：将攻击结构模式与有害话题解耦的规则抽象设计，是无需参数更新即可实现跨攻击家族防御泛化的核心。
