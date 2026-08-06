---
title: 'Agogic: Performance-Timed Music Tokens for LLM-Native Text-to-Symbolic-Music
  Generation'
title_zh: Agogic：面向LLM原生文本到符号音乐生成的性能时序音乐Token方案
authors:
- Junhao Chen
- Mingjin Chen
- Jingjia Mao
- Lin Chen
- Saining Zhang
- Minglin Chen
- Ruocheng Wu
- Liaoyuan Fan
- Wenyi Li
- Mingju Gao
affiliations:
- Tsinghua University
- The Hong Kong Polytechnic University
- Nanyang Technological University
- Peking University
- SparcAI Inc.
arxiv_id: '2608.03999'
url: https://arxiv.org/abs/2608.03999
pdf_url: https://arxiv.org/pdf/2608.03999
published: '2026-08-04'
collected: '2026-08-06'
category: LLM
direction: LLM符号音乐生成 · Token化方案优化
tags:
- Tokenization
- Text-to-Music
- LLM Generation
- Controlled Evaluation
- Symbolic Representation
one_liner: 控制变量验证音乐Token化比模型规模更影响生成质量，提出PMT时序Token小模型超34倍大模型
practical_value: '- 做生成式推荐/Agent多模态生成任务时，优先迭代Token化方案而非盲目扩模型规模，同等效果下可大幅降低算力成本

  - 生成类任务中可引入轻量化解码时约束，提升指定属性匹配度（如电商商品文案关键词对齐、广告元素合规），无分布质量损失

  - 验证业务新组件（如召回表示、生成Token）增益时，严格控制其他变量（模型、数据、训练策略）才能得到可信结论'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
文本到符号音乐生成任务中，音乐Token化方案的效果长期与模型架构、训练数据、训练策略耦合，从未被单独度量，行业盲目堆叠模型规模的投入产出比不清晰。
### 方法关键点
固定预训练Qwen3.5（0.8B~27B）、训练数据、算力预算、解码策略，仅替换7种不同的音乐表示方案做对照实验，同时提出性能分辨率Token流PMT：支持10ms时序精度、单音符力度、多轨纹理，仅含609个符号。
### 关键结果数字
模型规模扩大34倍仅带来Fréchet Music Distance（FMD）微幅下降，切换Token化方案可将FMD减半；0.8B参数的PMT方案FMD达159，beat grid方案27B参数FMD仅272~286，小模型效果远超34倍大模型；解码时增加轻量化约束可将乐器F1从0.28提升至0.60、正确调性占比从0.16提升至0.35，无分布质量损失。
