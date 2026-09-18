---
title: 'VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations,
  Active Perception, and Metric Control'
title_zh: VABench：基于视觉演示、主动感知与度量控制的具身空间智能评测基准
authors:
- Zhongbo Zhang
- Jiayi Jin
- Yifan Wang
- Zaibin Zhang
- Haiwen Diao
- Lijun Wang
- Huchuan Lu
affiliations:
- Dalian University of Technology
- Nanyang Technological University
arxiv_id: '2609.19554'
url: https://arxiv.org/abs/2609.19554
pdf_url: https://arxiv.org/pdf/2609.19554
published: '2026-09-16'
collected: '2026-09-18'
category: Eval
direction: 具身智能 · MLLM能力评测
tags:
- MLLM
- Embodied AI
- Evaluation Benchmark
- Active Perception
- Spatial Intelligence
one_liner: 提出覆盖观察-推理-行动-修正全闭环的通用MLLM具身空间智能评测基准VABench
practical_value: '- 主动感知对比被动多视角观测效果提升超100%，电商实景逛店、AR导购Agent可新增主动视角切换功能，提升找货、商品尺寸识别等空间类任务准确率

  - 通用MLLM无需定制动作头、无特权信息即可完成具身空间任务，开发电商具身导购Agent时可直接复用通用MLLM能力，降低定制训练成本

  - 可参考该基准的分层评测逻辑，上线Agent功能前先测单步能力、再测长链路+分布外泛化能力，提前拦截线上bad case'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有空间智能评测仅停留在视觉对象位置描述层面，无法衡量MLLM在观测不全场景下的观察-推理-行动-修正全闭环具身能力。
### 方法关键点
1. 推出VABench评测基准，覆盖14类基础操作任务、7种未见几何/布局变体、长时序多物体组合任务赛道
2. 评测设置无特权信息输入：不给模型提供物体位姿、预设轨迹、定制动作头，仅靠RGB演示让MLLM主动选择相机视角、输出度量级笛卡尔操作指令、基于执行反馈修正动作
3. 评测指标包含最终任务成功率、9项轨迹级行为诊断、子任务进度三类
### 关键结果
最优MLLM标注运行下目标定位准确率100%、空间关系识别准确率78.9%，三轮平均任务成功率仅53.93±3.17%；主动相机控制对比被动多视角观测，任务成功率从27.86%提升至57.50%；未见几何泛化场景下成功率下降超30pct，无模型可完成严格长时序任务
