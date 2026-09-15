---
title: 'BVB: Benchmarking Agentic Video Understanding via Programmatic Reconstruction
  in Blender'
title_zh: BVB：基于Blender程序化重建的智能体视频理解基准
authors:
- Yolo Y. Tang
- Daiki Shimada
- Jiayue Meng
- Jing Bi
- Pinxin Liu
- Yicheng Wang
- Yunzhong Xiao
- Zhangyun Tan
- Zeliang Zhang
- Chao Huang
affiliations:
- University of Rochester
- Sony Group Corporation
- Carnegie Mellon University
- University of Washington
arxiv_id: '2609.15478'
url: https://arxiv.org/abs/2609.15478
pdf_url: https://arxiv.org/pdf/2609.15478
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: 多模态智能体 · 视频理解评测
tags:
- Multimodal Agent
- Video Understanding
- Benchmark
- Programmatic Generation
- Evaluation
one_liner: 提出通过Blender程序化重建评估多模态智能体视频理解能力的基准BVB与配套评测框架
practical_value: '- 多模态Agent效果评测可参考双维度评估逻辑：用事实类VQA测语义准确度，用隐向量相似度测感知匹配度，兼顾客观事实和主观体验

  - 生成类任务的公平评测可借鉴统一沙箱+成本限制的框架，避免不同模型调用资源差异导致的结果偏差

  - 电商短视频/商品3D展示生成场景可复用程序化重建思路，相比扩散模型生成的结果可编辑性更强，适合后期调整'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态Agent视频理解评测仅依赖问答任务，无法验证模型对视频时空要素的完整理解能力，缺少统一公平的标准化评测范式
### 方法关键点
1. 推出BVB基准，要求Agent通过Mini-BVB轻量工具链，在统一沙箱、共享成本限制下，将真实视频编程重建为可渲染的Blender动效场景
2. 采用双维度评估：Dual VQA度量重建结果的时空事实保留率，Latent Similarity度量重建内容与原视频的感知相似度，最终得分取二者平方根均值，鼓励平衡表现
### 关键结果
测试10个模型家族的51种配置，最优模型Latent Similarity达88.6，但时空事实保留率仅53.7%；额外推理步骤可提升感知相似度，但无法缩小事实准确率差距；15人盲测验证Latent Similarity与人类偏好强相关
