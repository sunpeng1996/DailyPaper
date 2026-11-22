---
title: 'Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action,
  and Mind-Action Composition in Robotic Manipulation'
title_zh: Mind2Act World：机器人操作具身认知与动作协同诊断基准
authors:
- Yuzhi Huang
- Jie Wu
- Fanding Huang
- Junchao Lin
- Weichen Zhang
- Ziyi Xiong
- Yang Li
- Zhengwei Xie
- Zhimin Wang
- Zhen Liu
affiliations:
- THU
- UCam
- Oxford
- Stanford
- CMU
arxiv_id: '2611.26444'
url: https://arxiv.org/abs/2611.26444
pdf_url: https://arxiv.org/pdf/2611.26444
published: '2026-11-18'
collected: '2026-11-22'
category: Agent
direction: 具身Agent 能力诊断基准构建
tags:
- Embodied Agent
- Benchmark
- VLA
- WAM
- Multimodal Agent
- Capability Diagnosis
one_liner: 推出覆盖3个能力维度180种配置的具身智能诊断基准，可定位故障来源于认知、执行或二者协同
practical_value: '- 做Agent系统（如电商导购Agent、仓储自动化Agent）性能评测时，可复用「单模块能力诊断+组合协同诊断」框架，快速定位故障是来自认知、执行还是模块协同环节，降低迭代排障成本

  - 设计业务场景评测集时，可参考「三级难度+干净/随机双场景」的配置方式，同时覆盖标准化测试和真实复杂业务场景，提升评测结果的业务适配性

  - 搭建LLM+工具调用的Agent架构时，可参考该研究结论：单模块能力强不代表协同效果好，需重点优化基于环境/工具返回结果的闭环反馈迭代逻辑，提升端到端任务成功率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有具身智能基准要么在同一任务中同时评估推理与执行能力，要么将二者完全分开评估，无法定位系统故障来源于认知缺陷、执行缺陷，还是二者的协同能力不足。
### 方法关键点
推出Mind2Act World诊断基准，覆盖5类真实场景的30个模拟操作任务，每个任务设3级难度、2种场景（Clean可控场景/Random随机场景），共180种评测配置；分三个维度评测：Mind维度测基于历史观测的决策能力，Act维度测精确及时的执行能力，Mind2Act维度测闭环下二者的协同能力，配套诊断工具可输出系统能力画像。
### 关键结果数字
- 最强Agent的Mind任务成功率52.7%、Act任务成功率39.0%，但Mind2Act协同任务成功率仅12.0%
- 单维度能力无法迁移到协同任务，认知-执行的反馈协同是当前具身Agent的核心瓶颈
