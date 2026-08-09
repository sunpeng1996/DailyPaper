---
title: Audio-to-Score Transcription using Pre-trained Features, Data Augmentation,
  and the New SheetSage-A2S Dataset
title_zh: 基于预训练特征、数据增强与SheetSage-A2S数据集的音频转乐谱转录
authors:
- Eoin Cummins
- Zhongyi Huang
- Alexandre D'Hooge
- Zhuoro Mo
- Yaolong Ju
affiliations:
- University College Dublin
- Guangxi Normal University
- Great Bay University
- Shenzhen University
arxiv_id: '2608.06165'
url: https://arxiv.org/abs/2608.06165
pdf_url: https://arxiv.org/pdf/2608.06165
published: '2026-08-06'
collected: '2026-08-09'
category: Multimodal
direction: 多模态音乐处理 · 音频转乐谱转录
tags:
- Audio-to-Score
- Pre-trained Feature
- Data Augmentation
- Multimodal Dataset
- Music Computing
one_liner: 发布首个流行音乐音频转乐谱公开数据集，结合预训练特征与数据增强实现A2S任务SOTA效果
practical_value: '- 跨模态内容理解任务可复用「领域预训练特征提取器+场景适配数据增强」的通用架构，降低标注数据依赖，提升泛化性

  - 音乐类内容平台/电商（如乐器、数字音乐售卖）可直接复用开源MuQ模型与SheetSage-A2S数据集开发音乐内容理解、UGC审核能力

  - 垂类任务缺乏公开基准时可参考其思路：先构建大规模标注数据集，再给出可复现baseline，快速推进行业迭代'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音频转乐谱（A2S）系统研发多聚焦古典音乐场景，流行音乐领域相关研究极度匮乏，且缺少公开标注数据集支撑技术落地。

### 方法关键点
1. 构建发布SheetSage-A2S数据集：包含6066首唯一歌曲的9468条音频片段，总时长61小时，配套**kern格式标准化乐谱编码，是全球首个面向流行音乐A2S任务的公开基准数据集
2. 优化A2S模型架构：采用音乐领域预训练音频特征提取模型MuQ抽取有效特征，搭配针对性数据增强策略，大幅提升模型跨场景泛化能力

### 关键结果
- 古典音乐Quartets测试集上SER达4.98%，较此前SOTA的15.3%实现大幅提升
- 自研流行音乐SheetSage-A2S测试集上SER达20.92%，为后续流行音乐A2S研究提供强基准
