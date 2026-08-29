---
title: 'RegulAR: Graph-Grounded Error Recognition and Assistance for Procedural Tasks
  in AR'
title_zh: RegulAR：面向AR流程类任务的图结构错误识别与辅助系统
authors:
- Yi-Lin Ye
- Jindu Wang
- Hiu Tung Wong
- Shuchang Xu
- Huamin Qu
- Wong Kam-Kwai
affiliations:
- The Hong Kong University of Science and Technology
arxiv_id: '2608.26715'
url: https://arxiv.org/abs/2608.26715
pdf_url: https://arxiv.org/pdf/2608.26715
published: '2026-08-27'
collected: '2026-08-29'
category: Agent
direction: AR Agent 流程任务错误感知辅助
tags:
- MLLM
- Augmented Reality
- Task Dependency Graph
- Procedural Task
- Error Recognition
one_liner: 提出融合任务层级依赖图与MLLM的AR助手，支持流程任务错误识别与恢复指导
practical_value: '- 流程类任务Agent可复用「层级依赖图+MLLM」架构，替代纯MLLM方案，减少幻觉提升推理准确性

  - 电商场景的客服/直播流程质检、新手操作引导系统，可借鉴错误分类+影响评估+恢复指导的干预逻辑

  - 多模态交互Agent可参考状态可视化+原位干预的设计，提升用户对任务结构的理解度'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有AR流程指导系统仅关注步骤指令推送，缺少错误识别与恢复支持，用户操作出错后难以回归正轨。

### 方法关键点
1. 将任务指令建模为层级依赖图，显式刻画各步骤间的前置/后置依赖关系
2. 融合图结构与MLLM解析用户第一视角观测数据，实现任务进度追踪、错误按类型识别、偏差对后续步骤的影响评估
3. 通过抬头显示器原位可视化任务状态与恢复路径，提供匹配错误等级的显著干预

### 关键结果数字
12人被试内实验显示，相比纯MLLM基线，用户对任务结构的理解度、错误恢复支持满意度均显著更优
