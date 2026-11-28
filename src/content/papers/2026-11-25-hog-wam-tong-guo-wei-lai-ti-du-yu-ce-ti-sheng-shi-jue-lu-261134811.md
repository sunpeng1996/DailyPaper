---
title: 'HOG-WAM: Improving Visual Robustness through Future Gradient Prediction'
title_zh: HOG-WAM：通过未来梯度预测提升视觉鲁棒性
authors:
- Boxuan Dong
- Yupeng Qian
- Ying Wu
- Heshuai Li
- Junhao Tan
- Zhenxiong Tan
- Weijia Wu
- Weihao Yu
affiliations:
- Peking University
- National University of Singapore
arxiv_id: '2611.34811'
url: https://arxiv.org/abs/2611.34811
pdf_url: https://arxiv.org/pdf/2611.34811
published: '2026-11-25'
collected: '2026-11-28'
category: Other
direction: 视觉鲁棒控制 · 辅助训练监督
tags:
- Visual Robustness
- Auxiliary Training
- Diffusion Transformer
- World Action Model
- HOG
one_liner: 引入基于HOG的未来梯度结构监督训练模块，无推理开销下提升世界动作模型视觉鲁棒性
practical_value: '- 训练阶段新增仅训练用辅助监督模块、推理时移除的范式，可复用在多模态推荐视觉表征训练上，不增加线上延迟的同时提升表征抗噪声能力

  - 用HOG这类低层级结构特征作为辅助监督信号的思路，可借鉴到电商商品图表征训练，对抗商品图模糊、水印等常见噪声场景

  - 不对称注意力读取主模态特征做辅助任务的架构，可迁移到多模态LLM微调阶段，强化低层级视觉特征与语义的对齐效果'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
世界动作模型（WAM）的预测任务易受图像视觉噪声干扰，导致下游控制策略失效，现有优化方案要么会增加推理开销，要么对视觉表征的针对性优化不足。
### 方法关键点
1. 提出HOG-WAM，新增仅训练阶段启用的HOG diffusion transformer（DiT）辅助模块，通过不对称注意力读取RGB特征，以未来帧HOG预测为结构监督目标优化视觉表征
2. 推理阶段直接移除辅助模块，完全保留原有FastWAM的RGB-to-action架构，无额外推理开销
### 关键结果
在RoboTwin-Plus的4种视觉corruption场景下均取得最优性能，混合噪声下成功率较FastWAM从78.86%提升至82.86%；LIBERO Plus上传感器噪声场景成功率从74.14%升至78.89%；真实Franka任务下干净/噪声场景平均成功率分别提升19pct/7pct。
