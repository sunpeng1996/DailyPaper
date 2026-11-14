---
title: 'Duo: A Reciprocal World Model for Full-Duplex Interaction'
title_zh: Duo：面向全双工交互的双向世界模型
authors:
- Hengyuan Cao
- Biao Gong
- Guoshan Lu
- Qiyuan Zhang
- Lin Liu
- Yiding Tian
- Yilei Jiang
- Yuxin Ma
- Chengzhang Wu
- Kun Chen
affiliations:
- InclusionAI
arxiv_id: '2611.15131'
url: https://arxiv.org/abs/2611.15131
pdf_url: https://arxiv.org/pdf/2611.15131
published: '2026-11-10'
collected: '2026-11-14'
category: Agent
direction: Agent 全双工交互世界模型设计
tags:
- World Model
- Full-Duplex Interaction
- Autoregressive Modeling
- Knowledge Distillation
- Multimodal Agent
one_liner: 提出双向世界模型RWM及Duo v1，支持多模态实时感知的全双工自然交互
practical_value: '- 电商直播导购、虚拟数字人客服类交互Agent可复用Intent（交互认知）+Realization（多模态行为生成）的模块拆分方案，降低实时多模态交互的研发复杂度

  - 全双工交互场景可直接复用分块注意力掩码+统一时间轴Token同步的设计，避免未来信息泄露，天然支持用户随时打断、插话的业务需求

  - 多模态交互模型训练时可借鉴双rollout蒸馏方法，同时在两个模块用自生成数据做训练，有效缓解训练推理分布偏移问题，提升交互稳定性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有世界模型仅聚焦物理现实模拟，将推理决策作为外挂控制模块，无法适配无键鼠、可打断的自然全双工实时交互需求。
### 方法关键点
1. 提出双向世界模型RWM，将智能体认知与物理现实视为世界的同等核心要素，拆分出Intent（交互认知推理）、Realization（音视频行为生成）两大核心模块；
2. 采用自回归建模实现连续交互推理与参与决策，替代扩散模型仅做指令理解的传统范式；
3. 设计分块专属条件、统一时间轴跨模块Token同步机制，搭配模块专属注意力掩码保障块内、块间因果依赖，避免访问未来输入；
4. 采用双rollout蒸馏方案，分别用自生成的Intent Token、合成音视频历史训练两个模块，缓解分布偏移。
### 关键结果
Duo v1可实时感知音频、视频、文本输入，支持自发对话、用户随时打断，覆盖实物交互、虚拟场景编辑、无键鼠音视频游戏等场景，已开源代码与模型权重。
