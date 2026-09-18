---
title: Can MiniMax-H3 Reason About the Physical World? An Evaluation of Omni-Modal
  Generative Model
title_zh: MiniMax-H3能否对物理世界推理？全模态生成模型评估
authors:
- Haoyu Zhao
- Zihao Zhao
- Tianyu Deng
- Ziqin Xu
- Zihao Zhang
- Xudong Wang
- Jinxiang Guo
- Chen Gao
- Ziyi Ye
- Yeying Jin
affiliations:
- National University of Singapore
- Fudan University
- Tencent
arxiv_id: '2609.18323'
url: https://arxiv.org/abs/2609.18323
pdf_url: https://arxiv.org/pdf/2609.18323
published: '2026-09-15'
collected: '2026-09-18'
category: Eval
direction: 全模态生成模型 · 推理能力评估
tags:
- Omni-modal
- Model Evaluation
- Physical Reasoning
- Multimodal Alignment
- Generative Model
one_liner: 构建四维度全模态物理世界推理评估框架，实测MiniMax-H3跨模态推理表现
practical_value: '- 跨模态推理评估框架可直接复用至多模态商品理解、多模态搜索结果相关性评估场景，4种输入模态组合范式可直接套用到用户多模态Query理解的任务设计上

  - 实测结论显示音频模态的歧义消解推理准确率最低，做多模态内容生成/推荐时可优先优化音频-视觉跨模态对齐模块，降低音频信息缺失带来的推理误差

  - 多模态互补信息联合推理的范式可迁移到Agent现实场景决策任务中，例如下线导购Agent基于视频+音频+文本的综合用户意图判断'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有全模态生成模型的评估范式多受限于输入模态少、要求prompt与目标内容高度匹配，无法衡量模型基于多模态互补信息的物理世界推理能力，亟需适配全模态输入的新型评估体系。
### 方法关键点
构建覆盖4种多模态输入场景的物理世界推理评估框架：包括隐式prompt+多帧、音频-图像、前缀视频、音频-视频输入，每个场景下单模态仅提供部分事件证据，要求模型整合跨模态语义线索推理事件隐状态与未来动态，共设计517个评估实例。
### 关键结果
MiniMax-H3整体成功率达41.97%，其中基于视频的决策推理表现最优，成功率为56.00%；基于音频的歧义消解推理表现最差，仅27.40%，验证了高效跨模态融合是发挥全模态输入价值的核心瓶颈。
