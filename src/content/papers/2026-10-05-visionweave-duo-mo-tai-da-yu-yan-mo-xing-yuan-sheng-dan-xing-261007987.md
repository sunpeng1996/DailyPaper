---
title: 'VisionWeave: Weaving Elastic Visual Representations as a Native Capability
  of MLLMs'
title_zh: VisionWeave：多模态大语言模型原生弹性视觉表征框架
authors:
- Yuan Feng
- Qize Yang
- Ruizhe Chen
- Sibo Song
- Haolin He
- Muzhi Zhu
- Zihan Liu
- Yunfei Chu
- Xize Cheng
- Yuxuan Wang
affiliations:
- 中国科学技术大学
- 阿里巴巴集团
- 香港中文大学
- 浙江大学
arxiv_id: '2610.07987'
url: https://arxiv.org/abs/2610.07987
pdf_url: https://arxiv.org/pdf/2610.07987
published: '2026-10-05'
collected: '2026-10-12'
category: Multimodal
direction: 多模态大模型 · 视觉效率优化
tags:
- MLLM
- Visual Token Compression
- Self-distillation
- Serving Optimization
- Multimodal Efficiency
one_liner: 提出VisionWeave为MLLM植入原生弹性视觉表征，平均省43%视觉token保98.9%性能适配SGLang服务
practical_value: '- 电商商品图/短视频理解场景可直接复用VisionWeave架构，在几乎不掉点前提下压缩视觉token，大幅降低多模态推荐、多模态搜索的推理成本

  - 三阶段自蒸馏训练范式可迁移到自定义多模态模型的效率优化，无需额外标注数据，仅用原生预训练模型作为教师即可植入压缩能力

  - SGLang适配方案可直接借鉴：通过位置坐标缩放兼容半整数RoPE编码，最小改动即可实现混合粒度序列的动态批处理、KV缓存管理

  - 可通过调整路由阈值动态平衡性能与成本，适配不同业务场景：商品搜索、OCR场景调低阈值保证精度，feed流推荐场景调高阈值提升吞吐'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有MLLM采用固定尺寸patch token编码视觉输入，处理高分辨率图像、长视频时序列长度激增，带来极高计算与内存开销；传统下采样、固定比例token剪枝方法要么丢失细粒度信息导致效果掉点严重，要么适配性差，难以兼容主流MLLM架构与服务基础设施，无法适配不同视觉内容的信息密度差异。
### 方法关键点
- 门控空间池器：在统一MRoPE坐标体系下同时生成原生细粒度视觉token与粗粒度压缩token，粗粒度token通过位置插值对齐到对应空间块几何中心，保证位置编码一致性
- 粒度路由器：跨ViT浅、中、深三层特征探测，为每个空间块自主决策采用细/粗粒度token，自适应匹配内容信息密度
- 三阶段自蒸馏训练：以原生MLLM作为教师，依次训练无需额外标注数据，依次完成池器训练、路由器训练、全链路微调，保证训练推理一致性
### 关键结果
- 在Qwen3.8-27B上8个多模态基准（覆盖图文问答、GUI交互、长视频理解等）平均节省43.0%视觉token，仅损失1.08%性能，远优于固定50%压缩的FastV（损失11.82%）、VisionZip（损失12.46%）
- 部署到SGLang服务引擎，长视频任务下实现2.30×端到端吞吐量提升，平均TTFT下降54.4%，平均TPOT下降60.6%
- 推理阶段可通过调整路由阈值动态控制压缩率，无需重训即可适配不同业务的效率/质量要求

最值得记住的结论：弹性视觉表征作为MLLM原生能力，可根据内容信息密度自适应分配计算资源，是下一代高效多模态模型的重要发展方向。
