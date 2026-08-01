---
title: 'See2Think: Do Multimodal Models Really Use Intermediate Visual States?'
title_zh: See2Think：多模态模型真的会利用中间视觉状态吗？
authors:
- Siyu Yan
- Zhuoran Yan
- Haiying Xu
- Panhao Zhou
- Jingyu Chen
- Chenhao Ji
- Shuo Cao
- Yongheng Zhang
- Haoze Liu
- Siyu Zhang
affiliations:
- The Hong Kong University of Science and Technology
- Central South University
- Shanghai AI Laboratory
- The Hong Kong University of Science and Technology (Guangzhou)
- University of Science and Technology of China
arxiv_id: '2607.26769'
url: https://arxiv.org/abs/2607.26769
pdf_url: https://arxiv.org/pdf/2607.26769
published: '2026-07-28'
collected: '2026-08-01'
category: Eval
direction: 多模态推理能力统一评测
tags:
- Multimodal LLM
- Evaluation Framework
- Visual Reasoning
- Intermediate Visual State
- Chain-of-Thought
one_liner: 提出See2Think统一评测框架，诊断多模态模型对中间视觉状态的真实依赖与使用逻辑
practical_value: '- 搭建多模态电商推荐/导购Agent时，可复用VAoT思路，记录视觉操作+推理全链路，诊断模型是否真的用到商品图标注、场景草图等中间视觉信息，避免伪视觉推理

  - 优化多模态推理链路可优先攻克渲染保真问题，这是当前多模态模型有效利用中间视觉状态的核心瓶颈

  - 验证多模态推荐系统鲁棒性时，可引入受控破坏中间视觉反馈的方法，校验系统对视觉输入的真实依赖度，避免模型过拟合文本特征导致线上效果下跌'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前多模态大模型推理常引入草图、标注、工具生成的中间图像辅助决策，但现有评测体系存在两大缺陷：一是任务覆盖窄、大量样本可仅通过文本求解，二是仅关注最终答案，无法诊断中间视觉状态的生成、渲染、使用全链路，模型是否真的依赖视觉状态尚不明确。
### 方法关键点
提出See2Think统一评测框架，包含两大核心组件：
1. See2ThinkBench：覆盖12类任务共1200道纯视觉依赖开放题，横跨2D结构、3D场景、现实世界推理三类场景；
2. Visual Action-of-Thought（VAoT）：在4种受控推理设置下，全链路记录文本思路、视觉操作、渲染状态与后续推理过程。
### 关键结果
测试主流闭源/开源多模态模型得到：视觉推理表现强依赖模型与环境，无通用最优推理设置；模型大多能选择正确的视觉操作，但渲染保真度是核心瓶颈，高反馈接收率不一定转化为准确率提升；对3D场景任务的中间视觉反馈做针对性破坏时，模型准确率下降超10pp，确实存在对视觉状态的行为依赖。
