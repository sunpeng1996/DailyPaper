---
title: 'LAION-BVD: A 10-Million-Hour Open Video Dataset for Multimodal Pre-training'
title_zh: LAION-BVD：千万小时级多模态预训练公开视频数据集
authors:
- Andreas Hochlehnert
- Marianna Nezhurina
- Mehdi Cherti
- Andrej Radonjic
- Thaddäus Wiedemer
- Christoph Schuhmann
- Romain Beaumont
- Wieland Brendel
- Bernhard Schölkopf
- A. Sophia Koepke
affiliations:
- University of Tübingen
- LAION
- JSC, FZJ
- MPI for Intelligent Systems
- Technical University of Munich
arxiv_id: '2608.24845'
url: https://arxiv.org/abs/2608.24845
pdf_url: https://arxiv.org/pdf/2608.24845
published: '2026-08-24'
collected: '2026-08-27'
category: Multimodal
direction: 多模态预训练 · 大规模公开视频数据集
tags:
- Multimodal Pre-training
- Open Video Dataset
- Video-text Retrieval
- Audio-text Retrieval
- Frame Extraction
one_liner: 开源总时长1000万小时的大规模多模态视频数据集，支持音视频、图文多任务预训练
practical_value: '- 短视频/直播电商多模态召回排序模型可复用该数据集做预训练基座，降低自有标注数据依赖

  - 内容感知场景检测+自动生成音视频字幕的流水线，可复用在自有短视频内容的标签自动化生产环节

  - 从视频抽取场景切换帧补充图文训练数据的方法，可扩充电商商品短视频对应的图文样本库，提升图文检索效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有公开多模态数据集以图文为主，大规模音视频公开数据集规模远不足支撑开源多模态大模型的预训练需求，商业化数据集获取成本极高。

### 方法关键点
从CommonCrawl采集13亿条视频URL，清洗后下载得到8000万条、总时长1000万小时的合规视频；基于内容感知场景检测抽取独立视频片段，自动合成对应音视频字幕；额外抽取场景切换帧作为补充图文训练数据。

### 关键结果
基于该数据集训练的模型在视频-文本、音频-文本标准基准上达到竞争力性能，效果随训练规模、模型规模扩大稳定提升；抽取的场景切换帧训练的模型在图文检索任务上表现优异，视觉分布与普通网页图文数据集形成互补。
