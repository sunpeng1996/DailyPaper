---
title: 'QuantWAMs: Calibrating at the Right Granularity for World Action Models'
title_zh: QuantWAMs：面向世界动作模型的正确粒度校准后训练量化框架
authors:
- Jiacheng Zhou
- Jinfan Lv
- Ruixuan Li
- Longtai Zhang
- Yan Wang
- Wenqiang Zhang
- Lizhe Qi
affiliations:
- Fudan University
- East China Normal University
arxiv_id: '2607.28405'
url: https://arxiv.org/abs/2607.28405
pdf_url: https://arxiv.org/pdf/2607.28405
published: '2026-07-30'
collected: '2026-08-01'
category: Training
direction: 模型压缩 · 世界动作模型后训练量化
tags:
- PTQ
- Quantization
- World Action Model
- Diffusion Model
- Low-bit Inference
one_liner: 提出适配世界动作模型的PTQ框架，W4A4精度下性能接近FP16，显存占比29%，提速1.4-1.6倍
practical_value: '- 多分支多目标生成模型（如多模态推荐、生成式文案模型）做PTQ时，仅在坐标兼容的模块间共享激活统计信息，可在不增加精度预算的前提下降低量化损失

  - 权重精度分配时，基于多任务联合梯度计算Fisher分数做层粒度的精度分配，比单任务打分更适配电商多目标排序、多模态召回模型的压缩需求

  - 闭环交互系统（如对话Agent、交互式推荐）做量化时，可基于全精度真实交互rollout的固定干预回放修正调度策略，避免开环校准的分布偏移

  - W4A4低比特量化在损失可控的前提下可降低70%+显存、提升1.4-1.6倍推理速度，可直接复用在端侧/边缘部署的生成式推荐、轻量Agent服务上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
世界动作模型（WAM）联合预测未来观测与动作，需迭代去噪+闭环执行，部署推理成本极高；现有后训练量化（PTQ）方法依赖开环目标、同质模型假设，校准分布与实际部署场景不匹配，直接应用到WAM会出现精度大幅下降的问题，亟需适配WAM特性的PTQ框架。

### 方法关键点
- 共享基异常校准：仅在坐标兼容的模块间池化激活统计信息，计算池化能量Top-K通道保留高精度，其余量化为4bit，降低小样本下的估计噪声
- 联合训练目标显著性：基于视频-动作联合梯度计算经验Fisher分数，在校准稳定的层粒度分配权重精度，优先给对联合任务影响大的层分配更高比特
- 固定干预rollout审计：基于全精度模型生成的真实闭环轨迹回放，在不改变精度预算的前提下修正去噪步保护调度，避免开环校准的分布偏移

### 关键结果
在RoboTwin 2.0、LIBERO两个仿真基准以及AgiBot G2真实机器人任务上验证，对比GPTQ、SmoothQuant、Atom、SVDQuant等基线；W4A4主导精度下，仿真任务成功率仅比FP16低0.2-0.7个百分点，目标视频/动作块的峰值显存降至FP16的29%，块级推理速度提升1.4-1.6倍；真实机器人任务成功率仅比FP16低6.6个百分点，远低于基线Atom*的23.3个百分点损失。

最值得记住的一句话：量化校准的效果本质取决于校准的结构、分布、目标三个维度是否与实际部署场景对齐，而非单纯提升局部量化精度。
