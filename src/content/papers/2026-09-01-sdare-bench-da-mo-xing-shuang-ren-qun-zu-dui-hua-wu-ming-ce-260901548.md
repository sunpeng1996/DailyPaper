---
title: 'SDARE-Bench: Evaluating Large Language Models on Conversational Stigma Detection
  and Response in Dyadic and Group Dialogue'
title_zh: SDARE-Bench：大模型双人/群组对话污名检测与响应能力评估基准
authors:
- Stephanie Fong
- Yiwen Jiang
- Zimu Wang
- Hongxi Yang
- Yaling Shen
- Hiu Weh Naomi Chow
- Heung Ying Lai
- Xiangyu Zhao
- Qingyang Xu
- Zhongxing Xu
affiliations:
- Monash University
- University of Liverpool
- University of Edinburgh
- Federation University
- Orygen, The University of Melbourne
arxiv_id: '2609.01548'
url: https://arxiv.org/abs/2609.01548
pdf_url: https://arxiv.org/pdf/2609.01548
published: '2026-09-01'
collected: '2026-09-03'
category: Eval
direction: LLM安全评估 · 对话污名检测与响应
tags:
- LLM Safety
- Evaluation Benchmark
- Conversational AI
- Stigma Detection
- Dialogue System
one_liner: 推出首个覆盖双人/群组对话的污名化检测与响应基准SDARE-Bench，揭示LLM在复杂社交场景的安全脆弱性
practical_value: '- 做电商/社群服务Agent时，可复用该基准的双人/群组场景构造思路，测试Agent在多人诱导、偏见引导下的合规回复能力，避免输出歧视性内容

  - LLM安全对齐阶段可参考该基准的场景差异结论，补充群组压力下的对抗训练样本，提升Agent抗污名诱导的鲁棒性

  - 做UGC/社群内容审核算法时，可借鉴基准的污名检测标注框架，优化污名内容的识别召回率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM通用评估依赖静态prompt与固定格式任务，忽略对话上下文与受众效应，缺乏针对对话场景的污名化检测与响应能力的专用基准。
### 方法关键点
推出首个场景化对话污名评估基准SDARE-Bench，包含1138条双人对话查询、1388条群组对话，支持污名检测、开放式响应生成两类任务，使用基于1392条人工标注响应训练的分类器实现自动评估。
### 关键结果
8款主流LLM普遍存在污名成分识别能力不足问题，群组场景下表现更差；开放式响应中群组场景的污名输出率远高于双人场景，抗污名能力更弱、不合理建议占比更高；构造的群组压力场景下，LLM污名表达率平均高达97.5%，验证复杂社交场景下存在显著安全漏洞。
