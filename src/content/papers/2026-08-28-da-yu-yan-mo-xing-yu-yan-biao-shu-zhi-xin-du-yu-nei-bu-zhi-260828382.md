---
title: When Linguistic and Internal Confidence Diverge in Large Language Models
title_zh: 大语言模型语言表述置信度与内部置信度的偏差研究
authors:
- Hefan Zhang
- Bingquan Zhang
- Ming Cheng
- Saeed Hassanpour
- Weicheng Ma
- Soroush Vosoughi
affiliations:
- Dartmouth College
- Oakland University
arxiv_id: '2608.28382'
url: https://arxiv.org/abs/2608.28382
pdf_url: https://arxiv.org/pdf/2608.28382
published: '2026-08-28'
collected: '2026-08-31'
category: LLM
direction: LLM可靠性 · 置信度评估与校准
tags:
- LLM Reliability
- Confidence Calibration
- Uncertainty Estimation
- LLM Deployment
- Alignment
one_liner: 系统验证LLM自报告语言置信度与内部置信度存在多维度偏差，给出部署落地诊断规则
practical_value: '- 做电商问答/Agent推理调度时，优先用内部logits/语义熵作为置信度信号；无白盒权限时必须先在业务hold-out集上验证语言置信度的有效性，再落地拒答/重推理逻辑

  - 用LLM做文案生成/多路径投票时，引导输出0-10分细粒度数值置信度而非三级粗粒度标签，可提升投票准确率约3个百分点

  - prompt设计避免加态度类引导词（如「请自信作答」），会虚高报告置信度但不提升实际准确率；few-shot示例的置信度要分散，避免输出置信度压缩无区分度

  - 快速诊断语言置信度可用性：若置信度集中在9-10分区间无方差直接弃用；若方差足够且和业务目标正相关，可用于弱排序/加权场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM落地中常依赖自报告的语言置信度做拒答、内容过滤、多轮投票决策，但现有研究多评估置信度与实际准确率的校准性，未明确自报告置信度是否和模型内部实际置信度一致，黑盒场景下过度信任语言置信度易引发幻觉漏判、决策失效等问题。

### 方法关键点
- 评估框架：从**相关性（两种置信度排序一致性）、数值一致性（绝对值差）、校准性（置信度与实际准确率匹配度）**三个独立维度评估对齐程度，避免单维度误判
- 内部置信度代理：分类任务用输出logits softmax值，生成任务用**语义熵**（采样多个输出聚类后计算的熵值，取负数作为置信度代理）
- 变量控制：覆盖不同模型家族、大小、微调类型，同时测试prompt设计、任务难度对置信度对齐的影响

### 关键结果数字
- 实例级语言置信度与内部置信度的平均Pearson相关仅0.135，对齐程度极弱；指令微调模型相关系数近乎为0，且ECE比基础模型高9.6个百分点，过自信问题更严重
- 细粒度数值置信度加权投票比多数投票准确率高5.19个百分点，比三级标签置信度高2.99个百分点
- 态度类prompt可提升报告置信度，但会降低与内部置信度的相关性，完全无对齐增益

### 最值得记住的一句话
LLM自报告语言置信度是有损传输通道，仅当分布分散且在业务场景验证有效时可用于弱排序/加权，绝对不能直接当作校准后的概率使用。
