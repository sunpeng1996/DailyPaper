---
title: 'Thermo-FL: Thermal-Aware Robust Federated Fine-Tuning of Large Language Models
  for Edge AI'
title_zh: Thermo-FL：面向边缘AI的大语言模型热感知鲁棒联邦微调
authors:
- Shiva Shrestha
- Kazi Shaharair Sharif
- Zongxing Xie
- Jiajing Huang
- Anhao Xiang
- Honghui Xu
affiliations:
- Kennesaw State University Department of Computer Science
- Kennesaw State University School of Data Science and Analytics
- Kennesaw State University Department of Information Technology
arxiv_id: '2608.21172'
url: https://arxiv.org/abs/2608.21172
pdf_url: https://arxiv.org/pdf/2608.21172
published: '2026-08-21'
collected: '2026-08-24'
category: Training
direction: 边缘LLM 热感知联邦鲁棒微调
tags:
- Federated Learning
- LoRA
- Edge AI
- LLM Fine-tuning
- Robust Aggregation
one_liner: 提出热感知联邦LoRA微调框架，同时解决边缘LLM微调的热约束与对抗更新篡改问题
practical_value: '- 边缘端多设备联邦LoRA微调场景下，可复用「设备状态动态调整LoRA激活层占比+稀疏更新传输」策略，降低端侧算力负载、减少通信开销

  - 联邦更新聚合环节可复用TERRA pipeline的norm过滤、方向校验、自适应裁剪组合方案，提升对抗攻击下的模型鲁棒性

  - 稀疏更新传输可复用bitmap稀疏编码方案，降低端侧上传数据量，适配弱网/低带宽边缘部署场景'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
边缘LLM联邦微调存在两大痛点：一是设备热约束会导致降频、训练延迟，拖慢聚合效率；二是拜占庭客户端与通信层攻击会篡改更新，降低全局模型效果与安全性。

### 方法关键点
1. 端侧：以设备温度为控制信号，动态调整激活LoRA层占比与更新传输密度，热应力下自动降低 workload；
2. 服务端：提出TERRA鲁棒聚合管线，融合norm过滤、掩码感知方向校验、自适应坐标裁剪、掩码感知聚合，适配动态稀疏LoRA更新。

### 关键结果
- 仿真环境下，干净/攻击场景中BoolQ准确率均为最优，GSM8K效果保持竞争力；
- 物理测试床中，设备温度稳定，稀疏编码降低上传体积，sign-flip/scale、MITM扰动下GSM8K效果无明显损失
