---
title: 'Principia: Relational Physics Tests for Video Models'
title_zh: Principia：面向视频模型的关系物理测试基准
authors:
- Varun Varma Thozhiyoor
- Shivam Tripathi
- Venkatesh Babu Radhakrishnan
- Anand Bhattad
affiliations:
- Indian Institute of Science
- Johns Hopkins University
arxiv_id: '2609.04200'
url: https://arxiv.org/abs/2609.04200
pdf_url: https://arxiv.org/pdf/2609.04200
published: '2026-09-02'
collected: '2026-09-05'
category: Eval
direction: 视频模型物理推理能力评估
tags:
- VideoGeneration
- EvaluationBenchmark
- PhysicalReasoning
- VisionLanguageModel
- ModelEvaluation
one_liner: 提出无需校准的配对物体关系一致性视频模型物理推理能力评估基准
practical_value: '- 电商商品3D/AR演示视频生成场景，可复用配对物体相对物理一致性校验逻辑，无需复杂相机校准即可快速检测生成视频的物理bug

  - 迭代视频生成模型的物理合规性时，可直接适配Principia的8类物理现象测试集，覆盖商品掉落、碰撞等真实业务场景

  - UGC短视频物理造假检测场景，可复用校准无关的一致性评分逻辑，降低算力与数据标注成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频模型物理推理评估依赖绝对运动测量，受帧率、物体尺度、相机校准参数约束，生成视频中这类参数往往缺失或模糊，评估难以落地。

### 方法关键点
1. 基于同场景配对物体运动关系一致性做评估，物理规律约束的相对关系不受校准参数影响
2. 发布Principia基准，覆盖重力、restitution、摩擦、转动惯量等8类牛顿物理现象，包含平移、旋转、碰撞、振荡4类动力学的受控真实场景
3. 设计无需校准的一致性评分，直接在图像空间量化物理违规程度

### 关键结果数字
6款SOTA视频生成模型在Principia上最高分仅0.42，而其VBench得分均约0.8；VLM检测物理违规的最高准确率仅67%，多数模型接近随机水平
