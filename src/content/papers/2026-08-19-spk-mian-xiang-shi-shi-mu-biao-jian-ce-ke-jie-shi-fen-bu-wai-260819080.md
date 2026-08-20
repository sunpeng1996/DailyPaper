---
title: 'SPK: Eliciting Structured Prior Knowledge for Interpretable Out-of-Distribution
  Detection in Real-Time Object Detection'
title_zh: SPK：面向实时目标检测可解释分布外检测的结构化先验提取方法
authors:
- Changshun Wu
- Weicheng He
- Xiaowei Huang
- Saddek Bensalem
affiliations:
- University of Liverpool, UK
- Université Grenoble Alpes, France
- CSX-AI, France
arxiv_id: '2608.19080'
url: https://arxiv.org/abs/2608.19080
pdf_url: https://arxiv.org/pdf/2608.19080
published: '2026-08-19'
collected: '2026-08-20'
category: Other
direction: CV目标检测 · OOD可解释检测
tags:
- OOD Detection
- Object Detection
- Structured Prior
- Interpretability
- Real-time Inference
one_liner: 从预训练目标检测器提取结构化先验，实现SOTA级可解释分布外（OoD）检测
practical_value: '- 「从预训练模型隐含先验中显式提取结构化特征做异常检测」的思路，可迁移到推荐系统跨域/冷启动场景的OOD样本识别，缓解预测过置信问题

  - 多源先验（语义+几何+上下文）融合为低维紧凑表征的trick，可复用在推荐场景的虚假流量、异常点击行为检测模块

  - 无需修改原有模型结构、仅新增轻量校验层的架构，适合业务存量大模型快速迭代，可用于LLM4Rec生成结果的幻觉校验'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前预训练目标检测器对分布外（OoD）样本易输出过置信的错误预测（幻觉），现有OoD检测方案多基于检测器隐层表征直接构造打分或修改检测器结构，未挖掘利用模型隐含的先验知识，可解释性差。
### 方法关键点
提出SPK框架，无需修改原有检测器结构：1）以分布内数据、幻觉诱导样本为诊断监督，提取检测器决策依赖的部件级语义概念；2）将语义先验与几何、上下文先验融合，生成5维紧凑结构化表征用于OoD检测。
### 关键结果
在多架构检测器、多个OoD基准测试中达到SOTA检测效果；验证了预训练检测器隐含的知识量远高于现有OoD方案的利用程度，可显式组织为可解释知识空间用于预测可靠性校验。
