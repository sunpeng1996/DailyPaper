---
title: Dialogue-Aware Video-to-Music Generation Using Public Domain Film Collections
title_zh: 基于公域电影库的对话感知视频到音乐生成方法
authors:
- Haven Kim
- Zachary Novack
- Julian McAuley
- Hao-Wen Dong
affiliations:
- University of California San Diego
- University of Michigan
arxiv_id: '2608.11576'
url: https://arxiv.org/abs/2608.11576
pdf_url: https://arxiv.org/pdf/2608.11576
published: '2026-08-12'
collected: '2026-08-13'
category: Multimodal
direction: 多模态生成 · 视频到音乐生成
tags:
- Multimodal Generation
- Video-to-Music
- Dataset Construction
- Cross-Attention
- Public Domain Corpus
one_liner: 推出可复现无版权的OSSL-v2视频音乐数据集，提出融合对话信号的视频转音乐生成优化方案
practical_value: '- 电商短视频/内容平台的自动配乐场景，可参考将时序模态信号（如对话、旁白）逐帧调制cross-attention的设计，提升BGM与内容的匹配度；

  - 训练跨模态生成模型时，可优先整理无版权的公域自有数据集，规避爬取第三方内容的版权风险和链接失效问题；

  - 短视频配乐推荐场景可新增对话时序、语义特征作为匹配特征，提升推荐配乐和内容场景的契合度。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频转音乐生成研究多依赖爬取的YouTube等平台数据集，存在链接失效、版权风险高、实验可复现性差的痛点，且现有方法未利用影视内容中对话与配乐的强时序耦合关系。
### 方法关键点
1. 构建开源可复现的OSSL-v2公域电影数据集，包含34343条视频片段，总时长246.4小时，无版权风险可直接用于模型训练；
2. 优化现有模型的视频交叉注意力模块，新增时间轴维度，使用对话音轨逐帧调制注意力权重，将对话时序特征作为生成条件融入模型。
### 关键结果
在公域电影、商业电影两个测试集上，所提方法效果均优于当前SOTA基线。
