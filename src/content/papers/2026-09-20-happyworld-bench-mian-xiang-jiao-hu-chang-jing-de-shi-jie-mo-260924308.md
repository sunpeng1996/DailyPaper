---
title: HappyWorld-Bench
title_zh: HappyWorld-Bench：面向交互场景的世界模型统一评估基准
authors:
- Zhiqi Bai
- Junai Cai
- Yixin Chen
- Jingrun Du
- Tao Feng
- Wei Gong
- Siyuan Huang
- Xiao Lin
- Jiaheng Liu
- Jun Luo
affiliations:
- Alibaba Token Hub, Alibaba Group
- State Key Laboratory of General Artificial Intelligence, BIGAI
- Tsinghua University
- Nanjing University
- Peking University
arxiv_id: '2609.24308'
url: https://arxiv.org/abs/2609.24308
pdf_url: https://arxiv.org/pdf/2609.24308
published: '2026-09-20'
collected: '2026-09-24'
category: Eval
direction: 世界模型评估 · 多能力层级统一基准
tags:
- WorldModel
- Benchmark
- EmbodiedAgent
- Evaluation
- GenerativeWorld
one_liner: 提出覆盖6级能力、3条评估赛道的世界模型基准，含1692个测试用例与人类+自动评估体系
practical_value: '- 开发电商导购数字人、虚拟展厅等交互型Agent时，可复用W1-W6能力分层框架，拆解世界建模迭代的评估指标，避免仅关注静态生成质量

  - 电商3D样板间、虚拟逛街等场景的生成效果评估，可复用空间赛道的自动化指标，覆盖物理可用性、跨视角一致性、编辑保真性三类，降本提效

  - 做世界模型的用户偏好对齐时，可复用Arena的A/B对比+Elo评分机制，低成本实现大规模人类偏好的量化排序，匹配业务体验要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有世界模型评估体系碎片化，视频、空间、具身三类模型的评估标准不统一，普遍仅关注生成内容的视觉质量，忽略Agent交互、场景修改、重访等场景下的状态一致性、动作响应正确性，无法衡量世界模型在真实业务中的实用可靠性。
### 方法关键点
- 定义W1-W6共6级世界建模能力分层：从基础感知构建、交互响应、状态持久化、可编程干预、多Agent可扩展到通用世界建模，能力要求逐级提升
- 设置3条独立评估赛道：视频世界模型（1138条提示）、空间世界模型（300个场景）、具身世界模型（254个测试用例），所有赛道共用统一的能力评估框架
- 评估体系结合多维度自动指标（覆盖感知、一致性、因果性、可控性维度）与HappyWorld-Arena人类A/B对比Elo评分，兼顾客观行为正确性与主观用户偏好
### 关键实验
共测试14个视频世界模型、9个空间系统、8个具身候选模型，核心结果：① 视频赛道最高Elo评分1263，长时序交互下状态一致性普遍存在明显缺陷；② 空间模型最高摆放准确率70.14%、编辑执行准确率73.33%；③ 具身模型多步动作下的状态保留能力普遍薄弱。
### 核心结论
世界模型的实用价值不止于静态生成质量，更需要在持续交互、修改、重访场景下保持状态一致性与规则正确性，才能支撑真实业务落地
