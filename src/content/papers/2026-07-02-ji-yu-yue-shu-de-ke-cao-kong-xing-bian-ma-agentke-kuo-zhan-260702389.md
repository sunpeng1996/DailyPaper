---
title: 'Steerability via constraints: a substrate for scalable oversight of coding
  agents'
title_zh: 基于约束的可操控性：编码Agent可扩展监管的底层方案
authors:
- Thomas Winninger
affiliations:
- Télécom SudParis
- ENS Paris-Saclay
arxiv_id: '2607.02389'
url: https://arxiv.org/abs/2607.02389
pdf_url: https://arxiv.org/pdf/2607.02389
published: '2026-07-02'
collected: '2026-07-03'
category: Agent
direction: 编码Agent可扩展监管优化
tags:
- Coding Agent
- Steerability
- Scalable Oversight
- Backdoor Detection
- LLM Security
one_liner: 将传统软件工程约束迁移到编码Agent，小模型后门检测召回从54.5%升至90.9%
practical_value: '- 落地内部代码生成Agent的电商/推荐团队，可直接复用这套约束规范：严格lint/类型检查+模块不变量写入docstring，无需复杂Agent脚手架即可大幅降低代码审核成本

  - 做Agent安全监管的场景，可借鉴轻量CLI投影设计：用200行以内的AST解析工具按需提取函数/模块契约，无需喂全量代码给审核模型，降低上下文消耗

  - 弱模型监管强模型的场景，可复用多轮单视角审查范式：每轮仅检查一个维度（自洽性/契约合规/副作用），小模型也能达到高召回，无需依赖大模型审核

  - 工程层面Agent运行环境可参考隔离方案：用nftables做内核层网络限制+推理请求拦截代理，比单纯容器沙箱更安全，适配单用户开发场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
编码Agent代码生产能力快速提升后，人工/模型审核成为高风险落地场景的核心瓶颈。无约束Agent会引入安全漏洞、导致代码架构腐化，且现有Agent脚手架token开销高；受限于上下文长度限制，审核方无法加载全量代码库做全局校验，而传统软件工程团队落地数十年的准入控制、编码规范等方案已经被验证可解同类问题。
### 方法关键点
- 强制约束层：三层不可绕过的约束，1）环境隔离：VM/容器沙箱+内核级网络白名单+推理请求拦截代理，阻断prompt注入、数据泄露风险；2）代码规范：lint/类型检查/运行时契约校验/纯逻辑与执行层代码拆分，所有规则由工具强制校验，不依赖prompt提示；3）文档规范：模块级不变量直接写入对应docstring，而非集中式架构文档，保证审核上下文就近可见
- 轻量工具：200行以内的docs CLI，基于AST解析按需提取模块API、函数签名与注释，无需加载全量代码，降低审核模型上下文消耗
- 审核范式：多轮单视角审查，每轮仅验证一个维度（自洽性/IO契约合规/副作用/不变量遵守），降低小模型认知负载
### 关键实验
基于500行的Python LM评估代码库，插入11个分层后门（语法/语义/跨文件/模块不变量/全局不变量），采用8B级小模型Gemma 4 e4b作为审核方。对比无约束无工具的基线，仅加CLI后门召回率达81.8%，仅加约束召回率达81.8%，约束+CLI组合召回率达90.9%，精度保持95.7%。
### 核心结论
Prompt是建议性的，只有工具强制落地的约束不可绕过；面向人类工程师的软件工程治理方案，可直接迁移到编码Agent场景，成本远低于复杂的Agent脚手架。
