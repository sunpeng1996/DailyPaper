---
title: 'ReflectRec: Cycle-Consistency Preference Verification for LLM-based Recommendation'
title_zh: ReflectRec：面向LLM推荐的循环一致性偏好验证框架
authors:
- Dae Kyoo Kim
- Heejung Cho
- Sungmoo Hong
- Eunil Park
affiliations:
- Sungkyunkwan University
- NAVER Corp.
- KIAT
- KT Corp.
- Jaume I University
arxiv_id: '2611.23969'
url: https://arxiv.org/abs/2611.23969
pdf_url: https://arxiv.org/pdf/2611.23969
published: '2026-11-18'
collected: '2026-11-19'
category: GenRec
direction: 生成式推荐 · LLM偏好自验证
tags:
- LLM4Rec
- Cycle-Consistency
- Preference Verification
- Forward-Look RAG
- Sequential Recommendation
one_liner: 通过偏好-历史循环一致性验证+相似用户前瞻召回提升LLM推荐效果
practical_value: '- 可复用「偏好-历史循环一致性验证」思路：用生成的偏好反向召回用户历史交互的召回率作为偏好质量量化指标，替代不可靠的LLM自评分，避免幻觉偏好影响下游排序。

  - 分桶优化技巧可直接落地：按ValScore将用户分为4个桶，仅ValScore<0.4的低质量偏好触发最多2次温度0.5的重生成，中高质量偏好叠加相似用户前瞻RAG
  hints，不同模块收益互补无冲突。

  - 偏好生成Prompt可直接复用：要求LLM按品类专属语义维度（如电商的规格、兼容性、品牌、价位、形态）生成偏好，禁止提及历史商品名，保证偏好与原始历史信息互补。

  - 前瞻RAG设计可迁移：从训练数据构造「n个历史交互+后续m个真实交互」的片段池，用用户历史embedding匹配相似片段，将后续交互作为协同hint注入排序Prompt，需增加引导语句避免LLM将hint视为噪声。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有CoT式LLM推荐pipeline先生成用户偏好描述再排序，但存在两个核心缺陷：一是生成的偏好无校验机制，幻觉偏好会大幅拉低下游排序效果；二是推理仅依赖单用户历史，缺失传统推荐的协同信号，LLM长上下文注意力衰减会进一步放大该问题。

### 方法关键点
1. 循环一致性偏好验证：将生成的偏好输入LLM，从包含用户真实历史+随机负样本的50个候选中选出用户历史交互，用召回率作为ValScore衡量偏好质量，同时承担质量度量、重生成门控、重生成结果选择、分桶分析4个作用。
2. 条件重生成：ValScore<0.4的低质量偏好触发最多2次、温度0.5的重生成，选得分最高的偏好作为最终输入。
3. 前瞻召回：从训练集构造「5个历史交互+后续5个真实交互」的片段池，用BGE embedding匹配与当前用户历史最相似的Top10片段，把后续交互作为协同hint注入排序Prompt，同时增加引导语句强化LLM对hint的重视。
4. 语义偏好Prompt设计：要求LLM按品类专属维度生成60-100词偏好，禁止提及具体历史商品名，保证偏好信息与原始历史互补。

### 关键结果
在MovieLens-100K、MovieLens-1M、Amazon Electronics三个数据集测试，对比CoT4Rec-ICL基线，Hit@10分别提升16.25pp、4.46pp、3.07pp；效果在Qwen3-30B、Qwen2.5-72B、Llama-3.3-70B三个基座上均稳定正向；低质量偏好桶重生成可提升Hit@10约2.48pp，前瞻召回可提升Hit@10约3.3-3.5pp。

### 最值得记住的一句话
LLM推荐的中间偏好质量可通过可落地的循环一致性召回率量化，偏好校验优化和协同信号注入的收益互补，远好于单一模块优化。
