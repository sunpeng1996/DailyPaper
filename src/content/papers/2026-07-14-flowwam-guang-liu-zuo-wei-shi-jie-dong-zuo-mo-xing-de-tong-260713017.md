---
title: 'FlowWAM: Optical Flow as a Unified Action Representation for World Action
  Models'
title_zh: FlowWAM：光流作为世界动作模型的统一动作表征
authors:
- Yixiang Chen
- Peiyan Li
- Yuan Xu
- Qisen Ma
- Jiabing Yang
- Kai Wang
- Jianhua Yang
- Dong An
- He Guan
- Gaoteng Liu
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- FiveAges
- MBZUAI
- Alibaba Group
arxiv_id: '2607.13017'
url: https://arxiv.org/abs/2607.13017
pdf_url: https://arxiv.org/pdf/2607.13017
published: '2026-07-14'
collected: '2026-07-16'
category: Agent
direction: Agent 世界动作模型动作表征优化
tags:
- Action Representation
- Optical Flow
- World Model
- Diffusion Model
- Video Generation
one_liner: 提出采用光流作为统一动作表征的双流扩散世界动作模型，在操控与建模任务上大幅超越基线
practical_value: '- 涉及多模态交互的Agent场景（如直播电商数字人操控、商品3D展示交互）可复用「用与生成模型原生格式对齐的表征降低跨模态对齐成本」的思路

  - 缺乏标注的交互/视频数据场景，可借鉴光流无需动作标签即可从原始视频提取的特性，用无标注数据做预训练降低标注成本

  - 多任务生成框架可参考双流共享预训练backbone的设计，同时支持预测/生成两种任务模式，减少重复训练开销'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有世界动作模型（WAM）基于预训练视频生成器做控制时，存在动作表征适配难题：数值类动作无法对齐视频生成器输入格式，视觉类动作表征缺失帧间时序运动结构，无法支撑精准控制。

### 方法关键点
双流扩散框架FlowWAM采用光流作为统一的视频原生动作表征，光流与RGB视频格式完全对齐且编码逐像素位移信息；在共享预训练视频生成器中联合建模光流与RGB，天然支持两种WAM模式：策略模式生成光流做动作预测，世界模型模式用目标光流序列引导未来视频生成；光流可从无标注原始视频直接提取，可利用大规模无标注视频预训练。

### 关键结果
RoboTwin操控任务Clean/Random设置下成功率达92.94%/92.14%，超越VLA、WAM基线；WorldArena世界建模任务EWMScore达63.71，轨迹精度相对提升18.4%。
