---
title: 'TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts
  for Generalizable Manipulation'
title_zh: TableVerse：面向通用机器人操作的大规模真实落地桌面布局数据集
authors:
- Boyuan Wang
- Yue Zhang
- Xutao Xue
- Xueyu Song
- Yu Sun
affiliations:
- ByteDance
arxiv_id: '2607.21017'
url: https://arxiv.org/abs/2607.21017
pdf_url: https://arxiv.org/pdf/2607.21017
published: '2026-07-22'
collected: '2026-07-26'
category: Other
direction: 机器人通用操作 · 真实场景数据集构建
tags:
- Real2Sim
- Robotic Manipulation
- Dataset Construction
- Scene Reconstruction
one_liner: 推出全自动Real2Sim管线，构建10万级物理一致真实桌面场景数据集支撑机器人通用操作
practical_value: '- 布局生成类任务（如AR电商商品摆放、虚拟场景导购）可复用从真实图片重建带准确度量、力学稳定布局的管线，提升生成场景的真实感

  - 生成式推荐从业者可借鉴「从真实无结构数据确定性重构样本替代纯生成幻觉」的思路，降低GenRec生成物品/内容不符合真实分布的问题

  - 电商仓储履约场景的机器人Agent研发团队，可复用Real2Sim管线快速生成物理一致的仿真拣货场景训练数据，降低Sim2Real迁移成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
通用机器人操作策略迭代受限于大规模高保真真实场景数据的稀缺，现有自动化合成方法依赖文本生成布局或程序化生成，普遍存在物理不真实问题，无法复现真实人类环境的复杂密集排布特征。
### 方法关键点
- 全自动Real2Sim管线将布局生成范式从虚构生成改为基于无约束野外图片的确定性重建，可直接处理互联网非脚本媒体，输出具备准确度量尺度、真实拓扑、力学稳定性的仿真可用桌面环境
- 集成任务条件驱动的轨迹生成框架，自动生成无碰撞的抓取-摆放操作示范数据，无需人工标注
### 关键结果
最终构建的TableVerse-100K数据集包含10万个唯一物理一致环境及对应交互操作轨迹，覆盖近100万独立物体实例、3.5万+语义类别，为通用机器人操作策略学习提供高可扩展的高保真数据基础。
