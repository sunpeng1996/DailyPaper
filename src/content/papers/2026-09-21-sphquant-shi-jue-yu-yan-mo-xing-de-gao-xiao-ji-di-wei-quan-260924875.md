---
title: 'SPHQuant: Efficient extreme low bit weight quantization for Vision-Language
  Models'
title_zh: SPHQuant：视觉语言模型的高效极低位权重量化框架
authors:
- Kewei Zhang
- Zheng Chen
- Haotong Qin
- Yulun Zhang
affiliations:
- Shanghai Jiao Tong University
- The Hong Kong Polytechnic University
arxiv_id: '2609.24875'
url: https://arxiv.org/abs/2609.24875
pdf_url: https://arxiv.org/pdf/2609.24875
published: '2026-09-21'
collected: '2026-09-22'
category: Multimodal
direction: 多模态大模型 · 极低位权重量化
tags:
- Quantization
- VLM
- Post-training Quantization
- Low-bit Inference
- Edge Deployment
one_liner: 提出无旋转球面坐标权重量化，VLM极2/3位量化精度持平SOTA，解码吞吐量较QTIP提升30.3%
practical_value: '- 做端侧多模态Agent（如端侧商品图文理解、AR导购Agent）的团队，可直接复用SPHQuant的2/3位量化方案，在精度损失可接受的前提下大幅降低VLM内存占用、提升解码速度，适配移动端部署需求

  - 做LLM/VLM推理优化的业务团队，可借鉴球面坐标权重量化思路：将权重分解为符号、半径、方向，给集中了outliers的半径分配更多bits，相比笛卡尔坐标下直接量化，能大幅降低极低位量化的精度损失

  - 可复用其硬件友好的CUDA Kernel设计：将方向码本预加载到共享内存、位紧凑打包半径信息、融合反量化与GEMV计算，进一步提升低比特量化模型的推理吞吐量'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
当前VLM已成为下一代基础模型的核心形态，但大参数量和内存受限的自回归解码特性导致端侧部署难度极高；现有仅权重PTQ方案要么在2-3位极低比特场景下因权重outlier出现精度暴跌，要么基于旋转的优化方案虽提升精度但引入额外推理开销，无法兼顾精度与推理效率。

### 方法关键点
- 不在笛卡尔坐标下直接量化权重，将每个8维权重向量分解为坐标符号、半径、正单位方向，把outlier幅值隔离到半径分量，方向分量保持有界且统计规律稳定，给半径分配额外精度缓解outlier导致的精度下降
- 采用紧凑正方向码本，通过角度参数化微调码本条目，天然保留单位球约束，避免常规向量微调需重归一化导致的梯度损耗
- 设计硬件友好的CUDA GEMV内核，方向码本小到可放入共享内存查表，半径位紧凑打包，融合反量化、查表、矩阵乘计算，消除中间结果访存开销

### 关键实验
在Qwen3-VL-8B、Qwen3.5-9B、Gemma4-26B等主流VLM上测试，对比QTIP、ParoQuant、AWQ等SOTA量化方案：2/3位量化下精度持平SOTA QTIP；RTX A6000上W2A16设置下解码吞吐量较QTIP提升30.3%，较ParoQuant提升12.2%；RTX 4090上单batch解码吞吐量达288.63 token/s，为FP16版本的2.7倍。

### 核心洞见
极低位权重量化的核心瓶颈不是比特数不足，而是权重表示的坐标系统不合理，将outlier集中到独立分量分配额外精度，可在几乎不增加额外开销的前提下大幅提升量化精度。
