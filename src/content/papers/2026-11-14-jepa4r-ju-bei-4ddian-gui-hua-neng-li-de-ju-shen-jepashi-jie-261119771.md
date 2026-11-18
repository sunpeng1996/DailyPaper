---
title: 'JEPA4R: Embodied JEPA World Models with 4D Point Planning'
title_zh: JEPA4R：具备4D点规划能力的具身JEPA世界模型
authors:
- Jiarui Dong
- Zhiheng Liang
- Yanjun Li
- Zeyu Zhang
- Heejeong Nam
- Haoyu Chen
- Hao Tang
affiliations:
- Peking University
- UC Berkeley BAIR
- Brown University
- University of Oulu
arxiv_id: '2611.19771'
url: https://arxiv.org/abs/2611.19771
pdf_url: https://arxiv.org/pdf/2611.19771
published: '2026-11-14'
collected: '2026-11-18'
category: Agent
direction: 具身Agent · 世界模型规划
tags:
- JEPA
- World Model
- Embodied Agent
- 4D Point Planning
- Zero-shot Transfer
one_liner: 提出基于单目深度点云的4D点规划JEPA世界模型，具身任务性能超SOTA且支持零样本部署
practical_value: '- 数字孪生训练+零样本部署的架构可迁移至电商仓储分拣机械臂落地，大幅降低真实场景标注与调优成本

  - 几何感知的点云隐空间规划替代2D像素规划的思路，可优化仓储/物流场景下具身Agent的动作决策精度

  - 冻结世界模型隐层+独立策略头的解耦设计，可降低多场景具身任务的模型迭代与适配成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有JEPA世界模型依赖2D图像输入，几何度量信息与外观特征纠缠，且隐空间规划不可解释，仅能在仿真中完成短时序验证，无法适配真实机械臂操作需求。
### 方法关键点
输入单目深度相机点云，在隐空间完成4D时序点云预测与规划；基于冻结的世界模型隐层接入策略头输出动作；额外增设解码器将隐态还原为4D点云，实现规划过程可解释。
### 关键结果数字
200步长预测的点云平均误差小于1.1cm；OGBench多项任务性能远超最优2D JEPA模型；MetaWorld、Adroit Relocate任务上成功率达98.4%、88.0%，分别超亚军R3M 2.4、22.7个百分点；仅在数字孪生训练即可零样本迁移至真实机械臂的夹爪/灵巧手操作。
