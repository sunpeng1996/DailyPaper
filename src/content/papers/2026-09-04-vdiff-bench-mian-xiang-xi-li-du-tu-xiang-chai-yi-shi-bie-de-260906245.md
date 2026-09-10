---
title: 'VDiff-Bench: A Challenging Benchmark for Fine-Grained Image Difference Identification'
title_zh: VDiff-Bench：面向细粒度图像差异识别的挑战性评测基准
authors:
- Yixin Wan
- Tianle Zheng
- Kai-Wei Chang
affiliations:
- University of California, Los Angeles
arxiv_id: '2609.06245'
url: https://arxiv.org/abs/2609.06245
pdf_url: https://arxiv.org/pdf/2609.06245
published: '2026-09-04'
collected: '2026-09-10'
category: Eval
direction: 多模态大模型 · 视觉理解能力评测
tags:
- MLLM
- Visual Understanding
- Benchmark
- Fine-grained Recognition
- Evaluation
one_liner: 构建覆盖10类细粒度差异的图像差异识别基准，诊断多模态大模型的视觉对比理解能力
practical_value: '- 电商商品主图瑕疵检测、AB版效果对比场景，可复用基准的10类细粒度差异分类体系优化检测规则

  - 多模态Agent做商品同质化识别、竞品图片对比的评测，可引入该基准的难负例构造方法提升测试鲁棒性

  - 涉及图片对比的多模态推荐场景（如同款差异识别、搭配差异推荐），可优先测试MLLM对低阶视觉变化的识别精度，规避选型踩坑'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态大模型（MLLM）在通用视觉理解任务（如VQA）表现优异，但细粒度图像差异识别能力薄弱，过往同类基准存在差异设计简单、评估指标可靠性低等问题，无法精准定位模型缺陷。

### 方法关键点
VDiff-Bench为四选一选择题式评测基准，包含1756组图像对样本，覆盖位置、运动、颜色、纹理、OCR、光照等10类细粒度变化；每个样本配1个真实差异、2个语义近邻难负例、1个「无差异」干扰项，采用规则化指标实现客观可复现的评估。

### 关键结果
11款开源/闭源SOTA MLLM整体表现脆弱：7-8B规模开源模型在语义类差异上准确率达52.5%~70.6%，但噪声/纹理等低阶变化准确率仅8.7%~33.3%；闭源模型Grok 4.3在噪声、纹理差异识别上的表现显著落后于Kimi K2.5/K3等开源大模型。
