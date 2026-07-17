---
title: 'KeyFrame-Compass: Towards Comprehensive Evaluation of Keyframe-Conditioned
  Video Generation'
title_zh: KeyFrame-Compass：面向关键帧条件视频生成的综合评估基准
authors:
- Yuqi Tang
- Tengfei Liu
- Yizheng Lai
- Yuran Wang
- Yang Shi
- Wanshun Su
- Zhuoran Zhang
- Qixun Wang
- Xiaohan Zhang
- Xinlei Yu
affiliations:
- HKUST(GZ)
- PKU
- RUC
- THU
- Kling Team
arxiv_id: '2607.14202'
url: https://arxiv.org/abs/2607.14202
pdf_url: https://arxiv.org/pdf/2607.14202
published: '2026-07-14'
collected: '2026-07-17'
category: Eval
direction: 多模态生成 · 视频生成评测
tags:
- Video Generation
- Evaluation Benchmark
- Keyframe Conditioning
- MLLM
- Automated Metrics
one_liner: 首个关键帧条件视频生成综合评测基准，含多维度数据集与自动化评估框架
practical_value: '- 电商商品短视频生成场景可复用6维关键帧执行度指标，校验AI生成视频是否符合预设的首帧、卖点帧、尾帧等强制要求

  - 多模态生成效果评估可复用「MLLM证据化判决+专用感知模型增强」的自动化框架，大幅降低人工标注成本

  - 构建业务场景生成评测集时可参考其多控制变量设计，覆盖不同约束密度、输入格式等边界场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
关键帧引导的视频生成已成为主流范式，但当前缺乏统一评测基准，无法客观衡量模型还原预设关键帧的准确度与整体视频生成质量。
### 方法关键点
1. 发布KeyFrame-Compass基准，含386个精标样本，覆盖3个应用领域、2种视频结构、2种提示粒度、2种条件格式、4种关键帧密度，支持多场景可控分析
2. 提出自动化评估框架：将关键帧执行度拆解为存在性、保真度、时序顺序、定位、持久性、独特性6个互补指标，结合证据驱动的MLLM判决与专用感知模型评估整体视频质量
### 关键结果数字
对9款代表性视频生成系统测试发现：模型在关键帧还原度与视频自然度间存在明显权衡；关键帧密度越高性能下降越显著，多数开源模型无法正确解析故事板网格输入的时序顺序
