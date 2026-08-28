---
title: 'MMJailBench: A Factorized Benchmark for Disentangling Multimodal Jailbreak
  Vulnerabilities'
title_zh: MMJailBench：面向多模态大模型越狱漏洞拆解的因子化基准
authors:
- Tianshi Wang
- Jingsong Wang
- Yafei Huang
- Fengling Li
- Xin Li
- Lei Zhu
affiliations:
- Tongji University
- Mohamed bin Zayed University of Artificial Intelligence
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2608.25490'
url: https://arxiv.org/abs/2608.25490
pdf_url: https://arxiv.org/pdf/2608.25490
published: '2026-08-26'
collected: '2026-08-28'
category: Eval
direction: 多模态大模型安全评测
tags:
- MLLM
- Jailbreak
- Evaluation Benchmark
- Safety Alignment
- Multimodal
one_liner: 构建因子化多模态大模型越狱评测基准，支持漏洞来源定位与低成本规模化审计
practical_value: '- 搭建多模态Agent/LLM业务服务时，可复用该基准的因子化漏洞归因方法，定位多模态交互环节的安全风险点

  - 多模态内容审核场景，可借鉴核心结论优先做prompt framing维度的风险拦截，其次管控权威类视觉语义的输入

  - 业务侧做MLLM安全对齐时，可优先覆盖高风险危害域，避免现有对齐覆盖不均导致的合规风险

  - 内部多模态模型安全评测可直接使用该工具包的轻量化配置，大幅降低审计成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态越狱评测将有害意图、prompt构造、视觉语义、指令载体等因素耦合，无法准确定位漏洞来源，MLLM落地的安全风险难以量化归因。
### 方法关键点
构建因子化基准MMJailBench，在控制变量下组合四类影响因素，支持细粒度漏洞的因子级归因；配套模块化评测套件，支持全量/轻量化配置、多评判标准、多维度指标。
### 关键结果
对16款开源、闭源MLLM评测显示，漏洞分布高度异构且依赖模型本身；不同危害域越狱风险差异显著，当前多模态安全对齐覆盖不均；prompt构造是漏洞差异的核心来源，任务相关视觉语义会提升越狱概率，权威类视觉线索风险最高，视觉渲染指令相对文本指令未稳定提升越狱风险。
