---
title: 'FATE: Frame-Level Audio-Visual Temporal Embedding'
title_zh: FATE：帧级音视频时序嵌入模型
authors:
- Kaisi Guan
- Bingzi Zhang
- Xihua Wang
- Ying Ba
- Xin Cheng
- Yijing Chen
- Ruihua Song
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2608.01310'
url: https://arxiv.org/abs/2608.01310
pdf_url: https://arxiv.org/pdf/2608.01310
published: '2026-08-01'
collected: '2026-08-10'
category: Multimodal
direction: 多模态表征 · 音视频时序对齐
tags:
- Multimodal Embedding
- Audio-Visual Learning
- Temporal Alignment
- Contrastive Learning
- Zero-shot Learning
one_liner: 提出同时捕获语义与时序对齐能力的帧级音视频联合嵌入框架，多任务性能大幅超越现有基线
practical_value: '- 电商短视频/直播内容质检：基于FATE的帧级音视频对齐能力，做口播与画面/商品卖点的时序匹配校验，检测虚假宣传、音画不同步等低质内容，降低合规风险

  - 短视频推荐表征优化：替换现有将全视频池化为单embedding的多模态表征方案，保留帧级时序信息，提升好物演示、教程类强时序关联短视频的召回排序精度

  - 多模态Agent感知模块升级：复用FATE的跨语义+时序联合对比训练范式微调现有多模态编码器，提升Agent对音视频类指令的时序语义理解能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有音视频建模方法存在明显短板：语义嵌入类模型将各模态池化为单embedding，丢失细粒度时序信息；时序同步类模型仅输出偏移预测，缺少语义理解能力，无法同时覆盖语义匹配与时序对齐需求。
### 方法关键点
1. 保留音视频帧级序列，基于物理时间线严格对齐后计算帧对相似度，不做全模态全局池化；
2. 采用跨视频语义对比学习+视频内时序对比学习的联合训练目标，将时序同步信息编码到可复用的嵌入空间，而非仅输出偏移预测值。
### 关键结果
- 时序、语义检索任务性能大幅超越最强基线；
- 零样本事件定位效果与全监督方法持平；
- 作为生成评估指标时，与人类判断的相关性达到最优水平。
