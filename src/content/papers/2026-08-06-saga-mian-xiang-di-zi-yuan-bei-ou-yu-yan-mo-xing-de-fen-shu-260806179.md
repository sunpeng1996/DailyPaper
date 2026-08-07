---
title: 'SAGA: Score-Weighted Adaptive Generation Alignment for Low-Resource Nordic
  Language Models'
title_zh: SAGA：面向低资源北欧语言模型的分数加权自适应生成对齐
authors:
- Hoda Fakharzadehjahromy
- Emil Wiman
- Andreas Bueff
- Hafsteinn Einarsson
- Fredrik Heintz
affiliations:
- Linköping University
- University of Iceland
arxiv_id: '2608.06179'
url: https://arxiv.org/abs/2608.06179
pdf_url: https://arxiv.org/pdf/2608.06179
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 低资源LLM · 无标注偏好优化
tags:
- Low-resource LLM
- Preference Optimization
- DPO
- Dependency Parsing
- Reward Engineering
one_liner: 提出无需人工偏好标注的依赖解析引导的低资源语言模型偏好优化框架SAGA
practical_value: '- 小语种电商文案、多语言推荐话术生成场景，可复用依赖解析器替代人工标注做偏好优化，大幅降低跨语言业务的标注成本

  - 做DPO训练时可复用「语法质量+生成多样性」复合奖励、奖励gap过滤低信息偏好对的trick，提升训练样本效率

  - 垂类小语种LLM对齐落地时，可借鉴奖励hack监控机制，避免对齐过程中出现生成质量退化的问题'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
低资源语言LLM偏好优化依赖昂贵的人工偏好标注，语法错误类问题无法被常规token级指标捕捉，小语种模型对齐落地难度极高。
### 方法关键点
1. 提出SAGA框架，用依赖解析器的判断自动生成偏好对输入delta-DPO训练，全程无需人工标注
2. 设计结合语法解析质量+词汇多样性的复合奖励，通过奖励差阈值过滤低信息偏好对，新增奖励hack监控模块保证监督信号可靠性
### 关键结果
基于GPT-SW3-1.3B测试3种北欧语言：丹麦语解析成功率从69.0%提升至93.8%；冰岛语独立Stanza评测提升4.5pp，80%母语使用者偏好SAGA输出；挪威博克马尔语评测指标提升28pp
