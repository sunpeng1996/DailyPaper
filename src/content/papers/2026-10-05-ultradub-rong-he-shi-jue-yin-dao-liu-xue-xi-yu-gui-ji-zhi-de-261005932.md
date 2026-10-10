---
title: 'UltraDub: Towards Authentic Dubbing by Unifying Visually-Steered Flow Learning
  and Trajectory Guidance'
title_zh: UltraDub：融合视觉引导流学习与轨迹指导的高真实度配音框架
authors:
- Gaoxiang Cong
- Liang Li
- Jianwei Wen
- Zhedong Zhang
- Zheng-Jun Zha
- Qingming Huang
affiliations:
- Institute of Computing Technology, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Hangzhou Dianzi University
- ByteDance
- University of Science and Technology of China
arxiv_id: '2610.05932'
url: https://arxiv.org/abs/2610.05932
pdf_url: https://arxiv.org/pdf/2610.05932
published: '2026-10-05'
collected: '2026-10-10'
category: Multimodal
direction: 多模态音视频生成 · 视觉语音克隆
tags:
- Multimodal Generation
- Audio Synthesis
- Lip Synchronization
- Flow Learning
- Training-free Mechanism
one_liner: 提出融合视觉流学习与节奏锚定校正的SOTA配音框架，配套多场景基准数据集
practical_value: '- MDR模块的共享残差+时间条件门控校准多模态特征贡献的思路，可直接迁移至多模态推荐场景的文本/视觉/用户行为多源特征融合，降低不同模态信号的冲突

  - 训练免的RTG轨迹校正机制，可复用到生成式推荐推理阶段（如商品口播视频生成），无需额外训练成本即可平衡语义准确率与时序对齐度

  - 以视觉模态为锚点平衡多模态生成多维度指标的设计逻辑，可用于电商带货短视频的自动配音场景，同步保障语音语义正确与唇形匹配，提升内容转化率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视觉语音克隆方案存在两大痛点：一是序列多模态条件输入易破坏已建模的时序、说话人特征一致性；二是推理引导不平衡会牺牲唇形同步度换取语言准确率，无法兼顾多指标最优。
### 方法关键点
1. 提出UltraDub框架，从连续运动上下文聚合、结构节奏轨迹校正两个维度利用视觉信号指导配音生成
2. 设计Motion-guided Dual-context Retrieving (MDR)模块，通过共享唇动查询残差持续校准语言、说话人风格检索结果，采用独立时间条件门控动态调节两者贡献权重
3. 提出训练免的Rhythm-anchored Trajectory Guidance (RTG)机制，在纯视觉预测中点评估分层多模态修正强度，强化语义条件的同时保留时序对齐效果
4. 构建DiverseDub多场景基准数据集，覆盖真实复杂场景下的配音效果评估需求
### 关键结果
在4个公开数据集上实现端到端配音任务SOTA性能，同步提升语言准确率、说话人一致性与唇形同步度
