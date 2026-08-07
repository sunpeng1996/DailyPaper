---
title: 'The Low Frequency Trap: Video Language Models Fail at Simple Event Bookkeeping'
title_zh: 低频陷阱：视频语言模型在简单事件记录任务上存在明显失效
authors:
- Sarvesh Baskar
- Zikui Cai
- Shayan Shabihi
- Anirudh Satheesh
- Muhammad R. Islam
- Udari Madhushani Sehwag
- Tom Goldstein
- Furong Huang
affiliations:
- University of Maryland, College Park
- Scale AI
arxiv_id: '2608.06361'
url: https://arxiv.org/abs/2608.06361
pdf_url: https://arxiv.org/pdf/2608.06361
published: '2026-08-06'
collected: '2026-08-07'
category: Eval
direction: 多模态大模型 · 时序推理能力评估
tags:
- Video LLM
- Temporal Reasoning
- Evaluation Benchmark
- Event Counting
- Failure Analysis
one_liner: 提出带可执行事件轨迹的可控视频基准，诊断视频大模型时序事件计数的分层失效模式
practical_value: '- 做直播/短视频电商的多模态Agent事件识别时，要优先对高频瞬态事件（如弹窗、点击特效）做单独采样增强，不能依赖通用Video
  LLM原生能力

  - 评估多模态时序推理任务（如直播带货商品出现次数统计）时，不要只看最终计数准确率，要加事件级/时间戳级真值校验，避免指标虚高

  - 业务用Video LLM做时序事件统计时，优先控制事件频率≤1Hz、总数≤12，超过阈值需拆分任务或引入专用规则兜底'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有视频基准混淆事件数量、频率、视觉复杂度等变量，且仅评估最终答案准确率，无法定位Video LLM时序推理的具体失效模式。

### 方法关键点
构建含2190段可控渲染视频的基准，覆盖弹球碰墙、视觉闪烁、类别状态转换3类任务，固定渲染效果仅调整事件数量N与频率F，每段视频配套可执行事件轨迹，支持能力面估计与时间戳级细粒度评估。

### 关键结果数字
- 80%可靠性阈值下，Gemini 3.6 Flash仅能可靠计数0.5/1.0Hz下不超过12个的持续状态转换事件，对瞬态闪烁事件无可靠计数区间
- 高计数高频率场景下，最终计数准确率仅0.2%，真实事件召回率仅18.1%
- 提升采样率可将弹球任务准确率从19.6%提升至29.3%，但事件序列与真值一致率仅3.7%，存在明显指标虚高
