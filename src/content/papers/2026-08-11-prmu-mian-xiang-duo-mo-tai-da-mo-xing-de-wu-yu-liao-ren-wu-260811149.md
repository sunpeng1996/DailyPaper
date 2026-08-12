---
title: 'PRMU: A Corpus-Free Benchmark for Person-Centric Knowledge Unlearning in Multimodal
  Large Language Models'
title_zh: PRMU：面向多模态大模型的无语料人物知识遗忘基准
authors:
- Huafeng Chen
- Yueming Lyu
- Ziyuan Chen
- Wenda Tan
- Chenyang Si
- Liucheng Guo
- Caifeng Shan
affiliations:
- School of Intelligence Science and Technology, Nanjing University
- Department of Computing, Imperial College London
arxiv_id: '2608.11149'
url: https://arxiv.org/abs/2608.11149
pdf_url: https://arxiv.org/pdf/2608.11149
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: 多模态大模型 · 知识遗忘评估与优化
tags:
- Multimodal LLM
- Knowledge Unlearning
- Benchmark
- Parameter Editing
- Corpus-Free
one_liner: 提出无语料多模态人物知识遗忘基准PRMU及轻量基线方法SGPE
practical_value: '- 电商多模态应用（如图文生成、用户画像建模）可复用SGPE无语料参数编辑方案，无需回溯原始训练数据即可定向删除指定人物隐私知识，满足合规要求

  - 多模态模型迭代时可借鉴PRMU的「对抗探针+细粒度局部性分析」评估框架，验证定向遗忘操作是否误伤正常业务能力

  - SGPE采用的相似度门控、参数空间保护设计，相比全量重训成本大幅降低，适合业务侧快速响应隐私删除诉求'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态大模型（MLLM）知识遗忘方法依赖原始遗忘/保留语料，实际场景中用户隐私删除请求通常无法获取对应训练数据，缺乏适配真实场景的评估基准与低成本落地方案。
### 方法关键点
1. 提出PRMU基准，针对自然习得的人物类知识，通过文本+视觉多维度探针、对抗评估、细粒度局部性分析，同时衡量定向遗忘效果与非目标知识保留度
2. 提出轻量无语料遗忘基线SGPE，包含知识置换、受保护参数空间编辑、局部感知多模态控制三个核心模块
### 关键结果
现有遗忘方法在强遗忘设置下局部知识保留率下降40%以上，且易被多模态输入重新激活已遗忘知识；SGPE在目标遗忘率、局部知识保留率、通用多模态性能三个维度取得最优trade-off，相比基线方法局部性损失降低28%
