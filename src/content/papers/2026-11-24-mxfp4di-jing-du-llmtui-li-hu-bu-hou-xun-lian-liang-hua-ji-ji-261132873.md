---
title: 'MXFP4 for LLM Inference: Complementary Post-Training Quantization Techniques
  and Their Interactions'
title_zh: MXFP4低精度LLM推理：互补后训练量化技术及相互作用研究
authors:
- Natalia Frumkin
- Alireza Khodamoradi
- Kristof Denolf
- Eric Dellinger
- Stuart Biles
affiliations:
- AMD Research
arxiv_id: '2611.32873'
url: https://arxiv.org/abs/2611.32873
pdf_url: https://arxiv.org/pdf/2611.32873
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: LLM推理 · 后训练量化 低精度压缩
tags:
- LLM Inference
- Post-Training Quantization
- MXFP4
- NVFP4
- Low-Precision
one_liner: 系统对比MXFP4/NVFP4量化适配方案，提出免校准Midmax尺度选择，给出低精度LLM推理最优配方
practical_value: '- 部署支持MXFP4硬件的业务LLM时，可直接采用GPTQ+Block-32 Hadamard旋转+Midmax尺度选择的默认配方，A4W4精度下可获得约3%的准确率提升，无额外部署开销

  - 追求极致压缩比且对精度要求高的场景，可选择A6W4混合精度方案（MXFP6激活+MXFP4权重），在Llama-3.1-8B上精度持平甚至超过BF16基线，大幅降低显存占用和推理延迟

  - 不要盲目跨量化格式迁移优化技巧：NVFP4无需额外添加Hadamard旋转，MXFP4添加NVFP4式宏尺度反而会降低平均精度，避免无效调优'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM部署受显存带宽、能耗约束严重，4位微缩放量化是主流降本方案，但MXFP4、NVFP4两种主流量化格式的最优适配技术差异大，现有研究未系统分析量化技术与格式的组合效应，无法直接指导工业部署。
### 方法关键点
- 覆盖6款主流开源LLM（Llama 3/3.1/3.2、Qwen3全尺寸系列），系统遍历2种量化格式、4种Hadamard旋转粒度、3种PTQ算法、3种尺度选择策略的组合效果
- 提出Midmax免校准尺度选择策略，针对MXFP4幂次块尺度的边界裁剪问题，调整取整边界降低裁剪误差，无需校准数据和硬件修改
- 验证混合精度配置、NVFP4式宏尺度对MXFP4的增益效果
### 关键实验
在5个零样本常识基准+GSM8K数学推理基准测试：
- MXFP4搭配GPTQ+Block-32旋转+Midmax的组合，比基线配置提升约3%准确率，Midmax在67%的测试配置下优于默认floor取整
- A6W4混合精度（MXFP6激活+MXFP4权重）在Llama-3.1-8B上精度超过BF16基线，GSM8K准确率达85.7%
- 最优配置下MXFP4与NVFP4精度相当，无一种格式全局占优
### 核心结论
低精度量化的最终效果由完整的「格式+PTQ算法+旋转+尺度选择」配方决定，而非单一量化格式，不要盲目跨格式迁移优化技巧
