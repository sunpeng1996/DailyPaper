---
title: 'Reading Fine-Tuning Diffs Through Lenses: Model Diffing for Backdoor Detection'
title_zh: 基于透镜解析微调差异：面向后门检测的模型差分方法
authors:
- Maximilian Petrowitsch
- Ben Connors
- Chris Kapulkin
affiliations:
- Western University
- Vanderbilt University
arxiv_id: '2611.34758'
url: https://arxiv.org/abs/2611.34758
pdf_url: https://arxiv.org/pdf/2611.34758
published: '2026-11-25'
collected: '2026-11-27'
category: LLM
direction: LLM安全 · 微调后门检测
tags:
- Backdoor Detection
- Model Diffing
- Fine-tuning
- LLM Safety
- Weight Analysis
one_liner: 提出token级统一评测框架，结合J/J++透镜优化模型差分方法，提升微调LLM后门检测能力
practical_value: '- 对接入的第三方开源微调LLM，可优先采用ΔW J++权重差分方法做初筛，12种场景下11种能在前10位定位后门标识，无需运行模型成本低易落地

  - 若业务LLM支持运行时采样，可搭配ADL、Diff Mining等激活/输出类检测方法，补全权重法在隐藏单元置换、仅残差层训练场景的检测盲区

  - 业务内部微调模型上线前，可复用本文token级统一评分体系做后门自动化审计，避免恶意微调植入的后门影响线上服务'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
开源LLM微调复用场景广泛，微调过程易被植入隐蔽后门，现有模型差分后门检测方法缺乏统一评测标准，适用场景边界不明确。
### 方法关键点
1. 搭建基于token读出的统一评分体系，可横向对比权重、激活、输出三类模型差分检测方法效果；
2. 引入J透镜及优化版J++透镜改进检测方法，核心方案ΔW J++通过基模型J++透镜解码微调前后权重差，定位后门关联token。
### 关键结果
ΔW J++在12组测试场景中的11组可将后门token排在输出前10位；针对微调时惩罚干净输入下后门词输出概率的对抗场景，权重类方法不受影响，激活/输出类方法失效；针对隐藏单元置换、仅训练残差读取层的对抗场景，权重类方法失效，激活/输出类方法仍有效，暂无单方法覆盖所有对抗场景。
