---
title: 'OpenFrontiers: A Collection of Open Research Problems and a Benchmark for
  Scientific Rediscovery'
title_zh: OpenFrontiers：开放研究问题集合与科学再发现基准
authors:
- Jiarui Yao
- Ruida Wang
- Tong Zhang
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2610.37739'
url: https://arxiv.org/abs/2610.37739
pdf_url: https://arxiv.org/pdf/2610.37739
published: '2026-10-26'
collected: '2026-11-07'
category: Eval
direction: LLM科研能力评估 · 基准数据集构建
tags:
- LLM Evaluation
- Scientific Agent
- Benchmark Dataset
- Formal Verification
- Open Research Problem
one_liner: 构建跨学科开放研究问题语料与数学再发现基准，支持LLM科研能力标准化评估
practical_value: '- 做Agent能力评估可复用三级范式（闭卷/冻结检索/联网检索），精准区分原生推理能力和检索增益，可直接迁移到电商选品、营销文案生成等Agent的原创性评测

  - 构建业务场景测试集时，可参考双独立人工审核+自动化探针校验的质量控制流程，大幅降低标注噪声，提升基准集可靠性

  - 结论显示联网检索成功多来自已有方案复用，做业务Agent时需针对性设计无检索可用场景下的推理增强模块，避免仅依赖RAG的能力短板'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM在科研级问题解决上表现出巨大潜力，但缺乏体系化的开放研究问题集合，针对LLM科研能力的标准化评估存在较大难度。
### 方法关键点
1. 构建包含12151个跨学科开放研究问题的结构化语料，覆盖问题描述、上下文、研究进展等维度信息
2. 搭建数学领域科学再发现基准，含200道问题（110道2026年已解决、90道仍开放），所有问题均对应经自动化探针和双独立审核校验的Lean4形式化表述，同时筛选出高质量子集HQ-50
3. 设计闭卷、冻结检索、联网检索三级评估协议，在隔离沙箱中通过双独立校验器对形式化证明结果自动打分
### 关键结果数字
7款LLM Agent在HQ-50子集测试中，闭卷场景下最多仅能复现40道已解决问题中的7道，联网检索场景的成功结果80%以上来自对已公开解决方案的直接召回
