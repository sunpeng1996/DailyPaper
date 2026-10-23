---
title: 'WeVisOne-VL: Unified Visual Perception from Objects to Pixels'
title_zh: WeVisOne-VL：统一对象级到像素级的多任务视觉感知模型
authors:
- Tianming Liang
- Junyi Pan
- Yuxi Li
- Canmiao Fu
- Zhipeng Huang
- Chong Sun
- Chen Li
- Jing Lyu
affiliations:
- Tencent Inc. WeChat Vision
arxiv_id: '2610.31329'
url: https://arxiv.org/abs/2610.31329
pdf_url: https://arxiv.org/pdf/2610.31329
published: '2026-10-21'
collected: '2026-10-23'
category: Multimodal
direction: 多模态视觉语言模型 · 统一感知
tags:
- VLM
- Unified Perception
- Object Detection
- Segmentation
- OCR
- Matting
one_liner: 腾讯微信团队推出统一对象级与像素级感知的多任务VLM，在30+基准上实现同规模最优性能
practical_value: '- 电商场景可直接复用本模型实现商品检测、OCR识别、主体抠图、多模态商品检索的端到端处理，替换现有多模型串联方案，降低部署复杂度与延迟

  - 三阶段课程SFT+混合任务RL的训练范式可迁移至多目标推荐系统训练，先分阶段对齐单任务目标再用RL优化全局业务目标，缓解任务冲突

  - 数据引擎中知识图谱引导的概念对齐、难例筛选、跨任务实例关联方法，可复用在推荐系统训练数据构造，提升长尾/低质样本的标注质量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有VLM在细粒度视觉感知任务上可靠性不足，常出现幻觉、用户意图理解错误、非显著实例漏检问题，且需要多个专用模型串联才能覆盖从对象检测到像素抠图的全链路需求，部署成本高、性能对齐难，无法满足工业场景的统一感知需求。

### 方法关键点
- 数据引擎：构建覆盖1亿张图、36亿标注的统一数据流水线，通过知识图谱关联类目概念与指代表达式，融合多专家预测结果生成检测、分割、抠图的跨任务对齐标注，基于模型错误迭代挖掘难例优化数据集
- 模型架构：基于Qwen3-VL扩展，新增专用坐标编码Token与<OBJ>桥接Token，插入9.6M参数量的轻量像素解码器，实现检测、OCR等离散任务与分割、抠图等像素任务的统一输出
- 训练流程：采用三阶段课程SFT+混合任务GRPO RL训练，先对齐任务输出格式，再提升高分辨率/密集场景感知能力，最后关联<OBJ>Token与像素解码器，RL基于全局定位奖励优化抑制幻觉与重复预测

### 关键结果
在30+基准上对比Qwen3-VL、Rex-Omni、LocateAnything等同规模VLM：Dense200密集检测平均F1达71.3%，超基线最高12.6pct；RefCOCOg指代检测平均F1达81.8%，负例拒绝率达67.4%；MixCount计数任务准确率达40.4%，超基线最高25.2pct；SROIE OCR平均F1达68.1%，超基线最高23.3pct；语言引导抠图WeRefMat数据集SAD指标仅39.0，仅为基线的24%。

**最值得记住的一句话**：统一多粒度视觉感知的核心是用桥接Token打通离散语言输出与连续像素预测的链路，结合课程训练与RL可以在单模型内实现多任务性能的同步提升。
