---
title: 'TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond
  Vision and Action'
title_zh: TacInno：教视觉语言动作模型学习视觉与动作之外的接触动力学
authors:
- Weile Li
- Yunfan Lou
- Muqing Shi
- Zihao Zhang
- Zhenbiao Huang
- Boxian Yao
- Xiyu Zhu
- Zhibo Pang
affiliations:
- ShanghaiTech University
- Institute of AI for Industries (IAII), Chinese Academy of Sciences
- Peking University
- Washington University in St. Louis
- Beijing FiveAges Technology
arxiv_id: '2611.26405'
url: https://arxiv.org/abs/2611.26405
pdf_url: https://arxiv.org/pdf/2611.26405
published: '2026-11-19'
collected: '2026-11-21'
category: Multimodal
direction: 多模态VLA · 触觉感知优化
tags:
- VLA
- Tactile Perception
- Multimodal Learning
- Training Paradigm
- Robot Manipulation
one_liner: 将视觉与动作无法解释的触觉创新作为训练监督，大幅提升VLA模型富接触操作任务性能
practical_value: '- 多模态融合场景可借鉴「仅保留额外模态中无法被已有模态解释的增量信息作为训练监督」的思路，避免冗余信号干扰主任务性能

  - 训练时新增辅助预测目标、部署时不新增任何模块的轻量化设计，可复用在多模态推荐/Agent系统优化，不增加推理耗时

  - 多模态特征编码时，可参考基于已有模态做条件化编码新增模态增量的方案，降低特征冗余，提升信号利用率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有融合触觉输入的VLA模型性能提升不稳定，大部分触觉变化可被视觉观测与执行动作预测，模型实际对触觉信号的依赖度极低，触觉输入的价值未被充分挖掘。
### 方法关键点
1. 定义「触觉创新」：仅触觉可感知、无法被视觉与动作解释的接触动力学信号
2. 设计条件化Tokenizer，以视觉观测和历史动作为输入，将未来触觉变化中的增量部分压缩为离散编码
3. VLA模型将预测该编码作为辅助训练目标，部署阶段不新增任何模块，无额外推理开销
### 关键结果
- 6项仿真操作任务平均成功率达87.5%，较最优visuo-tactile基线高10.7个百分点
- 4项真实世界机器人操作任务平均成功率达70.5%，较最优基线高9.0个百分点
- 消融验证了条件化编码、多帧编码、辅助预测目标对性能提升的贡献
