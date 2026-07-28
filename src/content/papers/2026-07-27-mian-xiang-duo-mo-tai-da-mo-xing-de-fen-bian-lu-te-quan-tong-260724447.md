---
title: 'RP-OPSD: Resolution-Privileged On-Policy Self-Distillation for Multimodal
  Large Language Models'
title_zh: 面向多模态大模型的分辨率特权同策略自蒸馏方法RP-OPSD
authors:
- Qihui Zhu
- Yuchen Wang
- Zijian Wen
- Tao Zhang
- Mengjie Zhang
- Yang Liu
- Shuangwu Chen
- Siying Wu
- Jian Yang
- Xiaofeng Jiang
affiliations:
- University of Science and Technology of China
- ChangXin Memory Technologies, Inc.
arxiv_id: '2607.24447'
url: https://arxiv.org/abs/2607.24447
pdf_url: https://arxiv.org/pdf/2607.24447
published: '2026-07-27'
collected: '2026-07-28'
category: Multimodal
direction: 多模态大模型 · 自蒸馏训练优化
tags:
- MLLM
- Self-Distillation
- On-Policy Learning
- Knowledge Distillation
- Training Efficiency
one_liner: 利用同图高低分辨率能力差构造自蒸馏信号，无需额外标注提升MLLM性能且加速训练
practical_value: '- 电商多模态搜索/商品理解场景微调MLLM时，可复用该思路：用高分辨率商品图做teacher信号，低分辨率图做student输入，无需额外标注即可提升模型对缩略图、低清图的细节识别能力，同时降低训练成本

  - 开发多模态推荐Agent时，可借鉴该自蒸馏架构：无需额外标注或外部模型，仅构造输入的不同模态视图制造能力差做监督，即可低成本提升Agent的多模态理解精度

  - 训练多模态模型时，可直接复用带偏差修正的teacher-top-K reverse KL蒸馏目标，在减少蒸馏计算量的同时规避截断偏差，提升训练效率'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有On-Policy Self-Distillation（OPSD）依赖验证解轨迹、外部模型生成解释或人工标注视觉证据，无法低成本规模化应用到多模态大模型（MLLM）微调；同时MLLM对输入图像分辨率高度敏感，同模型在高低分辨率输入下存在天然能力差，该差异此前未被用作自蒸馏监督信号。
### 方法关键点
- 构造同图像的高低分辨率视图：student用1/2宽高（1/4像素）的低分辨率图生成on-policy轨迹，teacher用原始分辨率图作为特权信息，对student生成的同前缀提供token级分布监督
- 教师采用学生参数的指数移动平均（EMA）更新，无需单独训练教师模型
- 蒸馏目标使用带偏差修正的teacher-top-K reverse KL，仅对齐教师输出的top-K token分布，减少计算量同时规避截断偏差
### 关键结果
在Qwen3.5-4B、9B两个规模模型上验证，对比基线包括Base、SFT、GRPO、OPSD、Vision-OPD，训练仅用5.2K无标注图文对；9B模型原始分辨率推理平均性能相对Base提升5.45%，训练速度比传统OPSD快1.78倍；低分辨率推理平均性能提升6.09分，增益可完整迁移到原始分辨率推理。
最值得记住的一句话：利用同输入的不同视图天然存在的能力差构造自蒸馏信号，是无需额外标注、低成本提升模型能力的高性价比路径
