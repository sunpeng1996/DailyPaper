---
title: Does a model's stated reason for rejecting a candidate do any work?
title_zh: 大语言模型拒绝候选项的声明理由是否真的影响决策？
authors:
- Archit Rastogi
affiliations:
- Independent Researcher
arxiv_id: '2609.30151'
url: https://arxiv.org/abs/2609.30151
pdf_url: https://arxiv.org/pdf/2609.30151
published: '2026-09-24'
collected: '2026-09-25'
category: LLM
direction: 大模型可解释性 · 决策理由保真度验证
tags:
- LLM
- Explainability
- Faithfulness
- Decision Validation
- Measurement Validity
one_liner: 通过受控插入实验验证LLM拒绝理由同时存在内容效应与位置效应
practical_value: '- 做LLM驱动的电商推荐/广告理由生成时，需验证理由与决策的因果关联，避免生成看似合理但与实际决策无关的假理由，损害用户信任

  - 业务侧验证LLM决策逻辑时可复用本文对照设计：同位置插无关句、无关候选插相同内容，分离内容和位置混淆变量

  - LLM决策输出的解析规则必须做充分校验，本文发现17.1%的解析错误会大幅扭曲结论，推荐/搜索场景用LLM做规则解析时需加校验逻辑'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM决策的解释保真度缺乏无偏定量验证方法，无法判断模型给出的拒绝候选项理由是否真的是决策核心依据

### 方法关键点
设计三类对照实验在2WikiMultihopQA数据集上测试6款开源LLM：1）在被拒候选资料中插入模型提到的缺失事实；2）同位置插入长度匹配的无关句；3）在模型未提及的第三候选插入相同内容，通过greedy解码下的决策变化分离内容效应和位置效应，所有测量通过字符串规则校验避免解析误差

### 关键结果数字
插入对应事实使决策反转的概率是无关句的3.57倍（Holm p=0.0210）；无关句插入被拒候选的决策影响远高于插入第三候选（Holm p=0.0008）；17.1%的决策解析错误会直接导致结论偏差
