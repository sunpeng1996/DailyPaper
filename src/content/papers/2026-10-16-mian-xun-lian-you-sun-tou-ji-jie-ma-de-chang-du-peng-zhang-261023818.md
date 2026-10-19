---
title: 'Acceptance Is Not Speed: Length Inflation in Training-Free Lossy Speculative
  Decoding'
title_zh: 免训练有损投机解码的长度膨胀问题：接受率不等于实际推理速度
authors:
- Chiatzen Wang
- Bill Xu
- Haochen Gu
- Hongyang Zhang
affiliations:
- University of Waterloo
arxiv_id: '2610.23818'
url: https://arxiv.org/abs/2610.23818
pdf_url: https://arxiv.org/pdf/2610.23818
published: '2026-10-16'
collected: '2026-10-19'
category: LLM
direction: LLM推理加速 · 投机解码优化
tags:
- speculative_decoding
- lossy_verification
- inference_optimization
- length_inflation
- decoding_speed
one_liner: 揭示免训练有损投机解码的长度膨胀现象，指出接受率不能直接作为速度指标
practical_value: '- 评估投机解码加速效果不要只看单轮接受率，必须同时统计生成长度、验证轮数、端到端耗时，避免误选实际变慢的方案

  - 生成商品文案、客服回答等对精度要求高的场景，优先选spec_casc_tok规则，精度损失可忽略的前提下可获得约14%的端到端提速

  - 用带思考链的LLM做导购理由生成、营销方案推导等场景，可在接近生成预算时强制关闭思考块，实验中答案正确率从11%提升到39%

  - 采用EAGLE系列专属drafter时要额外监控长度膨胀，这类模型平均膨胀率达1.23倍，远高于独立小drafter的0.94倍，可通过限制最大生成长度抵消影响'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
免训练有损投机解码过去普遍用单轮接受token数作为速度指标，默认输出分布与原模型一致，但宽松验证规则会改变输出分布，导致生成长度异常变化，隐藏实际效率损失，尤其对长推理链场景影响极大，现有研究未系统量化该问题。

### 方法关键点
- 提出长度修正的速度计算公式，将生成长度膨胀率纳入评估，修正公式为 $S_{relax} ≈ S_{lossless} × \frac{\bar{L}_{lossless}}{\bar{L}_{relax}}$
- 将5种主流免训练宽松验证规则（CACTUS、mentored decoding、rFSD、spec_casc_opt、spec_casc_tok）统一适配到同一框架，按相同接受长度而非超参数对齐对比
- 实验覆盖12组target-drafter组合（含4个主流LLM、8个专属drafter、3个独立小drafter），跨数学、代码、聊天、长上下文6类基准数据集，共360组实验单元格

### 关键结果
- 宽松验证平均单轮接受token数比无损版本高1.34倍，但平均生成长度膨胀达1.54倍，大部分场景下加速收益被完全抵消，甚至反而变慢
- 仅spec_casc_tok规则精度损失可忽略（平均下降0.005），生成长度膨胀率仅0.96，验证轮数比无损版本少14%
- 针对带思考链的场景，在接近生成预算时强制关闭思考块，可将答案正确率从11%提升到39%

**最值得记住的一句话**：有损投机解码的单轮接受率不是可靠的速度指标，必须同时上报生成长度和验证轮数才能评估实际效率。
