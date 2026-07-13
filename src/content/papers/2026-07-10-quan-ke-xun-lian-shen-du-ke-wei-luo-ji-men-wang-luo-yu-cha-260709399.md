---
title: Fully Trainable Deep Differentiable Logic Gate Networks and Lookup Table Networks
title_zh: 全可训练深度可微逻辑门网络与查找表网络
authors:
- Wout Mommen
- Lars Keuninckx
- Matthias Hartmann
- Werner Van Leekwijck
- Piet Wambacq
affiliations:
- imec
- Vrije Universiteit Brussel
arxiv_id: '2607.09399'
url: https://arxiv.org/abs/2607.09399
pdf_url: https://arxiv.org/pdf/2607.09399
published: '2026-07-10'
collected: '2026-07-13'
category: Training
direction: 低资源模型训练 · 可微神经网络优化
tags:
- Differentiable Logic Gate Network
- Lookup Table Network
- Straight-through Estimator
- Backpropagation
- Edge Computing
one_liner: 提出可微逻辑门与查找表网络的连接优化训练方法，大幅压缩参数量同时提升基准任务精度
practical_value: '- 端侧小模型部署可借鉴该方法的低参数量逻辑门结构，降低边缘设备推理功耗，适合IoT场景下的推荐触发、广告预过滤等轻量化任务

  - 离散特征选择场景可复用「基于概率分布的连接择优+直通估计器」训练范式，替代硬剪枝提升特征选择的训练稳定性

  - 特征哈希/查表类推荐模型（如双塔召回的哈希层）可参考LUT可微训练方法，实现查表参数与结构的端到端联合优化'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有二值/神经形态模型训练存在连接固定导致参数冗余大、深层训练不稳定的问题，难以适配低功耗边缘推理场景。
### 方法关键点
1. 对每个逻辑门/LUT输入引脚维护连接概率分布，训练时并行学习最优连接、门类型/LUT条目，采用高学习率、直通估计器、裁剪恒输出门类型方案保障10层以内训练稳定性；
2. 提出支持反向传播的可微LUT神经元结构，适配6层以内深层LUT网络训练。
### 关键结果
MNIST数据集上2层8000门LGN精度达98.92%，1层8000门精度98.45%，门数量较固定连接LGN减少近50倍；可微LUT网络较固定连接LGN参数量减少75%，2层2000个6输入LUT的网络MNIST精度达98.88%。
