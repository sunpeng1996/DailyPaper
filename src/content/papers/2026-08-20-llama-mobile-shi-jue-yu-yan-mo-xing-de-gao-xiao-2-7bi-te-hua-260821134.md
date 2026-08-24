---
title: 'Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs'
title_zh: Llama-Mobile：视觉语言模型的高效2.7比特量化方案
authors:
- Luka Ribar
- Jeevan Bhoot
- Douglas Orr
affiliations:
- Graphcore Research
- Arm
arxiv_id: '2608.21134'
url: https://arxiv.org/abs/2608.21134
pdf_url: https://arxiv.org/pdf/2608.21134
published: '2026-08-20'
collected: '2026-08-24'
category: Training
direction: 大模型量化 · 端侧VLM部署
tags:
- Quantization
- VLM
- EdgeDeployment
- Arm
- QAT
- ModelCompression
one_liner: 提出无需原始训练数据的VLM量化框架，搭配Arm友好2.7bit格式，将11B VLM压缩至3.7GB性能损失可控
practical_value: '- 做端侧Agent、移动端多模态商品搜索/导购的团队，可直接复用S3D8量化格式+配套QAT流程，将10B级VLM压缩到4GB以内适配中高端手机部署，无需额外收集训练数据

  - 大模型低比特量化时，可复用「用模型自身生成多样prompt+公开数据集构造蒸馏数据」的方案，无需原始训练数据就能大幅降低低比特量化的性能损失

  - 端侧推理性能优化可参考其硬件协同设计思路：针对Arm CPU的SIMD指令集设计量化格式的存储布局与解码逻辑，在压缩比提升的同时保证推理速度甚至优于INT8'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前VLM内存与计算开销极高，无法直接部署在手机等资源受限的端侧设备；低比特量化是降本提效的核心方案，但传统量化感知训练（QAT）依赖原始训练数据，亚3比特量化往往带来严重性能损失，且缺乏适配Arm CPU的高效低比特存储与推理格式。
### 方法关键点
- 数据构造：无需原始训练数据，基于ImageNet公开图像+随机采样的通用视觉理解prompt，调用全精度VLM生成响应构造蒸馏数据集，覆盖不同长度、风格的输出，避免过拟合到特定任务
- 训练流程：采用知识蒸馏QAT，量化后的学生模型学习全精度教师模型的token输出分布，用直通估计器传播梯度，仅在通用蒸馏数据集上训练，不接触下游任务数据
- 量化格式：提出S3D8 2.7bit权重格式，每个字节存储3个权重，通过共享5比特质心索引+3个符号位编码，解码直接映射为INT8，适配Arm CPU的SIMD查表指令，解码开销极低
### 关键实验结果
在VQAv2、ChartQA、DocVQA、AI2D四个VQA任务上验证：
1. 将11B Llama 3.2 Vision Instruct模型压缩到3.7GB（8bit激活），平均任务性能仅比bfloat16原版下降0.083，比同大小的INT量化格式性能高0.314
2. 端侧推理性能：Pixel 8a手机上单用户文本生成速度达3.8 tokens/s，比INT8快27.5%；Graviton4服务器上单用户生成速度达36.8 tokens/s，比INT8快39.4%

低比特量化的落地效果不单纯取决于比特数，量化格式与硬件的协同设计、训练数据和模型原生行为的匹配度，对最终性能的影响更大
