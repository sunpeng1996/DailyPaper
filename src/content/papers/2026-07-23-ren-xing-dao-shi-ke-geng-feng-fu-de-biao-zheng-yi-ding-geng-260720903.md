---
title: 'Sidewalk Moments: Are Richer Representations Always More Human-Aligned? Evidence
  from City-Walk Videos'
title_zh: 人行道时刻：更丰富的表征一定更贴合人类感知？来自城市步行视频的证据
authors:
- Liu Liu
- Freya Huying Tan
- Fábio Duarte
affiliations:
- Massachusetts Institute of Technology
- MIT City Form Lab
- MIT Senseable City Lab
arxiv_id: '2607.20903'
url: https://arxiv.org/abs/2607.20903
pdf_url: https://arxiv.org/pdf/2607.20903
published: '2026-07-23'
collected: '2026-07-25'
category: Other
direction: 多模态表征 · 人类对齐效果评估
tags:
- Multimodal Representation
- Human Alignment
- Video Encoding
- Temporal Compression
- Perceptual Evaluation
one_liner: 通过城市步行视频多模态对比，验证时序平均图像可在二分类任务中媲美甚至超过全视频特征的人类对齐效果
practical_value: '- 做短视频内容推荐/广告素材优选时，对静态构图主导的素材可采用时序平均图像（TAI）替代全视频编码，大幅降低推理算力开销

  - 训练人类偏好对齐的多模态排序模型时，可按场景拆分特征：动态内容用全视频特征，静态结构主导内容用TAI特征，兼顾效果和效率

  - 做多模态召回特征选型时，不要默认选择复杂度更高的表征，需结合任务范式（连续打分/二分类）做AB验证再选型'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
业界普遍默认表征丰富度越高（如全视频时空特征），人类对齐效果越好，缺乏不同任务范式下的效果对比验证，算力开销冗余问题突出。
### 方法关键点
采集61条第一视角城市步行视频，切分为5万+10秒片段，分别提取四类表征：时空视频特征、时序平均图像（TAI）、audio embedding、文本语义描述，结合Spearman相关性分析、二分类任务、AMT人工标注对比不同表征的人类对齐效果。
### 关键结果数字
- 连续对齐任务中视频特征相关性最高
- 二分类高/低参与度任务中TAI效果持平甚至优于全视频，人工测试验证两者判断精度相当，文本效果下降显著，音频判断准确率接近随机
- 动态活动主导场景视频特征效果更优，静态结构主导场景TAI人类对齐效果更好
