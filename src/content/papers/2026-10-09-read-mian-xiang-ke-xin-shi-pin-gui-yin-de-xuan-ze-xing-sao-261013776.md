---
title: 'READ: Reading the Selective Scan for Faithful Video Attribution'
title_zh: READ：面向可信视频归因的选择性扫描解读方法
authors:
- Magdalena Trędowicz
- Piotr Kubaty
- Arkadiusz Lewicki
- Jacek Tabor
- Łukasz Struski
affiliations:
- Jagiellonian University
- University of Information Technology and Management in Rzeszów
- Centre for Credible AI, Warsaw University of Technology
arxiv_id: '2610.13776'
url: https://arxiv.org/abs/2610.13776
pdf_url: https://arxiv.org/pdf/2610.13776
published: '2026-10-09'
collected: '2026-10-14'
category: Multimodal
direction: 多模态可解释 · SSM序列归因
tags:
- SSM
- Video Attribution
- Interpretability
- Selective Scan
- Long Sequence Modeling
one_liner: 提出无参数选择性状态空间模型视频归因方法，仅需单次前向传播即可获得高保真时空相关性映射
practical_value: '- 对采用SSM（如Mamba）做长序列用户行为建模的推荐/广告场景，可借鉴READ的无参数归因思路，仅需单次前向即可回溯用户行为序列中对推荐结果贡献最高的item，大幅降低可解释性模块的推理开销

  - 对需要做序列归因的业务（如召回/排序结果可解释、低价值行为过滤），可复用「锚定输出层读头反推序列各token贡献」的设计，规避多轮反向传播或重复推理的高成本

  - 可迁移到长序列用户行为建模的偏差排查：借鉴READ无系统性偏差的归因逻辑，定位SSM序列建模中存在的特征偏误、训练数据偏差问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
Selective SSM是长序列视频建模的高效方案，但循环计算特性导致难以定位驱动预测的核心视频token，现有归因方法需额外反向传播或多次推理，开销远高于正向推理，无法落地低延迟场景。
### 方法关键点
1. 提出无参数归因方法READ，无需修改模型结构，在分类器读头读取的位置展开循环，将循环状态中累积的贡献回溯至对最终预测有贡献的视频token
2. 锚定分类器读出生成单张时空相关性映射，可直接输出帧级、区域级相关性结果，全程仅需1次前向传播，无额外推理开销
### 关键结果
与开销高出数个量级的现有SOTA归因方法相比，保真度、定位能力表现相当，可规避现有方法的系统性相关性偏差，在多数据集、多骨干网络上均能还原有效的时序、类别专属结构。
