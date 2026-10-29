---
title: 'VideoLVR: Latent Visual Reasoning over Grounded Video Evidence'
title_zh: VideoLVR：基于锚定视频证据的隐式视觉推理框架
authors:
- Shilong Li
- Xingyuan Bu
- Hao Shi
- Yun Xing
- Weixin Feng
- Qiangpeng Yang
- Shilei Wen
affiliations:
- Beijing University of Posts and Telecommunications
- Tsinghua University
- Nanyang Technological University
arxiv_id: '2610.37613'
url: https://arxiv.org/abs/2610.37613
pdf_url: https://arxiv.org/pdf/2610.37613
published: '2026-10-27'
collected: '2026-10-29'
category: Multimodal
direction: 多模态大模型 · 视频隐式视觉推理
tags:
- MLLM
- Video Understanding
- Chain-of-Thought
- Visual Reasoning
- Multimodal
one_liner: 提出基于隐式视觉证据的视频推理框架，无需大幅扩充上下文即可提升细粒度视频理解效果
practical_value: '- 电商短视频/直播内容理解场景可复用隐式视觉证据构造方法，无需扩充大量上下文即可提升细粒度商品属性识别、违规内容检测的准确率

  - 可借鉴视觉token预测与文本生成统一的训练框架，降低多模态理解任务的训练复杂度，适配长视频/直播流的实时推理需求

  - 视觉token与文本token联合RL优化的思路可迁移至多模态Agent的交互决策任务，提升多模态输入下的决策准确率'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有基于Chain-of-Thought的多模态大模型视频推理存在两类痛点：一是语言推理轨迹无法回溯视觉证据导致视觉遗忘，推理准确率下降；二是现有视觉锚定方案要么用文本坐标丢失视觉细节，要么重插裁剪帧导致上下文大幅膨胀，推理效率低。
### 方法关键点
1. VideoLVR从相关视频时刻的局部区域构造隐式视觉证据，为中间推理步骤提供视觉支撑；
2. 设计视觉token预测目标，将视觉token重构建模为输入视频派生词汇表上的预测任务，统一视觉证据重构与文本生成的token预测框架，支持交错文本token与隐式视觉状态的推理；
3. 拓展至RL优化范式，将采样的视觉token与文本token共同作为动作，基于最终答案reward联合优化策略。
### 关键结果
在多个公开视频理解基准上效果优于现有方案，细粒度视觉推理任务提升尤为明显，且无显著多模态上下文膨胀开销
