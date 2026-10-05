---
title: The Fragility of Trigger-Tag Mechanisms for Misuse Detection in Open-Weight
  LLMs
title_zh: 开源大模型滥用检测触发标签机制的脆弱性研究
authors:
- Toluwani Aremu
- Manit Baser
- Mohan Gurusamy
- Nils Lukas
- Dinil Mon Divakaran
affiliations:
- MBZUAI, UAE
- National University of Singapore
- A*STAR Institute of Advanced Intelligence and Computing
arxiv_id: '2610.03124'
url: https://arxiv.org/abs/2610.03124
pdf_url: https://arxiv.org/pdf/2610.03124
published: '2026-10-02'
collected: '2026-10-05'
category: LLM
direction: 开源LLM安全 · 滥用检测鲁棒性
tags:
- LLM
- Trigger-Tag
- Watermarking
- Backdoor
- Misuse Detection
one_liner: 形式化两类触发标签机制，提出Untag攻击框架证明现有滥用检测触发标签完全失效
practical_value: '- 业务中使用开源LLM生成商品文案、Agent回复时，不可依赖触发标签作为唯一滥用检测手段，需搭配敏感词匹配、语义校验等多层检测方案

  - 若需对业务生成内容做溯源，优先结合输出后显式水印与隐式触发标签的组合方案，降低被攻击者绕过的概率

  - 防范黑产利用开源LLM生成虚假评价、诈骗文案等恶意内容时，需补充外部用户行为检测、内容多维度审核能力，不能信任触发标签的检测结果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
开源大模型支持任意下载、微调与部署，原有中心化安全防护机制完全失效，业界近年提出触发标签机制实现滥用条件下的可检测信号输出，但尚未有研究系统性验证其对抗鲁棒性。
### 方法关键点
1. 形式化拆分两类触发标签机制：token级触发标签在解码阶段注入类水印信号，权重级触发标签通过训练学习目标滥用条件与可检测模型行为的类后门关联
2. 提出Untag统一攻击框架，对两类机制的专属攻击面做分类梳理，构造针对性规避攻击
### 关键结果
以钓鱼内容生成检测为场景测试，现有所有触发标签机制在Untag攻击下100%失效，当攻击者可修改模型输出或开源权重时，该类机制完全不具备作为可靠滥用检测器的能力。
