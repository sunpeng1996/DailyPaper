---
title: 'SpecMRL: Redesign Matryoshka Representation Learning within Parametric Spectrum'
title_zh: SpecMRL：参数化谱空间重构的套娃表示学习方法
authors:
- Zhongxin Chen
- Songhao Wu
- Heng Cui
- Cong Li
- Xiao Zhou
- Rui Yan
affiliations:
- Renmin University of China
- Lenovo Group
- Wuhan University
arxiv_id: '2610.26824'
url: https://arxiv.org/abs/2610.26824
pdf_url: https://arxiv.org/pdf/2610.26824
published: '2026-10-18'
collected: '2026-10-20'
category: Training
direction: 套娃表示学习 · 低维表征压缩优化
tags:
- MRL
- Representation Learning
- Embedding Compression
- Spectral Basis
- Contrastive Learning
one_liner: 通过参数导出的有序谱基重构MRL特征空间，大幅提升低维截断表征质量
practical_value: '- 推荐/检索场景的embedding训练可直接替换原有MRL为SpecMRL，仅新增训练时的幂迭代步骤，推理仅需固定矩阵投影，开销<1%；16倍压缩下精度最高提升3.8个点，还可减半embedding维度获得比全维度MRL更高的精度，显著节省存储与检索耗时

  - 可复用温启动幂迭代近似特征分解的工程实现，避免直接SVD/Eigh的高计算开销与数值不稳定问题，训练吞吐量下降不足1%，与原生MRL效率几乎持平

  - 针对低维表征需求高的场景（如端侧推荐、大规模向量检索），可直接复用WProj过参数化设计，设置R=128D即可获得最优低维表征效果，无需额外调参'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
原生Matryoshka Representation Learning（MRL）通过嵌套前缀截断支持灵活的表征维度适配，广泛用于检索、推荐场景的embedding压缩，但无显式约束保证前缀维度集中核心信息，高压缩比下精度损失严重；现有改进方案多通过新增跨维度监督优化，未改动原始坐标空间，无法从根本上适配前缀截断的需求，提升效果有限。

### 方法关键点
- 新增可学习参数矩阵WProj，从其Gram矩阵导出按特征重要性排序的正交谱基，将原始表征投影到该谱基空间后再执行MRL的前缀截断，仅修改表征读入逻辑，完全兼容原有MRL的损失函数与训练流程，无额外损失项
- 采用温启动幂迭代近似特征分解，每训练步仅执行一次矩阵乘法加QR正交化，避免直接SVD/Eigh的高计算开销与梯度数值不稳定问题；训练完成后谱基固定，推理仅需一次D×D线性投影，开销极低
- 采用过参数化设计，将WProj的第二维度R设置为128D，进一步提升低维表征的信息密度

### 关键实验结果
在MTEB基准数据集上跨Qwen3、Qwen2、Llama3.2等多个骨干模型验证，相比原生MRL：16倍压缩下精度最高提升3.80个点，仅用一半维度的表征就超过全维度原生MRL的精度，推理时向量检索速度最高提升1.86倍，训练吞吐量仅下降不到0.8%，效果也优于ESE、MIPIC等现有MRL改进方案。

### 核心结论
无需给MRL新增复杂的跨维度监督损失，仅通过参数化谱基重构特征空间，就能以几乎可忽略的开销获得全压缩比下的低维表征精度提升。
