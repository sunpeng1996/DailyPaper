---
title: 'AISPA: User-Centric System Prompt Auditing for Large Language Model Applications'
title_zh: AISPA：面向LLM应用的以用户为中心的系统提示词审计框架
authors:
- Xiangning Lin
- Shenzhe Zhu
- Shu Yang
- Zhenyu Zhang
- Haoqian Zhang
- Yipeng Zhao
- Chengxuan Qian
- Tianwei Wang
- Ziheng Zhang
- Zhenlong Yuan
affiliations:
- Stanford University
- CMU
- UT Austin
- University of Toronto
- MIT
arxiv_id: '2607.28617'
url: https://arxiv.org/abs/2607.28617
pdf_url: https://arxiv.org/pdf/2607.28617
published: '2026-07-30'
collected: '2026-08-01'
category: Eval
direction: LLM系统提示词用户导向审计评估
tags:
- System Prompt
- Auditing Framework
- LLM Application
- User Protection
- Prompt Governance
one_liner: 提出用户导向的系统提示词审计框架AISPA，完成88款商用AI产品3249条指令审计并披露核心发现
practical_value: '- 做Agent/LLM驱动的电商导购、智能客服产品时，可复用AISPA的8维度评估体系自查系统提示词的用户保护合规性，规避监管与用户投诉风险

  - 系统提示词设计可参考审计结论，优先覆盖身份透明、信息真实、隐私保护等高频用户关切维度，同时避免同一prompt内同时出现保护和侵害用户利益的矛盾指令

  - 面向合规需求的团队，可参考AISPA的分级分类方法搭建自有系统prompt审计流程，快速批量排查问题指令'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
商用AI产品的系统提示词由开发者定义、控制大模型行为，普遍不对外公开，导致AI落地存在严重的信任与问责缺口，缺乏统一的用户视角审计标准。
### 方法关键点
提出AISPA审计框架，从身份透明、信息真实、隐私保护、安全合规、用户控制权、有害请求处理、伤害预防、公平包容8个用户关切维度，对系统提示词的指令逐段评估，区分保护性指令（维护用户利益）与问题指令（损害用户利益）。
### 关键结果数字
完成88款商用AI产品的3249条系统指令审计，核心发现：① 不同产品的提示词设计差异极大，单产品保护性指令数区间为<5到>60；② 98.9%的产品至少含1条保护性指令，但仅24%覆盖全部8个维度；③ 近年系统提示词长度持续增长、保护性提升，但仍有40%的产品存在至少1条问题指令，且同一prompt内常同时存在保护与问题指令。
