---
title: A Multi-Stage Agentic Framework for Effective Counter-Narrative Generation
  and Refinement
title_zh: 多阶段智能体反叙事生成优化框架，对抗仇恨言论与虚假信息
authors:
- Carmel Kronfeld
- Sharva Gogawale
- Tetsuro Kobayashi
- Irad Ben-Gal
affiliations:
- Tel Aviv University, School of Industrial & Intelligent Systems Engineering
- Tel Aviv University, School of Electrical and Computer Engineering
- Waseda University, School of Political Science and Economics
arxiv_id: '2609.14178'
url: https://arxiv.org/abs/2609.14178
pdf_url: https://arxiv.org/pdf/2609.14178
published: '2026-09-12'
collected: '2026-09-15'
category: Agent
direction: 多智能体 · 内容生成与迭代优化
tags:
- Multi-Agent
- Content Generation
- Misinformation Mitigation
- LLM
- Human Evaluation
one_liner: 提出多阶段多Agent反叙事生成优化框架，效果匹配专家水平，优于原生LLM基线
practical_value: '- 多Agent迭代优化内容的架构可复用：针对电商文案/种草内容的说服力、传播度等多维度优化，可复用「小样本人工标注找最优风格搭配→多Agent迭代打磨→自动安全校验」的全链路

  - 多维度内容评估范式可迁移：做商品推荐话术、广告文案优化时，可直接复用说服力、情感共鸣度、可分享性三个核心评估维度，搭配人工+自动混合校验方法

  - 小样本预实验挖掘风格配对的思路可落地：不同品类/人群的文案优化可先做小范围测试找到适配的修辞+风格组合，再规模化生成，降低试错成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
社交平台仇恨言论、虚假信息直接封禁易加剧群体对立，现有LLM生成反叙事的修辞、风格适配性不足，落地效果不稳定

### 方法关键点
1. 先通过人工预实验挖掘反叙事有效修辞-风格配对，例如重复+情感框架组合可显著提升内容说服力
2. 设计多阶段多Agent框架，分生成、迭代优化、评估三个环节，围绕说服力、情感参与度、可分享性三个核心维度迭代打磨内容
3. 配套自动化安全校验模块，确保输出内容合规无风险

### 关键结果
- 人工验证显示生成内容质量优于vanilla LLM基线，匹配甚至超过专家撰写的反叙事水平
- 模拟实验显示生成的反叙事可有效降低目标虚假信息的感知可信度，支持规模化落地
