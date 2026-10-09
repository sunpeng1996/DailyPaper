---
title: 'WorldGuide: Goal-Directed Video World Model for Procedural Task Execution'
title_zh: WorldGuide：面向流程化任务执行的目标导向视频世界模型
authors:
- Ankan Deria
- Komal Kumar
- Hisham Cholakkal
- Fahad Shahbaz Khan
- Salman Khan
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2610.12459'
url: https://arxiv.org/abs/2610.12459
pdf_url: https://arxiv.org/pdf/2610.12459
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: Agent 视频世界模型任务执行优化
tags:
- World Model
- Closed-loop Execution
- Procedural Task
- Agent Planning
- Video Generation
one_liner: 提出规划执行耦合的闭环视频世界模型WorldGuide及配套步骤级标注基准
practical_value: '- 做电商场景流程化Agent（如直播脚本自动生成落地、数字人带货动作规划）时，可复用「规划器+执行器同步骤标注联合训练」架构，解决规划与执行脱节问题

  - 长序列任务Agent实现中，可借鉴分层视觉记忆方案，保留历史状态的同时控制token成本，降低推理开销

  - 缺少步骤级标注数据时，可参考WorldGuide Bench构建思路，标注步骤级动作-结果配对数据用于联合训练'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成/世界模型开环生成无法适配执行结果，闭环系统依赖预训练执行器或间接校验，存在规划与执行落地的Gap，且缺少步骤级动作-视频配对监督数据支撑联合训练。

### 方法关键点
1. 将流程化视频生成定义为视觉世界空间的闭环任务执行，提出WorldGuide架构，仅输入初始图像+任务目标即可迭代完成原子动作预测、对应视频片段生成、下一步动作选择/终止判断；
2. 规划器与执行器基于同一份步骤级流程演示联合训练，分层视觉记忆在长时序执行中维持状态同时限制历史token成本；
3. 构建包含59K步标注视频、覆盖245个任务27个流程类别的WorldGuide Bench数据集。

### 关键结果
仅目标输入条件下，WorldGuide在WorldGuide Bench任务成功率33.33%，优于有参考动作计划的MiniMax-H3（29.90%）；在VideoCraft-Bench任务成功率47.69%，超出MiniMax-H3 14.96个百分点。
