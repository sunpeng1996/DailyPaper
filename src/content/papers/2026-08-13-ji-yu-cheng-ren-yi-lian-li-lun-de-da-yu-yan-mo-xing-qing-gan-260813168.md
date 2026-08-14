---
title: Which LLM Is Your Ideal Companion? Evaluating Emotional Companion Capabilities
  of LLMs Based on Adult Attachment Theory
title_zh: 基于成人依恋理论的大语言模型情感陪伴能力评估
authors:
- Junkai Zhou
- Shiting Guan
- Zhaoyi Zhang
arxiv_id: '2608.13168'
url: https://arxiv.org/abs/2608.13168
pdf_url: https://arxiv.org/pdf/2608.13168
published: '2026-08-13'
collected: '2026-08-14'
category: Eval
direction: 大模型评估 · 情感陪伴能力测评
tags:
- LLM
- Evaluation
- Emotional Companion
- Benchmark
- ECR-R
- Prompt Engineering
one_liner: 引入成人依恋理论搭建ECBench测评基准，量化32款LLM的情感陪伴能力与依恋倾向
practical_value: '- 搭建客服/陪伴类Agent时，可复用ECR-R量表测试LLM依恋倾向，匹配不同用户群体的情感需求（如高焦虑用户优先选低回避高支持的模型）

  - 电商售后安抚、会员专属陪伴等高情感交互场景，可参考ECBench的4类场景+11项对话质量指标搭建自有模型测评体系

  - 业务中可通过prompt快速调控LLM的依恋倾向，无需微调即可适配不同情感场景的交互要求，降本提效'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM评估多聚焦通用人格特质刻画，无法有效反映模型在亲密、高情感敏感场景下的行为表现，随着LLM在情感陪伴类场景的落地，亟需针对性的能力评估体系。
### 方法关键点
1. 引入心理学成人依恋理论，采用ECR-R量表从依恋焦虑、依恋回避两个维度量化LLM的情感倾向
2. 构建ECBench测评基准，覆盖友谊、恋爱两类关系下的情感支持、协作任务、冲突解决、社交引导4类真实交互场景
3. 采用11项对话质量指标+3种评估方法，完成32款LLM的依恋倾向测评，同时验证prompt对依恋倾向的调控效果
### 关键结果
完成32款主流LLM的依恋倾向图谱绘制，证实可通过prompt有效调整LLM的情感陪伴行为，适配不同场景需求
