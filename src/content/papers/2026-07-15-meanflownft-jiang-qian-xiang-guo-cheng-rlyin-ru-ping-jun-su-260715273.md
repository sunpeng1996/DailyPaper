---
title: 'MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators'
title_zh: MeanFlowNFT：将前向过程RL引入平均速度生成器
authors:
- Yushi Huang
- Xiangxin Zhou
- Jun Zhang
- Liefeng Bo
- Tianyu Pang
affiliations:
- Tencent Hunyuan
- The Hong Kong University of Science and Technology
arxiv_id: '2607.15273'
url: https://arxiv.org/abs/2607.15273
pdf_url: https://arxiv.org/pdf/2607.15273
published: '2026-07-15'
collected: '2026-07-17'
category: Training
direction: 生成模型训练 · 少步生成RL偏好对齐
tags:
- Reinforcement Learning
- MeanFlow
- Few-step Generation
- Preference Alignment
- Flow Matching
one_liner: 基于MeanFlow恒等式搭建瞬时速度预测器，实现少步生成与RL偏好对齐的高效融合
practical_value: '- 生成式推荐的商品主图/短视频/文案生成场景，可复用该RL对齐框架，在少步快速生成的前提下，对齐用户点击、转化等业务 reward
  指标

  - Agent 生成类任务（如推荐理由生成、query应答）可借鉴平均/瞬时速度桥接思路，平衡推理速度与任务 reward 优化效果

  - 线上生成服务部署时，可参考该方案用少步MeanFlow替代多步扩散，在不损失生成质量的前提下降低推理延迟、提升服务QPS'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
MeanFlow 依托时间区间平均速度预测实现少步采样，推理效率优势突出，但现有适配扩散/流模型的前向RL对齐框架（如DiffusionNFT）仅支持优化瞬时速度，无法直接适配MeanFlow的结构，少步生成的RL偏好对齐存在技术缺口。
### 方法关键点
1. 基于MeanFlow恒等式构建诱导瞬时速度预测器，桥接平均速度与瞬时速度的映射关系；
2. 直接复用DiffusionNFT的前向过程RL优化目标，无需逆过程轨迹或似然估计即可完成reward优化；
3. 采样阶段仍基于平均速度推理，完全保留MeanFlow少步生成的效率优势，且理论上继承DiffusionNFT的严格策略提升保证。
### 关键结果
- SD3.5-M上8项指标中6项优于现有SOTA RL调优的少步生成器；
- Wan 2.1数据集上4步采样的VBench得分达84.33，超过50步采样的LongCat-Video RL方案的82.57，少步生成质量超越多步RL调优的扩散模型
