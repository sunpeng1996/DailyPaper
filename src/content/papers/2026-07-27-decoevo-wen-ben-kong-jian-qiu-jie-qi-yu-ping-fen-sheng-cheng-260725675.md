---
title: 'DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills
  in Text Space'
title_zh: DecoEvo：文本空间求解器与评分生成器的分数解耦协同进化
authors:
- Jiangwang Chen
- Zixin Song
- Junlin Liu
- Shuaiyu Zhou
- Haiyan Wu
- Haihan Shi
- Chenxi Zhou
- Hanqing Li
- Xiao Yang
- Da Zhu
affiliations:
- Tsinghua University
- University of Chinese Academy of Sciences
- Peking University
- Alibaba Qwen Business Unit
arxiv_id: '2607.25675'
url: https://arxiv.org/abs/2607.25675
pdf_url: https://arxiv.org/pdf/2607.25675
published: '2026-07-27'
collected: '2026-07-30'
category: Training
direction: 黑盒LLM · 文本空间技能优化
tags:
- Co-Evolution
- Text-Space Optimization
- Black-box LLM
- Rubric Generation
- LLM Alignment
one_liner: 提出分数解耦的黑盒LLM文本空间协同进化框架，无需金标准评分规则即可同步优化求解器和评分生成能力
practical_value: '- 电商Agent（客服、导购、文案生成）技能迭代时，可复用分数解耦设计：禁止用当前Agent的平均得分作为评估规则的优化目标，避免规则漂移到更容易满足的维度，保障优化方向和真实业务需求对齐

  - 生成内容（推荐理由、商品文案、营销话术）的自动评估体系优化，可直接复用双审计机制：先做结构审计覆盖必填业务规则（比如是否包含促销信息、售后保障），再对得分接近的样本做盲评对比审计，补充规则缺失的区分维度，大幅提升评估规则和人工标准的对齐度

  - 无法微调大模型的业务场景，可直接复用该框架做黑盒优化：仅通过优化外部的任务策略文本和评估规则文本实现效果提升，相对固定规则的SkillOpt可获得2.8~5%的相对收益，迭代成本远低于微调'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有文本空间优化方法依赖固定评估规则，开放任务下规则一旦存在维度遗漏，求解器会过度适配已覆盖维度，忽略未被度量的真实质量要求；若同步进化评分规则，又容易出现分数耦合问题：规则生成器会倾向于生成当前求解器更容易满足的规则，导致内部得分虚高但真实性能不升反降，且多数现有方案依赖金标准评分规则，落地成本高。

### 方法关键点
- 全程冻结LLM backbone，仅维护两个可编辑的文本化技能：求解器技能（存储通用任务策略）、评分规则生成器技能（存储任务专属评分规则的生成原则），所有迭代均在文本空间完成，无需微调
- 求解器基于规则生成器输出的细粒度准则级反馈更新，仅当验证集得分显著提升时才接受更新
- 规则生成器更新完全与求解器总分解耦，通过双审计机制优化：① 结构审计：仅基于任务公开描述检查生成规则的要求覆盖度，无需求解器结果；② 近邻对比审计：先盲评得分接近的求解器输出的质量差异，再反向定位现有规则缺失的区分维度
- 规则更新采用帕累托验证：至少在一个审计目标上有显著提升，且所有审计目标无明显退化才接受，无需多目标加权

### 关键结果
在5个基准（含2个跨域迁移任务）、3个LLM backbone的15组实验中全部最优，相对固定规则的SkillOpt平均相对提升2.8~5.0%，跨域迁移场景下也有1.4~4.5%的收益；而分数耦合的协同进化基线比SkillOpt平均低1.4分，验证了分数解耦的必要性。

> 最值得记住的一句话：开放任务下的技能迭代，永远不要让评估规则的更新和被评估对象的当前得分绑定，否则必然出现评估漂移和性能倒退
