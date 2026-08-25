---
title: What's the Catch? Evaluating Temporal Consistency in Vision-Language Models
title_zh: 视觉语言模型时间一致性能力评估基准TimeCatch
authors:
- Marek Hradil
- Danae Sánchez Villegas
affiliations:
- University of Copenhagen
arxiv_id: '2608.23474'
url: https://arxiv.org/abs/2608.23474
pdf_url: https://arxiv.org/pdf/2608.23474
published: '2026-08-24'
collected: '2026-08-25'
category: Eval
direction: 多模态VLM时序一致性能力评估
tags:
- VLM
- Temporal Consistency
- Anomaly Detection
- Benchmark
- Multimodal Evaluation
one_liner: 提出TimeCatch基准测试发现当前VLMs可识别单帧异常，跨帧时间一致性推理能力接近随机水平
practical_value: '- 短视频推荐/广告理解场景不要依赖通用VLMs做时序合理性校验，判断广告剪辑连贯性、商品展示时序合理性需额外补充时序规则模块

  - 电商内容审核场景中，单帧违规画面可直接用VLM检测，涉及时序造假（如虚假商品使用前后对比拼接）的场景需引入专门时序建模模块

  - 具身Agent、直播内容理解等需时序推理的场景，通用VLMs时序能力不足，需针对性做时序微调或额外引入时序特征抽取模块'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前VLMs在视频/图像序列基准任务上表现优异，但其时序结构捕捉能力缺乏系统、可控的评估，时序一致性推理的能力边界不明确。
### 方法关键点
将时序接地任务转化为异常检测问题，提出TimeCatch可控评估基准：通过交换连续帧构造时序异常，替换单帧为高斯噪声构造帧级异常，在4个合成及真实数据集上测试模型的异常检测与定位能力，同时开展人类对照实验。
### 关键结果数字
- VLMs帧级异常检测、定位准确率接近饱和，但时序异常检测性能接近随机水平，时序异常定位仅略高于随机
- 人类在两类任务上均达到接近天花板的性能
- 调整模型规模、prompt策略、序列长度、视觉相似度等变量，均无法显著改善VLMs的时序推理缺陷
