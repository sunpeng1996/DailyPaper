---
title: 'BOP-Refer: Benchmark for Monocular 3D and 2D Object Grounding'
title_zh: BOP-Refer：单目3D与2D物体指代定位基准数据集
authors:
- Tomas Hodan
- Vineet Bhat
- Martin Sundermeyer
- Jonathan Tremblay
- Yash Patel
- Médéric Fourmy
- Stephen Tyree
- Junwen Huang
- Varun Burde
- Martin Cífka
affiliations:
- Mistral
- NYU
- Google
- NVIDIA
- CTU Prague
arxiv_id: '2611.34862'
url: https://arxiv.org/abs/2611.34862
pdf_url: https://arxiv.org/pdf/2611.34862
published: '2026-11-25'
collected: '2026-11-27'
category: Multimodal
direction: 多模态VLM · 物体定位基准评测
tags:
- VLM
- 3D Object Grounding
- Benchmark
- Monocular Vision
- Referring Expression
one_liner: 首个覆盖日常与工业物体的单目2D/3D指代定位基准，完成17款主流VLM系统性评测
practical_value: '- 电商AR导购、虚拟试搭场景的3D物体定位任务可参考本基准的VLM评测结果选型

  - 多模态商品检索中query到2D/3D商品框映射的标注流程可复用本数据集的构建逻辑

  - 3D定位误差核心来自深度估计的结论可指导业务优先引入物体尺寸先验优化推理'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有VLM的2D/3D指代定位能力缺乏统一评测基准，机器人、AR、多模态交互等落地场景无标准化性能验证依据。
### 方法关键点
整合9个BOP数据集的日常、工业物体图像，配套VLM生成+人工校验的指代表达式，基于3D模型与6DoF位姿标注生成高精度2D/3D bounding box真值，构建BOP-Refer评测基准；对Gemini、GPT、Claude、Qwen、Gemma等系列共17款前沿VLM开展全维度评测。
### 关键结果数字
最优模型Gemini 4 Carbon的2D任务AP_IoU2D达72.6%，但3D任务AP_IoU3D仅12.4%；3D定位误差核心为深度估计偏差，超过物体本身尺寸，依赖可靠物体尺寸先验的metric尺度估计是当前最大性能瓶颈。
