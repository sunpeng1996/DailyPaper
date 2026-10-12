---
title: 'SoloQ: Calibration-Free Quantization for Diffusion Language Models'
title_zh: SOLOQ：面向扩散大语言模型的免校准量化框架
authors:
- Donghyun Lee
- Arkapravo Ghosh
- Varun Manjunath
- Bumjoon Kyle Rhee
- Hyunho Kook
- Shiting Xiao
- Youngeun Kim
- Priyadarshini Panda
affiliations:
- University of Southern California
- Yale University
- Korea University
arxiv_id: '2610.07121'
url: https://arxiv.org/abs/2610.07121
pdf_url: https://arxiv.org/pdf/2610.07121
published: '2026-10-04'
collected: '2026-10-12'
category: LLM
direction: 大语言模型 · 低比特推理量化
tags:
- Quantization
- Diffusion LLM
- KV cache
- NVFP4
- Calibration-Free
one_liner: 无需校准数据实现扩散大语言模型低比特量化，大幅降显存提升推理效率
practical_value: '- 业务部署垂直领域dLLM时可直接复用该免校准量化方案，无需收集领域校准数据即可完成4bit量化，大幅降低落地成本

  - 块扩散模型的提交时KV cache量化策略可迁移至任意长上下文LLM服务：仅压缩已生成的历史上下文KV，活跃生成块保留全精度，平衡压缩率与生成准确率

  - 支持硬件原生NVFP4的量化路径可直接适配现有NVIDIA GPU的FP4计算核，无需额外定制算子即可实现推理加速，适合快速上线'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散大语言模型（dLLM）凭借双向上下文生成能力成为自回归LLM的有力替代，但迭代去噪的推理模式带来极高计算与显存开销，块扩散模型的KV cache还会随上下文长度进一步膨胀。现有dLLM后训练量化方法高度依赖校准数据，而dLLM激活分布会随去噪步、掩码状态动态变化，校准数据的选择直接影响泛化性，难以适配多任务场景。
### 方法关键点
1. 提出K-RPBH旋转结构：结合随机置换、块Hadamard变换、跨块混合，将权重与激活映射到近似高斯的可预测边缘分布，无需校准数据即可完成低比特量化
2. 支持双量化路径：分布匹配码本量化（SOLOQ-C）适配精度优先场景，硬件原生NVFP4量化（SOLOQ-N）适配性能优先场景
3. 轻量仅缩放偏差校正：几乎无开销即可修正量化带来的幅值偏差，提升量化保真度
4. 块扩散模型专属KV量化策略：仅在块生成提交时量化其KV状态，活跃去噪块保留全精度，避免误差累积
### 关键结果
在LLaDA、Dream等全序列dLLM及Fast-dLLM v2、Nemotron等块扩散dLLM上测试，W4A4量化下准确率超过所有校准类基线；SOLOQ-N相比BF16基线峰值显存最高降低2.61×，端到端推理速度最高提升2.24×；2bit KV cache量化精度也优于KIVI、OScar等现有方案。
**最值得记住的一句话**：免校准量化的核心思路是将动态变化的分布转换为可预测的固定形式，而非费力跟踪分布的动态偏移
