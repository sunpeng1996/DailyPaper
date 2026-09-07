---
title: 'GazeFS: Target-Centered Gaze-Trajectory Forecasting and Stabilization from
  Gaze-Head History'
title_zh: GazeFS：基于眼动-头部历史的目标中心眼动轨迹预测与稳定
authors:
- Yaozheng Xia
- Zaiping Zhu
- Bo Pang
- Minghao Xie
- Hui Li
- Shaorong Wang
- Sheng Li
affiliations:
- 北京林业大学
- 南京艺术学院
- 北京大学
- 大连理工大学莱斯特国际学院
arxiv_id: '2609.03868'
url: https://arxiv.org/abs/2609.03868
pdf_url: https://arxiv.org/pdf/2609.03868
published: '2026-09-03'
collected: '2026-09-07'
category: Other
direction: 眼动交互 · 轨迹预测与稳定
tags:
- Gaze-Forecasting
- Human-Computer-Interaction
- Trajectory-Prediction
- Time-Series
- Stability-Optimization
one_liner: 提出无推理阶段目标信息的GazeFS框架，实现眼动轨迹预测与稳定，降低聚焦阶段偏差与误差
practical_value: '- 可借鉴时序历史窗口建模方法，优化电商用户浏览/点击等时序行为的预测精度

  - 可复用分阶段（搜索/聚焦）行为识别思路，拆分用户逛/买不同决策阶段的特征权重

  - 时序预测中可参考无目标信息推理的设计，降低冷启动阶段对上下文标签的依赖

  - 眼动交互相关业务（如AR试穿、智能导购屏）可直接复用轨迹稳定方案降低交互误差'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有目标中心眼动交互仅抑制帧间波动，未考虑目标采集过程中眼动-头部动态的任务对齐变化，也无法解决眼动轨迹残留的目标相对持久方向偏差问题，需在线完成无目标信息的眼动轨迹校正。

### 方法关键点
提出GazeFS框架，输入可变长度的眼动-头部历史序列，输出下一时刻目标中心方向与短时间窗口的搜索/聚焦状态估计，推理阶段无需依赖目标信息。

### 关键结果数字
在30名参与者的7960条采集序列上，聚焦阶段偏差、序列内离散度、P90目标误差较原始数据分别降低0.182°、0.257°、0.400°；阶段识别的平衡准确率/AUPRC达0.925/0.993，近期历史特征贡献显著优于显式进度元数据。
