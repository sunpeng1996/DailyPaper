---
title: 'VIBE: A VAD-Informed Benchmark for Entity-Centered Affective Profiling of
  Large Language Model Outputs'
title_zh: VIBE：基于VAD的大模型输出实体中心情感特征评测基准
authors:
- Andrei Chetvergov
- Alexander Evseev
- Timofei Sivoraksha
- Stepan Ukolov
- Mikhail Solovev
- Danil Sazanakov
- Sergey Bolovtsov
affiliations:
- RANEPA (Russian Presidential Academy of National Economy and Public Administration)
arxiv_id: '2608.03810'
url: https://arxiv.org/abs/2608.03810
pdf_url: https://arxiv.org/pdf/2608.03810
published: '2026-08-04'
collected: '2026-08-06'
category: Eval
direction: LLM实体情感评测 · VAD画像基准
tags:
- VAD
- LLM Evaluation
- Affective Profiling
- Benchmark
- Entity Analysis
one_liner: 提出整合目标导向VAD归因、评分契约、情感护照的LLM实体中心情感评测基准VIBE
practical_value: '- 可复用VAD三维情感度量框架替代单一sentiment评分，更精准刻画商品/品牌/达人在UGC、LLM生成文案中的用户感知，高唤醒高优势属性的主体可优先匹配爆点营销场景

  - 实体定向VAD与全局响应VAD拆分的思路，可用于AIGC文案生成效果校验，避免整体文案情感正向但提及的目标商品/品牌情感负面的错误

  - 情感护照附带评分规则、上下文元数据的报告形式，可迁移到AIGC营销文案合规审核的全链路溯源场景'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM情感评测仅覆盖sentiment、好感度等单维度，未整合目标导向VAD归因、明确评分契约、标准化报告格式，无法完整刻画实体在LLM输出中的多维度情感框架。
### 方法关键点
提出VIBE评测基准，核心为标准化测量契约：拆分生成与外部评分流程，区分标量好感度、全局响应VAD、实体定向VAD三类任务，最终输出附带评分身份、覆盖范围、协议、解释限制的Affective Passport报告。
### 关键结果数字
1. 标量好感度无法覆盖唤醒度、优势度：效价维度人机相关度达0.944、标注者间相关度达0.954；唤醒度、优势度为方向估计而非精确值，标注者间相关度分别为0.495、0.702；
2. 同一文本的全局VAD与实体定向VAD存在显著差异，需单独度量；
3. 诱导条件会大幅改变情感画像，必须在报告中附带上下文元数据。
