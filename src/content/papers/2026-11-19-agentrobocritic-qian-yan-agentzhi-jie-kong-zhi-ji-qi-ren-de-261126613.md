---
title: 'AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct
  Robot Control'
title_zh: AgentRoboCritic：前沿Agent直接控制机器人的能力分析框架
authors:
- Yiyang Du
- Yuxuan Kuang
- Qitao Zhao
- Yixuan Wang
- Zhanqiu Guo
- Yi Xu
- Xin Li
- Wenbin He
- Liu Ren
- Chenyan Xiong
affiliations:
- Carnegie Mellon University
- University of Illinois at Urbana-Champaign
- Bosch Research North America & Bosch Center for Artificial Intelligence (BCAI)
arxiv_id: '2611.26613'
url: https://arxiv.org/abs/2611.26613
pdf_url: https://arxiv.org/pdf/2611.26613
published: '2026-11-19'
collected: '2026-11-22'
category: Agent
direction: Agent能力评测 · 机器人控制
tags:
- Agent
- Multimodal LLM
- Evaluation
- Robot Control
- Failure Analysis
one_liner: 提出意图锚定的动作级评测框架，精准定位前沿Agent机器人直接控制的成败原因
practical_value: '- 做Agent能力评测时可复用「动作+本地意图绑定+评判器校验」框架，替代粗粒度任务级成功率指标，精准定位Agent短板

  - 电商客服/履约/导购Agent的故障归因可迁移该方案，给每个Agent动作绑定当前子意图，自动识别错误环节，降低人工标注成本

  - 自研Agent评判模块时，可参考标注数据集微调开源大模型的方案，大幅提升错误模式识别准确率，无需完全依赖闭源大模型'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有前沿多模态Agent直接控制机器人的评测仅输出任务级成功率，无法拆解成功路径、定位具体失败环节，缺少细粒度能力归因手段。
### 方法关键点
1. 覆盖12个机器人操控基准测试集，开展动作级系统能力分析
2. 提出AgentRoboCritic意图锚定评测框架：要求策略Agent输出每个动作对应的本地子意图，评判器基于意图匹配动作执行结果，自动识别失败模式
3. 开源12844条标注动作数据集，以及微调后的30B参数开源评判模型Muse-Glimmer-30B
### 关键结果
开源评判模型的失败模式识别准确率从32.58%提升至74.24%；验证前沿Agent具备执行故障闭环恢复、跨场景语义对齐、零样本操控能力，但存在抓取对齐等物理执行瓶颈、不同故障模式恢复能力不均的短板
