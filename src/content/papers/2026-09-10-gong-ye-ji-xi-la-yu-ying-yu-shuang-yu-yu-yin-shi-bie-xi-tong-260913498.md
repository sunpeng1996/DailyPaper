---
title: Building a Production Greek-English Speech Recognizer
title_zh: 工业级希腊语-英语双语语音识别系统的构建
authors:
- Christos Petrocheilos
- Cleopatra Papadopoulou
- Chris Porikis
- Ioakeim Perros
- Ayoub Kirouane
- Themistoklis Nikolis
affiliations:
- Sophea AI Lab, KIEFER SA, Athens, Greece
arxiv_id: '2609.13498'
url: https://arxiv.org/abs/2609.13498
pdf_url: https://arxiv.org/pdf/2609.13498
published: '2026-09-10'
collected: '2026-09-17'
category: Other
direction: 工业级多语种语音识别系统落地
tags:
- ASR
- Production System
- Bilingual Model
- ROVER Ensemble
- WER Optimization
one_liner: 公开工业级希腊语-英语双语ASR系统的完整工程实现流程与量化优化结果
practical_value: '- 多业务指标互斥时可优先采用多模型集成方案替代单模型调优，平衡不同维度的生产要求，降低迭代成本

  - 数据预处理阶段可基于领域内锚点校准通用过滤阈值，大幅降低高质量业务训练数据的丢弃率

  - 上线前预设多维度生产准入校验门，可提前识别单模型的漏判缺陷、幻觉等隐性问题

  - 预注册消融实验可快速定位训练数据/流程中的隐藏缺陷，有效缩短算法迭代周期'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
工业级双语ASR系统需同时满足多维度互斥的生产指标要求，单模型调优难以覆盖全部准入条件，行业缺乏可复用的落地工程实践框架。
### 方法关键点
1. 预设9项生产准入门限：覆盖4项希腊语、3项英语WER上限，95%语种识别准确率下限，非语音音频零幻觉要求；
2. 设计6阶段数据pipeline，基于领域内锚点校准UTMOS音频质量过滤阈值，替代通用教科书阈值；
3. 采用三模型ROVER集成方案平衡多指标冲突，搭配预注册消融实验快速定位训练数据缺陷。
### 关键结果数字
- 三模型集成覆盖全部9项准入要求，重叠语音WER从53.35%降至37.87%，相对优化29%；
- 音频过滤优化后希腊语有效训练数据保留率从1.3%提升至89.4%；
- 单仲裁模型在公开英文测试集平均WER 4.26%，希腊语嘈杂环境实时流量WER达25.88%。
