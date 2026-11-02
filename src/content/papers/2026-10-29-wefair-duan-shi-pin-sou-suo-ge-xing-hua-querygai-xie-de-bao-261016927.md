---
title: 'WeFair: Fidelity-Aware Alignment from Human Feedback for Personalized Query
  Rewriting in Short-Video Search'
title_zh: WeFair：短视频搜索个性化Query改写的保真感知人类反馈对齐框架
authors:
- Yingtao Ren
- Aolin Li
- Cheng Cheng
- Huiyun Hu
- Huasheng Liang
- Baoxing Xie
- Jun Yuan
- Haijun Wu
- Yiwei Fu
- Chenxing Wang
affiliations:
- Weixin Group, Tencent
- East China Normal University
arxiv_id: '2610.16927'
url: https://arxiv.org/abs/2610.16927
pdf_url: https://arxiv.org/pdf/2610.16927
published: '2026-10-29'
collected: '2026-11-02'
category: QueryRec
direction: 个性化Query改写 · 人类反馈分层对齐
tags:
- Query Rewriting
- Human Feedback Alignment
- DPO
- GRPO
- Short-video Search
- Personalization
one_liner: 提出三阶段保真感知对齐框架，训练轻量模型实现低时延低漂移的短视频搜索个性化Query改写
practical_value: '- 小模型对齐可采用「低保真SFT打基础→中保真DPO做偏好→高保真GRPO做约束」的分层训练范式，兼顾泛化性和准确性，避免引入额外辅助奖励带来的信号噪声

  - 个性化Query改写场景可直接复用数据集构建流程：从搜索会话挖掘用户改写/保留行为，通过规则过滤+多LLM majority vote筛选高保真样本，大幅降低标注成本

  - 工程落地可选择2B参数量的小模型，在精度接近4B模型的同时，单样本推理时延仅0.316s，P95 latency 81ms，完全满足搜索场景严苛时延要求，改写结果可同时对接缓存召回和向量召回两路提升业务效果'
score: 10
source: huggingface-daily
depth: full_pdf
---

### 动机
短视频搜索场景下用户输入Query常存在歧义，需要结合用户上下文做个性化改写，现有基于LLM的方案要么大模型时延过高无法落地，要么小模型对齐时过度依赖消费反馈，容易出现意图漂移（如用户搜「可丽饼」推食谱而非想要的吃播内容），同时还要精准判断改写/保留时机，现有方案难以兼顾效果、时延和意图保真度。

### 方法关键点
- 数据层：从搜索会话挖掘三类样本池（上下文到Query池、用户改写池、保留原Query池），经规则过滤+3个LLM majority vote筛选，确保样本符合意图连续性、信息增益、上下文支撑三个要求
- 训练层：三阶段分层对齐，第一阶段课程SFT：先做上下文到Query预测，再做带CoT的改写推理，最后做直接改写/保留预测，打牢基础能力；第二阶段DPO：基于用户后续消费行为构造偏好对，优化改写结果的消费匹配度；第三阶段GRPO：仅奖励和人类真实改写/保留标签完全匹配的结果，严格约束意图漂移，不引入任何辅助相似性/奖励模型信号
- 推理层：模型直接输出改写结果或保留标记，无额外CoT开销，改写结果同时对接缓存召回和向量召回，排名时结合原Query和改写Query的相关性加权

### 关键结果
离线测试用4周微信搜索日志训练，3天数据做测试，对比DeepSeek-V4、Gemini-3.1、WeWrite、AWHCP等基线，2B参数量的WeFair整体准确率达72.81%，意图漂移率仅5.36%（为同类基线的1/3），单样本推理时延0.316s；10天线上A/B测试，CTR相对提升2.951%，有效播放率提升2.593%，用户主动改写率下降2.35%，目前已落地微信短视频搜索，日处理超1亿次Query。

### 核心结论
小模型对齐阶段不需要追求所有环节监督信号都高保真，低保真广覆盖样本打基础，高保真严格信号做最终约束，就能实现效果和效率的最优平衡。
