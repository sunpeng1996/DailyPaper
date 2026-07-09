---
title: 'CompressedVQA-AEV: Full-Reference and No-Reference Quality Assessment Models
  for Asymmetric Encoded Videos'
title_zh: CompressedVQA-AEV：面向非对称编码视频的全参考/无参考质量评估模型
authors:
- Wei Sun
- Xingwei Liu
- Dandan Zhu
- Xiangyang Zhu
- Weixia Zhang
- Guangtao Zhai
affiliations:
- East China Normal University
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2607.04606'
url: https://arxiv.org/abs/2607.04606
pdf_url: https://arxiv.org/pdf/2607.04606
published: '2026-07-06'
collected: '2026-07-09'
category: Other
direction: 非对称编码视频质量评估
tags:
- Video Quality Assessment
- Asymmetric Encoding
- Swin Transformer
- SigLIP2
- Model Ensembling
one_liner: 针对非对称编码视频提出两款VQA模型，获QoMEX 2026挑战赛FR赛道第一、NR赛道第四
practical_value: '- 电商短视频/直播ROI编码场景可复用该VQA方案，在不牺牲用户观看体验的前提下降低带宽成本

  - 无参考VQA的SigLIP2+Swin-B双编码器+时序平均池化组合可直接迁移到无标注视频质量打分任务

  - 跨折集成策略可用于小样本视频标注场景下的模型效果提升，减少人工标注成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有VQA模型大多基于对称编码视频训练，无法适配当前广泛应用的ROI非对称编码（重点区域高码率、背景低码率）场景的质量评估，相关评估指标可靠性存在明显缺口。

### 方法关键点
全参考（FR）模型采用Swin-B骨干提取参考视频与失真视频的多阶段相似度统计特征，直接预测质量得分；无参考（NR）模型采用SigLIP2+Swin-B双互补帧级编码器提取单帧特征，经时序平均池化聚合时域信息，结合交叉折集成策略实现无参考数据下的感知质量评估。

### 关键结果数字
FR模型在QoMEX 2026挑战赛FR赛道排名第1，NR模型在NR赛道排名第4，完整方案已开源。
