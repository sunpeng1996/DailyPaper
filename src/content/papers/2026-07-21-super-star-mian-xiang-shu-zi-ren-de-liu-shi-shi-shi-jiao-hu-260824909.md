---
title: 'Super Star: Towards Streaming Real-time Interactive Agents for Digital Humans'
title_zh: Super Star：面向数字人的流式实时交互Agent
authors:
- Wentao Jiang
- Youchen Xie
- Haidi Fan
- Yajing Chen
- Xin Wang
- Ye Shi
- Jingya Wang
affiliations:
- ShanghaiTech University
- LIGHTSPEED
arxiv_id: '2608.24909'
url: https://arxiv.org/abs/2608.24909
pdf_url: https://arxiv.org/pdf/2608.24909
published: '2026-07-21'
collected: '2026-08-27'
category: Agent
direction: 数字人交互Agent · 低延迟流式推理
tags:
- Digital Human
- Streaming Inference
- Co-speech Gesture
- Real-time Agent
- Continual Learning
one_liner: 提出耦合流式语音与在线手势生成的低延迟数字人实时交互Agent架构
practical_value: '- 因果多模态自回归的低延迟流式推理设计可直接复用在电商直播数字人、导购虚拟Agent等实时交互场景，无需依赖未来输入即可生成语音同步的动作/文本输出

  - 离线主题/情感感知语料合成+在线用户反馈自进化训练闭环可复用在垂直领域虚拟Agent的持续迭代，大幅降低人工标注成本，快速适配特定用户群体偏好

  - 离线训练与在线部署的gap bridging思路可迁移至实时对话推荐、实时广告文案生成等有严格低延迟要求的生成类业务，兼顾输出质量与响应速度'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有共语音手势生成方法均为离线方案，依赖完整语音段甚至未来语音信息，推理延迟高，无法满足真实场景中数字人实时交互的严格低延迟要求。
### 方法关键点
1. 提出流式语音响应模块与在线手势生成模块耦合的实时交互框架，手势生成器采用因果多模态自回归结构，仅基于当前流式语音输入和历史动作生成同步手势，无需访问未来语音
2. 配套虚拟陪伴场景专属离线数据合成管线，基于主题、情感感知的主体语料库构建多样化人机对话，生成与Agent响应对应的共语音手势
3. 搭建自进化训练闭环，将在线交互收集的用户反馈接入数据生成流程，实现对用户偏好的持续适配
### 关键结果
相比现有最优基线，延迟-质量权衡表现更优，语音-动作同步性更强，用户偏好度显著高于对比方案
