---
title: 'GlassGround: GUI Grounding Beyond Native Screenshots with Egocentric Wearable
  Vision'
title_zh: GlassGround：面向第一视角可穿戴视觉的非截图GUI定位基准
authors:
- Yun Wang
- Siyue Sun
- Jiaying Du
- Xinyi Wei
- Xiaoming Zhai
- Zhenlin An
- Ninghao Liu
affiliations:
- University of Georgia
- Northeastern University
- The Hong Kong Polytechnic University
arxiv_id: '2611.33760'
url: https://arxiv.org/abs/2611.33760
pdf_url: https://arxiv.org/pdf/2611.33760
published: '2026-11-25'
collected: '2026-11-27'
category: Agent
direction: 可穿戴Agent GUI感知基准构建
tags:
- GUI_Grounding
- Egocentric_Vision
- Wearable_Agent
- Benchmark
- Knowledge_Distillation
one_liner: 构建跨原生截图与可穿戴相机视角的GUI定位基准，提出跨视角蒸馏方案提升非截图场景定位性能
practical_value: '- 跨视角蒸馏PairDistill的思路可迁移至多模态推荐跨域表征对齐场景，例如手机端/穿戴端用户行为表征的统一映射

  - 推理侧局部放大+坐标矫正的预处理trick可直接复用在穿戴端视觉Agent的GUI感知环节，提升低质输入下的识别准确率

  - 成对跨场景数据标注的范式可借鉴到推荐系统跨域适配的小样本训练数据集构建中，降低跨域调优的标注成本'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有GUI grounding基准仅针对原生截图，无法适配可穿戴AI助手无截图权限、仅能通过第一视角摄像头采集屏幕图像的真实场景，现有模型在相机输入下性能暴跌。
### 方法关键点
1. 构建GlassGround基准：覆盖安卓/iOS双系统、4款可穿戴设备、4种拍摄条件，共3250组对齐的「原生截图-可穿戴相机视角」配对任务，GUI状态、指令、定位目标完全一致
2. 推理侧优化：引入局部放大+屏幕几何矫正预处理
3. 训练侧优化：提出PairDistill跨视角蒸馏方案，对齐不同视角的目标表征同时增加坐标监督
### 关键结果
10个开源模型平均定位准确率从原生截图场景的94.8%降至相机输入场景的48.5%；PairDistill可在推理不依赖截图的前提下，提升2个基线模型准确率9.4、12.2个百分点，结合预处理后最高准确率可达69.6%、64.4%
