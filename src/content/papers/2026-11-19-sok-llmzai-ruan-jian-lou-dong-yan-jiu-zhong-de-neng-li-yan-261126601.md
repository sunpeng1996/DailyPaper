---
title: 'SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research'
title_zh: SoK：LLM在软件漏洞研究中的能力演进评估
authors:
- Amine Lbath
- Manan Suri
- Aurelien Delaitre
- Vadim Okun
- Massih-Reza Amini
- Dinesh Manocha
affiliations:
- National Institute of Standards and Technology
- Université Grenoble Alpes, CNRS
- University of Maryland, College Park
arxiv_id: '2611.26601'
url: https://arxiv.org/abs/2611.26601
pdf_url: https://arxiv.org/pdf/2611.26601
published: '2026-11-19'
collected: '2026-11-21'
category: Agent
direction: LLM Agent 能力分级与安全领域应用
tags:
- LLM Agent
- Capability Evaluation
- Autonomy Level
- Vulnerability Research
one_liner: 提出类自动驾驶的能力分级框架，系统梳理LLM Agent在漏洞研究领域的能力演进与产业影响
practical_value: '- 可复用类自动驾驶的自主能力分级框架，用于业务Agent（如运营自动化、智能客服）的自治度分层，实现不同方案的横向对比

  - 参考其证据强度校验方法，评估业务中LLM应用的效果可信度，避免能力高估

  - 涉及代码生成/修复类业务工具（如平台规则自动审计Agent），可复用其能力验证指标指导迭代'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM Agent在软件漏洞发现、验证、修复场景的能力宣称分散在论文、厂商报告中，缺乏统一可对比的评估标准，无法准确衡量能力演进趋势与实际影响。

### 方法关键点
1. 参考自动驾驶自动化分级思路，设计LLM Agent漏洞研究能力的自主等级评估框架，从正确性、可用性、证据强度三个维度校验相关能力宣称。
2. 基于框架系统梳理公开研究证据，结合十年公共漏洞记录、披露与利用数据，测算LLM能力演进的产业影响。

### 关键结果数字
2026年公开漏洞数量翻倍，严重/高危漏洞占比持续提升，已留存十年以上的存量严重漏洞发现效率提升数倍；当前漏洞生命周期各阶段（从上报到修复、披露到被利用）时长暂未出现明显变化。
