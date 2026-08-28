---
title: Emotion Understanding in Streaming Video with Trajectory-Aware Reliability
title_zh: 融合轨迹感知可靠性的流视频情绪理解方法
authors:
- Qingsong Wang
- Qigong Lei
- Zitong Wang
- Bohan Yu
- Zhiang Dong
- Jian liu
- Weiqiang Wang
- Chang Yao
- Jingyuan Chen
affiliations:
- Zhejiang University
- Ant Group
- Innovation and Management Center, School of Software Technology (Ningbo), Zhejiang
  University
arxiv_id: '2608.26786'
url: https://arxiv.org/abs/2608.26786
pdf_url: https://arxiv.org/pdf/2608.26786
published: '2026-08-27'
collected: '2026-08-28'
category: Multimodal
direction: 多模态流处理 · 推理成本优化
tags:
- Multimodal Understanding
- Streaming Processing
- Cost-Effective Inference
- Emotion Recognition
- Trajectory Perception
one_liner: 提出轨迹感知可靠性框架TRACE，优化流视频情绪识别的准确率与推理成本平衡
practical_value: '- 可复用「双路径推理」架构：稳定低优先级请求走低延迟轻量通路，模糊高优请求触发重推理，适配电商直播实时互动、客服情绪识别等场景的算力分配

  - 可借鉴轨迹可靠性评估逻辑：除置信度/熵外，增加预测稳定性、类别切换频次特征，优化动态内容（如直播弹幕、实时搜索query序列）的识别准确率

  - 可复用流数据处理trick：基于前缀数据先出初步结果，后续上下文到后仅对不稳定结果重解释，降低实时任务端到端延迟，适合实时推荐、流式内容审核场景'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频情绪理解多基于离线全片段输入建模，无法适配实时交互场景下仅能获取不完整流数据、需要低延迟决策的需求，且单步前缀预测即使置信度高，也可能因信念轨迹不稳定、类别反复切换出现误判。

### 方法关键点
提出TRACE轨迹感知可靠性框架：1）从流音频前缀生成低延迟初步情绪信念；2）基于置信度、熵、稳定性、类别切换模式4类特征评估预测可靠性；3）仅对不可靠预测触发多模态重推理，引入视觉、文本、相邻上下文信息修正结果，稳定预测留在低延迟通路。

### 关键结果
在StreamMER、MELD、MER2024三个基准数据集上，大幅降低不必要的上下文推理开销，同时保留90%+全上下文推理的精度收益，实现精度与推理成本的最优平衡。
