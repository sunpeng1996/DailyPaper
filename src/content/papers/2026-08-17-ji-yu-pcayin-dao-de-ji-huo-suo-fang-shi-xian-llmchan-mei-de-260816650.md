---
title: PCA-guided Activation Scaling for Monotonic Bidirectional Control over LLM
  Sycophancy
title_zh: 基于PCA引导的激活缩放实现LLM谄媚性的单调双向调控
authors:
- Zheng Chen
- Zhaoxin Feng
- Yip Tin Po
- Jianfei Ma
- Emmanuele Chersoni
- Bo Li
affiliations:
- The Hong Kong University of Science and Technology
- The Hong Kong Polytechnic University
arxiv_id: '2608.16650'
url: https://arxiv.org/abs/2608.16650
pdf_url: https://arxiv.org/pdf/2608.16650
published: '2026-08-17'
collected: '2026-08-18'
category: LLM
direction: LLM对齐 · 激活干预行为调控
tags:
- Activation Steering
- PCA
- Sycophancy
- LLM Alignment
- Inference Control
one_liner: 通过PCA激活空间分解与非对称缩放实现LLM谄媚性的单调双向可控调节
practical_value: '- 电商Agent/智能客服场景可复用PAS框架灵活调节顺从度：售后场景调高诚实性避免误导用户，情感陪伴场景适当调高顺从度提升用户体验

  - 激活干预思路可迁移到推荐系统LLM排序模块：用PCA提取用户偏好/合规相关激活子空间，通过缩放参数动态调整个性化与合规性的平衡

  - 小样本构造思路可复用：仅需200组正负对比样本即可提取有效调控子空间，无需全量重训，适配业务快速迭代需求

  - 非对称缩放trick值得借鉴：对核心子空间和残差分别设置不同缩放指数，兼顾调控强度与稳定性，避免极端参数下输出退化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM普遍存在sycophancy（谄媚性），即无条件认同用户观点而忽略事实正确性，完全消除该特性可能导致模型过度对抗、拒绝用户合理观点；现有调控方法无法保证调控强度与行为输出的双向单调映射，参数调整效果不可预测，无法适配不同场景下的顺从度动态需求。

### 方法关键点
- 构造200组对比样本对：保持输出后缀完全一致，仅调整选项顺序与用户偏好指向，分离谄媚与诚实回答的激活差异，避免token层面的干扰
- 对残差流激活差异做PCA分解，得到K维谄媚-诚实子空间与正交残差分量，通过AUC指标自动选择最优中间层与子空间维度
- 推理时对PCA子空间分量缩放β²、残差分量缩放β，β<1时放大谄媚性，β=1恢复原生输出，β>1时提升诚实性，仅需调整单个参数即可实现连续调控

### 关键实验
在Llama3.1-8B、Qwen2.5-7B、Gemma2-9B三个开源模型，NLPClaim、Feedback、MATH三个数据集上测试，对比CAA、Angular Steering、Conceptor、Few-shot四个基线：PAS的Spearman单调相关系数达+0.92（基线平均仅-0.05），四个调控方向平均行为偏移量15.4%（基线平均8.7%），且子空间可迁移到开放生成场景，单调相关系数仍达+0.94。

### 核心结论
对于多维度的复杂行为调控，基于子空间分解的非对称激活缩放远优于单向量加减的activation steering方法，可实现可预测的连续双向控制。
