---
title: 'MiniVer-V: Identifying Minimal Sufficient Evidence for Short Video Verification'
title_zh: 'MiniVer-V: 短视频事实核验的最小充分证据识别'
authors:
- Leran Chen
- Lingnan Kong
- Zile Cai
affiliations:
- The University of Sydney
arxiv_id: '2610.11233'
url: https://arxiv.org/abs/2610.11233
pdf_url: https://arxiv.org/pdf/2610.11233
published: '2026-10-08'
collected: '2026-10-09'
category: Multimodal
direction: 多模态事实核验 · 证据高效筛选
tags:
- Multimodal Reasoning
- Fact Checking
- Evidence Selection
- Benchmark
- Sufficiency Driven
one_liner: 提出最小充分证据驱动的短视频核验框架与多模态基准，仅用16%证据达到与全量证据相当的精度
practical_value: '- 电商短视频虚假宣传核验场景可复用「内外部证据分层校验+充分性阈值终止搜索」框架，降低RAG检索与LLM调用成本

  - 高成本LLM推理场景可借鉴最小充分证据选择逻辑，无需喂入全量上下文，仅用16%证据即可达到等价效果，大幅降本

  - 信息校验类Agent可加入「证据不足主动弃权」逻辑，避免强制输出错误结论，提升输出可靠性'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
短视频事实核验现有方案要么喂入全量证据引入噪声，要么按相关性选证据混淆相关性与充分性，存在冗余高、无证据不足弃权机制的问题。
### 方法关键点
1. 发布MiniVer-V多模态基准，含195条短视频、5510条涵盖关键帧、语音转写、网页检索结果的多模态证据单元，支持三分类标注（支持/反驳/证据不足）；
2. 提出两层核验框架：先基于内部证据校验声明与视频一致性，再引入外部证据完成事实判定；
3. 设计充分性驱动的贪心搜索策略：证据凑够阈值就停止检索，证据池耗尽则输出「不足」而非强制出结论。
### 关键结果
用Claude Sonnet 4时，平均仅用4.5条证据（占全量的16%），Macro-F1达0.510，与全量证据基线的0.518无统计显著差异，同时证据不足案例识别效果显著优于无弃权机制的方案；效果在GPT-5.5上可复现，Qwen2.5-72B上部分生效。消融实验证明外部证据对事实判定不可或缺，内部证据保障声明与视频一致性。
