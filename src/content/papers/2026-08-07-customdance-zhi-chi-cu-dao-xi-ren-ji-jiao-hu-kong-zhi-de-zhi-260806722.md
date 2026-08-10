---
title: 'CustomDance: Customized 3D Dance Generation with Coarse-to-Fine Human-Centered
  Interactive Control'
title_zh: CustomDance：支持粗到细人机交互控制的定制化3D舞蹈生成方法
authors:
- Xulong Tang
- Kaixing Yang
- Xiaohu Guo
- Prabhakaran Balakrishnan
- Rawan Alghofaili
affiliations:
- University of Texas at Dallas, USA
- MalouTech Inc, USA
- University at Albany, USA
arxiv_id: '2608.06722'
url: https://arxiv.org/abs/2608.06722
pdf_url: https://arxiv.org/pdf/2608.06722
published: '2026-08-07'
collected: '2026-08-10'
category: Multimodal
direction: 多模态生成 · 人机交互式内容创作
tags:
- Multimodal Generation
- Human-in-the-loop
- Diffusion Model
- MLLM
- Interactive System
one_liner: 提出三阶段粗到细人机交互3D舞蹈生成系统，对齐用户创意意图且效果优于现有基线
practical_value: '- 粗到细的人机交互范式可复用在电商定制化内容生成场景（如AI生成直播舞蹈动作、定制商品展示动效），先锚定核心节点再补全细节，大幅降低用户控制门槛

  - 「大模型解析用户意图+检索库召回候选+生成模型补全」的三段式架构，可迁移到定制化文案生成、商品短视频生成等业务，兼顾生成可控性与效率

  - 多模态对齐的检索逻辑可复用到短视频平台的音乐-内容匹配推荐场景，提升内容与背景音的契合度'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有3D舞蹈生成方法无法精准响应用户多模态输入（音乐、动作描述），生成结果仅满足统计合理性，不符合用户创意预期，缺乏艺术表现力。
### 方法关键点
参考专业编舞流程，设计三阶段粗到细交互生成范式：1. 用MLLM解析音乐与高层文本prompt，提取时间锚点与创作线索；2. 多模态检索器针对每个锚点从舞蹈库召回匹配的优质动作片段，给用户提供可预测的可选方案；3. 音乐条件驱动的扩散补全模型无缝拼接选中的动作片段，支持用户迭代优化最终生成结果。
### 关键结果
定量、定性评估表现均优于现有竞争基线，大幅提升用户创作满意度，验证了AI辅助编舞范式的实用价值。
