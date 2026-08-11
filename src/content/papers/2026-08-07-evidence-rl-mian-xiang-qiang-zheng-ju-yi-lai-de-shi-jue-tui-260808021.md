---
title: 'Evidence-RL: Towards Evidence-intensive Visual Reasoning'
title_zh: Evidence-RL：面向强证据依赖的视觉推理优化方法
authors:
- Haojie Huang
- Xinlei Yu
- Chengming Xu
- Zhangquan Chen
- Cheng Yang
- Qingdong He
- Yu Yang
- Jiangning Zhang
- Xiaobin Hu
affiliations:
- National University of Singapore
- Zhejiang University
- Fudan University
- Tsinghua University
- Tencent
arxiv_id: '2608.08021'
url: https://arxiv.org/abs/2608.08021
pdf_url: https://arxiv.org/pdf/2608.08021
published: '2026-08-07'
collected: '2026-08-11'
category: Multimodal
direction: 多模态大模型 · 视觉证据推理优化
tags:
- VLM
- Visual Reasoning
- GRPO
- Counterfactual Learning
- Reinforcement Learning
one_liner: 反事实证据解耦CED结合GRPO训练，强化VLM回答对图像局部证据的依赖
practical_value: '- 电商多模态导购/客服Agent可复用CED逻辑，训练时校验回答是否依赖商品图核心属性区域，降低商品属性回答幻觉率

  - 多模态商品内容理解场景，可直接引入CED无标注训练策略，仅需弱目标检测框就能强化模型对商品关键区域的grounding能力，无额外标注成本

  - 多模态生成式推荐场景，可将CED的反事实校验逻辑加入RLHF训练流程，奖励依赖商品图真实特征的生成结果，避免生成不符合商品实际的推荐理由/文案'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
VLM视觉推理常依赖语言先验、数据集捷径而非真实图像局部证据，现有感知后训练方法仅通过全局扰动或注意力代理约束，无法验证回答与支撑证据的因果依赖。

### 方法关键点
1. 训练端反事实证据解耦（CED）模块：对每个回答抹除目标级证据区域，对比证据区与非证据区抹除后的回答置信度下降差异，提取证据依赖信号
2. 将证据依赖信号与回答正确性结合融入GRPO训练，奖励依赖真实证据路径的正确回答，抑制捷径路径
3. 仅需弱目标级候选框，无需问题特定证据标注，无推理额外开销

### 关键结果
在9个公开基准、4种不同VLM骨干上，性能全面超越此前基于RL的后训练方法，消融实验验证了目标级证据信号的有效性。
