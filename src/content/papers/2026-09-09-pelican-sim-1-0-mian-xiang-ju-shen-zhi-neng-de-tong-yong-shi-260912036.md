---
title: 'Pelican-Sim 1.0: A General World Model Simulator for Embodied Intelligence'
title_zh: Pelican-Sim 1.0：面向具身智能的通用世界模型模拟器
authors:
- Shilong Zou
- Shilin Zhang
- Yingji Zhang
- Yuhang Huang
- Yi Zhang
- Zeyuan Ding
- Han Dong
- Junwei Liao
- Yong Dai
- Jian Tang
affiliations:
- Beijing Innovation Center of Humanoid Robotics (X-Humanoid)
- WFM System Group
arxiv_id: '2609.12036'
url: https://arxiv.org/abs/2609.12036
pdf_url: https://arxiv.org/pdf/2609.12036
published: '2026-09-09'
collected: '2026-09-15'
category: Agent
direction: 具身Agent · 通用世界模型模拟器
tags:
- World Model
- Embodied Agent
- Sparse MoE
- Video Prediction
- Simulator
one_liner: 设计支持多异构具身设备的通用世界模型模拟器，生成质量与下游效果显著优于基线
practical_value: '- 统一多模态输入表示的设计思路可迁移至多设备多场景的Agent决策系统，降低不同硬件/场景下的模型适配成本

  - 稀疏MoE融合多模态输入的方案可复用，有效缓解模态冲突、提升模型容量的同时控制推理延迟

  - 少量样本蒸馏缩短自回归步数的加速技巧可直接应用于生成式推荐、Agent轨迹预测等需要连续生成的业务场景

  - 用世界模型生成合成数据增强小样本下游任务的范式，可迁移到冷启动推荐、低资源搜索场景的样本扩充'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有具身智能世界模型多适配单一设备/场景，可控性差、推理速度慢，难以支撑异构具身Agent的下游决策与训练需求。

### 方法关键点
1. 设计28维统一动作表示空间，兼容主流异构具身设备；
2. 引入URDF与相机渲染的动作视频桥接动作与像素模态，提升跨场景可控性；
3. 采用稀疏MoE层缓解模态冲突，提升异构动力学建模容量；
4. 通过因果适配与少步蒸馏实现4步自回归生成，大幅提升推理速度。

### 关键结果数字
在RoboTwin数据集上PSNR比最强基线高10.343，FVD比稠密 backbone低6.53，推理速度较35步模型提升5.67倍；下游任务中，生成轨迹增强后策略成功率从70%提升至93%，策略评估皮尔逊相关系数达0.994，动作选择成功率提升47.7%，策略优化成功率提升20.3%。
