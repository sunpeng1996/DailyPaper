---
title: 'GRNEdit: Efficient General Video Editing from a New Binary-Evidence Perspective
  in Generative Refinement Networks'
title_zh: GRNEdit：生成式精炼网络二进制证据视角的高效通用视频编辑
authors:
- Feng Xie
- Jiagao Hu
- Fuhao Li
- Zepeng Wang
- Yuxuan Chen
- Dahua Gao
- Fei Wang
- Daiguo Zhou
affiliations:
- Xidian University
- MiLM Plus, Xiaomi Inc.
arxiv_id: '2608.16328'
url: https://arxiv.org/abs/2608.16328
pdf_url: https://arxiv.org/pdf/2608.16328
published: '2026-08-16'
collected: '2026-08-19'
category: Multimodal
direction: 多模态生成·通用视频编辑
tags:
- VideoEditing
- GenerativeRefinementNetwork
- BinaryRepresentation
- LightweightFinetune
- MultimodalGeneration
one_liner: 基于二进制证据视角提出轻量两阶段视频编辑框架，低参数开销下性能超越更大参数量同类模型
practical_value: '- 电商短视频/商品图编辑场景可复用二进制表征压缩思路，降低生成编辑任务的推理资源开销，适配端侧短视频批量生成需求

  - 借鉴null-prompt训练范式做内容保留约束，可迁移到商品风格迁移、背景替换、卖点叠加等业务场景，减少原商品主体信息失真

  - 主干冻结+新增轻量编码器的微调方案仅需调整<3%参数即可适配下游生成任务，大幅降低垂直场景生成模型的微调成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有指令驱动通用视频编辑方法依赖 heavyweight 条件分支或源内容拼接，资源开销高，缺少高效的编辑意图建模方案。
### 方法关键点
- 将编辑语义转化为二进制表征的局部保留/翻转决策，源信息建模为坐标级二进制状态证据，GRN主干负责全局组合生成连贯语义
- 阶段一用紧凑型编码器将离散源编码转为连续证据信号输入GRN，引入null-prompt训练：空指令对应不编辑，通过源重构监督强化内容保留能力
- 阶段二对比编辑状态与同源保留状态的表征差异，修正未决目标位决策，整个训练过程仅微调<3%的条件参数
### 关键结果
仅用0.6M训练样本对，GRNEdit-2B在OpenVE-Bench得分4.03，性能优于多个14B参数量开源编辑器；GRNEdit-8B得分4.18，追平头部开源视频编辑模型。
