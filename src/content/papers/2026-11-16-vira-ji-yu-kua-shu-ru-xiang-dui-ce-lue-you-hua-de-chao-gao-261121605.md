---
title: 'ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative
  Policy Optimization'
title_zh: ViRA：基于跨输入相对策略优化的超高分辨率视觉Agent
authors:
- Huawei Lin
- Jinting Liu
- Tongyan Wang
- Xuyang Chen
- Ruihua Shi
- Zhichao Xu
- Jiaxin Qin
- Guoshenghui Zhao
- Baijian Yang
- Yingjie Victor Chen
affiliations:
- Rochester Institute of Technology
- Purdue University
- University of Utah
- NVIDIA
arxiv_id: '2611.21605'
url: https://arxiv.org/abs/2611.21605
pdf_url: https://arxiv.org/pdf/2611.21605
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: 视觉Agent · 强化学习优化
tags:
- Visual Agent
- Reinforcement Learning
- GRPO
- High Resolution
- Contrast Set
one_liner: 提出CrossRPO强化学习策略，训练出性能超越GPT-6-Luna的超高分辨率视觉Agent
practical_value: '- 解决推荐/广告的常识偏倚问题：将相同query下仅核心属性不同的商品/素材构造成对比集，用CrossRPO思路训练排序/生成模型，奖励全对的行为，避免模型依赖高频先验猜结果，提升小众需求/特殊属性的识别准确率

  - 多模态电商Agent训练可复用对比集构建方法：仅修改商品图的关键属性（颜色、型号、参数）其他不变，构造训练数据，有效提升模型从详情页/商品图读取精准信息的能力，减少常识性错误

  - 小样本RL调优经验：针对特定垂直任务（如高分辨率商品识图），仅需数千条高质量对比训练集，即可通过RL在基座模型上获得20%以上的性能提升，无需大规模全量微调'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有超高分辨率视觉Agent普遍依赖常识猜测答案，而非读取图像中的实际证据；传统基于单样本的GRPO等强化学习方法无法区分「猜对」和「读对」，二者在单个样本上获得的奖励完全一致，导致模型学习捷径，高分辨率下的信息读取准确率极低。
### 方法关键点
- 提出Cross-Input Relative Policy Optimization（CrossRPO）：基于对比集训练，对比集包含同一问题对应的多张仅关键证据区域不同、答案不同的图像，仅答对整个集合才获得额外联合奖励，从机制上消除对常识猜测的奖励
- 构建三类超高分辨率数据集：训练集ViRA-Train（21-120MP，共9261组对比集）、评测集ViRA-Bench（762组编辑生成的对比集）、ViRA-Bench-Real（78组实拍无编辑的真实对比集，排除编辑痕迹干扰）
- 基于Qwen3.5-9B、Qwen3.8-27B基座训练ViRA-9B、ViRA-27B模型，仅用3500条左右训练样本，通过CrossRPO的联合奖励加权梯度更新
### 关键结果
- CrossRPO相比传统GRPO，在ViRA-Bench最高分辨率下集准确率提升4个百分点（63.3% vs 59.3%）
- ViRA-27B在绝大多数基准上超过Claude Haiku 5.5、GPT-6-Luna的最高思考档位，相比同量级基座+缩放工具的准确率最高提升24.4个百分点
- 该方法可直接迁移到文本任务，解决大模型依赖预训练记忆而非给定上下文回答的问题
### 核心结论
仅靠单样本的正确性奖励无法区分模型是真的理解输入还是靠先验猜对，基于对比集的联合奖励是破解模型捷径学习的高效路径
